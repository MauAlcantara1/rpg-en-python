salas = {

  
    "inicio": {
        "descripcion": "Una sala médica descuidada. Las luces parpadean. Algo salió muy mal aquí.",
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
        "descripcion": "Un pasillo oscuro que conecta todas las zonas de la base. El zumbido de los conductos de ventilación es lo único que se escucha.",
        "opciones": {
            "1": {"texto": "Zona científica", "destino": "laboratorio"},
            "2": {"texto": "Zona civil", "destino": "dormitorios"},
            "3": {"texto": "Zona militar", "destino": "hangar"},
            "4": {"texto": "Zona política", "destino": "sala_control"},
            "5": {"texto": "Zona minera", "destino": "tunel_extraccion"},
            "6": {"texto": "Zona de energía", "destino": "planta_generacion"},
            "7": {"texto": "Zona de exploración", "destino": "esclusa_salida"},
            "8": {"texto": "Volver a enfermería", "destino": "inicio"}
        }
    },

    "laboratorio": {
        "descripcion": "Un laboratorio destruido con luces parpadeantes. Hay cristales rotos en el suelo.",
        "opciones": {
            "1": {"texto": "Ir a laboratorio biológico", "destino": "laboratorio_biologico"},
            "2": {"texto": "Ir a cuarentena", "destino": "cuarentena"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "laboratorio_biologico": {
        "descripcion": "Experimentos fallidos y muestras contaminadas. El olor es insoportable.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Microscopio", "mensaje": "Las células no son humanas. Nunca lo fueron.", "evento": None},
            "2": {"nombre": "Centrífuga", "mensaje": "Restos de sangre infectada con estructuras desconocidas.", "evento": None},
            "3": {"nombre": "Frasco sellado", "mensaje": "Un líquido oscuro vibra levemente. No lo toques.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Ir a archivo central", "destino": "archivo_central"},
            "2": {"texto": "Volver al laboratorio", "destino": "laboratorio"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "cuarentena": {
        "descripcion": "Módulo sellado con marcas de desesperación en las paredes. Alguien intentó salir.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Camilla", "mensaje": "Las correas están rotas desde adentro.", "evento": None},
            "2": {"nombre": "Ventana interior", "mensaje": "Algo se mueve en la oscuridad afuera.", "evento": None},
            "3": {"nombre": "Registro de mutaciones", "mensaje": "'Día 3: las transformaciones se aceleran. No reconocen su propio nombre.'", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver al laboratorio", "destino": "laboratorio"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "archivo_central": {
        "descripcion": "Registros secretos y decisiones ocultas. Alguien borró archivos a toda prisa.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Terminal", "mensaje": "'PROYECTO SEMILLA: el meteorito llegó hace 4.000 años. No fue accidente.'", "evento": None},
            "2": {"nombre": "Documentos clasificados", "mensaje": "Hay firmas de gobiernos de la Tierra. Sabían lo que había aquí.", "evento": None},
            "3": {"nombre": "Mapa holográfico", "mensaje": "Muestra la base completa y una cavidad subterránea no registrada.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver a sala de control", "destino": "sala_control"},
            "2": {"texto": "Volver al laboratorio biológico", "destino": "laboratorio_biologico"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "dormitorios": {
        "descripcion": "Habitaciones abandonadas del personal civil. Las camas están deshechas. Alguien salió corriendo.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Cama", "mensaje": "'Día 21: ya no duermo. Los escucho en las paredes por la noche.'", "evento": None},
            "2": {"nombre": "Locker", "mensaje": "Una foto familiar. Alguien que esperaba volver.", "evento": None},
            "3": {"nombre": "Botella de agua", "mensaje": "Sellada. Aún está bien.",  "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Ir al comedor", "destino": "comedor"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "comedor": {
        "descripcion": "Cafetería en silencio absoluto. Las bandejas siguen en las mesas, a medio comer.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Máquina expendedora", "mensaje": "Una bebida energética cae. Rara pero útil.", "evento": "curar", "usado": False},
            "2": {"nombre": "Mesa central", "mensaje": "Marcas de arrastre en el suelo. Algo pesado fue llevado hacia el pasillo.", "evento": None},
            "3": {"nombre": "Pantalla mural", "mensaje": "'ALERTA NIVEL 5: evacuar sector H. Repito: evacuar sector H.'", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver a dormitorios", "destino": "dormitorios"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    
    "sala_control": {
        "descripcion": "Centro de mando de la base. Las pantallas siguen encendidas mostrando alertas sin responder.",
        "opciones": {
            "1": {"texto": "Ir al archivo central", "destino": "archivo_central"},
            "2": {"texto": "Ir a telecomunicaciones", "destino": "sala_telecomunicaciones"},
            "3": {"texto": "Ir al reactor", "destino": "reactor"},
            "4": {"texto": "Ir a planta de generación", "destino": "planta_generacion"},
            "5": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "sala_telecomunicaciones": {
        "descripcion": "Mensajes perdidos hacia la Tierra. La última transmisión fue hace 72 horas.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Consola principal", "mensaje": "'...socorro... no queda nadie... el sector H está...' La señal se corta.", "evento": None},
            "2": {"nombre": "Servidor de grabaciones", "mensaje": "Última llamada: alguien llorando. No dice nada. Solo llora.", "evento": None},
            "3": {"nombre": "Kit de emergencia", "mensaje": "Un estimulante de emergencia. Recuperas energía.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Ir a antena de rescate exterior", "destino": "antena_rescate"},
            "2": {"texto": "Volver a sala de control", "destino": "sala_control"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "reactor": {
        "descripcion": "El núcleo energético tiembla. Los indicadores están todos en rojo.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Panel de control", "mensaje": "'SOBRECARGA CRÍTICA: tiempo estimado hasta fallo — desconocido.'", "evento": None},
            "2": {"nombre": "Tubería principal", "mensaje": "Una fuga está congelada por la temperatura. Por ahora.", "evento": None},
            "3": {"nombre": "Botiquín de radiación", "mensaje": "Pastillas de yoduro. Algo es mejor que nada.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Ir a control térmico", "destino": "control_termico"},
            "2": {"texto": "Volver a sala de control", "destino": "sala_control"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "hangar": {
        "descripcion": "Hangar con vehículos dañados. Hay marcas de impacto en las paredes desde adentro.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Rover de exploración", "mensaje": "Hay un kit de primeros auxilios bajo el asiento.", "evento": "curar", "usado": False},
            "2": {"nombre": "Caja de herramientas", "mensaje": "Faltan piezas. Alguien las usó recientemente.", "evento": None},
            "3": {"nombre": "Puerta de acceso exterior", "mensaje": "Hay rasguños en el metal desde afuera. Algo intentó entrar.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Ir al domo de observación", "destino": "domo_observacion"},
            "2": {"texto": "Ir al túnel de extracción", "destino": "tunel_extraccion"},
            "3": {"texto": "Ir a la esclusa de salida", "destino": "esclusa_salida"},
            "4": {"texto": "Ir al núcleo del meteorito", "destino": "nucleo_meteorito"},
            "5": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "domo_observacion": {
        "descripcion": "Vista panorámica al exterior lunar contaminado. La superficie parece... moverse.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Telescopio orbital", "mensaje": "Restos de naves en la superficie. Nadie viene a rescatarlos.", "evento": None},
            "2": {"nombre": "Panel de sensores", "mensaje": "Lecturas erráticas de biomasa a 40 metros bajo la superficie.", "evento": None},
            "3": {"nombre": "Silla giratoria", "mensaje": "Orientada hacia el sector H. Alguien vigilaba ese punto específico.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver al hangar", "destino": "hangar"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "tunel_extraccion": {
        "descripcion": "Un túnel de extracción que desciende en espiral. Las luces de emergencia parpadean en rojo. Aquí empezó todo.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Taladro de perforación", "mensaje": "Detenido a mitad de operación. Hay algo incrustado en la broca.", "evento": None},
            "2": {"nombre": "Bitácora de perforación", "mensaje": "'Día 1: alcanzamos la cavidad. Día 2: la cavidad respira.'", "evento": None},
            "3": {"nombre": "Casco de minero", "mensaje": "La linterna aún funciona. La tomas.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Bajar al frente minero", "destino": "frente_minero"},
            "2": {"texto": "Ir al depósito mineral", "destino": "deposito_mineral"},
            "3": {"texto": "Volver al hangar", "destino": "hangar"},
            "4": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "frente_minero": {
        "descripcion": "El punto más profundo excavado. El suelo vibra. Desde aquí se puede oír al meteorito pulsar.",
        "enemigo": "infectado_minero",
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Cavidad expuesta", "mensaje": "Un hueco en la roca del tamaño de una persona. Lleva directo al núcleo.", "evento": None},
            "2": {"nombre": "Equipo abandonado", "mensaje": "El último equipo de mineros. No dejaron notas. Solo herramientas tiradas.", "evento": None},
            "3": {"nombre": "Mochila médica", "mensaje": "De un minero que no llegó a usarla.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Entrar a la cavidad (ir al núcleo)", "destino": "nucleo_meteorito"},
            "2": {"texto": "Volver al túnel", "destino": "tunel_extraccion"}
        }
    },

    "deposito_mineral": {
        "descripcion": "Un almacén de muestras lunares. Algunas están marcadas con advertencias biológicas.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Muestra lunar sellada", "mensaje": "Etiqueta: 'SECTOR H - NO ABRIR'. Está abierta.", "evento": None},
            "2": {"nombre": "Registro geológico", "mensaje": "'El meteorito no impactó. Emergió desde abajo. Llevaba aquí milenios.'", "evento": None},
            "3": {"nombre": "Suministros de emergencia", "mensaje": "Raciones de energía para mineros. Todavía sirven.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Ir a sala de procesado", "destino": "sala_procesado"},
            "2": {"texto": "Volver al túnel", "destino": "tunel_extraccion"}
        }
    },

    "sala_procesado": {
        "descripcion": "Maquinaria pesada para procesar minerales. Algunas máquinas siguen activas, procesando algo oscuro.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Cinta transportadora", "mensaje": "Transporta fragmentos negros con textura orgánica. No son minerales.", "evento": None},
            "2": {"nombre": "Informe de análisis", "mensaje": "'Composición desconocida. Reacciona al calor humano. DETENER EXTRACCIÓN.'", "evento": None},
            "3": {"nombre": "Panel de emergencia", "mensaje": "Hay un botón de sellado del túnel. ¿Lo activas?", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver al depósito", "destino": "deposito_mineral"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },


    "planta_generacion": {
        "descripcion": "La planta eléctrica principal de la base. Sin ella, todo se apaga. Está al límite.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Generador principal", "mensaje": "'CARGA AL 18%. FALLO ESTIMADO: desconocido.' Cada hora cuenta.", "evento": None},
            "2": {"nombre": "Manual de ingeniería", "mensaje": "Hay instrucciones para desviar energía desde las baterías de respaldo.", "evento": None},
            "3": {"nombre": "Botiquín técnico", "mensaje": "Para quemaduras eléctricas. Encuentras algo de analgésico.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Ir a almacén nuclear", "destino": "almacen_nuclear"},
            "2": {"texto": "Ir a baterías de respaldo", "destino": "baterias_respaldo"},
            "3": {"texto": "Ir a control térmico", "destino": "control_termico"},
            "4": {"texto": "Volver a sala de control", "destino": "sala_control"},
            "5": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "almacen_nuclear": {
        "descripcion": "Barras de combustible y contenedores sellados. El contador Geiger no para de sonar.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Barra de combustible", "mensaje": "Podría recargar el reactor. También podría matarte si la tocas sin traje.", "evento": None},
            "2": {"nombre": "Traje de protección", "mensaje": "Talla equivocada, pero algo es algo. Reduces la exposición.", "evento": None},
            "3": {"nombre": "Registro de inventario", "mensaje": "Falta una barra. Alguien la sacó. Hace tres días.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver a planta de generación", "destino": "planta_generacion"}
        }
    },

    "baterias_respaldo": {
        "descripcion": "La última reserva de energía de la base. Zumban con intensidad. Están casi agotadas.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Panel de baterías", "mensaje": "'RESERVA: 6%. Tiempo restante con consumo actual: 4 horas.'", "evento": None},
            "2": {"nombre": "Cable de emergencia", "mensaje": "Podría conectar esto a la antena exterior. Si llegas a tiempo.", "evento": None},
            "3": {"nombre": "Botiquín de emergencia", "mensaje": "Para el personal de mantenimiento. Encuentras vendas y pastillas.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Volver a planta de generación", "destino": "planta_generacion"},
            "2": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "control_termico": {
        "descripcion": "Regula la temperatura de toda la base. Actualmente la base se está enfriando. Rápido.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Termostato central", "mensaje": "Interior: -12°C y bajando. Sin calefacción, quedan horas.", "evento": None},
            "2": {"nombre": "Tubería de calor", "mensaje": "Rota. Alguien la cortó deliberadamente.", "evento": None},
            "3": {"nombre": "Traje térmico", "mensaje": "Viejo pero funcional. Te protege del frío por ahora.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Volver al reactor", "destino": "reactor"},
            "2": {"texto": "Volver a planta de generación", "destino": "planta_generacion"},
            "3": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },


    "esclusa_salida": {
        "descripcion": "La esclusa presurizada de salida al exterior lunar. Detrás de ese cristal: el vacío y la superficie contaminada.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Traje espacial", "mensaje": "Hay uno operativo. Sello intacto. Oxígeno al 60%.", "evento": None},
            "2": {"nombre": "Panel de salida", "mensaje": "Requiere código de autorización. El código está en la sala de control.", "evento": None},
            "3": {"nombre": "Localizador GPS lunar", "mensaje": "Marca una señal activa a 800 metros. ¿La antena de rescate?", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Salir a zona de impacto", "destino": "zona_impacto"},
            "2": {"texto": "Ir al garaje de rovers", "destino": "garaje_rovers"},
            "3": {"texto": "Volver al hangar", "destino": "hangar"},
            "4": {"texto": "Volver al pasillo", "destino": "pasillo"}
        }
    },

    "zona_impacto": {
        "descripcion": "La superficie lunar contaminada. El meteorito está aquí, emergiendo de la roca. Respira.",
        "enemigo": "criatura_exterior",
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Meteorito expuesto", "mensaje": "No es roca. Es orgánico. Lleva aquí desde antes que existiera la humanidad.", "evento": None},
            "2": {"nombre": "Restos de equipo de exploración", "mensaje": "El primer equipo que salió. No llegaron lejos.", "evento": None},
            "3": {"nombre": "Señal de balizamiento", "mensaje": "Aún transmite. Alguien la activó antes de morir.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Ir a las catacumbas lunares", "destino": "catacumbas"},
            "2": {"texto": "Ir a la antena de rescate", "destino": "antena_rescate"},
            "3": {"texto": "Volver a la esclusa", "destino": "esclusa_salida"}
        }
    },

    "garaje_rovers": {
        "descripcion": "Seis rovers aparcados. Cuatro están destruidos desde adentro. Uno tiene las llaves puestas.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Rover operativo", "mensaje": "Batería al 40%. Alcance: 12 km. La antena está a 800 metros.", "evento": None},
            "2": {"nombre": "Caja de reparaciones", "mensaje": "Parches para trajes espaciales. Muy necesarios.", "evento": "curar", "usado": False},
            "3": {"nombre": "Mapa de superficie", "mensaje": "Ruta marcada hasta la antena de rescate. Y otra ruta, borrada a medias.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Ir a zona de impacto", "destino": "zona_impacto"},
            "2": {"texto": "Ir a la antena de rescate", "destino": "antena_rescate"},
            "3": {"texto": "Volver a la esclusa", "destino": "esclusa_salida"}
        }
    },

    "catacumbas": {
        "descripcion": "Cuevas naturales bajo la superficie lunar. Aquí realizaron experimentos que no aparecen en ningún registro oficial.",
        "enemigo": "criatura_mutada",
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Laboratorio oculto", "mensaje": "Experimentos de fusión entre ADN humano y el organismo del meteorito. Voluntarios.", "evento": None},
            "2": {"nombre": "Diario del Dr. Voss", "mensaje": "'Si esto funciona, no seremos vulnerables al virus. Si falla... ya no importa.'", "evento": None},
            "3": {"nombre": "Muestra experimental", "mensaje": "Una jeringa. Podría curar el virus o terminar con todo. No hay forma de saber cuál.", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Subir al núcleo del meteorito", "destino": "nucleo_meteorito"},
            "2": {"texto": "Volver a zona de impacto", "destino": "zona_impacto"}
        }
    },

    "antena_rescate": {
        "descripcion": "Una antena de transmisión de largo alcance. Si la activas, alguien en la Tierra podría escuchar. En 72 horas.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Panel de transmisión", "mensaje": "Operativo. Solo necesitas energía suficiente desde las baterías de respaldo.", "evento": None},
            "2": {"nombre": "Mensaje pregrabado", "mensaje": "'Base lunar Omega. Solicitud de rescate urgente. Origen biológico desconocido...' Alguien ya intentó esto.", "evento": None},
            "3": {"nombre": "Refugio de emergencia", "mensaje": "Un módulo sellado con oxígeno para 48 horas. Un lugar donde esperar.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Volver a zona de impacto", "destino": "zona_impacto"},
            "2": {"texto": "Volver a telecomunicaciones", "destino": "sala_telecomunicaciones"},
            "3": {"texto": "Volver a la esclusa", "destino": "esclusa_salida"}
        }
    },

    "estacion_meteorologica": {
        "descripcion": "Una pequeña estación en la superficie. Registró todo. El impacto, la propagación, el silencio.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Registro sísmico", "mensaje": "El meteorito no impactó desde arriba. Surgió desde el interior de la luna.", "evento": None},
            "2": {"nombre": "Sensor atmosférico", "mensaje": "Detecta partículas orgánicas en suspensión. El virus ya está en el aire exterior.", "evento": None},
            "3": {"nombre": "Kit de supervivencia", "mensaje": "Preparado para situaciones exactamente como esta.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Volver al garaje de rovers", "destino": "garaje_rovers"},
            "2": {"texto": "Volver a la esclusa", "destino": "esclusa_salida"}
        }
    },

    "puesto_avanzada": {
        "descripcion": "Un módulo de avanzada sellado a 300 metros de la base. El último lugar donde alguien sobrevivió.",
        "enemigo": None,
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Diario de superviviente", "mensaje": "'Día 5 aquí dentro. Tengo comida para 3 días más. Si alguien lee esto: el reactor es la clave.'", "evento": None},
            "2": {"nombre": "Radio de emergencia", "mensaje": "Funciona. Captas una señal. Alguien más sigue vivo. O algo que suena como alguien.", "evento": None},
            "3": {"nombre": "Reservas de emergencia", "mensaje": "El superviviente dejó provisiones. Las tomas sin sentirte mal por ello.", "evento": "curar", "usado": False}
        },
        "opciones": {
            "1": {"texto": "Volver a zona de impacto", "destino": "zona_impacto"},
            "2": {"texto": "Volver a la esclusa", "destino": "esclusa_salida"}
        }
    },

  
    "nucleo_meteorito": {
        "descripcion": "El origen del horror. El meteorito late como un corazón. El aire vibra. Esto no es mineral. Nunca lo fue.",
        "enemigo": "criatura_origen",
        "explorada": False,
        "objetos": {
            "1": {"nombre": "Núcleo pulsante", "mensaje": "Late con un ritmo que reconoces. Es el mismo ritmo que tu corazón.", "evento": None},
            "2": {"nombre": "Restos del equipo de contención", "mensaje": "Intentaron sellarlo con todo lo que tenían. No fue suficiente.", "evento": None},
            "3": {"nombre": "Registro final del Dr. Voss", "mensaje": "'No puede morir. Pero puede ser contenido. El reactor. Usad el reactor.'", "evento": None}
        },
        "opciones": {
            "1": {"texto": "Huir al hangar", "destino": "hangar"},
            "2": {"texto": "Huir al frente minero", "destino": "frente_minero"}
        }
    }
}