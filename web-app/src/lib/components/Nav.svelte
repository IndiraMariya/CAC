<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,200;0,8..60,300;0,8..60,900;1,8..60,200;1,8..60,900&display=swap" rel="stylesheet">

<div class=" text-black  top-0 left-0 right-0 z-50 py-2 text-center">
    <a href="/">
        <!-- svelte-ignore a11y-img-redundant-alt -->
        <img src="/src/static/cartoonsketches500.png" alt="Description of the image" width="300" height="200" class="mx-auto">
    </a>
</div>

<div class=" text-black top-40 left-0 right-0 z-50 text-center" >
    <div class="p-4" style="color: rgb(59,73,155; font-weight: bold; font-size: 25px;">
        <nav class="container mx-auto flex justify-evenly items-center py-2 ">
            <a class="nav-link px-4 hover:text-red-500" href="/"><i>HOME</i></a>
            <a class="nav-link px-4 hover:text-red-500" href="/explore"><i>EXPLORE</i></a>
            <a class="nav-link px-4 hover:text-red-500" href="/about"><i>ABOUT</i></a>
            <a class="nav-link px-4 hover:text-red-500" href="/learn"><i>LEARN</i></a>
            <a class="nav-link px-4 hover:text-red-500" href="/contact"><i>CONTACT</i></a>
        </nav>
    </div>
</div>
<!-- <script>
    let isHovered = false;
  
    function toggleHover() {
      isHovered = !isHovered;
    }
  
    function handleBlur() {
      isHovered = false;
    }
</script> -->
  
  <!-- <style>
    /* Add your Tailwind CSS classes here */
    .red-dot {
      left: -4px; /* Adjust the left position as needed */
      top: 50%; /* Adjust the top position as needed */
      transform: translateY(-50%);
      width: 8px;
      height: 8px;
      background-color: red;
      border-radius: 50%;
      position: absolute;
    }
  </style> -->
  
  <!-- <div class="text-black top-0 left-0 right-0 z-50 py-2 text-center">
    <a href="/">
      <img src="/src/static/cartoonsketches500.png" alt="Description of the image" width="300" height="200" class="mx-auto" />
    </a>
  </div> -->
  
  <!-- <div class="text-black top-40 left-0 right-0 z-50 text-center">
    <div class="p-4" style="color: rgb(59,73,155); font-weight: bold; font-size: 25px;">
      <nav class="container mx-auto flex justify-evenly items-center py-2">
        <a
          class="nav-link px-4 hover:text-red-500 relative"
          href="/"
          on:mouseover={toggleHover}
          on:focus={toggleHover}
          on:mouseout={handleBlur}
          on:blur={handleBlur}
          tabindex="0"
        >
          <i>HOME</i>
          {#if isHovered}
            <span class="red-dot"></span>
          {/if}
        </a>

        <a
        class="nav-link px-4 hover:text-red-500 relative"
        href="/explore"
        on:mouseover={toggleHover}
        on:focus={toggleHover}
        on:mouseout={handleBlur}
        on:blur={handleBlur}
        tabindex="0"
      >
        <i>EXPLORE</i>
        {#if isHovered}
          <span class="red-dot"></span>
        {/if}
      </a>

      <a
      class="nav-link px-4 hover:text-red-500 relative"
      href="/"
      on:mouseover={toggleHover}
      on:focus={toggleHover}
      on:mouseout={handleBlur}
      on:blur={handleBlur}
      tabindex="0"
    >
      <i>HOME</i>
      {#if isHovered}
        <span class="red-dot"></span>
      {/if}
    </a>

    <a
    class="nav-link px-4 hover:text-red-500 relative"
    href="/"
    on:mouseover={toggleHover}
    on:focus={toggleHover}
    on:mouseout={handleBlur}
    on:blur={handleBlur}
    tabindex="0"
  >
    <i>HOME</i>
    {#if isHovered}
      <span class="red-dot"></span>
    {/if}
  </a>
      </nav>
    </div>
  </div>
   -->