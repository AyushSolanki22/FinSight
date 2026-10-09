import { runAnalysis } from '../services/ai.service.js';

export async function createAnalysis(req, res, next) {
  try {
    const { company, question, years } = req.body ?? {};
    if (!company || !question) {
      return res.status(400).json({ error: 'company and question are required' });
    }
    const result = await runAnalysis({ company, question, years });
    return res.status(202).json(result);
  } catch (error) {
    next(error);
  }
}
