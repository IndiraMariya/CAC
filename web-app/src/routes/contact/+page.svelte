<script>
	import Nav from '$lib/components/Nav.svelte';
    import Footer from '$lib/components/footer.svelte';
	import PageContainer from '$lib/components/PageContainer.svelte';
    // Data for each member
    let members = [
      {
        name: 'Indira Mariya',
        role: 'Developer',
        blurb: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non purus at ante aliquet.',
        image: '/filler_img.jpeg', // Image file path
      },
      {
        name: 'Jane Smith',
        role: 'Developer',
        blurb: 'Vestibulum cursus ultricies nulla, ut vehicula ligula iaculis at. Fusce tristique malesuada.',
        image: '/filler_img.jpeg',
      },
      {
        name: 'Bob Johnson',
        role: 'Designer',
        blurb: 'Aenean a libero elit. Phasellus egestas vel elit id bibendum. Vivamus bibendum euismod dui.',
        image: '/filler_img.jpeg',
      },
      {
        name: 'Shmob Johnson',
        role: 'Designer',
        blurb: 'Aenean a libero elit. Phasellus egestas vel elit id bibendum. Vivamus bibendum euismod dui.',
        image: '/filler_img.jpeg',
      },
    ];
</script>

<PageContainer>
    <header>
        <Nav></Nav>
    </header>
    <h1 class="pb-5 text-4xl ">Meet the Members</h1>
  
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4">
    {#each members as member (member.name)}
      <div class="bg-white shadow-md p-4 rounded-lg">
        <img src={member.image} alt={member.name} class="w-full h-auto" />
  
        <h2 class="text-xl font-semibold mt-2">{member.name}</h2>
        <p class="text-gray-600">{member.role}</p>
        <p class="text-sm mt-2">{member.blurb}</p>
      </div>
    {/each}
  </div>  
    
</PageContainer>

<Footer></Footer>