import os
import sys
from src.video_splitter import VideoSplitter
from src.frame_extractor import FrameExtractor
from src.coach_counter import CoachCounter
from src.component_detector import ComponentDetector
from src.color_validator import ColorValidator
from src.coverage_selector import CoverageSelector
from src.report_generator import ReportGenerator

def main():
    # Define paths relative to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_video_path = os.path.join(script_dir, 'data', 'input_video', 'CCTV_HZBN_DHN_1_LEFT_UP_20251230_064707_fs.mp4')
    output_dir = os.path.join(script_dir, 'data', 'coaches')
    frames_dir = os.path.join(script_dir, 'data', 'frames')
    reports_dir = os.path.join(script_dir, 'data', 'reports')
    train_number = '12309'  # Example train number

    # Check if input video exists
    if not os.path.exists(input_video_path):
        print(f"Input video not found at {input_video_path}")
        sys.exit(1)

    # Step 1: Video Splitting and Coach Counting
    splitter = VideoSplitter(input_video_path, output_dir, train_number)
    coach_videos = splitter.split_video()
    coach_count = len(coach_videos)
    print(f"Detected {coach_count} coaches.")

    # Step 2: Frame Extraction
    extractor = FrameExtractor()
    for coach_video in coach_videos:
        coach_dir = os.path.dirname(coach_video)
        extractor.extract_frames(coach_video, coach_dir)

    # Step 3: Component Detection
    detector = ComponentDetector()
    for coach_video in coach_videos:
        coach_dir = os.path.dirname(coach_video)
        frames_path = os.path.join(coach_dir, 'frames')
        annotated_path = os.path.join(coach_dir, 'annotated')
        os.makedirs(annotated_path, exist_ok=True)
        detector.detect_components(frames_path, annotated_path)

    # Step 4: Color Consistency Validation
    validator = ColorValidator()
    for coach_video in coach_videos:
        coach_dir = os.path.dirname(coach_video)
        frames_path = os.path.join(coach_dir, 'frames')
        validator.validate_colors(frames_path)

    # Step 5: Coverage Frame Selection
    selector = CoverageSelector()
    selected_frames = {}
    for coach_video in coach_videos:
        coach_dir = os.path.dirname(coach_video)
        frames_path = os.path.join(coach_dir, 'frames')
        selected_frames[coach_dir] = selector.select_coverage_frames(frames_path)

    # Step 6: Report Generation
    generator = ReportGenerator(reports_dir, train_number, coach_count, selected_frames)
    generator.generate_pdf_report()
    generator.generate_html_report()

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
