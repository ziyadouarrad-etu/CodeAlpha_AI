import cv2
import argparse
import time
from src.video_manager import VideoManager
from src.detector import ObjectDetector
from src.visualizer import Visualizer
from src.logger import DataLogger
from pathlib import Path

def run_pipeline(source_path=None, model_name="yolov8n.pt", enable_logging=0):
    # 1. SETUP STAGE
    if source_path:
        # Check if the input is a digit (like '0' or '1' for webcams)
        if source_path.isdigit():
            source = int(source_path)
        else:
            # It's a file path, so resolve it
            p = Path(source_path).resolve()
            if not p.exists():
                print(f"[ERROR] Path does not exist: {p}")
                return
            source = str(p)
    else:
        source = 0 # Default to internal webcam
    
    try:
        video = VideoManager(source)
        # Using the Nano model for speed on your Intel integrated GPU
        detector = ObjectDetector(model_name=model_name, confidence=0.4)
        viz = Visualizer()
        
        print(f"[SUCCESS] Pipeline started on {source if source != 0 else 'Webcam'}. Press 'q' to exit.")
    except Exception as e:
        print(f"[ERROR] Could not initialize pipeline: {e}")
        return

    # Initialize logger only if requested
    logger = DataLogger("logs/session_log.csv") if enable_logging else None
    
    if logger:
        print("[INFO] Logging enabled. Saving to logs/session_log.csv")

    # FPS calculation variables
    prev_time = 0
    curr_time = 0    

    # 2. THE LOOP (The Heartbeat of the App)
    while True:
        # A. Input Stage
        success, frame = video.get_frame()

        if not success:
            print("[INFO] End of video stream or source disconnected.")
            break

        # Calculate FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        

        # B. Inference & Tracking Stage
        # This returns our clean list of dictionaries
        detections = detector.get_detections(frame)
        
        # Log the detections
        if logger:
            logger.log_detections(detections)

        # C. Output Stage
        # Draw the data back onto the frame
        processed_frame = viz.draw(frame, detections)
        processed_frame = viz.draw_fps(processed_frame, fps)
        # Optional: UI indicator for logging
        if enable_logging:
            cv2.circle(processed_frame, (10, 10), 10, (0, 0, 255), -1) # Red "REC" dot

        # Display to the user
        cv2.imshow("CodeAlpha AI - Object Detection & Tracking", processed_frame)

        # Handle keyboard interrupt (wait 1ms for 'q' key)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 3. CLEANUP STAGE
    video.release()
    cv2.destroyAllWindows()
    print("[INFO] Pipeline shut down safely.")

if __name__ == "__main__":
    # Handle command line arguments for video files
    parser = argparse.ArgumentParser(description="CodeAlpha AI Task 4")
    parser.add_argument("--video", type=str, help="Path to input video file")
    parser.add_argument("--model", type=str, default="yolov8n.pt", help="YOLO model version (e.g., yolov8n.pt, yolov8m.pt)")
    parser.add_argument("--log", type=int, default=0, choices=[0, 1], help="Enable logging (1) or disable (0)")
    
    args = parser.parse_args()
    run_pipeline(args.video, args.model, args.log)