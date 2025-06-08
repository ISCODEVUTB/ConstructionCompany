#!/bin/bash
set -e

# Instalar Flutter SDK
wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_$FLUTTER_VERSION-stable.tar.xz
tar xf flutter_linux_$FLUTTER_VERSION-stable.tar.xz
export PATH="$PATH:$(pwd)/flutter/bin"

# Instalar dependencias y construir
flutter pub get
flutter build web --release