<script>
	import Article from '$lib/components/Article.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import Footer from '$lib/components/footer.svelte';
	import Modal from '$lib/components/Modal.svelte';
	import Search from '$lib/components/Search.svelte'; 
	export let data;
	let showModal = false;
</script>


<Search></Search>
<Modal bind:showModal>
	<h2 class="text-3xl">
		Article Information
	</h2>

	<p>
		Title: Lorem Ipsum Article
		Author: John Doe
		Publication Date: October 1, 2023

		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae elit libero, a pharetra augue. Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Cras justo odio, dapibus ac facilisis in, egestas eget quam.

		Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Vestibulum id ligula porta felis euismod semper. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Nulla vitae elit libero, a pharetra augue. Etiam porta sem malesuada magna mollis euismod.

		Cras mattis consectetur purus sit amet fermentum. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Nullam quis risus eget urna mollis ornare vel eu leo. Donec id elit non mi porta gravida at eget metus. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Nulla vitae elit libero, a pharetra augue.

		Sed posuere consectetur est at lobortis. Nulla vitae elit libero, a pharetra augue. Integer posuere erat a ante venenatis dapibus posuere velit aliquet. Aenean lacinia bibendum nulla sed consectetur. Vestibulum id ligula porta felis euismod semper. Donec id elit non mi porta gravida at eget metus.
	</p>

	<a href="https://www.merriam-webster.com/dictionary/modal">merriam-webster.com</a>
</Modal>

<div class="p-5 text-black w-100 bg-p_bg">
	<Nav></Nav>
	<div class="font-body border-[1px] border-black">
		<div class="px-6">
			<h1 class="font-light font-display italic py-4 text-2xl color-p_text">What's the daily scoop?</h1>
			<div class="articles flex flex-wrap gap-4 ">
				{#each data.articles as article}
					{#if article.articleData}
						<Article {...article.articleData} bind:showModal={showModal}/>
					{/if}
				{/each}
			</div>
		</div>	
	</div>
</div>

<Footer></Footer>

<!-- <Topic></Topic> -->
