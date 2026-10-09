export function notFoundHandler(req, res) {
  res.status(404).json({ error: 'Route not found', path: req.originalUrl });
}
export function errorHandler(error, _req, res, _next) {
  console.error(error);
  res.status(error.status || 500).json({ error: error.message || 'Internal server error' });
}
