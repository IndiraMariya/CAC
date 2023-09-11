<div class="header-bar">
	<h1 class="text-4xl font-bold">The Double Scoop</h1>
	<h2 class=""><i>A really catchy slogan</i></h2>
</div>

<nav class="nav-bar">
	<div class="container mx-auto nav-links">
		<a class="nav-link" href="/">Home</a>
		<a class="nav-link" href="/explore">Explore</a>
		<a class="nav-link" href="/faq">FAQ</a>
		<a class="nav-link" href="/about">About Us</a>
		<a class="nav-link" href="/learn">Learn More</a>
	</div>
</nav>

<style>
	/* Style for the header bar */
	.header-bar {
		background-color: #d6f1ff; /* Your desired color */
		color: black; /* Text color for the headers */
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 50;
		padding: 10px 0; /* Adjust the padding as needed */
		text-align: center;
	}

	/* Style for the navigation bar */
	.nav-bar {
		background-color: #b5ccdf; /* Your desired color */
		color: black; /* Text color for the links */
		position: fixed;
		top: 80px; /* Adjust the value to match the height of the header bar */
		left: 0;
		right: 0;
		z-index: 50;
		text-align: center;
	}

	/* Style the navigation links */
	.nav-links {
		display: flex;
		justify-content: space-evenly;
		align-items: center;
		padding: 10px 0; /* Adjust the padding as needed */
	}

	.nav-link {
		padding: 8px 16px; /* Adjust the horizontal and vertical padding as needed */
		font-size: 18px;
	}
</style>
