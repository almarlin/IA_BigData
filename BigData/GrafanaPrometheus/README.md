# Monitorización con Prometheus y Grafana

Este proyecto muestra cómo monitorizar un microservicio Node.js usando Prometheus y Grafana.

## Requisitos
- Docker y Docker Compose
- Node.js

## Servicios
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000
- **Node.js Service**: http://localhost:8080

## Despliegue y uso
1. `docker-compose up`
2. Accede a los servicios desde el navegador
3. Ejecuta `curl http://localhost:8080/cities` para generar tráfico
4. Revisa métricas en Prometheus y visualízalas en Grafana

## Métricas expuestas
- Total de peticiones (`http_requests_total`)
- Duración de peticiones (`http_request_duration_seconds`)
- Peticiones en vuelo (`http_requests_in_flight`)

# Ejercicio 5: Preguntas Teóricas
## Counter vs Gauge

Counter: Es un contador, perfecto para calcular el total de peticiones.

Gauge: Variable, ideal para comprobar conexiones activas.

## ¿Por qué Prometheus hace scraping?

Permite control centralizado, evita dependencias del cliente y reduce carga al cliente.

## Ventaja de Histogram sobre Gauge para latencia

Histogram permite ver distribución y percentiles; Gauge solo muestra un valor actual.

## Problemas con muchas etiquetas dinámicas

La alta cardinalidad consume memoria, reduce rendimiento de Prometheus y puede hacerlo inestable.