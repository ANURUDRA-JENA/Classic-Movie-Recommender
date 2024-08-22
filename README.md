# Classic-Movie-Recommender

![MOV_REC](https://github.com/ANURUDRA-JENA/Web-Scraping-Project-2/blob/6045fc0f32a07d37d7d5fcc442898769fa879365/asset_management/Designer%20(4).png)

<p data-sourcepos="3:1-3:38"><strong>Movie Recommender I: A Walkthrough</strong></p>
<p data-sourcepos="5:1-5:23"><strong>Dataset Preparation</strong></p>
<p data-sourcepos="7:1-7:84">Our starting point was the extensive IMDB Dataset,&nbsp;which encompasses movie metadata,&nbsp;ratings,&nbsp;links,&nbsp;keywords,&nbsp;and credits.&nbsp;For our recommender system,&nbsp;we focused on key features like genre,&nbsp;keywords,&nbsp;overview,&nbsp;cast,&nbsp;and crew,&nbsp;all of which are readily available on individual movie pages.&nbsp;While initially considering reviews,&nbsp;we decided to exclude them due to their subjective nature,&nbsp;which could potentially introduce bias into our LSTM algorithm&apos;s decision-making process.</p>
<p data-sourcepos="9:1-9:138">To consolidate the necessary information,&nbsp;we merged the various datasets and extracted the relevant features.&nbsp;This initial data processing step yielded a comprehensive dataset spanning from 1984 to 2013.</p>
<p data-sourcepos="11:1-11:25"><strong>Expanding the Dataset</strong></p>
<p data-sourcepos="13:1-13:390">To ensure our recommendations included more recent movies,&nbsp;we embarked on a web scraping endeavor.&nbsp;We initially attempted to extract movie titles from Wikipedia using its API,&nbsp;but when that proved unsuccessful,&nbsp;we turned to IMDB&apos;s website.&nbsp;Our scraper,&nbsp;hosted on GitHub,&nbsp;efficiently collected genre,&nbsp;keywords,&nbsp;overview,&nbsp;and other essential details for movies released between 2013 and 2023.</p>
<p data-sourcepos="15:1-15:152">To expedite the scraping process,&nbsp;we leveraged Python&apos;s Multiprocessing and Pooling modules.&nbsp;While multi-threading might have been faster for read-write operations,&nbsp;our approach of opening four links simultaneously and scraping data for individual movies proved to be more efficient.&nbsp;We iteratively scraped movie information,&nbsp;appended it to a shared memory pool,&nbsp;converted the pool into a DataFrame,&nbsp;and finally outputted the results in CSV format.</p>
<p data-sourcepos="17:1-17:32"><strong>Data Cleaning and Processing</strong></p>
<p data-sourcepos="19:1-19:276">Once the data was collected,&nbsp;we meticulously cleaned and processed it.&nbsp;Given our prior knowledge of the required features,&nbsp;we focused solely on extracting and preparing these specific elements.&nbsp;This step resulted in two datasets,&nbsp;ready for the subsequent recommendation phase.</p>
<p data-sourcepos="21:1-21:29"><strong>Recommendation Generation</strong></p>
<p data-sourcepos="23:1-23:138">With the data prepared, we employed the LSTM algorithm to generate personalized movie recommendations. By analyzing the extracted features and patterns within the dataset, the LSTM model was able to suggest movies that aligned with users&apos; preferences and interests.</p>


<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:19px;">Objective</span></strong></p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>To create a movie recommender system that:</p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Utilizes the latest movie data.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Employs LSTM for recommendation.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Leverages movie reviews as a significant factor.</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:19px;">Challenges</span></strong></p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>Lack of Data:</strong> The system cannot be pre-built and tested with old datasets.</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:19px;">Proposed Solution</span></strong></p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:16px;">Data</span> Collection</strong></p>
<ol style="margin-bottom:0in;margin-top:0in;" start="1" type="1">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>Title Scraper:</strong>
        <ul style="margin-bottom:0in;margin-top:0in;" type="circle">
            <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Create a script to scrape movie titles from online sources (e.g., IMDB, Rotten Tomatoes).</li>
            <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Focus on movies released post-2013 for the latest data.</li>
        </ul>
    </li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>Movie Data Scraper:</strong>
        <ul style="margin-bottom:0in;margin-top:0in;" type="circle">
            <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>For each scraped title, create a script to extract detailed information:<ul style="margin-bottom:0in;margin-top:0in;" type="square">
                    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Release year</li>
                    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Genre</li>
                    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Cast</li>
                    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Director</li>
                    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Plot summary</li>
                    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>User ratings</li>
                    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Movie reviews</li>
                </ul>
            </li>
            <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Utilize web scraping techniques (e.g., BeautifulSoup, Selenium) to extract data from relevant websites.</li>
        </ul>
    </li>
</ol>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:16px;">Dataset Creation</span></strong></p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Combine the scraped data with the old IMDB dataset to create a comprehensive dataset.</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:16px;">LSTM Model</span></strong></p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Develop an LSTM-based recommender system.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Train the model on the combined dataset, focusing on the relationship between movie attributes (e.g., genre, cast, plot) and user preferences (e.g., liked movies, reviews).</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>The model should be able to predict future movie preferences based on past behavior.</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:16px;">Recommendation Generation</span></strong></p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Use the trained LSTM model to generate recommendations for users based on their liked movies.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Consider factors like genre preferences, actor preferences, and sentiment analysis of movie reviews.</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:16px;">Testing and Evaluation</span></strong></p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Collect user feedback on the recommendations to assess the system&apos;s accuracy and effectiveness.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>Iterate on the model and data collection process to improve performance.</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style="font-size:16px;">Potential Improvements</span></strong></p>
<ul style="margin-bottom:0in;margin-top:0in;" type="disc">
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>User-Generated Data:</strong> Encourage users to provide ratings and reviews to enrich the dataset.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>Real-time Updates:</strong> Implement mechanisms to continuously update the dataset with new movies and user data.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>Hybrid Approach:</strong> Combine collaborative filtering techniques with content-based filtering for more personalized recommendations.</li>
    <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>Contextual Recommendations:</strong> Consider factors like user mood, time of day, or location to provide more relevant suggestions.</li>
</ul>
