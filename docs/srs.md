# Especificación de requisitos de software (SRS) para Construction Company  
**Versión 1.1 aprobado**  
**Preparado por**: Jesús Andrés Pérez Fuentes, Gabriel Elias Leon Simancas, Valery Georgina Aurela Perez  
**Universidad Tecnológica de Bolivar**  
**Fecha**: 9/04/2025  

---

## Tabla de contenido  
1. [Introducción](#1-introducción)  
2. [Descripción general](#2-descripción-general)  
   - 2.1 [Características del producto](#21-características-del-producto)  
   - 2.2 [Clases de usuarios](#22-clases-de-usuarios-y-características)  
   - 2.3 [Limitaciones](#23-limitaciones-de-diseño-y-aplicación)  
   - 2.4 [Documentación](#24-documentación-del-usuario)  
   - 2.5 [Supuestos](#25-supuestos-y-dependencias)  
3. [Características del sistema](#3-características-del-sistema)  
   - 3.1 [MVP](#31-mvp--producto-mínimo-viable)  
   - 3.2 [Secuencias estímulo/respuesta](#32-secuencias-de-estímulorespuesta)  
   - 3.3 [Requisitos funcionales](#321-requisitos-funcionales)  
4. [Requisitos de interfaz](#4-requisitos-de-la-interfaz)  
   - 4.1 [Interfaces de usuario](#41-interfaces-de-usuario)  
   - 4.2 [Interfaces de hardware](#42-interfaces-de-hardware)  
   - 4.3 [Interfaces de software](#43-interfaces-de-software)  
5. [Requisitos no funcionales](#5-otros-requisitos-no-funcionales)  
   - 5.1 [Desempeño](#51-requerimientos-de-desempeño)  
   - 5.2 [Seguridad](#52-requisitos-de-seguridad)  
6. [Referencias](#7-referencias)  
7. [Apéndices](#apéndices)  

---

### 1. Introducción  
Software para optimizar la gestión en empresas de construcción, con beneficios como:  
- Automatización de procesos.  
- Centralización de información.  
- Mayor visibilidad del avance de proyectos.  

---

### 2. Descripción general  
Solución independiente con arquitectura de microservicios, enfocada en:  
- Gestión de proyectos.  
- Control de costos.  
- Seguimiento de recursos.  

#### 2.1 Características del producto  
- Gestión de proyectos y recursos.  
- Control de inventarios y compras.  
- Generación de informes automatizados.  

#### 2.2 Clases de usuarios y características  
| Rol | Acceso |  
|------|--------|  
| Gerentes | Todas las funcionalidades. |  
| Supervisores | Actualización de estado de proyectos. |  
| Administrativos | Gestión financiera limitada. |  

#### 2.3 Limitaciones de diseño y aplicación  
- Integración con ERPs existentes.  
- Compatibilidad con dispositivos móviles.  
- Cumplimiento de normativas de protección de datos.  

#### 2.4 Documentación del Usuario  
- Manuales, guías rápidas y tutoriales interactivos.  

#### 2.5 Supuestos y dependencias  
- Infraestructura informática básica en las empresas.  
- Capacitación para usuarios clave.  

---

### 3. Características del sistema  
#### 3.1 MVP – Producto Mínimo Viable  
- **Gestión centralizada**: Equipos, inventarios y proyectos.  
- **APIs de integración**: Conexión con software externo.  
- **Dashboards**: Visualización de datos clave.  

#### 3.2 Secuencias de estímulo/respuesta  
| Estímulo | Respuesta |  
|----------|-----------|  
| Consulta de disponibilidad de equipos | Muestra estado y ubicación. |  
| Asignación de recursos | Sugiere recursos disponibles. |  

#### 3.2.1 Requisitos funcionales  
| ID | Nombre | Descripción | Prioridad |  
|----|--------|-------------|-----------|  
| RF01 | Gestión de Empleados | CRUD de empleados. | Alta |  
| RF03 | Gestión de Materiales | Control de stock. | Alta |  

---

### 4. Requisitos de la interfaz  
#### 4.1 Interfaces de Usuario  
- Panel de control en tiempo real.  
- Acceso restringido por roles.  

#### 4.2 Interfaces de hardware  
- Compatibilidad con Windows, MacOS, Android e iOS.  

#### 4.3 Interfaces de software  
- APIs REST para integración con ERPs.  

---

### 5. Otros requisitos No funcionales  
#### 5.1 Requerimientos de desempeño  
- Tiempo de respuesta < 2 segundos.  
- Soporte para 500 usuarios concurrentes.  

#### 5.2 Requisitos de seguridad  
- Cifrado AES-256.  
- Autenticación multifactor (MFA).  

---

### 7. Referencias  
- IEEE 830-1998.  
- ISO/IEC 25010:2011.  

---

### Apéndices  
#### Arquitectura de microservicios  
- Módulos independientes (ej: gestión de proyectos) comunicados via APIs REST.  

#### Glosario  
- **Gateway**: Punto de acceso centralizado para APIs.  
- **Silo de Datos**: Sistema aislado sin integración.  

