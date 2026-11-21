# Software FJ — Sistema Integral de Gestión de Clientes, Servicios y Reservas

Sistema desarrollado en Python bajo el paradigma de **Programación Orientada a Objetos (POO)** para la gestión integral de clientes, servicios especializados y reservas de la empresa **Software FJ**. La aplicación opera completamente en memoria (sin motores de bases de datos) mediante listas y objetos, utilizando manejo avanzado de excepciones y registro continuo de eventos y fallos en archivo de logs.

- **Universidad:** Universidad Nacional Abierta y a Distancia (UNAD)
- **Unidad Gestora:** Escuela de Ciencias Básicas Tecnología e Ingeniería (ECBTI)
- **Programa:** Ingeniería de Sistemas
- **Curso:** Programación — Código `213023` (Fase 4 — Ejercicio 1)

---

## Equipo de Desarrollo

| # | Estudiante | Grupo | Módulo o Responsabilidad |
| :- | :--- | :--- | :--- |
| 1 | Rubén Darío Anaya Polo | 213023_552 | Entidad base, encapsulación de `Cliente` y documentación (`entidad.py`, `cliente.py`, `README.md`) |
| 2 | Carlos Alonso Ruiz Hernández | 213023_552 | Jerarquía de `Servicio`, polimorfismo y excepciones personalizadas (`servicios.py`, `excepciones.py`) |
| 3 | Erik Duway Carpeta Niño | 213023_552 | Ciclo de vida de `Reserva`, controlador `SistemaFJ` y simulación (`reserva.py`, `sistema.py`, `main.py`) |

---

## Estructura del Proyecto

```text
Software-FJ/
├── entidad.py        # Clase abstracta base Entidad con identificador protegido
├── cliente.py        # Clase Cliente con encapsulación (@property) y validaciones estrictas
├── servicios.py      # Clase abstracta Servicio y 3 servicios especializados
├── reserva.py        # Clase Reserva con flujo de estados y encadenamiento de excepciones
├── excepciones.py    # Excepciones personalizadas derivadas de ErrorSistema
├── sistema.py        # Clase SistemaFJ que administra clientes, servicios y reservas en memoria
├── main.py           # Punto de entrada con simulación de operaciones válidas e inválidas
├── software_fj.log   # Archivo generado automáticamente con el historial de eventos y errores
└── README.md         # Documentación técnica y guía de ejecución del proyecto
```
