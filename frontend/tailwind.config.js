/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        background: '#1e293b', // <- aqui você pode definir a cor que quiser
      },
    },
  },
  plugins: [],
}