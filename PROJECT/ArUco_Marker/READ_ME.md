# Mã ArUco là gì --- giải thích ngắn gọn

**Mã ArUco** là một họ *fiducial marker* 2D dạng ô vuông (binary square
markers) được thiết kế để dễ phát hiện và giải mã trong ảnh/luồng video.
Mỗi marker chứa một **lưới bit** (ví dụ 4×4, 5×5, 6×6...) ở giữa và được
bao quanh bởi một **viền 1 ô** (quiet border) để tách marker khỏi nền.
Bộ marker được tổ thành *dictionary* (tập nhãn đã mã hóa) với khoảng
cách Hamming tối thiểu giữa các mã --- điều này giúp phát hiện và sửa
lỗi đơn giản. ArUco thường dùng trong robotics, AR, tracking, và ước
lượng pose (vị trí + hướng) của camera.

------------------------------------------------------------------------

# Nguyên lý và pipeline giải thuật (chi tiết từng bước)

Dưới đây là pipeline điển hình dùng để phát hiện --- giải mã --- ước
lượng pose một ArUco marker trong một ảnh:

## 1. Tiền xử lý ảnh

-   Chuyển ảnh sang **grayscale**.
-   Áp dụng **adaptive threshold** (hoặc Otsu) để chuyển ảnh thành nhị
    phân (đen/trắng). Mục tiêu: tách rõ các ô trong marker khỏi nền, bất
    chấp thay đổi ánh sáng.
-   (Tùy chọn) Dùng **morphology** (closing/opening) để loại nhiễu nhỏ.

**Lưu ý:** adaptive threshold theo vùng thường tốt khi điều kiện sáng
không đều.

## 2. Tìm đường viền (contours) và lọc ứng viên

-   Dùng `findContours` trên ảnh nhị phân.
-   Lọc contours theo **diện tích** (loại bỏ quá nhỏ) và theo **độ tương
    thích với tứ giác**:
    -   Là đa giác 4 cạnh sau `approxPolyDP`.
    -   Hình phẳng (convex).
    -   Tỷ lệ cạnh hợp lý (không quá dài/nhỏ).
-   Các tứ giác này là **ứng viên marker**.

## 3. Chuẩn hoá hình học (homography / perspective warp)

-   Với mỗi ứng viên tứ giác, sắp xếp bốn đỉnh theo thứ tự cố định (ví
    dụ: top-left, top-right, bottom-right, bottom-left) bằng cách dùng
    tổng/hiệu toạ độ.
-   Tính **homography** từ bốn đỉnh này đến bốn góc của một ảnh vuông
    chuẩn (ví dụ kích thước `S × S` pixel).\
-   Dùng `warpPerspective` để thu được ảnh "top-down" (view trực diện)
    của marker.

## 4. Lấy mẫu lưới bit (sampling)

-   Marker nội bộ có **k × k** ô bit (k phụ thuộc dictionary, ví dụ
    4,5,6,...).
-   Marker thực tế bao gồm **viền 1 ô** ngoài cùng, nên tổng lưới là
    **(k + 2) × (k + 2)** modules.
-   Trên ảnh warp, chia ảnh thành `(k+2) × (k+2)` ô vuông có kích thước
    đều; **bỏ ô biên ngoài** và chỉ đọc k×k ô bên trong.
-   Với mỗi ô bit, tính trung bình cường độ pixel (hoặc phần trăm pixel
    đen) để quyết định 0/1 (tối =\> 1, sáng =\> 0) theo ngưỡng.

## 5. Xác định hướng và giải mã (decode)

-   Vì marker có thể xoay 0°, 90°, 180°, 270°, ta **xoay ma trận bit 4
    lần** và ở mỗi xoay so sánh với dictionary:
    -   Mỗi pattern trong dictionary có một mã id (số).
    -   Tính **Hamming distance** (số bit khác) giữa bit matrix ứng viên
        và các pattern trong dictionary.
    -   Chọn id có Hamming distance nhỏ nhất; nếu nhỏ hơn ngưỡng cho
        phép thì chấp nhận ứng viên và xác định orientation tương ứng.
-   Nếu mọi xoay đều không tìm được khớp chấp nhận được =\> ứng viên bị
    loại.

## 6. Tinh chỉnh góc (corner refinement)

-   Sau khi xác nhận marker, có thể tinh chỉnh vị trí góc bằng
    `cornerSubPix` (subpixel refinement) hoặc thuật toán dựa trên biên
    (edge fitting) để giảm lỗi vị trí góc (quan trọng cho pose chính
    xác).

## 7. Ước lượng pose (nếu cần)

-   Nếu **camera intrinsics** (ma trận camera K: fx, fy, cx, cy) và kích
    thước thật của marker (chiều dài cạnh, đơn vị mét) đã biết, ta dùng
    `solvePnP`:
    -   Định nghĩa 3D object points (4 góc marker) trong hệ toạ độ
        marker --- thường đặt z=0:\
        `(-s/2, s/2, 0), (s/2, s/2, 0), (s/2, -s/2, 0), (-s/2, -s/2, 0)`
        (đơn vị = s: kích thước marker).
    -   Dùng `cv2.solvePnP` (hoặc solvePnPRansac) với 2D image points
        (các góc) để tìm `rvec, tvec`.
    -   Chuyển rvec sang bảng quay (Rodrigues) nếu cần và tính toạ độ /
        góc Euler.
-   Có thể dùng `solvePnPRefineLM` để tối ưu hóa reprojection error
    (Levenberg--Marquardt).

------------------------------------------------------------------------

# Một bản tóm tắt thuật toán dưới dạng pseudocode

``` text
input: image, dictionary (k x k patterns), camera_intrinsics (optional), marker_size (optional)
1. gray = toGrayscale(image)
2. bw = adaptiveThreshold(gray)
3. contours = findContours(bw)
4. candidates = []
5. for c in contours:
     poly = approxPolyDP(c)
     if poly has 4 vertices and area large and convex:
         sortCorners(poly)
         H = findHomography(poly, destSquare)
         warp = warpPerspective(gray, H, destSize)
         bits = sampleBits(warp, k)   # read k x k internal bits
         for rot in 0..3:
             bits_rot = rotate(bits, rot)
             (best_id, best_hamming) = matchDictionary(bits_rot, dictionary)
             if best_hamming <= threshold:
                 refineCorners(poly)  # subpixel
                 if camera_intrinsics given:
                     pose = solvePnP(objectPoints, imagePoints, camera_intrinsics)
                 store detected marker (id, corners, rot, pose)
                 break
```

------------------------------------------------------------------------

# Một số chi tiết kỹ thuật quan trọng & tips thực tế

-   **Dictionary & Hamming distance:** dictionary được xây dựng sao cho
    mã khác nhau có khoảng cách Hamming tối thiểu (ví dụ ≥ 3). Khi giải
    mã, cho phép một số lỗi bit nhỏ (nhưng không quá lớn) tùy yêu cầu.
-   **Viền (quiet border):** cần có viền 1 ô (màu đen/white tùy tiêu
    chuẩn) để tách vùng mã khỏi nền --- giúp giảm false positives.
-   **Thresholding:** adaptive theo vùng hoặc local threshold tốt hơn
    global khi điều kiện sáng không đồng nhất.
-   **Corner ordering:** quy tắc nhất quán là rất quan trọng (để warp
    đúng mặt).
-   **Cỡ marker vs camera:** marker nhỏ quá so với độ phân giải ảnh sẽ
    khó đọc; marker nên chiếm đủ pixel để các ô bên trong có nhiều
    pixel.
-   **In ấn & tương phản:** in marker với tương phản cao (đen thật ---
    trắng thật), tránh bóng phản quang.
-   **Pose accuracy:** phụ thuộc lớn vào độ chính xác góc (corner
    positions) và ma trận nội tại camera (calibration). Nên calibrate
    camera trước khi ước lượng pose.
-   **Kháng nhiễu & giả dương (false positives):** dùng
    `rejectedCandidates` và kiểm tra score/Hamming; tăng kích thước
    dictionary (với nhiều bits) để giảm trùng lặp; hoặc kết hợp nhiều
    marker cùng lúc để tăng tính tin cậy.

------------------------------------------------------------------------

# Về hiệu năng và so sánh ngắn

-   **ArUco**: đơn giản, nhanh, dễ dùng; có nhiều dictionary trong
    OpenCV-contrib (`cv2.aruco`). Thích hợp cho ứng dụng thời gian thực
    nhẹ.
-   **AprilTag** (như tham khảo): thiết kế cho độ ổn định/khả năng phát
    hiện cao hơn trong nhiễu, distortion, bị che khuất; có thể chậm hơn
    tùy cài đặt.\
    (Tóm lại: chọn theo yêu cầu --- nhanh vs cực kỳ chắc chắn.)

------------------------------------------------------------------------

# Nếu bạn muốn code sẵn (ví dụ OpenCV/Python)

Mình có thể gửi đoạn code Python dùng `cv2.aruco` để: - tạo marker, -
phát hiện marker từ camera/video, - in ra id + pose (nếu có camera
calibration).

Bạn muốn mình gửi đoạn code ví dụ hay mẫu chạy trực tiếp không? (Mình sẽ
gửi luôn --- không cần chờ.)

------------------------------------------------------------------------

Nếu bạn cần mình **diễn giải sâu hơn** phần nào (ví dụ: công thức
homography, cách tính Hamming chi tiết, các biến thể refine pose, hay
code Python/OpenCV đầy đủ), nói luôn phần bạn muốn khám phá --- mình sẽ
tiếp tục.

