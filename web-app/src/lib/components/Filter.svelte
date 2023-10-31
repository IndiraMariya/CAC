<script>
	import { slide } from 'svelte/transition';

	let isClicked = false;
	let isPicked = false;
	let formElement;
	let filterCriteria = '';

	export let filterData = [
		{ name: 'Date', value: 'date', ascending: null },
		{ name: 'Topic', value: 'topic', ascending: null },
		{ name: 'Bias', value: 'bias', ascending: null }
	];

	// Function to set the current filter criteria
	function setFilter(value) {
		filterCriteria = value;
		isPicked = !isPicked;

		// Update the URL when filterCriteria changes
		const urlSearchParams = new URLSearchParams(window.location.search);
		const existingQ = urlSearchParams.get('q');
		urlSearchParams.set('filter', filterCriteria);
		// If 'q' parameter exists, set it back to the updated URL
		if (existingQ) {
			urlSearchParams.set('q', existingQ);
		}

		const updatedURL = `${window.location.pathname}?${urlSearchParams.toString()}`;
		window.history.pushState({}, '', updatedURL);
		window.location.reload();
	}

	function toggleFilter() {
		isClicked = !isClicked;
	}

	// Watch for changes in isPicked
	$: {
		if (isPicked) {
			formElement.submit();
		}
	}

	let innerWidth;
</script>

<svelte:window bind:innerWidth />

<div class="h-full inline-flex items-center justify-center sm:ml-3 w-full sm:w-auto">
	{#if isClicked || innerWidth < 640}
		<div class="flex flex-row font-body w-full" transition:slide={{ axis: 'x' }}>
			{#each filterData as filter}
				<button
					class="w-full h-full border-black border-[1px] py-2 px-5 border-s-0 sm:border-s-[1px] sm:border-e-0 flex flex-row gap-2 hover:underline"
					on:click={() => {
						if (filter.ascending == true) {
							filter.ascending = false;
						} else if (filter.ascending == false) {
							filter.ascending = null;
						} else if (filter.ascending == null) {
							filter.ascending = true;
						}
					}}
				>
					<span>{filter.name}</span>
					{#if filter.ascending == true}
						<span>
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
									d="M15 11.25l-3-3m0 0l-3 3m3-3v7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
						</span>
					{:else if filter.ascending == false}
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
								d="M9 12.75l3 3m0 0l3-3m-3 3v-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
					{:else}
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
								d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
					{/if}
				</button>
			{/each}
		</div>
	{/if}
	<button
		on:click={toggleFilter}
		class="border-black border-[1px] p-2 sm:hover:shadow-[0_3px_3px_rgba(0,0,0,0.3)] -order-last sm:order-last"
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			fill="currentColor"
			stroke-width="1"
			class="h-6 w-6 fill-black block"
			viewBox="0 0 16 16"
		>
			<path
				d="M1.5 1.5A.5.5 0 0 1 2 1h12a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.128.334L10 8.692V13.5a.5.5 0 0 1-.342.474l-3 1A.5.5 0 0 1 6 14.5V8.692L1.628 3.834A.5.5 0 0 1 1.5 3.5v-2zm1 .5v1.308l4.372 4.858A.5.5 0 0 1 7 8.5v5.306l2-.666V8.5a.5.5 0 0 1 .128-.334L13.5 3.308V2h-11z"
			/>
		</svg>
	</button>
</div>

<!-- <div class="flex items-center">
	<button class="mr-4" on:click={toggleFilter}>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			height="1em"
			viewBox="0 0 512 512"
			id="filterIcon"
			class="fill-red-300 hover:fill-red-500 w-70 h-70"
		>
			! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc.
			<path
				d="M3.9 54.9C10.5 40.9 24.5 32 40 32H472c15.5 0 29.5 8.9 36.1 22.9s4.6 30.5-5.2 42.5L320 320.9V448c0 12.1-6.8 23.2-17.7 28.6s-23.8 4.3-33.5-3l-64-48c-8.1-6-12.8-15.5-12.8-25.6V320.9L9 97.3C-.7 85.4-2.8 68.8 3.9 54.9z"
			/>
		</svg></button
	>

	{#if isClicked}
		<div class="flex space-x-2 absolute top-6 left-20">
			{#each filterOptions as option}
				<button
					on:click={() => setFilter(option.value)}
					class="px-2 py-1 rounded border border-gray-400 hover:bg-gray-200"
					class:active={filterCriteria === option.value}
				>
					{option.name}
				</button>
			{/each}
		</div>
	{/if}
</div> -->

<!-- {#if isPicked}
	<form bind:this={formElement}>
		<input id="filter" class="hidden" type="text" name="filter" bind:value={filterCriteria} />
	</form>
{/if} -->
