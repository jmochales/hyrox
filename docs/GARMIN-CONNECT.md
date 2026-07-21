# Integración con Garmin Connect

## Descripción

Esta skill importa datos de entrenamientos desde Garmin Connect usando la librería [`python-garminconnect`](https://github.com/cyberjunky/python-garminconnect), que se autentica mediante el mismo flujo SSO que la app oficial de Garmin para Android.

> **Nota**: La librería `garth` original está deprecada. `python-garminconnect` es su sucesor activo y mantenido.

## Requisitos

- Python 3.9+
- Cuenta de Garmin Connect activa
- Dispositivo Garmin sincronizado

## Instalación

```bash
pip install garminconnect
```

## Autenticación

La librería usa el flujo mobile SSO de Garmin (mismo que la app Android), obteniendo OAuth Bearer tokens nativos.

### Primera vez (login con credenciales del .env)

```python
import os
from garminconnect import Garmin

email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")

client = Garmin(email, password)
client.login()
```

### Consultar actividad por ID

```python
# El ID se obtiene de la URL: https://connect.garmin.com/modern/activity/123456789
activity_id = 123456789

activity = client.get_activity(activity_id)
exercise_sets = client.get_activity_exercise_sets(activity_id)
splits = client.get_activity_splits(activity_id)
```

## Datos extraídos automáticamente

De una actividad de Garmin se extraen y mapean a la plantilla:

| Campo plantilla | Campo Garmin | Método |
|----------------|--------------|--------|
| Fecha | `startTimeLocal` | `get_activity(id)` |
| Duración total | `duration` | `get_activity(id)` |
| Tipo | `activityType` | `get_activity(id)` |
| Tiempo de trabajo | `movingDuration` | `get_activity(id)` |
| Frecuencia cardíaca media | `averageHR` | `get_activity(id)` |
| Calorías | `calories` | `get_activity(id)` |
| Distancia | `distance` | `get_activity(id)` |
| Ritmo medio | `averageSpeed` (convertido) | `get_activity(id)` |
| Series/Ejercicios | `exerciseSets` | `get_activity_exercise_sets(id)` |

## Datos que requieren input manual

Estos campos no están disponibles en Garmin y se deben completar a mano:

- ¿Cómo te has sentido? (emoji)
- Percepción de esfuerzo (RPE 1-10)

## Endpoints principales usados

```python
# Últimas actividades
activities = client.get_activities(start=0, limit=10)

# Detalle de una actividad por ID
activity = client.get_activity(activity_id)

# Series y ejercicios de una actividad
exercise_sets = client.get_activity_exercise_sets(activity_id)

# Splits de carrera
splits = client.get_activity_splits(activity_id)

# Datos de frecuencia cardíaca
hr_data = client.get_activity_hr_in_timezones(activity_id)
```

## Cómo obtener el ID de actividad

El ID de actividad se encuentra en la URL de Garmin Connect:

```
https://connect.garmin.com/modern/activity/123456789
                                          ─────────
                                          Este es el activityId
```

Puedes copiar el número directamente de la barra de direcciones del navegador al visualizar cualquier actividad.

## Flujo de importación

```
1. Usuario proporciona activityId (visible en la URL de Garmin Connect)
2. Autenticar con Garmin Connect (email/contraseña del .env)
3. Consultar actividad + exercise sets
4. Detectar tipo de actividad (running → carrera, strength → fuerza, multi_sport → híbrido)
5. Seleccionar plantilla apropiada
6. Rellenar campos automáticos
7. Solicitar campos subjetivos al usuario (sensación, RPE)
8. Generar fichero en log/YYYY/MM/YYYY-MM-DD-{tipo}.md
```

## Mapeo de tipos de actividad

| Tipo Garmin | Tipo skill |
|-------------|-----------|
| `running` (distancia > 5km) | `carrera-larga` |
| `running` (con intervalos) | `carrera-intervalos` |
| `strength_training` | `fuerza` |
| `multi_sport` / `other` | `hibrido` |

## Configuración

Editar el fichero `.env` en la raíz del proyecto con tus credenciales de Garmin Connect:

```env
GARMIN_EMAIL=tu_email@ejemplo.com
GARMIN_PASSWORD=tu_contraseña
```

> ⚠️ **Importante**: El fichero `.env` está en `.gitignore` para no exponer credenciales.

## Referencia

- Repositorio: [cyberjunky/python-garminconnect](https://github.com/cyberjunky/python-garminconnect)
- Métodos disponibles: 134+ endpoints organizados en 13 categorías
- Licencia: MIT
