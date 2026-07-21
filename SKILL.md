# Hyrox Training Log

## Descripción

Skill para registrar, consultar, planificar y hacer seguimiento de entrenamientos orientados a competiciones Hyrox. Mantiene un histórico completo en formato Markdown organizado por fecha y tipo de entrenamiento.

## Capacidades

### 1. Registrar entrenamiento

Registra un nuevo entrenamiento en el histórico. Dos modos disponibles:

- **Manual**: El usuario proporciona los datos y se genera el fichero a partir de la plantilla correspondiente.
- **Garmin Connect**: Se consulta la API de Garmin Connect para obtener los datos automáticamente. Los campos subjetivos (sensación, RPE) se solicitan al usuario.

**Fichero destino**: `log/YYYY/MM/YYYY-MM-DD-{tipo}.md`

### 2. Consultar entrenamiento

Permite buscar y consultar entrenamientos del histórico por:

- Fecha exacta
- Rango de fechas
- Tipo de entrenamiento
- Combinación de filtros

### 3. Planificar entrenamientos

Genera o actualiza un plan de entrenamiento en `plan/current.md` basado en:

- Fecha objetivo de competición
- Nivel actual del usuario
- Disponibilidad semanal
- Histórico de entrenamientos previos

### 4. Seguimiento

Compara lo planificado vs lo ejecutado y genera recomendaciones:

- Volumen semanal (sesiones realizadas vs planificadas)
- Equilibrio entre tipos de entrenamiento
- Progresión de cargas y tiempos
- Alertas de sobreentrenamiento o baja actividad

## Tipos de entrenamiento

| Tipo | Clave fichero | Descripción |
|------|---------------|-------------|
| Fuerza | `fuerza` | Ejercicios de fuerza en gimnasio |
| Carrera larga distancia | `carrera-larga` | Rodajes, fondos, tiradas largas |
| Carrera intervalos | `carrera-intervalos` | Series, fartlek, tempo runs |
| Híbrido | `hibrido` | Carrera combinada con estaciones funcionales (estilo Hyrox) |

## Estructura de datos de un entrenamiento

### Campos generales (todos los tipos)

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| Fecha | `YYYY-MM-DD` | Sí | Fecha del entrenamiento |
| Duración total | `HH:MM:SS` | Sí | Tiempo total de la sesión |
| Tipo | enum | Sí | Uno de los 4 tipos definidos |
| Tiempo de trabajo | `HH:MM:SS` | No | Tiempo efectivo de ejercicio |
| Frecuencia cardíaca media | int (bpm) | No | FC media de la sesión |
| Calorías | int (kcal) | No | Calorías estimadas |
| ¿Cómo te has sentido? | emoji | No | 😀 / 😐 / 😓 / 🤕 |
| Percepción de esfuerzo | int (1-10) | No | RPE subjetivo |

### Campos de series (todos los tipos)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| # | int | Número de serie |
| Ejercicio | string | Nombre del ejercicio o segmento |
| Tiempo | `MM:SS` | Duración de la serie |
| Descanso | `MM:SS` | Tiempo de descanso tras la serie |
| Repeticiones | int | Número de repeticiones |
| Peso | float (kg) | Peso utilizado (si aplica) |

## Plantillas

Las plantillas se encuentran en `templates/` y sirven como base para generar cada entrada del log:

- `templates/fuerza.md`
- `templates/carrera-larga.md`
- `templates/carrera-intervalos.md`
- `templates/hibrido.md`

## Estructura del repositorio

```
├── SKILL.md                 ← Este fichero (definición de la skill)
├── README.md                ← Descripción del proyecto para GitHub
├── .gitignore
├── docs/
│   ├── USAGE.md             ← Guía de uso detallada
│   ├── GARMIN-CONNECT.md    ← Integración con Garmin Connect API
│   └── PLANNING.md          ← Guía de planificación y seguimiento
├── templates/
│   ├── fuerza.md
│   ├── carrera-larga.md
│   ├── carrera-intervalos.md
│   └── hibrido.md
├── log/
│   ├── README.md            ← Índice y estadísticas del histórico
│   └── YYYY/MM/             ← Entrenamientos organizados por fecha
└── plan/
    ├── current.md           ← Plan de entrenamiento activo
    └── archive/             ← Planes finalizados
```

## Integración con Garmin Connect

La skill importa datos automáticamente usando la librería [`python-garminconnect`](https://github.com/cyberjunky/python-garminconnect), que se autentica mediante el mismo flujo SSO mobile que la app oficial de Garmin para Android.

**Campos auto-importados**: fecha, duración, tipo, FC media, calorías, distancia, ritmo, series/ejercicios.  
**Campos manuales**: sensación (emoji), RPE (1-10).

Ver detalles en `docs/GARMIN-CONNECT.md`.

## Instrucciones para el agente

Cuando el usuario pida:

- **"Registra un entrenamiento"** → Preguntar tipo y activityId de Garmin (visible en la URL `connect.garmin.com/modern/activity/XXXXXXXXX`). Si no tiene Garmin, registrar manualmente. Generar fichero en `log/YYYY/MM/`.
- **"Consulta la actividad XXXXXXXXX"** → Conectar a Garmin con credenciales del `.env`, obtener datos por ID y mostrar resumen.
- **"¿Qué entrené el día X?"** → Buscar en `log/` por fecha y devolver contenido.
- **"Muéstrame los entrenamientos de esta semana/mes"** → Listar ficheros del período y resumir.
- **"Planifica mi semana"** → Consultar histórico reciente + `plan/current.md` y sugerir sesiones.
- **"¿Cómo voy con el plan?"** → Comparar `plan/current.md` con entrenamientos registrados en `log/`.
