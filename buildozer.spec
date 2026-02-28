[app]
title = Apple Doctor
package.name = appledoctor
package.domain = org.rahilafzal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Sabse zaroori: In requirements ko dhyan se dekhein
requirements = python3,kivy==2.2.1,kivymd,google-generativeai,pillow,requests,certifi,urllib3

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# Android specific
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
