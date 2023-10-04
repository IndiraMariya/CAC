/** @type {import('tailwindcss').Config}*/

const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			colors: {
				p_blue: 'rgb(59,73,155)',
				p_red: 'rgb(229, 49, 49)'
			},
			fontFamily: {
				display: ['"Roboto Serif"'],
				header: ['"Roboto Serif"'],
				body: ['"Source Serif 4"']
			}
		}
	},

	plugins: []
};

module.exports = config;
