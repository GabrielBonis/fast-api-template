export default function Button({ children }) {
  return (
    <button className="bg-primary text-white px-4 py-2 rounded">
      {children}
    </button>
  )
}
