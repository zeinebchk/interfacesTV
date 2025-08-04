[app]
# Titre et identification
title = tvApp
package.name = tvapp
package.domain = org.test

# Configuration spécifique Android TV
android.meta_data = android.app.uses_leanback=true
orientation = landscape
fullscreen = 1

# Requirements (version unifiée)
requirements = 
    python3,
    kivy==2.3.1,
    kivymd==1.2.0,
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

# Intent filter pour Android TV
android.manifest.intent_filters = 
<intent-filter>
    <action android:name="android.intent.action.MAIN"/>
    <category android:name="android.intent.category.LEANBACK_LAUNCHER"/>
</intent-filter>

# Options supplémentaires
p4a.bootstrap = sdl2
android.allow_backup = false
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1
