import { Routes, Route, Navigate } from 'react-router-dom'
import RegisterPage from './component/RegisterPage'
import LoginPage from './component/LoginPage'
import Dashboard from './component/Dashboard'

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="*" element={<Navigate to="/register" replace />} />
    </Routes>
  )
}

export default App;