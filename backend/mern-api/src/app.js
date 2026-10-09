import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import healthRoutes from './routes/health.routes.js';
import analysisRoutes from './routes/analysis.routes.js';
import reportRoutes from './routes/report.routes.js';
import { notFoundHandler, errorHandler } from './middleware/error.middleware.js';

const app = express();
app.use(helmet());
app.use(cors({ origin: process.env.FRONTEND_URL || 'http://localhost:5173' }));
app.use(express.json({ limit: '1mb' }));
app.use(morgan('dev'));

app.use('/api/v1/health', healthRoutes);
app.use('/api/v1/analysis', analysisRoutes);
app.use('/api/v1/reports', reportRoutes);
app.use(notFoundHandler);
app.use(errorHandler);

export default app;
