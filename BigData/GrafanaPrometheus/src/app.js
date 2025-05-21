const express = require('express');
const { metricsMiddleware, register, requestCounter, inFlightGauge, histogram } = require('./config/metrics');

const app = express();
const port = 8080;

app.use(metricsMiddleware);

app.get('/cities', async (req, res) => {
  await new Promise(resolve => setTimeout(resolve, 2000)); // 2 segundos
  res.json([{ name: 'Barcelona' }, { name: 'Madrid' }]);
});

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

app.listen(port, '0.0.0.0',() => {
  console.log(`Servidor escuchando en http://0.0.0.0:${port}`);
});
