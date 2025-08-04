[app]

# Titre et identification
title = tvApp
package.name = tvapp
package.domain = org.test

# Fichiers sources
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# Version
version = 0.1

# Requirements
requirements = 
    python3,
    kivy==2.2.1,
    kivymd==1.1.1,
    python-socketio,
    android

# Configuration Android TV
orientation = landscape
fullscreen = 1
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE,
    WAKE_LOCK

# Configuration spécifique TV
android.meta_data = 
    android.app.uses_leanback=true

android.manifest.intent_filters = 
<intent-filter>
    <action android:name="android.intent.action.MAIN"/>
    <category android:name="android.intent.category.LEANBACK_LAUNCHER"/>
</intent-filter>

# Options de build
p4a.bootstrap = sdl2
android.allow_backup = false
android.debug_artifact = apk

# Logs
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
