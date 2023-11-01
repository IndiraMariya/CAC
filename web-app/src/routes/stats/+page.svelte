<script>
	import PageContainer from '$lib/components/PageContainer.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import { readingData } from '../../store';

	import { Bar, Pie } from 'svelte-chartjs';
	import {
		Chart,
		Title,
		Tooltip,
		Legend,
		BarElement,
		CategoryScale,
		LinearScale,
		ArcElement
	} from 'chart.js';
	import {
		getLeanColor,
		getObjectivityColor,
		getPropertyData,
		getSourceColor
	} from '../../utilities';
	Chart.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement);
	Chart.defaults.font.size = 16;
	Chart.defaults.font.family = 'Roboto Serif';

	$: newsData = getPropertyData($readingData, 'newsSource', 'articles', getSourceColor);
	$: biasData = getPropertyData($readingData, 'bias', 'articles', getObjectivityColor);
	$: leanData = getPropertyData($readingData, 'sourceLean', 'articles', getLeanColor);
</script>

<PageContainer>
	<Nav />
	<h1 class="font-medium text-4xl pb-7">Your Stats</h1>
	<div class="grid grid-cols-3 gap-6 h-10">
		<div>
			<div class="text-xl pb-2">Favorite News Sites (%)</div>
			<Bar
				data={newsData}
				width="100%"
				height="100%"
				options={{
					indexAxis: 'y',
					responsive: true,
					scales: {
						x: {
							min: 0
						}
					},
					plugins: {
						legend: {
							display: false
						}
					}
				}}
			/>
		</div>
		<div>
			<div class="text-xl pb-2">Article Subjectivity (%)</div>
			<Bar
				data={biasData}
				width="100%"
				height="100%"
				options={{
					indexAxis: 'y',
					responsive: true,
					scales: {
						x: {
							min: 0
						}
					},
					plugins: {
						legend: {
							display: false
						}
					}
				}}
			/>
		</div>
		<div>
			<div class="text-xl pb-2">Article Lean (%)</div>
			<Pie
				data={leanData}
				width="100%"
				height="100%"
				options={{
					indexAxis: 'y',
					responsive: true,
					plugins: {
						legend: {
							position: 'top'
						}
					}
				}}
			/>
		</div>
	</div>
</PageContainer>
