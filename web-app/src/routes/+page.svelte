<script>
	import Article from '$lib/components/Article.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Footer from '$lib/components/footer.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import Search from '$lib/components/Search.svelte';
	import search_term from '$lib/components/Search.svelte';
	
	export let data;
	let showModal = false;
	let modalData = {
		title: '',
		href: '',
		description: '',
		author: '',
		date: '',
		src: '',
		alt: '',
		newsSource: '',
		color: ''
	};
</script>

<Search />
<Modal bind:showModal bind:data={modalData} />

<div class="p-5 text-black w-100 bg-p_bg">
	<Nav />
	<div class="font-body border-[1px] border-black">
		<div class="px-6">
			<h1 class="font-light font-display italic py-4 text-2xl color-p_text">
				What's the daily scoop?
			</h1>
			<div class="articles grid grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-4">
				<!-- TODO: Account for accurately grouping articles without images -->
				{#each data.articles as article}
					{#if article.articleData}
						<Article {...article.articleData} bind:showModal bind:modalData />
					{/if}
				{/each}
			</div>
		</div>
	</div>
</div>

<Footer />


<!-- <Topic></Topic> -->
