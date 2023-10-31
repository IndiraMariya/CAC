<script>
	import Article from '$lib/components/Article.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Footer from '$lib/components/footer.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import Search from '$lib/components/Search.svelte';
	import Filter from '$lib/components/Filter.svelte';
	import Topic from '$lib/components/Topic.svelte';
	import { filterDataBySearch, getData, sortData } from '../utilities.js';

	import { setContext } from 'svelte';
	import { writable } from 'svelte/store';

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

	let filterData = writable([
		{ name: 'Date', value: 'date', ascending: null },
		{ name: 'Popularity', value: 'popularity', ascending: null },
		{ name: 'Bias', value: 'bias', ascending: null }
	]);
	setContext('filterData', filterData);

	let searchText = '#';
	let searchingTags = false;

	$: filteredTopics = filterDataBySearch(data.articlesGroups, searchText);
	$: sortedTopics = sortData(filteredTopics, $filterData);
</script>

<div class="min-h-[100vh] flex flex-col justify-between">
	<div>
		<Modal bind:showModal bind:data={modalData} />

		<div class="p-5 pt-0 text-black w-full h-full">
			<Nav />
			<div class="flex items-center p-0">
				<Search bind:searchText bind:searchingTags />
			</div>
			{#each sortedTopics as topic}
				<Topic {...topic} bind:showModal bind:modalData bind:searchText />
			{/each}
		</div>
	</div>

	<div class="justify-self-end">
		<Footer />
	</div>
</div>
<!-- <Topic></Topic> -->
