#!/bin/bash
# 1. System updates aur libraries
sudo apt-get update
sudo apt-get install -y build-essential git python3 python3-dev ffmpeg \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# 2. Asli tools (Cython aur Buildozer) ko pehle hi install karna
pip install --user --upgrade pip
pip install --user --upgrade buildozer cython==0.29.33 wheel
