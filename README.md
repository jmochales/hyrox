# Hyrox Training Log

Skill para registrar, consultar, planificar y hacer seguimiento de entrenamientos orientados a Hyrox.

## Estructura

```
hyrox/
├── README.md                    # Este fichero
├── docs/
│   ├── USAGE.md                 # Guía de uso de la skill
│   ├── GARMIN-CONNECT.md        # Integración con Garmin Connect API
│   └── PLANNING.md             # Guía de planificación y seguimiento
├── templates/
│   ├── fuerza.md               # Plantilla: entrenamiento de fuerza
│   ├── carrera-larga.md        # Plantilla: carrera larga distancia
│   ├── carrera-intervalos.md   # Plantilla: carrera por intervalos
│   └── hibrido.md             # Plantilla: entrenamiento híbrido (carrera + workouts)
├── log/
│   ├── 2026/                   # Entrenamientos registrados por año
│   │   ├── 07/                 # y por mes
│   │   │   ├── 2026-07-21-fuerza.md
│   │   │   └── ...
│   └── README.md               # Índice del histórico
└── plan/
    ├── current.md              # Plan de entrenamiento activo
    └── archive/                # Planes anteriores
```

## Tipos de entrenamiento

| Tipo | Descripción |
|------|-------------|
| **Fuerza** | Sesiones de gimnasio con ejercicios de fuerza pura |
| **Carrera larga distancia** | Rodajes largos, tiradas, fondos |
| **Carrera intervalos** | Series, fartlek, tempo runs |
| **Híbrido** | Combinación de carrera con ejercicios funcionales (estilo Hyrox) |

## Uso rápido

- **Registrar entrenamiento manual**: Copiar la plantilla correspondiente a `log/YYYY/MM/` y rellenar
- **Registrar desde Garmin Connect**: Seguir guía en `docs/GARMIN-CONNECT.md`
- **Consultar histórico**: Navegar `log/` o buscar por fecha/tipo
- **Planificar**: Ver `docs/PLANNING.md` y `plan/current.md`
