<script>
	import { slide } from 'svelte/transition';

	export let title = '';
	export let href = '';
	export let description = '';
	export let author = '';
	export let date = new Date();
	export let src = '';
	export let alt = '';
	export let newsSource = '';

	let hovering = false;
</script>

<div class="relative shadow h-60 w-96 flex flex-row rounded-md overflow-hidden me-4">
	<a
		{href}
		on:mouseenter={() => {
			hovering = true;
		}}
		on:mouseleave={() => {
			hovering = false;
		}}
		class="w-full h-full"
	>
		<img {src} {alt} class="w-full h-full object-cover" />
		<div class="absolute w-full text-white bg-black/30 bottom-0 p-3">
			<div class="uppercase text-sm">{newsSource} - {date.toLocaleDateString()}</div>
			<div class="font-bold text-xl">{title}</div>
			<div>{author}</div>
			{#if hovering}
				<div class="text-sm mt-3" transition:slide>{description}</div>
			{/if}
		</div>
	</a>
</div>
