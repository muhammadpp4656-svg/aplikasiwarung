[app]

# (str) Title of your application
title = Aplikasi Keuangan warung

# (str) Package name
package.name = keuanganwarung

# (str) Package domain
package.domain = com.warung

# (str) Application version
version = 0.1

# (str) Source code where the main.py lives
source.dir = .

# (list) Application requirements
requirements = python3,kivy,sqlite3,kivy_garden.graph,requests

# (str) Main application file
main.py = main.py

# (list) List of exclusions for packaging
# exclude_dirs = tests, docs
# include_exts = png, jpg, kv, atlas

# (int) Android API target level
android.api = 33

# (int) Minimum Android API target level
android.minapi = 21

# (list) Android permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (list) Android features
# android.features =

# (str) Android presplash color
# android.presplash_color = #ffffff

# (str) Android presplash image
# android.presplash_image = data/presplash.png

# (str) Android icon path
# android.icon_path = data/icon.png

# (str) Path to keystore
# keystore = android.keystore

# (str) Path to keystore password
# keystore.pass = somepass

[build]

# (bool) Use the Android NDK provided by Kivy
# use_ndk_from_kivy = True

# (int) Number of processes to use for compilation
# build.jobs = 1

# (str) Path to the Android SDK
# android.sdk = /home/user/android-sdk

# (str) Path to the Android NDK
# android.ndk = /home/user/android-ndk

# (bool) Add a shortcut to the application on the desktop
# desktop.shortcut = False

# (bool) Automatically check for required dependencies
# check.deps = True

[android]
# (str) Android NDK version
# ndk = 25b

# (bool) Automatically sign the APK
# release = False

# (str) Path to keystore
# keystore = android.keystore

# (str) Path to keystore password
# keystore.pass = somepass

# (str) Path to a file containing a list of permissions
# android.permissions =

# (list) Android features
# android.features =

# (int) Set the build number for the Android version code
# android.version_code = 1

[ios]
# (list) List of Python packages to include
# python_packages =
# (str) Path to the iOS SDK
# ios.sdk = /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk

# (str) Path to the iOS NDK
# ios.ndk = /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang

[osx]
# (list) List of Python packages to include
# python_packages =
# (str) Path to the OSX SDK
# osx.sdk = /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk

[win]
# (list) List of Python packages to include
# python_packages =
# (str) Path to the Windows SDK
# win.sdk = C:\Program Files (x86)\Windows Kits\10\bin\10.0.18362.0\x64\rc.exe

[linux]
# (list) List of Python packages to include
# python_packages =
# (str) Path to the Linux SDK
# linux.sdk = /usr/share/doc/python-dev/README.Debian.gz

[p4a]
# (str) Path to the Android build system
# p4a.path =
# (str) Path to the iOS build system
# p4a.path_ios =