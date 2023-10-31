<script>
	import Filter from './Filter.svelte';
	import { slide } from 'svelte/transition';

	let showMessage = false;
	let isClicked = false;

	export let searchText = '#';
	export let searchingTags = false;
	export let filterData;

	function setSearchingTags(searchText) {
		searchingTags = searchText.trim().substring(0, 1) == '#';
	}

	$: setSearchingTags(searchText);
</script>

<div class="w-full">
	<div class="flex flex-col gap-2 sm:gap-0 sm:flex-row mb-3 items-start sm:items-stretch w-full">
		<div
			class="h-full border-[1px] border-black drop-shadow-sm font-body bg-p_bg hover:shadow-[0_3px_3px_rgba(0,0,0,0.3)] focus-within:shadow-[0_3px_3px_rgba(0,0,0,0.3)] w-full sm:w-[30%] min-w-max relative p-2"
		>
			<span class="absolute inset-y-0 left-0 flex items-center pl-2 h-full">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-6 h-6"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
					/>
				</svg>
			</span>
			<input
				class="rounded-none outline-none bg-p_bg pl-10 w-full"
				type="text"
				name="q"
				placeholder="Search.."
				bind:value={searchText}
			/>
			<!-- <p>You entered: {searchText}</p> Display the entered text -->
			{#if searchingTags}
				<span class="absolute inset-y-0 right-0 flex items-center pr-2 h-full text-sm text-cente">
					<div class="bg-black/10 rounded p-1 px-2 text-xs">searching tags</div>
				</span>
			{/if}
		</div>
		<Filter bind:filterData />
	</div>
</div>
