import cv2
import argparse
import imutils

# các dictionary có sẵn trong OpenCV
ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
    "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
    "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
    "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
    "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
    "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
    "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
    "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
    "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11,
}


def draw_marker_annotations(frame, markerCorner, markerID):
    # vẽ khung và id marker
    corners = markerCorner.reshape((4, 2))
    (topLeft, topRight, bottomRight, bottomLeft) = corners

    topRight = (int(topRight[0]), int(topRight[1]))
    bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
    bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
    topLeft = (int(topLeft[0]), int(topLeft[1]))

    cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
    cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
    cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
    cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

    # vẽ tâm
    cX = int((topLeft[0] + bottomRight[0]) / 2.0)
    cY = int((topLeft[1] + bottomRight[1]) / 2.0)
    cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

    # ghi ID marker
    cv2.putText(frame, str(markerID),
                (topLeft[0], topLeft[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)


def detect_in_image(image_path, aruco_type):
    print(f"[INFO] loading image {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        print(f"[ERROR] cannot load image: {image_path}")
        return

    arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])
    arucoParams = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)

    corners, ids, rejected = detector.detectMarkers(image)

    if ids is not None and len(corners) > 0:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            draw_marker_annotations(image, markerCorner, markerID)
            print(f"[INFO] detected ArUco marker ID: {markerID}")

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_in_video(source, aruco_type, resize_w=1000):
    print(f"[INFO] starting video stream from {source} (press 'q' to quit)")
    cap = cv2.VideoCapture(source)

    arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])
    arucoParams = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] End of stream or cannot read frame")
            break

        frame = imutils.resize(frame, width=resize_w)

        corners, ids, rejected = detector.detectMarkers(frame)

        if ids is not None and len(corners) > 0:
            ids = ids.flatten()
            for (markerCorner, markerID) in zip(corners, ids):
                draw_marker_annotations(frame, markerCorner, markerID)
                print(f"[INFO] ArUco marker ID: {markerID}")

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", type=str, default="video",
                    help="Mode: 'image' or 'video'")
    ap.add_argument("--source", type=str, default="0",
                    help="Video source (0 for webcam or path to video file)")
    ap.add_argument("--type", type=str, default="DICT_6X6_50",
                    help="Type of ArUco tag to detect")
    ap.add_argument("--resize", type=int, default=1000,
                    help="Resize width of frame")
    args = vars(ap.parse_args())

    if args["type"] not in ARUCO_DICT.keys():
        print(f"[ERROR] ArUco tag type '{args['type']}' is not supported")
        exit(0)

    if args["mode"] == "image":
        detect_in_image(args["source"], args["type"])
    else:
        try:
            src = int(args["source"])
        except ValueError:
            src = args["source"]
        detect_in_video(src, args["type"], resize_w=args["resize"])
