<script>
	import { slide } from 'svelte/transition';

	export let title = '';
	export let href = '';
	export let description = '';
	export let author = '';
	export let date = '';
	export let src = '';
	export let alt = '';
	export let newsSource = '';

	let hovering = false;
</script>

<div class="relative group shadow h-70 w-96 flex flex-col rounded-md overflow-hidden">
    <div class="flex justify-between">
        <div class=" font-bold p-2" style="font-style:oblique; background-color: #FFFFFF; border-radius: 10px;">{newsSource}</div>
        <div class="p-2 text-right" style="color:red;background-color: #FFFFFF; border-radius: 10px;">{new Date(date).toLocaleDateString()}</div>
    </div>

    <div class="bg-gray-200 p-2">
        <div class="font-bold text-xl line-clamp-2 overflow-hidden">{title}</div>
    </div>

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
        <img {src} {alt} class="w-full h-40 object-cover" />
        <div class="p-3 overflow-hidden">
            <div>{author}</div>
            {#if hovering}
                <div class="text-sm mt-3" transition:slide>{description}</div>
            {/if}
        </div>
    </a>
</div>





<!-- <div class="relative shadow h-60 w-96 flex flex-row rounded-md overflow-hidden transition-transform hover:scale-105 hover:border-2 border-transparent hover:border-red-500">
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
		<div class="absolute w-full bg-black/30 bottom-0 p-3" style="color:rgb(155,73,155);">
			<div class="uppercase text-sm">{newsSource} - {new Date(date).toLocaleDateString()}</div>
			<div class="font-bold text-xl">{title}</div>
			<div>{author}</div>
			{#if hovering}
				<div class="text-sm mt-3" transition:slide>{description}</div>
			{/if}
		</div>
	</a>
</div> -->


