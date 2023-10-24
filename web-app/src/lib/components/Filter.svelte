<script>
    let isClicked = false;
    let isPicked = false;
    let formElement;
    let filterCriteria = '';
  
    const filterOptions = [
      { name: 'Date', value: 'date' },
      { name: 'Topic', value: 'topic' },
      { name: 'Bias', value: 'bias' },
    ];
  
    // Function to set the current filter criteria
    function setFilter(value) {
      filterCriteria = value;
      isPicked = !isPicked;
  
      // Update the URL when filterCriteria changes
      const urlSearchParams = new URLSearchParams(window.location.search);

// Get the existing 'q' parameter
const existingQ = urlSearchParams.get('q');

// Update the 'filter' parameter
urlSearchParams.set('filter', filterCriteria);

// If 'q' parameter exists, set it back to the updated URL
if (existingQ) {
  urlSearchParams.set('q', existingQ);
}

// Get the updated URL with both 'q' and 'filter' parameters
const updatedURL = `${window.location.pathname}?${urlSearchParams.toString()}`;

// Push the updated URL to the browser's history
window.history.pushState({}, '', updatedURL);

// Reload the page to reflect the changes
window.location.reload();

    }
  
    function toggleFilter() {
      isClicked = !isClicked;
    }
  
    // Watch for changes in isPicked
    $: {
      if (isPicked) {
        formElement.submit();
      }
    }
  </script>
  
  <div class="flex items-center">
    <button class="mr-4" on:click={toggleFilter}>
        <svg 
        xmlns="http://www.w3.org/2000/svg" 
        height="1em" 
        viewBox="0 0 512 512" 
        id = "filterIcon"
        class = "fill-red-300 hover:fill-red-500 absolute left-2 top-2 w-70 h-70">
        
        <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
        <path d="M3.9 54.9C10.5 40.9 24.5 32 40 32H472c15.5 0 29.5 8.9 36.1 22.9s4.6 30.5-5.2 42.5L320 320.9V448c0 12.1-6.8 23.2-17.7 28.6s-23.8 4.3-33.5-3l-64-48c-8.1-6-12.8-15.5-12.8-25.6V320.9L9 97.3C-.7 85.4-2.8 68.8 3.9 54.9z"/>
    </button>
  
    {#if isClicked}
      <div class="flex space-x-2 absolute top-6 left-20">
        {#each filterOptions as option}
          <button
            on:click={() => setFilter(option.value)}
            class="px-2 py-1 rounded border border-gray-400 hover:bg-gray-200"
            class:active={filterCriteria === option.value}>
            {option.name}
          </button>
        {/each}
      </div>
    {/if}
  </div>
  
  {#if isPicked}
    <form bind:this={formElement}>
      <input id="filter" class="hidden" type="text" name="filter" bind:value={filterCriteria} />
    </form>
  {/if}
  
  <style>
    svg{
        height: 70px;
        width: 70px;
        padding: 20px;
    }
  </style>
