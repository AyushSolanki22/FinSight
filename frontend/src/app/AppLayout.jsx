import { NavLink, Outlet } from 'react-router-dom';

const links = [
  ['/', 'Research'],
  ['/dashboard', 'Dashboard'],
  ['/reports', 'Report history']
];

export default function AppLayout() {
  return (
    <div className="app-shell">
      <header className="topbar">
        <NavLink className="brand" to="/">FinSight</NavLink>
        <nav aria-label="Main navigation">
          {links.map(([to, label]) => <NavLink key={to} to={to} end={to === '/'}>{label}</NavLink>)}
        </nav>
      </header>
      <main className="page-container"><Outlet /></main>
      <footer className="footer">For research and educational purposes only. Not investment advice.</footer>
    </div>
  );
}
