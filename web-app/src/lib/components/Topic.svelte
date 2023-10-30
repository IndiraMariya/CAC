<script>
	import Article from './Article.svelte';

	export let topic = -1;
	export let tags = [''];
	/**
	 * @type {any[]}
	 */
	export let articles = [];

	export let showModal = false;
	export let modalData;
</script>

<div class="p-6">
	<div class="font-light font-display italic pb-4 text-2xl color-p_text">
		{#each tags as tag}
			<div>{tag}</div>
		{/each}
	</div>
	<div class="articles grid grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-4">
		<!-- TODO: Account for accurately grouping articles without images -->
		{#each articles as article}
			{#if article.articleData}
				<Article {...article.articleData} bind:showModal bind:modalData />
			{/if}
		{/each}
	</div>
</div>
<!-- 
<div class="mb-10 p-5 shadow shadow-black/50 rounded-lg">
	<h1 class="capitalize font-bold mb-3 text-lg">{name}</h1>
	<div class="flex flex-wrap justify-center gap-6">
		{#each articleData as article}
			<Article {...article} />
		{/each}
	</div>
</div> -->
