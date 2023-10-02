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
	<h1 class="h1">Learn About Bias Detection</h1>
    <br>
    <section>
        <h2 class="h2" >Understanding Bias</h2>
        <p>Bias in articles can come in various forms, including political, cultural, and personal biases. It's important to recognize these biases to critically evaluate the information you consume.</p>
    </section>
    <br>
    <br>
    <section>
        <h2 class="h2" >Check the Source</h2>
        <p>Start by assessing the credibility of the source. Is it a reputable news organization or a personal blog? Reliable sources are less likely to have biased content.</p>
    </section>
    <br>
    <br>
    <section>
        <h2 class="h2" >Identify Loaded Language</h2>
        <p>Look for emotionally charged or loaded language in the article. Biased articles often use words that appeal to your emotions rather than presenting facts.</p>
    </section>
    <br>
    <br>
    <section>
        <h2 class="h2" >Consider the Tone</h2>
        <p>Pay attention to the overall tone of the article. Biased articles may have a strong, one-sided perspective without presenting counterarguments.</p>
    </section>
    <br>
    <br>
    <section>
        <h2 class="h2" >Check for Omissions</h2>
        <p>Biased articles may omit important information or downplay opposing viewpoints. Always look for a balanced presentation of facts.</p>
    </section>
    <br>
    <br>
    <section>
        <h2 class="h2" >Fact-Check Information</h2>
        <p>Verify any statistics, quotes, or claims presented in the article. Biased sources may manipulate data to support their agenda.</p>
    </section>
    <br>
    <br>
    <section>
        <h2 class="h2" >Seek Multiple Perspectives</h2>
        <p>To avoid biases, read articles from various sources with different viewpoints. This helps you gain a well-rounded understanding of the topic.</p>
    </section>
    <br>
    <br>
	<h1 class="h2">Frequently Asked Questions</h1>
    <br>
    <section>
        <h2 class="h3" >Q: What is Lorem Ipsum?</h2>
        <p>A: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
    </section>
    <br>
    <section>
        <h2 class="h3" >Q: Why do we use it?</h2>
        <p>A: It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
    </section>
    <br>
    <section>
        <h2 class="h3" >Q: Where does it come from?</h2>
        <p>A: Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.</p>
    </section>
    <br>
    <section>
        <h2 class="h3" >Q: Is it safe to use Lorem Ipsum?</h2>
        <p>A: Yes, Lorem Ipsum is safe to use in design and typesetting. It's often used as a placeholder text in the printing and typesetting industry.</p>
    </section>
    <br>
    <section>
        <h2 class="h3" >Q: How can I generate Lorem Ipsum text?</h2>
        <p>A: There are many online Lorem Ipsum generators available that can provide you with Lorem Ipsum text for your projects.</p>
    </section>
	
</div>
<Footer></Footer>
