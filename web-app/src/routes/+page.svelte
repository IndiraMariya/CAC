<script>
	import Topic from '$lib/components/Topic.svelte';

	export let data;
</script>

<div class="p-6">
	<h1 class="pb-5 text-4xl font-bold">APP NAME</h1>
	<ul>
		{#each data.topics as topic}
			{#if topic.articleData}
				<Topic {...topic} />
			{/if}
		{/each}
	</ul>
</div>
