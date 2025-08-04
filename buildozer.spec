[app]
title = tvApp
package.name = tvapp
package.domain = org.test
version = 0.1

orientation = landscape
fullscreen = 1

requirements =
    python3,
    kivy==2.3.1,
    kivymd==1.2.0,
    sdl2_ttf==2.0.15,
    sdl2_image==2.0.5,
    sdl2_mixer==2.0.4,
    python-socketio,
    android

android.permissions =
    INTERNET,
    ACCESS_NETWORK_STATE,
    WAKE_LOCK

android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

android.meta_data = android.app.uses_leanback=true

android.manifest.intent_filters =
<intent-filter>
    <action android:name="android.intent.action.MAIN"/>
    <category android:name="android.intent.category.LEANBACK_LAUNCHER"/>
</intent-filter>

[buildozer]
log_level = 2
warn_on_root = 1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
