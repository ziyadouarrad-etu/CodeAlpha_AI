import cv2

class Visualizer:
    def __init__(self):
        # We'll use a bright color (BGR format: Green)
        self.color = (0, 255, 0)
        self.thickness = 2
        self.font = cv2.FONT_HERSHEY_SIMPLEX

class Visualizer:
    def __init__(self):
        self.color = (0, 255, 0)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.max_id = 0 # Track the highest ID seen

    def draw(self, frame, detections):
        for obj in detections:
            # Update the max_id if we see a higher track_id
            if obj['track_id'] > self.max_id:
                self.max_id = obj['track_id']

            x1, y1, x2, y2 = map(int, obj['bbox'])
            label = f"ID:{obj['track_id']} {obj['class_name'].capitalize()}"
            
            # Draw box and labels (your existing logic)
            cv2.rectangle(frame, (x1, y1), (x2, y2), self.color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), self.font, 0.5, self.color, 2)

        # Draw the Total Counter in the top-right corner
        self._draw_overlay(frame)
        return frame

    def _draw_overlay(self, frame):
        """Draws a semi-transparent background for the counter"""
        overlay_text = f"Total Unique Objects: {self.max_id}"
        cv2.putText(frame, overlay_text, (20, 80), 
                    self.font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    def draw_fps(self, frame, fps):
        cv2.putText(frame, f"FPS: {int(fps)}", (20, 50), 
                    self.font, 1, (0, 255, 255), 2)
        return frame