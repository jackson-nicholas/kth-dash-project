KTH Group Project — Adaptive DASH Simulation

Course: EP2120 Internetworking (Fall 2025)
Team: Naicheng Jiang, Jairui Pan. Shentong Wang

Overview

This project implements a simplified Dynamic Adaptive Streaming over HTTP (DASH) simulation in Python.
It models both ideal adaptive bitrate switching (offline simulation) and real network adaptation using Linux traffic control (tc) and FFmpeg.

Repository Contents

dash_client.py	
Offline DASH simulation with adaptive bitrate selection based on bandwidth traces.

real_dash_test.py	
Real-time DASH test using network throttling (tc) and download monitoring.

dash_result.png	
Visualization of bitrate adaptation results in simulation.

real_dash_result.png	
Visualization of results in a real test environment.

.gitignore	
Ignores large video files and temporary outputs.

README.md	Project documentation (this file).


Requirements

Run inside an Ubuntu/Debian environment or a Linux-based container (e.g. Kathara, WSL) with the following packages:

sudo apt update
sudo apt install -y ffmpeg python3 python3-pip iproute2
pip install requests matplotlib



How to Run

1. Offline Simulation (dash_client.py)

python3 dash_client.py

This simulates adaptive video streaming with synthetic bandwidth traces and produces dash_result.png.

2. Real Network Test (real_dash_test.py)
Make sure you have root access (for tc command):

sudo python3 real_dash_test.py


This dynamically changes network conditions and logs the adaptation behavior.


Video Samples

The .mp4 video samples (360p, 480p, 720p) are not uploaded to GitHub due to file size limits.
They are available here:
[Google Drive / OneDrive link here – to be filled by you]

Download them and place in the same directory before running the scripts.


	
Contributors

Naicheng Jiang (repo maintainer)
Jiarui Pan
Shentong Wang


*Notes

Large media files are excluded via .gitignore

The project is open-source and intended for educational use under KTH course policies.
