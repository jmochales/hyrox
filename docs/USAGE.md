# Guía de uso

## Registrar un entrenamiento manualmente

1. Copiar la plantilla correspondiente desde `templates/`:
   - `fuerza.md` — Sesión de fuerza
   - `carrera-larga.md` — Carrera de larga distancia
   - `carrera-intervalos.md` — Series o intervalos de carrera
   - `hibrido.md` — Entrenamiento híbrido (carrera + estaciones)

2. Crear el fichero en `log/YYYY/MM/` con el formato de nombre:
   ```
   YYYY-MM-DD-tipo.md
   ```
   Ejemplo: `log/2026/07/2026-07-21-fuerza.md`

3. Rellenar los campos de la plantilla con los datos del entrenamiento.

## Registrar desde Garmin Connect

Ver la guía detallada en [GARMIN-CONNECT.md](GARMIN-CONNECT.md).

Resumen:
1. Obtener los datos de la actividad desde Garmin Connect API
2. La skill parsea los datos y rellena la plantilla automáticamente
3. Se genera el fichero en `log/YYYY/MM/` con los datos importados

## Consultar entrenamientos

### Por fecha
Navegar directamente a `log/YYYY/MM/` para ver los entrenamientos de un mes concreto.

### Por tipo
Buscar ficheros cuyo nombre contenga el tipo: `fuerza`, `carrera-larga`, `carrera-intervalos`, `hibrido`.

### Resumen
El fichero `log/README.md` contiene un índice actualizado con estadísticas básicas.

## Planificar entrenamientos

1. Definir objetivos en `plan/current.md`
2. La skill puede recomendar distribución semanal según tus objetivos
3. Hacer seguimiento comparando planificado vs ejecutado

Ver más detalle en [PLANNING.md](PLANNING.md).
