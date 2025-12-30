# Wagon Coach Counting & Full-Coverage Report

This project implements a pipeline for detecting and counting wagon coaches in train videos, extracting frames, detecting components like doors, and generating a comprehensive coverage report.

## Features

- **Video Splitting**: Splits input video into segments for each coach.
- **Coach Counting**: Counts the number of coaches in the train.
- **Frame Extraction**: Extracts frames from each coach's video segment.
- **Component Detection**: Uses YOLO for detecting doors and their states (open/closed).
- **Color Validation**: Ensures color consistency across frames of the same coach.
- **Coverage Selection**: Selects minimal set of frames for full wagon coverage.
- **Report Generation**: Generates PDF and HTML reports with selected frames.

## Project Structure

```
wagon_coverage_project/
│
├── data/
│   ├── input_video/
│   │   └── train_video.mp4
│   ├── frames/
│   ├── coaches/
│   │   ├── 12309_1/
│   │   │   ├── 12309_1.mp4
│   │   │   ├── frames/
│   │   │   └── annotated/
│   │   └── ...
│   └── reports/
│       ├── Wagon_Coverage_Report.pdf
│       └── Wagon_Coverage_Report.html
│
├── models/
│   └── yolo/
│       ├── yolov8.pt
│       └── classes.txt
│
├── src/
│   ├── video_splitter.py
│   ├── frame_extractor.py
│   ├── coach_counter.py
│   ├── component_detector.py
│   ├── color_validator.py
│   ├── coverage_selector.py
│   ├── report_generator.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone or download the project.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Place the input video in `data/input_video/CCTV_HZBN_DHN_1_LEFT_UP_20251230_064707_fs.mp4` (or update the path in `main.py` if using a different video).
4. Download YOLOv8 model weights and place in `models/yolo/yolov8.pt`.

## Usage

Navigate to the project directory and run the main script:
```
cd wagon_coverage_project
python main.py
```

This will process the video and generate the reports in `data/reports/`.

This will process the video and generate the reports in `data/reports/`.

## Key Components

- **VideoSplitter**: Splits video into coach segments using optical flow and gap detection.
- **FrameExtractor**: Extracts frames from each coach video.
- **ComponentDetector**: Uses YOLO to detect doors and their states.
- **ColorValidator**: Checks color consistency across frames.
- **CoverageSelector**: Selects representative frames for coverage.
- **ReportGenerator**: Creates PDF and HTML reports.

## Limitations

- Requires pre-trained YOLO model for component detection.
- Assumes side-view train videos.
- Color validation is basic; may need refinement for complex scenarios.

## Submission

- Code: Submit via GitHub or zip file.
- Demo: Screen record explaining features and upload to Google Drive.
