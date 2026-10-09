import { Router } from 'express';
import { createAnalysis } from '../controllers/analysis.controller.js';
const router = Router();
router.post('/', createAnalysis);
export default router;
