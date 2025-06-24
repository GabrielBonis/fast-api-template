import { useState } from 'react'

export function useAuth() {
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const login = async (username, password) => {
    setError(null)
    setLoading(true)

    const formData = new URLSearchParams()
    formData.append('username', username)
    formData.append('password', password)

    try {
      const response = await fetch('http://localhost:8000/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData
      })

      if (!response.ok) {
        throw new Error('Usuário ou senha incorretos')
      }

      const data = await response.json()
      sessionStorage.setItem('token', data.access_token)
      return true
    } catch (err) {
      setError(err.message)
      return false
    } finally {
      setLoading(false)
    }
  }

  const logout = () => {
    sessionStorage.removeItem('token')
    window.location.href = '/auth'
  }

  const isAuthenticated = () => {
    return !!sessionStorage.getItem('token')
  }

  return {
    login,
    logout,
    isAuthenticated,
    error,
    loading
  }
}
