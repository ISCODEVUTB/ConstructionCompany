#!/bin/bash

# Instalar Flutter
echo "Instalando Flutter SDK..."
FLUTTER_VERSION="3.22.0"
wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_${FLUTTER_VERSION}-stable.tar.xz
tar xf flutter_linux_${FLUTTER_VERSION}-stable.tar.xz
export PATH="$PATH:$(pwd)/flutter/bin"

# Verificar instalación
flutter --version

# Construir la aplicación
echo "Construyendo aplicación Flutter..."
flutter pub get
flutter build web --release

echo "Build completado exitosamente!"