/** @type {import('tailwindcss').Config} */
module.exports = {
    /** paths to all of your pages and components so Tailwind can tree-shake unused styles in production builds **/
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
}