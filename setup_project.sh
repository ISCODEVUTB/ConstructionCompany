#!/bin/bash

# Script para verificar y corregir la estructura del proyecto
# Ejecutar desde la raíz del repositorio

echo "Verificando estructura del proyecto Construction Company..."

# 1. Crear la estructura de directorios si no existe
mkdir -p src/backend/app/tests
mkdir -p src/backend/app/api
mkdir -p src/backend/app/models
mkdir -p src/backend/app/logic

# 2. Crear archivos __init__.py si no existen
touch src/backend/__init__.py
touch src/backend/app/__init__.py
touch src/backend/app/tests/__init__.py
touch src/backend/app/api/__init__.py
touch src/backend/app/models/__init__.py
touch src/backend/app/logic/__init__.py

# 3. Verificar y crear archivo main.py básico si no existe
if [ ! -f "src/backend/app/main.py" ]; then
    echo "Creando archivo main.py básico..."
    cat > src/backend/app/main.py << EOL
def example_function():
    return "Hello World"

if __name__ == "__main__":
    print(example_function())
EOL
fi

# 4. Verificar y crear archivo de test básico si no existe
if [ ! -f "src/backend/app/tests/test_basico.py" ]; then
    echo "Creando archivo test_basico.py..."
    cat > src/backend/app/tests/test_basico.py << EOL
from ..main import example_function

def test_example():
    assert example_function() == "Hello World"
EOL
fi

# 5. Verificar estructura final
echo "Estructura de directorios creada:"
find src -type d | sort

echo "Archivos Python creados:"
find src -name "*.py" | sort

echo "¡Estructura del proyecto preparada para SonarCloud!"
echo "Recuerda ejecutar los tests antes de subir a SonarCloud:"
echo "cd \$(git rev-parse --show-toplevel) && PYTHONPATH=. pytest src/backend/app/tests/ --cov=src/backend/app --cov-report=xml:coverage.xml"