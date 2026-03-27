salas = {

    "inicio": {
        "descripcion": "Una sala médica descuidada...",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {
                "nombre": "Camilla",
                "mensaje": "Está manchada de sangre... sigue húmeda.",
                "evento": None
            },
            "2": {
                "nombre": "Monitor médico",
                "mensaje": "Parpadea con signos vitales inestables...",
                "evento": None
            },
            "3": {
                "nombre": "Botiquín tirado",
                "mensaje": "Encuentras suministros útiles.",
                "evento": "curar",
                "usado": False
            }
        },
        "opciones": {
            "1": {"texto": "Ir al laboratorio", "destino": "laboratorio"},
            "2": {"texto": "Salir al pasillo principal", "destino": "pasillo"}
        }
    },

    "pasillo": {
        "descripcion": "Un pasillo oscuro que conecta todas las zonas de la base.",
        "opciones": {
            "1": {"texto": "Zona científica", "destino": "laboratorio"},
            "2": {"texto": "Zona civil", "destino": "dormitorios"},
            "3": {"texto": "Zona militar", "destino": "hangar"},
            "4": {"texto": "Zona política", "destino": "sala_control"},
            "5": {"texto": "Volver a enfermería", "destino": "inicio"}
        }
    },

    "laboratorio": {
        "descripcion": "Un laboratorio destruido con luces parpadeantes.",
        "opciones": {
            "1": {"texto": "Ir a laboratorio biológico", "destino": "laboratorio_biologico"},
            "2": {"texto": "Ir a cuarentena", "destino": "cuarentena"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "laboratorio_biologico": {
        "descripcion": "Experimentos fallidos y muestras contaminadas.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Microscopio", "mensaje": "Las células no son humanas.", "evento": None},
            "2": {"nombre": "Centrífuga", "mensaje": "Restos de sangre infectada.", "evento": None},
            "3": {"nombre": "Frasco", "mensaje": "Un líquido oscuro vibra.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Ir a archivo central", "destino": "archivo_central"},
            "2": {"texto": "Volver al laboratorio", "destino": "laboratorio"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "cuarentena": {
        "descripcion": "Módulo sellado con marcas de desesperación.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Camilla", "mensaje": "Las correas están rotas.", "evento": None},
            "2": {"nombre": "Ventana", "mensaje": "Algo se mueve afuera.", "evento": None},
            "3": {"nombre": "Registro", "mensaje": "Mutaciones aceleradas.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver al laboratorio", "destino": "laboratorio"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "dormitorios": {
        "descripcion": "Habitaciones abandonadas del personal.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Cama", "mensaje": "Notas de paranoia.", "evento": None},
            "2": {"nombre": "Locker", "mensaje": "Objetos personales.", "evento": None},
            "3": {"nombre": "Agua", "mensaje": "Te recupera un poco.", "evento": "curar"}
        },
        "opciones": {
            "1": {"texto": "Ir al comedor", "destino": "comedor"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "comedor": {
        "descripcion": "Cafetería en silencio absoluto.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Máquina", "mensaje": "Bebida rara pero útil.", "evento": "curar"},
            "2": {"nombre": "Mesa", "mensaje": "Marcas de arrastre.", "evento": None},
            "3": {"nombre": "Pantalla", "mensaje": "Mensaje de emergencia.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver a dormitorios", "destino": "dormitorios"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "sala_control": {
        "descripcion": "Centro de mando de la base.",
        "opciones": {
            "1": {"texto": "Ir al archivo central", "destino": "archivo_central"},
            "2": {"texto": "Ir a telecomunicaciones", "destino": "sala_telecomunicaciones"},
            "3": {"texto": "Ir al reactor", "destino": "reactor"},
            "4": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "archivo_central": {
        "descripcion": "Registros secretos y decisiones ocultas.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Terminal", "mensaje": "Datos del meteorito.", "evento": None},
            "2": {"nombre": "Documentos", "mensaje": "Encubrimiento.", "evento": None},
            "3": {"nombre": "Mapa", "mensaje": "Mapa de la base.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver a sala de control", "destino": "sala_control"},
            "2": {"texto": "Volver al laboratorio biológico", "destino": "laboratorio_biologico"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "sala_telecomunicaciones": {
        "descripcion": "Mensajes perdidos hacia la Tierra.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Consola", "mensaje": "Señales de auxilio.", "evento": None},
            "2": {"nombre": "Servidor", "mensaje": "Llamadas grabadas.", "evento": None},
            "3": {"nombre": "Kit", "mensaje": "Recuperas energía.", "evento": "curar"}
        },
        "opciones": {
            "1": {"texto": "Volver a sala de control", "destino": "sala_control"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "hangar": {
        "descripcion": "Hangar con vehículos dañados.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Rover", "mensaje": "Kit útil.", "evento": "curar"},
            "2": {"nombre": "Herramientas", "mensaje": "Faltan piezas.", "evento": None},
            "3": {"nombre": "Puerta", "mensaje": "Algo entró.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Ir al domo de observación", "destino": "domo_observacion"},
            "2": {"texto": "Ir al núcleo del meteorito", "destino": "nucleo_meteorito"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "domo_observacion": {
        "descripcion": "Vista al exterior lunar contaminado.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Telescopio", "mensaje": "Restos en la superficie.", "evento": None},
            "2": {"nombre": "Panel", "mensaje": "Lecturas erráticas.", "evento": None},
            "3": {"nombre": "Silla", "mensaje": "Alguien vigilaba.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver al hangar", "destino": "hangar"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "reactor": {
        "descripcion": "El núcleo energético es inestable.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Panel", "mensaje": "Riesgo alto.", "evento": None},
            "2": {"nombre": "Tubería", "mensaje": "Fuga congelada.", "evento": None},
            "3": {"nombre": "Botiquín", "mensaje": "Suministros.", "evento": "curar"}
        },
        "opciones": {
            "1": {"texto": "Volver a sala de control", "destino": "sala_control"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "nucleo_meteorito": {
        "descripcion": "El origen del horror.",
        "enemigo": "criatura_origen",
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Fragmento", "mensaje": "Late...", "evento": None},
            "2": {"nombre": "Restos", "mensaje": "Intentaron contenerlo.", "evento": None},
            "3": {"nombre": "Registro", "mensaje": "No puede morir.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Huir al hangar", "destino": "hangar"}
        }
    }
}