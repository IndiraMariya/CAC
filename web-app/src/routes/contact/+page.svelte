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
    
    .h3{
        font-weight: medium;
        font-size: 20px;
    }
    
 </style>
<div class="page-container">
    <header>
        <Nav></Nav>
    </header>
    <h1 class="pb-5 text-4xl ">Meet the Members</h1>
    <p></p>
    
</div>
<Footer></Footer>