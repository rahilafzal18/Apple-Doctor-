#!/bin/bash
# 1. System updates
sudo apt-get update
sudo apt-get install -y build-essential git python3 python3-dev ffmpeg \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# 2. Tools installation
pip install --user --upgrade buildozer cython==0.29.33 wheel

# 3. FIX: Aidl not found and License error
# Ye command saare licenses ko automatic 'Yes' bol degi
mkdir -p ~/.android
touch ~/.android/repositories.cfg
yes | sdkmanager --licenses || true
