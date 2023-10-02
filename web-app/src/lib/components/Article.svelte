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
  	export let showModal = false;
  	// @ts-ignore
  	let dialog; // Reference to the dialog element

	function openModal() {
		showModal = true;
		// @ts-ignore
		dialog.showModal();
	}

</script>
<style>
	@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,200&display=swap');
	.all{
		font-family: 'Source Serif 4';
	}
	.card{
		border: 1px solid black;
		background-color: rgba(255, 255, 255, 0.747);
		
	}
	.card:hover{
		border: 2px solid rgb(229, 49, 49);
		background-color: rgba(255, 255, 255, 0.747);
		background-color:rgba(255, 255, 255, 0.392);
	}
</style>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="card relative group shadow h-70 w-96 flex flex-col overflow-hidden all" role="button" tabindex="0" on:click={openModal}>
    <div class="flex justify-between">
        <div class="font-medium p-2" style="font-style:oblique; color: black;">{newsSource}</div>
        <div class="p-2 text-right" style="color:red;">{new Date(date).toLocaleDateString()}</div>
    </div>

    <div class="p-2">
        <div class="font-medium text-xl line-clamp-2 overflow-hidden">{title}</div>
    </div>

    <a
        {href}
        on:mouseenter={() => {
            hovering = true;
        }}
        on:mouseleave={() => {
            hovering = false;
        }}
        class="w-full h-full font-thin"
    >
        <img {src} {alt} class="w-full h-60 object-cover" />
        <div class="p-3 overflow-hidden">
            <div>{author}</div>
            {#if hovering}
                <div class="font-normal text-sm mt-3" transition:slide>{description}</div>
            {/if}
        </div>
    </a>
</div>
