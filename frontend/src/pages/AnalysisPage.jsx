export default function AnalysisPage() {
  const query = JSON.parse(sessionStorage.getItem('finsight-query') || '{}');
  return <section><p className="eyebrow">RESEARCH WORKSPACE</p><h1>Company analysis</h1>
    <div className="panel"><h2>{query.company || 'No company selected'}</h2>
      <p>{query.question || 'Return to Research to enter a question.'}</p>
      <p className="muted">API integration placeholder: connect this page to POST /api/v1/analysis.</p>
      <span className="status-pill">Awaiting analysis service</span>
    </div>
  </section>;
}
