<script>
	import { DATA } from '../data';
	import Topic from '$lib/components/Topic.svelte';
</script>

{#each DATA.TOPICS as topic}
	<Topic {...topic} />
{/each}
