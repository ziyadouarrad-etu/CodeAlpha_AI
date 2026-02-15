import cv2
import os

class VideoManager:
    def __init__(self, source):
        # source: 0 for webcam or 'path/to/video.mp4'
        self.source = source
        self.cap = cv2.VideoCapture(source)
        
        if not self.cap.isOpened():
            raise ValueError(f"Could not open video source: {source}")

    def get_frame(self):
        # Returns (success, frame)
        return self.cap.read()

    def get_properties(self):
        # Returns useful metadata for professional reporting
        return {
            "width": int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            "height": int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            "fps": self.cap.get(cv2.CAP_PROP_FPS),
            "source_type": "Webcam" if self.source == 0 else "File"
        }

    def release(self):
        self.cap.release()