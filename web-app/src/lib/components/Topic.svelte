<script>
	import { fade, slide, blur } from 'svelte/transition';
	import { getArticles } from '../../utilities';
	import Article from './Article.svelte';
	import { getContext } from 'svelte';

	export let topic = -1;
	export let tags = [''];
	/**
	 * @type {any[]}
	 */
	export let articles = [];
	let filterData = getContext('filterData');
	export let searchText = '';

	$: ({ peek, hidden } = getArticles(articles, $filterData, searchText));

	export let showModal = false;
	export let modalData;

	let innerWidth;
	let expanded = false;

	function getNumArticles(innerWidth, groupedArticles) {
		let numCols;
		if (innerWidth > 1280) numCols = 3;
		else if (innerWidth > 1024) numCols = 4;
		else numCols = 2;

		let spotsFilled = 0;
		let numArticles = 0;
		while (spotsFilled < numCols * 2 && numArticles < groupedArticles.length) {
			// has image
			if (groupedArticles[numArticles].articleData.src) {
				spotsFilled += 2;
			}
			// doesn't have image
			else {
				spotsFilled += 1;
			}
			numArticles += 1;
		}
		return numArticles;
	}

	$: numPeekArticles = getNumArticles(innerWidth, peek);
	$: peekArticles = peek.slice(0, numPeekArticles);
	$: hiddenArticles = peek.slice(numPeekArticles).concat(hidden);
</script>

<svelte:window bind:innerWidth />

{#if peekArticles.length > 0}
	<div class="font-body border-[1px] border-black mb-5">
		<div class="p-6">
			<div
				class="font-light font-display italic pb-3 sm:pb-6 sm:pt-3 text-xl sm:text-3xl color-p_text flex flex-wrap gap-x-6 gap-y-2"
			>
				{#if tags}
					{#each tags.slice(0, 3) as tag}
						<div class=""># {tag}</div>
					{/each}
				{/if}
			</div>
			<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-4">
				{#each peekArticles as article}
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
			{#if hiddenArticles.length > 0}
				{#if expanded}
					<div
						class="pt-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-4"
						transition:fade
					>
						{#each hiddenArticles as article}
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
				{/if}
				<button
					on:click={() => {
						expanded = !expanded;
					}}
					class="px-3 py-2 mt-3 outline outline-black outline-1 hover:shadow-[0_3px_3px_rgba(0,0,0,0.3)]"
				>
					{expanded ? 'See less...' : 'See More...'}
				</button>
			{/if}
		</div>
	</div>
{/if}
