<script>
	export let data;
	import { slide } from 'svelte/transition';
</script>

<div class="page-container">
	<h1>APP NAME</h1>
	<ul>
		{#each data.topics as topic}
			{#if topic.articleData}
				<h2>{topic.name}</h2>
				{#each topic.articleData as article}
					<li class="article">
						<div class="relative shadow h-60 w-96 flex flex-row rounded-md overflow-hidden me-4">
							<a
								href={article.href}
								on:mouseenter={() => {
									article.hovering = true;
								}}
								on:mouseleave={() => {
									article.hovering = false;
								}}
								class="w-full h-full"
							>
								<img src={article.src} alt={article.alt} class="w-full h-full object-cover" />
								<div class="absolute w-full text-white bg-black/30 bottom-0 p-3">
									<div class="uppercase text-sm">
										{article.newsSource} - {new Date(article.date).toLocaleDateString()}
									</div>
									<div class="font-bold text-xl">{article.title}</div>
									<div>{article.author}</div>
									{#if article.hovering}
										<div class="text-sm mt-3" transition:slide>{article.description}</div>
									{/if}
								</div>
							</a>
						</div>
					</li>
				{/each}
			{/if}
		{/each}
	</ul>
</div>

<style>
	.page-container {
		padding: 25px; /* Adjust the desired padding value as needed */
	}
	.article {
		padding-bottom: 5px;
	}

	h1 {
		font-size: 60px;
		padding-bottom: 20px;
	}
	h2 {
		font-size: 40px;
	}
</style>
