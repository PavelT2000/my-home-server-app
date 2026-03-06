import { Routes, Route, Navigate } from 'react-router-dom';
import { LoginPage } from './routes/LoginPage';

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
}

export default App;

