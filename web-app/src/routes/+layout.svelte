<script>
	import '../app.postcss';
	import Footer from '$lib/components/Footer.svelte';
</script>

<div class="min-h-[100vh] flex flex-col justify-between">
	<slot />
	<div class="justify-self-end">
		<Footer />
	</div>
</div>
