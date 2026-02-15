from ultralytics import YOLO
import torch
import os

class ObjectDetector:
    def __init__(self, model_name='yolov8n.pt', confidence=0.5):
        # 1. Define the models directory
        # This gets the directory where detector.py is, then goes up one level to the root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        models_dir = os.path.join(base_dir, 'models')
        
        # 2. Create the folder if it doesn't exist
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
            print(f"[INFO] Created directory: {models_dir}")

        # 3. Define the full path to the weights file
        model_path = os.path.join(models_dir, model_name)
        
        # 4. Load the model using the full path
        self.model = YOLO(model_path)
        self.confidence = confidence
        
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model.to(self.device)
        
        print(f"[INFO] Model loaded from: {model_path}")
        print(f"[INFO] Inference Engine initialized on: {self.device.upper()}")

    def get_detections(self, frame):
        """
        Takes a raw frame and returns a structured list of detections.
        """
        # Run the model with tracking enabled
        # persist=True: maintains ID consistency between frames
        # verbose=False: keeps the terminal clean
        results = self.model.track(
            source=frame, 
            persist=True, 
            conf=self.confidence,
            device=self.device,
            verbose=False
        )
        
        # Extract and format the data from the Results object
        return self._parse_results(results[0])

    def _parse_results(self, result):
        detections = []
        
        # Get the dictionary of names from the model
        class_names = self.model.names 

        if result.boxes is not None and result.boxes.id is not None:
            for box in result.boxes:
                class_id = int(box.cls[0])
                
                # Look up the human-readable name (e.g., 0 -> 'person')
                class_name = class_names.get(class_id, "unknown")

                detections.append({
                    "bbox": box.xyxy[0].tolist(),
                    "class_id": class_id,
                    "class_name": class_name,  # Added this field
                    "confidence": float(box.conf[0]),
                    "track_id": int(box.id[0])
                })
                
        return detections