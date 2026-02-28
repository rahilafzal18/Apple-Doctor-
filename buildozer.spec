[app]
title = Apple Doctor
package.name = appledoctor
package.domain = org.rahilafzal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requirements for the app
requirements = python3,kivy==2.2.1,requests,certifi,pillow

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# --- Android Specific Settings (Fixed) ---
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.0
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
