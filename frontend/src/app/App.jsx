import { Navigate, Route, Routes } from 'react-router-dom';
import AppLayout from './AppLayout.jsx';
import HomePage from '../pages/HomePage.jsx';
import AnalysisPage from '../pages/AnalysisPage.jsx';
import DashboardPage from '../pages/DashboardPage.jsx';
import ReportHistoryPage from '../pages/ReportHistoryPage.jsx';
import NotFoundPage from '../pages/NotFoundPage.jsx';

export default function App() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route index element={<HomePage />} />
        <Route path="analysis" element={<AnalysisPage />} />
        <Route path="dashboard" element={<DashboardPage />} />
        <Route path="reports" element={<ReportHistoryPage />} />
        <Route path="home" element={<Navigate to="/" replace />} />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  );
}
