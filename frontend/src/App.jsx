import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import DefaultLayout from './layouts/DefaultLayout'

const isAuthenticated = () => {
  return !!sessionStorage.getItem('token')
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/auth" element={<Login />} />
        <Route
          path="/"
          element={
            isAuthenticated() ? (
              <DefaultLayout>
                <Home />
              </DefaultLayout>
            ) : (
              <Navigate to="/auth" replace />
            )
          }
        />
      </Routes>
    </BrowserRouter>
  )
}
