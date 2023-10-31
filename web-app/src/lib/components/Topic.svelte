<script>
	import { groupArticlesWithImages } from '../../utilities';
	import Article from './Article.svelte';

	export let topic = -1;
	export let tags = [''];
	/**
	 * @type {any[]}
	 */
	export let articles = [];
	export let filterData;

	$: groupedArticles = groupArticlesWithImages(articles, filterData);

	export let showModal = false;
	export let modalData;
</script>

<div class="font-body border-[1px] border-black mb-5">
	<div class="p-6">
		<div class="font-light font-display italic pb-4 text-3xl color-p_text flex flex-wrap gap-6">
			{#if tags}
				{#each tags.slice(0, 3) as tag}
					<div class="py-3"># {tag}</div>
				{/each}
			{/if}
		</div>
		<div class="articles grid grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-4">
			<!-- TODO: Account for accurately grouping articles without images -->
			{#each groupedArticles as article}
				{#if article.articleData}
					<Article
						{...article.articleData}
						sourceLean={article.source_lean}
						bias={article.bias}
						bind:showModal
						bind:modalData
					/>
				{/if}
			{/each}
		</div>
	</div>
</div>
