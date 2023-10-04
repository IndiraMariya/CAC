<script>
	export let showModal; // boolean
	let dialog; // HTMLDialogElement

	$: if (dialog && showModal) dialog.showModal();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-noninteractive-element-interactions -->
<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
    class="max-w-4xl mx-5 rounded-sm text-color-p_blue p-3 font-body open:backdrop:bg-black/30"
>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div on:click|stopPropagation class="p-4">
        <!-- svelte-ignore a11y-autofocus -->
		<button autofocus 
        on:click={() => dialog.close()} class="absolute top-10 right-20 text-2xl cursor-pointer">x</button>
		<slot name="header" />
		<hr />
		<slot />
		<hr />
	</div>
</dialog>

<style>
	dialog[open] {
		animation: zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
	}
	@keyframes zoom {
		from {
			transform: scale(0.95);
		}
		to {
			transform: scale(1);
		}
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
</style>
