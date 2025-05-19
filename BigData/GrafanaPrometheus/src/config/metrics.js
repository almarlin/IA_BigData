const promClient = require('prom-client');

const collectDefaultMetrics = promClient.collectDefaultMetrics;
collectDefaultMetrics();

const register = new promClient.Registry();
register.setDefaultLabels({ app: 'nodejs_app' });
collectDefaultMetrics({ register });

const requestCounter = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Número total de peticiones',
  labelNames: ['method', 'route', 'status_code'],
});

const inFlightGauge = new promClient.Gauge({
  name: 'http_requests_in_flight',
  help: 'Número de peticiones en vuelo',
});

const histogram = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duración de las peticiones HTTP',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.1, 0.3, 0.5, 1, 1.5, 2, 5],
});

register.registerMetric(requestCounter);
register.registerMetric(inFlightGauge);
register.registerMetric(histogram);

const metricsMiddleware = (req, res, next) => {
  const end = histogram.startTimer({ method: req.method, route: req.path });

  inFlightGauge.inc();

  res.on('finish', () => {
    end({ status_code: res.statusCode });
    requestCounter.inc({ method: req.method, route: req.path, status_code: res.statusCode });
    inFlightGauge.dec();
  });

  next();
};

module.exports = { register, requestCounter, inFlightGauge, histogram, metricsMiddleware };
