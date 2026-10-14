[app]

# (str) Title of your application
title = Naumii AI

# (str) Package name
package.name = naumiiai

# (str) Package domain (needed for android packaging)
package.domain = org.naumii

# (list) Source files to include (let it include all python and general files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) Application requirements
# Add requests, certifi, urllib3 so API calls to Gemini work smoothly
requirements = python3,kivy,requests,certifi,urllib3,idna,charset-normalizer

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
