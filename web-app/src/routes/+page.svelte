<script>
	import Article from '$lib/components/Article.svelte';

	export let data;
</script>

<div class="p-6">
	<h1 class="pb-5 text-4xl font-bold">APP NAME</h1>
	<div class="flex flex-wrap gap-4">
		{#each data.articles as article}
			{#if article.articleData}
				<Article {...article.articleData} />
			{/if}
		{/each}
	</div>
</div>
