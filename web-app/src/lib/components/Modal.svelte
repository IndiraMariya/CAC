<script>
	/**
	 * @type {boolean}
	 */
	export let showModal;

	/**
	 * @type {any}
	 */
	export let data;

	$: ({ title, href, description, author, date, src, alt, newsSource, color } = data);

	/**
	 * @type {HTMLDialogElement}
	 */
	let dialog;

	$: if (dialog && showModal) dialog.showModal();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-noninteractive-element-interactions -->
<dialog
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
	class="w-full mx-5 text-color-p_blue bg-transparent font-body open:backdrop:bg-black/70"
>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div
		on:click|stopPropagation
		class="m-auto bg-p_bg rounded-sm max-w-4xl p-7 grid grid-cols-2 gap-5"
	>
		<div>
			{#if src}
				<div class="w-full h-full shrink-0">
					<img {src} {alt} class="w-full h-full object-cover" />
				</div>
			{/if}
		</div>
		<div class="flex flex-col justify-between align-start">
			<div>
				<div class="text-3xl pb-4">{title}</div>
				<div class="font-light text-lg font-body italic uppercase pb-3">{newsSource}</div>
				<div class="font-bold text-sm pb-3">
					{#if author}
						<span class="pe-3">{author}</span>
					{/if}
					<span>{new Date(date).toLocaleDateString()}</span>
				</div>
				<div class="font-light text-sm">{description}</div>
			</div>
			<div class="flex gap-2">
				<!-- svelte-ignore a11y-autofocus -->
				<button
					autofocus
					on:click={() => window.open(href, '_blank')}
					class="cursor-pointer outline-black outline outline-1 inline-block py-1 px-3"
					>Read article</button
				>
				<button
					on:click={() => dialog.close()}
					class="cursor-pointer outline-black outline outline-1 inline-block py-1 px-3"
					>Close</button
				>
			</div>
		</div>
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
