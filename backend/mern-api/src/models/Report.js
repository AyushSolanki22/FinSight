import mongoose from 'mongoose';

const citationSchema = new mongoose.Schema({
  sourceTitle: String,
  sourceUrl: String,
  pageNumber: Number,
  excerpt: String
}, { _id: false });

const reportSchema = new mongoose.Schema({
  company: { type: String, required: true, index: true },
  question: { type: String, required: true },
  status: { type: String, enum: ['queued', 'running', 'completed', 'failed'], default: 'queued' },
  summary: String,
  report: mongoose.Schema.Types.Mixed,
  citations: [citationSchema],
  createdAt: { type: Date, default: Date.now }
});

export default mongoose.model('Report', reportSchema);
