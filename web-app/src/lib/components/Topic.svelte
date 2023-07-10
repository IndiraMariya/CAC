<script>
	import Article from './Article.svelte';

	export let name = '';

	/**
	 * @type {any[]}
	 */
	export let articles = [];
</script>

<div class="m-10 p-5 shadow shadow-black/50 rounded-lg">
	<h1 class="capitalize font-bold mb-3 text-lg">{name}</h1>
	<div class="flex flex-wrap justify-start">
		{#each articles as articles}
			<Article {...articles} />
		{/each}
	</div>
</div>
