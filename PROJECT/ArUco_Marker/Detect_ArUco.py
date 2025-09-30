"""
ESP32 + DHT11 + Blynk Simulator GUI (PyQt5) + Multi-point Map & AQI

Chương trình sau là bản nâng cấp theo yêu cầu:
- Thêm form nhập nhiều điểm (Name, Lat, Lon, Temp, Hum, PM2.5).
- Add Point lưu vào danh sách và hiển thị trong bảng.
- Clear Points xóa toàn bộ.
- Update Map hiển thị tất cả marker với popup và màu theo PM2.5.
- Send 1 lần / Start/Stop gửi payload mô phỏng qua UDP/TCP/HTTP.
- Tuỳ chọn: Auto-add when sending, Auto-update map when adding/sending.

Yêu cầu cài đặt:
- pip install pyqt5 pyqtwebengine requests

Chạy:
- python main2.py
"""

"""=================================== IMPORT THƯ VIỆN ===================================
📂 Thư viện chuẩn Python:
-) import json
Dùng để xử lý dữ liệu JSON (JavaScript Object Notation) – thường để chuyển đổi dữ liệu từ/to dạng chuỗi JSON, ví dụ gửi thông tin sensor lên Blynk.
👉 json.dumps(obj) (dict → JSON string), json.loads(str) (JSON string → dict).
-) import socket
Dùng để tạo và quản lý kết nối mạng (UDP, TCP). Trong mô phỏng này, ESP32 giả lập việc gửi dữ liệu cảm biến đến server/Blynk.
👉 socket.socket(socket.AF_INET, socket.SOCK_DGRAM) tạo socket UDP.
-) import threading
Cho phép chạy nhiều tiến trình song song (multithread). Trong chương trình này thường dùng để chạy vòng lặp gửi dữ liệu liên tục mà không làm đứng GUI.
-) import time
Dùng để quản lý thời gian: time.sleep(), lấy timestamp, tính khoảng thời gian delay khi gửi dữ liệu.
-) from datetime import datetime
Lấy thời gian hệ thống (giờ, phút, giây, ngày tháng). Thường dùng để ghi log: "đã gửi lúc 12:30:15".
📂 PyQt5 – GUI:
-) from PyQt5.QtCore import QTimer, QUrl
    -) QTimer: tạo timer định kỳ (ví dụ: cứ 5 giây gửi dữ liệu 1 lần).
    -) QUrl: định nghĩa URL (dùng khi load trang web vào QWebEngineView – ví dụ bản đồ Google/Leaflet).\
-) from PyQt5.QtWidgets import (...)
Đây là các widget GUI cơ bản để tạo giao diện người dùng:

-) QApplication: khởi tạo ứng dụng PyQt5.
    -) QWidget: lớp cơ sở của mọi cửa sổ/khung giao diện.
    -) QLabel: nhãn hiển thị text.
    -) QLineEdit: ô nhập liệu 1 dòng (ví dụ nhập tọa độ, nhiệt độ).
    -) QPushButton: nút bấm.
    -) QComboBox: dropdown chọn (ví dụ chọn giao thức UDP/TCP/HTTP).
    -) QTextEdit: ô nhập/xuất text nhiều dòng (log).
    -) QGridLayout, QHBoxLayout, QVBoxLayout: các bộ layout để sắp xếp widget theo dạng lưới, ngang, dọc.
    -) QSplitter: cho phép kéo giãn giữa các vùng giao diện.
    -) QSpinBox: ô nhập số (có mũi tên tăng giảm).
    -) QMessageBox: popup thông báo, cảnh báo.
    -) QTableWidget, QTableWidgetItem: bảng hiển thị dữ liệu dạng lưới (ví dụ danh sách điểm GPS, nhiệt độ, độ ẩm, PM2.5).

from PyQt5.QtWebEngineWidgets import QWebEngineView
Đây là trình duyệt web mini tích hợp trong PyQt5.
👉 Dùng để hiển thị bản đồ Google Maps hoặc Leaflet Map trực tiếp trong GUI.
Bạn có thể load URL (ví dụ Google Maps) hoặc file HTML (Leaflet custom map).
"""

import sys
import json
import socket
import threading
import time
from datetime import datetime

from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox,
    QTextEdit, QGridLayout, QHBoxLayout, QSpinBox, QMessageBox, QVBoxLayout, QSplitter, QTableWidget, QTableWidgetItem
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

try:
    import requests
    HAS_REQUESTS = True
except Exception:
    HAS_REQUESTS = False

MAP_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Map</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>html, body, #map { height:100%; margin:0; padding:0; }</style>
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
</head>
<body>
<div id="map"></div>
<script>
  var points = POINTS_JSON; // replaced by Python
  var defaultLat = DEFAULT_LAT;
  var defaultLon = DEFAULT_LON;
  var map = L.map('map').setView([defaultLat, defaultLon], 12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
  }).addTo(map);

  function getColor(pm){
    if(pm <= 50) return 'green';
    if(pm <= 100) return 'yellow';
    if(pm <= 150) return 'orange';
    if(pm <= 200) return 'red';
    return 'purple';
  }

  function createIcon(color){
    var html = '<div style="width:18px;height:18px;border-radius:9px;border:2px solid #333;background:' + color + ';box-shadow:0 0 6px rgba(0,0,0,0.4)"></div>';
    return L.divIcon({html: html, className: ''});
  }

  var markers = [];
  for(var i=0;i<points.length;i++){
    var p = points[i];
    var col = getColor(p.pm25);
    var icon = createIcon(col);
    var marker = L.marker([p.lat, p.lon], {icon: icon}).addTo(map);
    var popup = '<b>Point:</b> ' + (p.name||('ID ' + (p.id || (i+1)))) + '<br>' +
                '<b>Location:</b> ' + p.lat.toFixed(6) + ', ' + p.lon.toFixed(6) + '<br>' +
                '<b>Temp:</b> ' + p.temp + ' °C<br>' +
                '<b>Humidity:</b> ' + p.hum + ' %<br>' +
                '<b>PM2.5:</b> ' + p.pm25 + ' µg/m³<br>' +
                '<b>AQI Level:</b> ' + (p.pm25<=50? 'Tốt': (p.pm25<=100? 'Trung bình': (p.pm25<=150? 'Kém': (p.pm25<=200? 'Xấu': 'Rất xấu'))));
    marker.bindPopup(popup);
    markers.push(marker);
  }

  if(markers.length>0){
    var group = L.featureGroup(markers);
    map.fitBounds(group.getBounds().pad(0.2));
  }
</script>
</body>
</html>
"""


class SimulatorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ESP32 + DHT11 + Blynk Simulator - Multi-point & AQI")
        self.resize(1200, 700)

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer)

        self.points = []
        self.next_id = 1

        self._build_ui()
        self.sending = False

    def _build_ui(self):
        main_layout = QHBoxLayout(self)

        left_layout = QGridLayout()

        left_layout.addWidget(QLabel("Name (optional):"), 0, 0)
        self.name_input = QLineEdit("")
        left_layout.addWidget(self.name_input, 0, 1)

        left_layout.addWidget(QLabel("Latitude:"), 1, 0)
        self.lat_input = QLineEdit("10.776889")
        left_layout.addWidget(self.lat_input, 1, 1)

        left_layout.addWidget(QLabel("Longitude:"), 2, 0)
        self.lon_input = QLineEdit("106.700806")
        left_layout.addWidget(self.lon_input, 2, 1)

        left_layout.addWidget(QLabel("Nhiệt độ (°C):"), 3, 0)
        self.temp_input = QLineEdit("25.0")
        left_layout.addWidget(self.temp_input, 3, 1)

        left_layout.addWidget(QLabel("Độ ẩm (%):"), 4, 0)
        self.hum_input = QLineEdit("60.0")
        left_layout.addWidget(self.hum_input, 4, 1)

        left_layout.addWidget(QLabel("PM2.5 (µg/m³):"), 5, 0)
        self.pm25_input = QLineEdit("12.0")
        left_layout.addWidget(self.pm25_input, 5, 1)

        left_layout.addWidget(QLabel("Phương thức giao tiếp"), 6, 0)
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["UDP", "TCP", "HTTP_POST"])
        left_layout.addWidget(self.mode_combo, 6, 1)

        left_layout.addWidget(QLabel("IP / Host:"), 7, 0)
        self.ip_input = QLineEdit("127.0.0.1")
        left_layout.addWidget(self.ip_input, 7, 1)

        left_layout.addWidget(QLabel("Port:"), 8, 0)
        self.port_input = QSpinBox()
        self.port_input.setRange(1, 65535)
        self.port_input.setValue(5005)
        left_layout.addWidget(self.port_input, 8, 1)

        left_layout.addWidget(QLabel("HTTP URL"), 9, 0)
        self.url_input = QLineEdit("http://127.0.0.1:5000/data")
        left_layout.addWidget(self.url_input, 9, 1)

        left_layout.addWidget(QLabel("Blynk Token"), 10, 0)
        self.blynk_token_input = QLineEdit("")
        left_layout.addWidget(self.blynk_token_input, 10, 1)

        left_layout.addWidget(QLabel("Chu kỳ gửi (ms):"), 11, 0)
        self.interval_spin = QSpinBox()
        self.interval_spin.setRange(200, 3600000)
        self.interval_spin.setValue(2000)
        left_layout.addWidget(self.interval_spin, 11, 1)

        # Buttons
        btn_layout1 = QHBoxLayout()
        self.add_btn = QPushButton("Add Point")
        self.add_btn.clicked.connect(self.add_point)
        btn_layout1.addWidget(self.add_btn)

        self.clear_btn = QPushButton("Clear Points")
        self.clear_btn.clicked.connect(self.clear_points)
        btn_layout1.addWidget(self.clear_btn)

        left_layout.addLayout(btn_layout1, 12, 0, 1, 2)

        btn_layout2 = QHBoxLayout()
        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.start_stop)
        btn_layout2.addWidget(self.start_btn)

        self.single_btn = QPushButton("Gửi 1 lần")
        self.single_btn.clicked.connect(self.send_once)
        btn_layout2.addWidget(self.single_btn)

        self.update_map_btn = QPushButton("Update Map")
        self.update_map_btn.clicked.connect(self.update_map)
        btn_layout2.addWidget(self.update_map_btn)

        left_layout.addLayout(btn_layout2, 13, 0, 1, 2)

        # Options (as checkable buttons)
        self.auto_add_btn = QPushButton("Auto-add on Send: OFF")
        self.auto_add_btn.setCheckable(True)
        self.auto_add_btn.toggled.connect(lambda v: self.auto_add_btn.setText("Auto-add on Send: ON" if v else "Auto-add on Send: OFF"))
        left_layout.addWidget(self.auto_add_btn, 14, 0, 1, 2)

        self.auto_map_btn = QPushButton("Auto-update Map: OFF")
        self.auto_map_btn.setCheckable(True)
        self.auto_map_btn.toggled.connect(lambda v: self.auto_map_btn.setText("Auto-update Map: ON" if v else "Auto-update Map: OFF"))
        left_layout.addWidget(self.auto_map_btn, 15, 0, 1, 2)

        # Points table
        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Lat", "Lon", "Temp°C", "Hum%", "PM2.5"])
        left_layout.addWidget(self.table, 16, 0, 6, 2)

        # Log
        left_layout.addWidget(QLabel("Log"), 22, 0)
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        left_layout.addWidget(self.log, 23, 0, 6, 2)

        # Map view
        self.webview = QWebEngineView()
        self.update_map()

        splitter = QSplitter()
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)
        splitter.addWidget(self.webview)
        splitter.setSizes([450, 750])

        main_layout.addWidget(splitter)

    def log_message(self, *parts):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text = ' '.join(str(p) for p in parts)
        self.log.append(f"[{ts}] {text}")

    def add_point(self):
        try:
            name = self.name_input.text().strip()
            lat = float(self.lat_input.text())
            lon = float(self.lon_input.text())
            temp = float(self.temp_input.text())
            hum = float(self.hum_input.text())
            pm25 = float(self.pm25_input.text())
        except ValueError:
            QMessageBox.warning(self, "Dữ liệu lỗi", "Vui lòng nhập số hợp lệ cho Lat/Lon/Temp/Hum/PM2.5")
            return

        pt = {"id": self.next_id, "name": name, "lat": lat, "lon": lon, "temp": temp, "hum": hum, "pm25": pm25}
        self.points.append(pt)
        self.next_id += 1
        self._refresh_table()
        self.log_message("Added point", pt)
        if self.auto_map_btn.isChecked():
            self.update_map()

    def clear_points(self):
        self.points = []
        self.next_id = 1
        self._refresh_table()
        self.update_map()
        self.log_message("Cleared points")

    def _refresh_table(self):
        self.table.setRowCount(0)
        for pt in self.points:
            r = self.table.rowCount()
            self.table.insertRow(r)
            self.table.setItem(r, 0, QTableWidgetItem(str(pt['id'])))
            self.table.setItem(r, 1, QTableWidgetItem(pt['name']))
            self.table.setItem(r, 2, QTableWidgetItem(str(pt['lat'])))
            self.table.setItem(r, 3, QTableWidgetItem(str(pt['lon'])))
            self.table.setItem(r, 4, QTableWidgetItem(str(pt['temp'])))
            self.table.setItem(r, 5, QTableWidgetItem(str(pt['hum'])))
            self.table.setItem(r, 6, QTableWidgetItem(str(pt['pm25'])))

    def build_payload_from_inputs(self):
        lat = float(self.lat_input.text())
        lon = float(self.lon_input.text())
        temp = float(self.temp_input.text())
        hum = float(self.hum_input.text())
        pm25 = float(self.pm25_input.text())
        payload = {"device": "sim_esp32", "timestamp": int(time.time()), "location": {"lat": lat, "lon": lon}, "dht": {"temperature": temp, "humidity": hum}, "pm25": pm25}
        return payload

    def send_once(self):
        try:
            payload = self.build_payload_from_inputs()
        except Exception as e:
            QMessageBox.warning(self, "Dữ liệu lỗi", str(e))
            return

        mode = self.mode_combo.currentText()
        ip = self.ip_input.text().strip()
        port = int(self.port_input.value())
        url = self.url_input.text().strip()
        token = self.blynk_token_input.text().strip()

        # If auto-add enabled, add current inputs as a point
        if self.auto_add_btn.isChecked():
            try:
                name = self.name_input.text().strip()
                pt = {"id": self.next_id, "name": name, "lat": payload['location']['lat'], "lon": payload['location']['lon'], "temp": payload['dht']['temperature'], "hum": payload['dht']['humidity'], "pm25": payload['pm25']}
                self.points.append(pt)
                self.next_id += 1
                self._refresh_table()
                self.log_message("Auto-added point on send", pt)
            except Exception:
                pass

        threading.Thread(target=self._send_payload, args=(mode, ip, port, url, token, payload), daemon=True).start()

        if self.auto_map_btn.isChecked():
            self.update_map()

    def start_stop(self):
        if not self.sending:
            interval = int(self.interval_spin.value())
            self.timer.start(interval)
            self.start_btn.setText("Stop")
            self.sending = True
            self.log_message("Bắt đầu gửi theo chu kỳ", interval, "ms")
        else:
            self.timer.stop()
            self.start_btn.setText("Start")
            self.sending = False
            self.log_message("Dừng gửi")

    def on_timer(self):
        self.send_once()

    def _send_payload(self, mode, ip, port, url, token, payload):
        pkt = json.dumps(payload)
        try:
            if mode == 'UDP':
                self._send_udp(ip, port, pkt)
            elif mode == 'TCP':
                self._send_tcp(ip, port, pkt)
            elif mode == 'HTTP_POST':
                self._send_http(url, token, payload)
            else:
                self.log_message('Unknown mode', mode)
        except Exception as e:
            self.log_message('Lỗi gửi:', str(e))

    def _send_udp(self, ip, port, pkt):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        s.sendto(pkt.encode('utf-8'), (ip, port))
        s.close()
        self.log_message('UDP sent to', f"{ip}:{port}", 'payload=', pkt)

    def _send_tcp(self, ip, port, pkt):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, port))
        s.sendall(pkt.encode('utf-8'))
        try:
            resp = s.recv(4096)
            self.log_message('TCP sent to', f"{ip}:{port}", 'payload=', pkt, 'response=', resp.decode('utf-8', errors='ignore'))
        except socket.timeout:
            self.log_message('TCP sent to', f"{ip}:{port}", 'payload=', pkt, '(no response)')
        s.close()

    def _send_http(self, url, token, payload):
        if not HAS_REQUESTS:
            self.log_message('requests library not installed; cannot send HTTP')
            return
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Authorization'] = f"Bearer {token}"
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=5)
            self.log_message('HTTP POST to', url, 'status=', r.status_code, 'resp=', r.text[:200])
        except Exception as e:
            self.log_message('HTTP error:', str(e))

    def update_map(self):
        # Build JS-safe JSON
        if len(self.points) == 0:
            default_lat = float(self.lat_input.text() or 0)
            default_lon = float(self.lon_input.text() or 0)
        else:
            default_lat = self.points[-1]['lat']
            default_lon = self.points[-1]['lon']
        points_json = json.dumps(self.points)
        html = MAP_HTML_TEMPLATE.replace('POINTS_JSON', points_json)
        html = html.replace('DEFAULT_LAT', str(default_lat)).replace('DEFAULT_LON', str(default_lon))
        self.webview.setHtml(html, QUrl('http://localhost/'))
        self.log_message('Map updated with', len(self.points), 'points')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SimulatorGUI()
    win.show()
    sys.exit(app.exec_())
