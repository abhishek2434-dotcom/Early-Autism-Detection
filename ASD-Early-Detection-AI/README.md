# AI-Driven Early Detection of Autism in Toddlers

## Problem Statement
This project aims to detect early signs of Autism Spectrum Disorder (ASD) in toddlers.

##  Objectives
We focus on detecting:
1. Reduced Eye Contact
2. Repetitive Behaviors
3. Limited Social Reciprocity

## Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy

## How It Works:
- Uses webcam/video to track facial and pose keypoints
- Detects eye contact using eye landmarks
- Detects repetitive motions using pose estimation
- Checks for social reciprocity based on gesture response

## How to Run:
1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python main.py`

## Folder Structure:
- `main.py`: Entry point
- `utils/`: Helper scripts
- `models/`: Pose model logic
- `sample_videos/`: Test videos
