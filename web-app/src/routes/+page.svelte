<script>
	import Topic from '$lib/components/Topic.svelte';

	export let data;
</script>

<div class="p-6">
	<h1>APP NAME</h1>
	<ul>
		{#each data.topics as topic}
			{#if topic.articleData}
				<Topic {...topic} />
			{/if}
		{/each}
	</ul>
</div>
