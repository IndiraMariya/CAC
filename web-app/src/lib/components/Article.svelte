<script>
	export let title = '';
	export let href = '';
	export let description = '';
	export let author = '';
	export let date = '';
	export let src = '';
	export let alt = '';
	export let newsSource = '';
	export let bias = '';
	export let sourceLean = '';
	export let color = 'p_blue';

	export let showModal = false;
	export let modalData;

	function openModal() {
		modalData = {
			title,
			href,
			description,
			author,
			date,
			src,
			alt,
			newsSource,
			color,
			bias,
			sourceLean
		};
		showModal = true;
	}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
	class="{src
		? 'row-span-2 sm:row-span-1 sm:col-span-2'
		: 'row-span-1 sm:col-span-1'} outline outline-1 outline-black hover:outline-2 hover:outline-p_red relative shadow h-70 w-full py-5 px-4 flex flex-col sm:flex-row items-center gap-4 overflow-hidden font-body color-p_text card hover:bg-white/30"
	role="button"
	tabindex="0"
	title={description}
	on:click={openModal}
>
	{#if src}
		<div
			class="sm:px-0 sm:max-w-[50%] w-full sm:w-[350px] h-60 shrink-0 outline outline-1 outline-black overflow-hidden"
		>
			<img {src} {alt} class="w-full h-full object-cover" />
		</div>
	{/if}

	<div class="h-full flex flex-col justify-between w-full">
		<div class="font-normal text-2xl color-p_text pb-5">{title}</div>

		<div class="flex flex-row gap-2 text-center flex-wrap">
			<div
				class="text-sm py-1 px-2 bg-{color} text-white uppercase italic font-normal outline outline-1 outline-black inline-block min-w-max"
			>
				{newsSource}
			</div>
			<div
				class="bg-p_red text-white text-sm font-normal py-1 px-2 outline outline-1 outline-black inline-block"
			>
				{new Date(date).toLocaleDateString()}
			</div>
		</div>
	</div>
</div>
