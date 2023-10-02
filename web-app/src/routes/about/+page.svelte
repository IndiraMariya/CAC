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
	<Nav></Nav>
	<h1 class="h1">About the Project</h1>
	<div class="container">      
        <br>
        <br>  
        <h2 class="h2">Our Mission</h2>
        <p>
            At Double Scoop, our mission is clear: we're dedicated to empowering young minds by equipping them with the tools they need to critically evaluate news content. We recognize that teenagers are the future leaders and decision-makers of the world, and it's crucial that they have access to accurate, unbiased information to make informed choices.
        </p>
        <br>
        <br>
        <h2 class="h2">The Problem</h2>
        <p>
            Teenagers today are bombarded with political news from various sources, each with its own agenda and perspective. This can make it challenging to separate facts from opinions, identify biases, and understand the implications of different political viewpoints. Misinformation and bias can lead to misunderstandings and reinforce stereotypes, hindering the development of well-informed citizens.
        </p>
        <br>
        <br>
        <h2 class="h2">Our Solution</h2>
        <p>
            Double Scoop offers a user-friendly platform that encourages teens to engage with political news critically. Our unique features include:
        </p>
        <ul>
            <li><strong>1. Bias Detection Tools:</strong> Our advanced algorithms analyze news articles and provide users with a bias score, helping them understand the political slant of the content.</li>
            <li><strong>2. Educational Resources:</strong> We offer a comprehensive library of articles, videos, and interactive tutorials designed to enhance media literacy skills, including fact-checking and source evaluation.</li>
            <li><strong>3. Community Engagement:</strong> Double Scoop fosters a supportive community where teenagers can discuss news stories, ask questions, and share their perspectives in a respectful environment.</li>
            <li><strong>4. Tailored Content:</strong> We curate news stories specifically aimed at teenagers, ensuring that the content is age-appropriate, engaging, and easy to understand.</li>
        </ul>
        <br>
        <br>
        <h2 class="h2">Why Double Scoop?</h2>
        <p>
            <strong>Empowerment:</strong> We believe that knowledge is power. By teaching teens how to identify biases and assess news sources, we empower them to become informed, independent thinkers.
        </p>
        <p>
            <strong>Critical Thinking:</strong> Our platform encourages teens to think critically about the news they encounter, fostering a habit of discernment that will serve them well throughout their lives.
        </p>
        <p>
            <strong>Safe Space:</strong> Double Scoop is a safe space where teenagers can explore political topics without fear of judgment or hostility.
        </p>
        <br>
        <br>
        <h2 class="h2">Join Us Today</h2>
        <p>
            Whether you're a teenager looking to understand the world of politics or a concerned parent hoping to guide your child through the information maze, Double Scoop is here to help. Together, we can build a generation of young citizens who are well-equipped to engage with the political landscape, challenge biases, and contribute to a more informed and equitable society.
        </p>
        <p>
            Join Double Scoop today and embark on a journey toward media literacy and unbiased news consumption. Together, we can create a brighter future built on understanding, tolerance, and well-informed decision-making.
        </p>
    </div>
</div>
<br>
<br>
<Footer></Footer>