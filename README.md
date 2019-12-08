# Q-and-A-Analysis

NLP analysis of an Australian TV Show

<p>QandA is a weekly Australian social and political interactive live TV show, where each week a diverse range of panellist come together and discuss the social/political issues of the day. Panellists are politicians, business leaders, NGO representatives, journalist, artists, local and international and display a broad range of views.</p>  

<p>Format of the show is debate like with the show host as the mediator, topics discussed are outlined loosely in the shows promotional material for the week, questions are asked by audience members, panellists then have a discussion around the question. Viewing audience can also participate through voicing their opinions about the question/subject/panellists-answers via social media Facebook and Twitter.</p>


<p>As part of this analysis, data used will be the shows transcript available through their <a href="https://www.abc.net.au/qanda/episodes/">website</a> and Twitter data from Twitter, all data will be collected via web-scrapping.</p>

<p>The current working “hypothesis” is:</p>

<ul>
   <li>How do panellists address the question asked? (bias, positive/negative)</li>
   <li>Measure discussion between panellist relative to the question ( stronger/weaker arguments)</li>
   <li>What do Twitter audience think of the questions/subject/panellists-answers ? (for/against)</li>
</ul>
<ul>
   <p>Note: the ‘hypothesis’ may evolve as the analysis unfolds</p>
</ul>
   
<p>Python will be the main tool used for this analysis.</p>

<p><strong>Stage 1:</strong></p>
<p>Scrapping data: <i><strong>Completed</strong></i></p>
<ul>
    <li>Twitter data was scraped and saved to json file using twitterscrapper package</li>
    <li>QandA data was scrapped saved in txt file using requests package</li>
</ul>

<p><strong>Stage 2:</strong></p>
<p>Cleaning QandA data: <i><strong>Completed</strong></i></p>
<ul>
    <li>Data cleaning was completed using the Beautifulsoup package</li>
    <li>Data was organised into data frame using pandas package</li>
</ul>

<p><strong>Stage 3:</strong></p> 
<p>Natural language processing:  <strong>Current stage of analysis</strong></p>

<ul>
    <li>Data will be tokenized, stemmed/lemmatized, tagged, chunked and grouped</li>
</ul>

<p><strong>Stage 4:</strong></p>
<p>Analysis: NLP <strong>"TODO"</strong> </p>

<ul>
    <li>Python scikit-learn will be used to perform analysis</li>
</ul>
