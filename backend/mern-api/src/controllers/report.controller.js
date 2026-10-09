export async function listReports(_req, res) {
  // TODO: Query saved report metadata from MongoDB.
  res.json({ items: [], message: 'Report persistence not implemented yet.' });
}
export async function getReport(req, res) {
  // TODO: Validate ID and load a report from MongoDB.
  res.status(404).json({ error: `Report ${req.params.reportId} not found` });
}
