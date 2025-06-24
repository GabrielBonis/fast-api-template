import { useState } from 'react'
import { useAuth } from '../../hooks/useAuth'

export default function LoginForm() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const { login, error, loading } = useAuth()

  const handleSubmit = async (e) => {
    e.preventDefault()
    const success = await login(username, password)
    if (success) {
      window.location.href = '/'
    }
  }

  return (
    <form className="flex flex-col gap-3 max-w-sm mx-auto" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Usuário"
        className="border p-2"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Senha"
        className="border p-2"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button disabled={loading} className="bg-primary text-white px-4 py-2">
        {loading ? 'Entrando...' : 'Entrar'}
      </button>
      {error && <p className="text-red-500">{error}</p>}
    </form>
  )
}
