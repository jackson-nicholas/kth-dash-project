# KTH Group Project: Adaptive DASH Simulation

This repository contains our group project for the KTH **Internetworking (IK2218)** course.  
We implemented a simplified **Dynamic Adaptive Streaming over HTTP (DASH)** simulation using Python.

---

## 🧠 Project Overview
The project simulates both **ideal (offline)** and **real network** adaptive video streaming using FFmpeg and Python.

Two main scripts:
- `dash_client.py`: Simulated adaptive bitrate switching based on random network bandwidth traces.
- `real_dash_test.py`: Tests adaptation under real network conditions using Linux `tc` and live download speed measurements.

---

## ⚙️ Requirements
Run inside an Ubuntu/Debian container or VM with the following packages:

```bash
sudo apt update
sudo apt install -y ffmpeg python3 python3-pip iproute2
pip install requests matplotlib
