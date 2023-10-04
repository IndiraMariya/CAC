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

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="outline outline-1 outline-black hover:outline-2 hover:outline-p_red relative group shadow h-70 w-96 flex flex-col overflow-hidden font-body card hover:bg-white/30" role="button" tabindex="0" on:click={openModal}>
    <div class="flex justify-between">
        <div class="font-medium p-2 text-black">{newsSource}</div>
        <div class="p-2 text-right text-p_red">{new Date(date).toLocaleDateString()}</div>
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
        class="w-full h-full"
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
