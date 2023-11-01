<script>
	import PageContainer from '$lib/components/PageContainer.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import { readingData } from '../../store';
</script>

<PageContainer>
	<Nav />
	<h1 class="font-medium text-4xl">Your Stats</h1>
	<div class="grid grid-cols-4">
		<div>
			<div>News Sites Visited</div>
		</div>
	</div>
</PageContainer>
