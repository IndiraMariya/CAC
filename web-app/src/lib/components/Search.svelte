<script>
	let showMessage = false;
	let isClicked = false;

	let searchText = '';

	function toggleMessage() {
		showMessage = !showMessage;
		isClicked = !isClicked;
	}
</script>

<div>
	<button on:click={toggleMessage}>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			height="1em"
			viewBox="0 0 512 512"
			class="fill-red-300 hover:fill-red-500 absolute right-2 top-2"
			id="searchIcon"
			class:move-right={isClicked}
			><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
			<path
				d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"
			/>
		</svg>
	</button>
</div>

{#if showMessage}
	<form action="/">
		<input class = "absolute right-2 top-4" type="text" name="q" placeholder="Search.." bind:value={searchText} />
		<!-- <p>You entered: {searchText}</p> Display the entered text -->
	</form>
{/if}

<style>
	.move-right {
		transform: translateX(-200px); /* Adjust the value to control the shift distance */
		transition: transform 0.3s; /* Add a smooth transition effect */
	}
	svg {
		/* position: absolute; */
		padding: 20px;
		width: 70px;
		height: 70px;
	}
	input {
		position: absolute;
		padding: 20px;
		right: 20px;
		width: 200px;
		height: 50px;
		border-radius: 5px;
	}
	div {
		background-color: #fdf5f0;
	}
</style>
