import axios from 'axios';

export async function runAnalysis(payload) {
  const baseURL = process.env.AI_SERVICE_URL || 'http://localhost:8000';
  const response = await axios.post(`${baseURL}/api/v1/analysis`, payload, { timeout: 120000 });
  return response.data;
}
