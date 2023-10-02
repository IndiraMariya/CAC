<script>
	import Nav from '../../lib/components/Nav.svelte';
	import Footer from '$lib/components/footer.svelte';
</script>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,200&display=swap');
	.page-container {
		padding: 10px;
		padding-left: 80px;
		padding-right: 80px;
		color: rgb(59,73,155);
		font-family: 'Source Serif 4';
		zoom: 0.8; /* Adjust the zoom value to scale down the content */
	}
	.h1{
		font-weight: medium;
		font-size: 50px;
	}
	
	.h2{
		font-weight: medium;
		font-size: 30px;
	}
	
</style>

<div class="page-container">
	<Nav></Nav>
	<h1 class="h1">Explore</h1>
	<p>this is the explore page.</p>
</div>
<Footer></Footer>