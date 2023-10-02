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
>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div on:click|stopPropagation>
        <!-- svelte-ignore a11y-autofocus -->
		<button autofocus on:click={() => dialog.close()}>x</button>
		<slot name="header" />
		<hr />
		<slot />
		<hr />
	</div>
</dialog>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,200&display=swap');
	dialog {
		max-width: 62em;
		border-radius: 0.2em;
		border: none;
		padding: 15dpx;
        color: rgb(34, 44, 98);
        font-family: 'Source Serif 4';
	}
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.3);
	}
	dialog > div {
		padding: 1em;
	}
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
	button {
		display: block;
        position: absolute;
		top: 10px;
		right: 20px;
		font-size: 24px;
		cursor: pointer;
	}
</style>
