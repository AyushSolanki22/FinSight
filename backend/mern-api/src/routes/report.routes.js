import { Router } from 'express';
import { listReports, getReport } from '../controllers/report.controller.js';
const router = Router();
router.get('/', listReports);
router.get('/:reportId', getReport);
export default router;
