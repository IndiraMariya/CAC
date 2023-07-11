<script>
	import Article from './Article.svelte';

	export let id = '';
	export let name = '';
	/**
	 * @type {any[]}
	 */
	export let articleData = [];
</script>

<div class="mb-10 p-5 shadow shadow-black/50 rounded-lg">
	<h1 class="capitalize font-bold mb-3 text-lg">{name}</h1>
	<div class="flex flex-wrap justify-center gap-6">
		{#each articleData as article}
			<Article {...article} />
		{/each}
	</div>
</div>
