import mongoose from 'mongoose';

const userSchema = new mongoose.Schema({
  displayName: { type: String, trim: true },
  email: { type: String, unique: true, sparse: true, lowercase: true, trim: true }
}, { timestamps: true });

export default mongoose.model('User', userSchema);
