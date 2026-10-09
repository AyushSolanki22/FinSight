import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function HomePage() {
  const [company, setCompany] = useState('Reliance Industries');
  const [question, setQuestion] = useState('How have revenue, debt, and profit margins changed over the last five years?');
  const navigate = useNavigate();

  function submit(event) {
    event.preventDefault();
    sessionStorage.setItem('finsight-query', JSON.stringify({ company, question }));
    navigate('/analysis');
  }

  return (
    <section className="hero">
      <p className="eyebrow">AI-POWERED FINANCIAL RESEARCH</p>
      <h1>Research companies with <span>evidence.</span></h1>
      <p className="muted">Explore financial performance, filings, and disclosed risks with traceable sources.</p>
      <form className="query-card" onSubmit={submit}>
        <label>Company or ticker<input value={company} onChange={e => setCompany(e.target.value)} required placeholder="e.g. RELIANCE" /></label>
        <label>Research question<textarea value={question} onChange={e => setQuestion(e.target.value)} required rows="4" /></label>
        <button type="submit">Prepare analysis</button>
      </form>
    </section>
  );
}
