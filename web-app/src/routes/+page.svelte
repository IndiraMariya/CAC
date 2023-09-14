<script>
	import Article from '$lib/components/Article.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Footer from '$lib/components/footer.svelte';
	export let data;
</script>



<style>
	main {
	  padding-top: 10px; /* Adjust the value to match the height of your navbar */
	  /* font-family: 'Source Serif 4', sans-serif; */
	  font-weight: 200;
	  background-color: rgba(59, 73, 155, 0.126);
	  border-radius: 15px;
	}
	.page-container {
        border: 10px solid rgb(59,73,155); /* Adjust the border width and color as needed */
        padding: 20px; /* Add padding to create space between the content and the border */
		color: rgb(59,73,155);
		
    }
  </style>

<div class="page-container">
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
</div>

<Footer></Footer>


