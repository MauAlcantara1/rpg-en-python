## Español

# RPG en Python — Base Lunar Omega

Juego RPG de texto desarrollado en Python que incluye sistema de combate por turnos, inventario, enemigos y progresión del jugador. El proyecto está enfocado en aplicar lógica de programación, estructuras de datos y diseño modular, permitiendo expandir fácilmente nuevas mecánicas como habilidades, misiones o mapas.

---

## Descripción

**Base Lunar Omega** es un RPG de texto por consola ambientado en una base científica lunar. Un meteorito emergió desde el interior de la luna y liberó una criatura que esparció un virus por todas las instalaciones. El jugador despierta sin memoria en la enfermería y debe explorar más de 25 salas divididas en 7 zonas para descubrir qué ocurrió y encontrar una salida.

A diferencia de un juego lineal, este sistema utiliza un mapa ramificado donde cada decisión de movimiento, investigación y combate afecta las posibilidades del jugador.

---

## Funcionalidades

### Sistema de Clases y Personaje

* El jugador elige un nombre y una clase al inicio:

  * `Soldado` → alta vida y daño
  * `Médico` → alta energía y curación
  * `Ingeniero` → equilibrio entre daño y energía
  * `Explorador` → alto crítico y movilidad
* Cada clase tiene estadísticas únicas: vida, daño, crítico y energía

---

### Exploración por Salas

* Más de 25 salas organizadas en 7 zonas:

  * Científica, Civil, Militar, Política, Minera, Energía y Exploración exterior
* Navegación por menú numérico entre salas conectadas
* Cada sala tiene descripción, objetos investigables y conexiones únicas

---

### Sistema de Objetos e Investigación

* El jugador puede inspeccionar objetos dentro de cada sala
* Los objetos pueden tener eventos:

  * `curar` → restaura puntos de vida
  * `pista` → revela información narrativa
* Los objetos de un solo uso se marcan como `usado: True` tras activarse

---

### Sistema de Combate por Turnos

* Enemigos únicos en salas específicas (en desarrollo)
* Combate basado en estadísticas de clase
* Posibilidad de golpe crítico según atributo del personaje

---

### Sistema de Log Narrativo

* La intro genera texto progresivo con pausas dramáticas
* Ejemplo de salida:

  ```
  [ERROR] Memoria corrupta
  [ERROR] Soporte vital al 32%
  —Reiniciando protocolo médico—
  Abres los ojos.
  ```

---

## Estructura del Proyecto

```
rpg-en-python/
│
├── main.py
├── salas.py
│
├── zona_cientifica/
│   ├── laboratorio
│   ├── laboratorio_biologico
│   └── cuarentena
│
├── zona_civil/
│   ├── dormitorios
│   └── comedor
│
├── zona_militar/
│   ├── hangar
│   └── domo_observacion
│
├── zona_politica/
│   ├── sala_control
│   ├── telecomunicaciones
│   └── reactor
│
├── zona_minera/
│   ├── tunel_extraccion
│   ├── frente_minero
│   ├── deposito_mineral
│   └── sala_procesado
│
├── zona_energia/
│   ├── planta_generacion
│   ├── almacen_nuclear
│   ├── baterias_respaldo
│   └── control_termico
│
└── zona_exploracion/
    ├── esclusa_salida
    ├── zona_impacto
    ├── garaje_rovers
    ├── catacumbas
    ├── antena_rescate
    └── puesto_avanzada
```

---

## ¿Cómo funciona?

1. El jugador crea su personaje eligiendo nombre y clase
2. El sistema calcula estadísticas según la clase elegida
3. Se muestra la intro narrativa con pausas dramáticas
4. El jugador navega entre salas usando el menú principal
5. En cada sala puede investigar objetos, curarse o moverse
6. Los eventos de los objetos modifican el estado del jugador
7. Los enemigos activan combate por turnos al entrar a su sala

---

## Uso

```bash
python main.py
```

El juego solicita nombre y clase al inicio. No requiere archivos adicionales ni configuración previa.

---

## Tecnologías Utilizadas

* Python 3
* `time` (pausas narrativas y timing)
* `random` (críticos y variación de combate)
* Diccionarios anidados (estructura de salas y objetos)

---

## Mejoras Futuras

* Sistema de combate por turnos completo
* Inventario con objetos recolectables
* Pistas narrativas acumulativas entre salas
* Finales alternativos (antena de rescate, reactor, núcleo)
* Habilidades especiales por clase
* Sistema de guardado de partida
* Interfaz de color en terminal con `colorama`

---

## Mau Alcantara

Desarrollado como parte del aprendizaje en Python, estructuras de datos y diseño de videojuegos por texto.

---

## ¿Por qué es relevante este proyecto?

Este proyecto demuestra:

* Diseño modular con separación de datos y lógica
* Uso de diccionarios anidados como base de datos ligera
* Programación orientada a estructuras de datos
* Resolución de problemas de navegación y estado del jugador

---

## Licencia

Proyecto de código abierto disponible para fines educativos.

---

## ENGLISH

# Python RPG — Lunar Base Omega

A text-based RPG developed in Python featuring a turn-based combat system, inventory, enemies, and player progression. The project focuses on applying programming logic, data structures, and modular design, making it easy to expand with new mechanics like skills, quests, or maps.

---

## Overview

**Lunar Base Omega** is a console text RPG set in a scientific lunar base. A meteorite emerged from inside the moon and released a creature that spread a virus throughout the facility. The player wakes up with no memory in the medical bay and must explore over 25 rooms across 7 zones to discover what happened and find a way out.

Unlike a linear game, this system uses a branching map where every decision — movement, investigation, and combat — affects the player's options.

---

## Features

### Class and Character System

* The player chooses a name and class at the start:

  * `Soldier` → high health and damage
  * `Medic` → high energy and healing
  * `Engineer` → balanced damage and energy
  * `Explorer` → high critical rate and mobility
* Each class has unique stats: health, damage, critical, and energy

---

### Room-Based Exploration

* Over 25 rooms organized across 7 zones:

  * Scientific, Civil, Military, Political, Mining, Energy, and Exterior Exploration
* Navigation via numbered menus between connected rooms
* Each room has a unique description, investigable objects, and connections

---

### Object Investigation System

* The player can inspect objects inside each room
* Objects can trigger events:

  * `heal` → restores health points
  * `clue` → reveals narrative information
* Single-use objects are flagged as `used: True` after activation

---

### Turn-Based Combat System

* Unique enemies in specific rooms (in development)
* Combat based on class statistics
* Critical hit chance based on character attribute

---

### Narrative Log System

* The intro generates progressive text with dramatic pauses
* Example output:

  ```
  [ERROR] Corrupted memory
  [ERROR] Life support at 32%
  —Restarting medical protocol—
  You open your eyes.
  ```

---

## Project Structure

```
rpg-en-python/
│
├── main.py
├── salas.py
│
├── scientific_zone/
│   ├── laboratory
│   ├── biological_lab
│   └── quarantine
│
├── civil_zone/
│   ├── dormitories
│   └── cafeteria
│
├── military_zone/
│   ├── hangar
│   └── observation_dome
│
├── political_zone/
│   ├── control_room
│   ├── telecommunications
│   └── reactor
│
├── mining_zone/
│   ├── extraction_tunnel
│   ├── mining_front
│   ├── mineral_deposit
│   └── processing_room
│
├── energy_zone/
│   ├── power_plant
│   ├── nuclear_storage
│   ├── backup_batteries
│   └── thermal_control
│
└── exploration_zone/
    ├── exit_airlock
    ├── impact_zone
    ├── rover_garage
    ├── catacombs
    ├── rescue_antenna
    └── outpost
```

---

## How It Works

1. The player creates their character by choosing a name and class
2. The system calculates stats based on the chosen class
3. The narrative intro plays with dramatic timing
4. The player navigates between rooms using the main menu
5. In each room they can investigate objects, heal, or move
6. Object events modify the player's state
7. Enemies trigger turn-based combat when their room is entered

---

## Usage

```bash
python main.py
```

The game prompts for a name and class at startup. No additional files or prior configuration needed.

---

## Technologies Used

* Python 3
* `time` (narrative pacing and timing)
* `random` (criticals and combat variation)
* Nested dictionaries (room and object structure)

---

## Future Improvements

* Full turn-based combat system
* Inventory with collectible items
* Cumulative narrative clues across rooms
* Alternate endings (rescue antenna, reactor, meteorite core)
* Class-specific special abilities
* Save system
* Terminal color interface with `colorama`

---

## Mau Alcantara

Developed as part of a learning journey in Python, data structures, and text-based game design.

---

## Why This Project Matters

This project demonstrates:

* Modular design with separation of data and logic
* Nested dictionaries as a lightweight database
* Data-structure-oriented programming
* Navigation and state management problem solving

---

## License

This project is open-source and available for educational purposes.
