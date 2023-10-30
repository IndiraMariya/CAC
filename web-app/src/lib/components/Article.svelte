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
		? 'col-span-2'
		: 'col-span-1'} outline outline-1 outline-black hover:outline-2 hover:outline-p_red relative shadow h-70 w-full py-5 px-4 flex flex-row items-center gap-4 overflow-hidden font-body color-p_text card hover:bg-white/30"
	role="button"
	tabindex="0"
	on:click={openModal}
>
	{#if src}
		<div class="max-w-[50%] w-[350px] h-60 shrink-0">
			<img {src} {alt} class="w-full h-full object-cover" />
		</div>
	{/if}

	<div class="h-full flex flex-col justify-between w-full">
		<div class="font-normal text-2xl color-p_text">{title}</div>

		<div class="">
			<div class="text-p_red">{new Date(date).toLocaleDateString()}</div>
			<div
				class="text-sm py-1 px-2 bg-{color} text-white uppercase italic font-normal outline outline-1 outline-black inline-block"
			>
				{newsSource}
			</div>
		</div>
	</div>
</div>
