<script>
	import { fade, slide, blur } from 'svelte/transition';
	import { getArticles, getDailyScoops } from '../../utilities';
	import Article from './Article.svelte';
	import { getContext } from 'svelte';

	/**
	 * @type {any[]}
	 */
	export let topics = [];
	$: scoops = getDailyScoops(topics);

	export let showModal = false;
	export let modalData;

	let innerWidth;
	let expanded = false;

	function getNumArticles(innerWidth, scoops) {
		let numCols;
		if (innerWidth > 1280) numCols = 6;
		else if (innerWidth > 1024) numCols = 4;
		else numCols = 4;

		let spotsFilled = 0;
		let numArticles = 0;
		while (spotsFilled < numCols * 2 && numArticles < scoops.length) {
			// has image
			if (scoops[numArticles].article.articleData.src) {
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

	$: numPeekArticles = getNumArticles(innerWidth, scoops);
	$: peekScoops = scoops.slice(0, numPeekArticles);
	$: hiddenScoops = scoops.slice(numPeekArticles);
</script>

<svelte:window bind:innerWidth />

{#if peekScoops.length > 0}
	<div class="font-body border-[1px] border-black mb-5 shadow-[0_3px_3px_rgba(0,0,0,0.3)]">
		<div class="p-6">
			<div
				class="font-light font-display italic pb-3 sm:pb-6 sm:pt-3 text-xl sm:text-3xl color-p_text flex flex-wrap gap-x-6 gap-y-2"
			>
				What's the daily scoop?
			</div>
			<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-4">
				{#each peekScoops as scoop}
					{#if scoop.article.articleData}
						<Article
							{...scoop.article.articleData}
							sourceLean={scoop.article.source_lean}
							bias={scoop.article.bias}
							bind:showModal
							bind:modalData
						/>
					{/if}
				{/each}
			</div>

			{#if hiddenScoops.length > 0}
				{#if expanded}
					<div
						class="pt-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-4"
						transition:fade
					>
						{#each hiddenScoops as scoop}
							{#if scoop.article.articleData}
								<Article
									{...scoop.article.articleData}
									sourceLean={scoop.article.source_lean}
									bias={scoop.article.bias}
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
