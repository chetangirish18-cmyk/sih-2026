import time
import json
import cv2
from pathlib import Path
from ultralytics import YOLO

def format_mmss(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins}:{secs:02d}"

def run_test(video_path: str):
    start_time = time.time()
    
    print(f"[TEST] Video File: {video_path}")
    print("[TEST] Loading YOLOv8n model...")
    model = YOLO("yolov8n.pt")
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video file: {video_path}")
        
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_duration = total_frames / fps
    
    print(f"[TEST] Video Metadata: {total_frames} frames, {fps:.2f} FPS, Duration: {format_mmss(video_duration)} ({video_duration:.2f}s)")
    print("[TEST] Processing frame by frame (sampling every 5th frame for speed)...")
    print("-" * 65)

    person_present = False
    transitions = []
    frame_number = 0
    sampled_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process every 5th frame
        if frame_number % 5 == 0:
            sampled_count += 1
            results = model(frame, verbose=False, conf=0.35)
            
            # Check for person class (class_id 0)
            person_dets = []
            if results and len(results[0].boxes) > 0:
                for box in results[0].boxes:
                    cls_id = int(box.cls[0])
                    conf = float(box.conf[0])
                    if cls_id == 0:  # "person"
                        person_dets.append(conf)
            
            if person_dets:
                best_conf = max(person_dets)
                if not person_present:
                    # Transition: Not-Present -> Present
                    person_present = True
                    ts_sec = frame_number / fps
                    timestamp_mmss = format_mmss(ts_sec)
                    
                    event = {
                        "event": "Person First Appeared",
                        "timestamp_sec": round(ts_sec, 2),
                        "timestamp_mmss": timestamp_mmss,
                        "confidence": round(best_conf, 4),
                        "frame_number": frame_number
                    }
                    transitions.append(event)
                    print(f"→ [APPEARED] Frame #{frame_number:05d} | Time: {ts_sec:.2f}s ({timestamp_mmss}) | Confidence: {best_conf:.2%}")
            else:
                person_present = False
                
        frame_number += 1
        
    cap.release()
    total_processing_time = time.time() - start_time
    
    output_data = {
        "video_path": video_path,
        "video_duration_sec": round(video_duration, 2),
        "video_duration_mmss": format_mmss(video_duration),
        "total_frames": total_frames,
        "fps": round(fps, 2),
        "sampled_frames_count": sampled_count,
        "processing_time_sec": round(total_processing_time, 2),
        "processing_speed_fps": round(total_frames / total_processing_time, 2) if total_processing_time > 0 else 0,
        "person_appearances_count": len(transitions),
        "transitions": transitions
    }
    
    output_json_path = Path("test_results.json")
    with open(output_json_path, "w") as f:
        json.dump(output_data, f, indent=2)
        
    print("-" * 65)
    print(f"[TEST COMPLETE]")
    print(f"• Total Video Duration  : {output_data['video_duration_mmss']} ({output_data['video_duration_sec']}s)")
    print(f"• Total Processing Time : {output_data['processing_time_sec']} seconds")
    print(f"• Processing Speed      : {output_data['processing_speed_fps']} FPS")
    print(f"• Person Appearances    : {output_data['person_appearances_count']} detected")
    print(f"• Saved Results to      : {output_json_path.resolve()}")
    
    return output_data

if __name__ == "__main__":
    test_video = r"C:\Users\HP\Desktop\internship submissio\telegram video.mp4"
    run_test(test_video)
