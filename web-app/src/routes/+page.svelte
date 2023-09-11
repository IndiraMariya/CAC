<script>
	import Article from '$lib/components/Article.svelte';
	import Nav from '$lib/components/Nav.svelte';
	export let data;
</script>



<style>
	main {
	  padding-top: 120px; /* Adjust the value to match the height of your navbar */
	}
  </style>

<Nav></Nav>

<main>
	<div class="p-6">
		<h1 class="pb-5 text-4xl font-bold">Your Daily Scoop</h1>
		<div class="flex flex-wrap gap-4">
			{#each data.articles as article}
				{#if article.articleData}
					<Article {...article.articleData} />
				{/if}
			{/each}
		</div>
	</div>	
</main>
