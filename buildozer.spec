[app]

# Titre et identification
title = tvApp
package.name = tvapp
package.domain = org.test
[app]

# (str) Titre de l'application
title = tvApp

# (str) Nom du package
package.name = tvapp

# (str) Domaine du package
package.domain = org.test

# Configuration spécifique Android TV
android.meta_data = android.app.uses_leanback=true
orientation = landscape
fullscreen = 1

# Requirements
requirements = 
    python3,
    kivy==2.2.1,
    kivymd==1.1.1,
    sdl2_ttf==2.0.15,
    sdl2_image==2.0.5,
    sdl2_mixer==2.0.4,
    python-socketio,
    android

# Permissions
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE,
    WAKE_LOCK

# Configuration build
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2

# Intent filter pour Android TV
android.manifest.intent_filters = 
<intent-filter>
    <action android:name="android.intent.action.MAIN"/>
    <category android:name="android.intent.category.LEANBACK_LAUNCHER"/>
</intent-filter>

[buildozer]
log_level = 2
warn_on_root = 1
# Fichiers sources
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# Version
version = 0.1

# Requirements
requirements = 
    python3,
    kivy==2.3.1,
    kivymd==1.2.0,
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
