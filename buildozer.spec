[app]
# App ka naam jo phone par dikhega
title = Apple Doctor

# Package name (bina space ke)
package.name = appledoctor
package.domain = org.rahilafzal

# Source code ki location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Sabse zaroori: Libraries jo app ko chahiye
requirements = python3,kivy,google-generativeai,pillow,requests

# Android Permissions
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Android orientation
orientation = portrait

# (int) Target Android API
android.api = 31

# (list) Architectures jo support karni hain
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
