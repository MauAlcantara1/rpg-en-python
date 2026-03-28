# RPG en Python — Base Lunar Omega

> Juego RPG de texto desarrollado en Python. Sobrevive en una base lunar abandonada, descubre la verdad detrás del meteorito y enfrenta la criatura que acabó con la tripulación.

---

## Descripción

**Base Lunar Omega** es un RPG de texto por consola ambientado en una base científica lunar. Un meteorito impactó la superficie y liberó una criatura que esparció un virus por todas las instalaciones. El jugador despierta sin memoria en la enfermería y debe explorar más de 25 salas para descubrir qué ocurrió y encontrar una salida.

El proyecto aplica conceptos de programación orientada a datos, estructuras modulares y lógica de progresión, con un diseño pensado para escalar fácilmente con nuevas mecánicas.

---

## Características

- Sistema de clases con estadísticas diferenciadas (soldado, médico, ingeniero, explorador)
- Más de 25 salas divididas en 7 zonas: científica, civil, militar, política, minera, energía y exploración exterior
- Sistema de investigación de objetos con eventos (curación, pistas narrativas)
- Enemigos por sala con sistema de combate por turnos
- Narrativa ramificada con finales alternativos
- Diseño modular: las salas están separadas del juego principal para facilitar expansión

---

## Estructura del proyecto

```
rpg-en-python/
├── main.py          # Bucle principal del juego
├── salas.py         # Definición de todas las salas, objetos y conexiones
├── combate.py       # Lógica de combate por turnos (en desarrollo)
└── README.md
```

---

## Instalación y uso

No requiere dependencias externas. Solo Python 3.

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/rpg-en-python.git
cd rpg-en-python

# Ejecutar el juego
python main.py
```

---

## Clases disponibles

| Clase | Vida | Daño | Crítico | Energía |
|---|---|---|---|---|
| Soldado | 15 | 6 | 3 | 2 |
| Médico | 12 | 3 | 2 | 5 |
| Ingeniero | 10 | 4 | 3 | 4 |
| Explorador | 11 | 5 | 4 | 3 |

---

## Mapa de zonas

```
                    [ Enfermería ]
                         |
                  [ Pasillo central ]
       ┌──────┬──────┬──────┬──────┬──────┬──────┐
  Científica Civil Militar Política Minería Energía Exploración
```

Cada zona tiene entre 2 y 6 subnodos conectados, con objetos investigables, enemigos opcionales y pistas narrativas.

---

## Cómo está estructurado `salas.py`

Cada sala es un diccionario con la siguiente estructura:

```python
"nombre_sala": {
    "descripcion": "Texto que ve el jugador al entrar.",
    "enemigo": None,           # nombre del enemigo o None
    "explorada": False,
    "objetos": {
        "1": {
            "nombre": "Objeto",
            "mensaje": "Texto al investigar.",
            "evento": "curar",  # curar | pista | None
            "usado": False
        }
    },
    "opciones": {
        "1": {"texto": "Ir a...", "destino": "nombre_sala"}
    }
}
```

---

## Roadmap

- [x] Sistema de salas y navegación
- [x] Clases de personaje con estadísticas
- [x] Sistema de objetos e investigación
- [x] Eventos de curación
- [ ] Sistema de combate por turnos
- [ ] Sistema de inventario
- [ ] Pistas narrativas acumulativas
- [ ] Finales alternativos (antena de rescate, reactor, núcleo)
- [ ] Enemigos con IA básica
- [ ] Habilidades especiales por clase
- [ ] Sistema de guardado

---

## Tecnologías

- Python 3
- Estructuras de datos nativas (diccionarios, listas)
- Módulos estándar: `random`, `time`

---

## Contribuir

Las salas nuevas se agregan directamente en `salas.py` siguiendo la estructura estándar. El juego las detecta automáticamente si están referenciadas en las `opciones` de otra sala.

---

## Licencia

MIT
