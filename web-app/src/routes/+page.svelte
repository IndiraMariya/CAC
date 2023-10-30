<script>
	import Article from '$lib/components/Article.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Footer from '$lib/components/footer.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import Search from '$lib/components/Search.svelte';
	import Filter from '$lib/components/Filter.svelte';
	import Topic from '$lib/components/Topic.svelte';

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
		color: '',
		sourceLean: '',
		bias: ''
	};
</script>

<div class="min-h-[100vh] flex flex-col justify-between">
	<div>
		<div style="display: flex; align-items: center;">
			<Search />
			<Filter />
		</div>
		<Modal bind:showModal bind:data={modalData} />

		<div class="p-5 text-black w-full h-full">
			<Nav />
			{#each data.articlesGroups as topic}
				<Topic {...topic} bind:showModal bind:modalData />
			{/each}
		</div>
	</div>

	<div class="justify-self-end">
		<Footer />
	</div>
</div>
<!-- <Topic></Topic> -->
