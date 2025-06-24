export default function DefaultLayout({ children }) {
  return (
    <div className="h-screen w-screen bg-gray-100">
      <header className="bg-primary text-white p-4">Meu App</header>
      <main className="p-4">{children}</main>
    </div>
  )
}
