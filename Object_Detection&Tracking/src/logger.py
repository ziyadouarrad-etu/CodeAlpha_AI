import csv
import datetime
import os

class DataLogger:
    def __init__(self, filename="detections_log.csv"):
        self.filename = filename
        # Write header if file doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Track_ID", "Class", "Confidence"])

    def log_detections(self, detections):
        """Appends detection data to the CSV file"""
        if not detections:
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(self.filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            for obj in detections:
                writer.writerow([
                    timestamp,
                    obj['track_id'],
                    obj['class_name'],
                    round(obj['confidence'], 2)
                ])