# Classic-Movie-Recommender

![MOV_REC](https://github.com/ANURUDRA-JENA/Web-Scraping-Project-2/blob/6045fc0f32a07d37d7d5fcc442898769fa879365/asset_management/Designer%20(4).png)

<p data-sourcepos="3:1-3:43"><strong>Movie Recommender I: A Personal Journey</strong></p>
<p data-sourcepos="5:1-5:36"><strong>Data Acquisition and Preparation</strong></p>
<p data-sourcepos="7:1-7:58">I started with the IMDB Dataset,&nbsp;a treasure trove of movie information.&nbsp;My plan was to leverage key features like genre,&nbsp;keywords,&nbsp;overview,&nbsp;cast,&nbsp;and crew to identify movie connections and make personalized recommendations.&nbsp;While I initially considered incorporating reviews,&nbsp;I decided against it due to their subjective nature,&nbsp;which could introduce bias into my LSTM algorithm.</p>
<p data-sourcepos="9:1-9:41">To create a unified dataset,&nbsp;I merged the various components of the IMDB Dataset and extracted the necessary features.&nbsp;This initial data processing step yielded a comprehensive dataset spanning from 1984 to 2013.</p>
<p data-sourcepos="11:1-11:43"><strong>Expanding the Dataset with Web Scraping</strong></p>
<p data-sourcepos="13:1-13:361">To include more recent movies,&nbsp;I embarked on a web scraping project.&nbsp;I initially attempted to use Wikipedia&apos;s API to extract movie titles but found it to be ineffective.&nbsp;Instead,&nbsp;I turned to IMDB&apos;s website and used a Python scraper (available on GitHub) to collect genre,&nbsp;keywords,&nbsp;overview,&nbsp;and other relevant details for movies released between 2013 and 2023.</p>
<p data-sourcepos="15:1-15:229">To optimize the scraping process,&nbsp;I utilized Python&apos;s Multiprocessing and Pooling modules.&nbsp;While multi-threading might have been faster for read-write operations,&nbsp;my approach of opening four links simultaneously and scraping data for individual movies proved to be more efficient.&nbsp;I iteratively scraped movie information,&nbsp;appended it to a shared memory pool,&nbsp;converted the pool into a DataFrame,&nbsp;and finally outputted the results in CSV format.</p>
<p data-sourcepos="17:1-17:32"><strong>Data Cleaning and Processing</strong></p>
<p data-sourcepos="19:1-19:242">With the data collected,&nbsp;I focused on cleaning and processing it.&nbsp;Given my prior knowledge of the required features,&nbsp;I extracted only those elements,&nbsp;streamlining the process.&nbsp;This resulted in two datasets,&nbsp;ready for the recommendation phase.</p>
<p data-sourcepos="21:1-21:29"><strong>Recommendation Generation</strong></p>
<p data-sourcepos="23:1-23:201">Once the data was prepared, I employed the LSTM algorithm to generate personalized movie recommendations. By analyzing the extracted features and patterns within the dataset, the LSTM model was able to suggest movies that aligned with users&apos; preferences and interests.</p>

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

<h3>About the LSTM Model:</h3>
<ol>
    <li>
        <p><strong>Stemming:</strong></p>
        <ul>
            <li>A <code>PorterStemmer</code> object is created to reduce words to their base form.</li>
            <li>A function <code>stem</code> is defined to apply stemming to a given text, splitting it into words and stemming each word using the <code>PorterStemmer</code>.</li>
            <li>The <code>stem</code> function is applied to the <code>collection</code> column of the <code>final_merge</code> DataFrame, creating a new column with stemmed words.</li>
        </ul>
    </li>
    <li>
        <p><strong>Feature Extraction:</strong></p>
        <ul>
            <li>A&nbsp;<code>CountVectorizer</code> object is created with a maximum feature count of 5000 and English stop words removed.</li>
            <li>The&nbsp;<code>fit_transform</code> method of the&nbsp;<code>CountVectorizer</code> is applied to the stemmed&nbsp;<code>collection</code> column of&nbsp;<code>final_merge</code>,&nbsp;creating a term frequency matrix.</li>
            <li>The matrix is converted to a NumPy array and its shape is printed.</li>
        </ul>
    </li>
    <li>
        <p><strong>Similarity Calculation:</strong></p>
        <ul>
            <li>A&nbsp;<code>cosine_similarity</code> function is used to calculate the cosine similarity between the feature vectors of the movies.</li>
        </ul>
    </li>
    <li>
        <p><strong>Recommendation Function:</strong></p>
        <ul>
            <li>A function&nbsp;<code>recommend</code> is defined to take a movie title as input and recommend similar movies.</li>
            <li>The index of the input movie is found in the&nbsp;<code>final_merge</code> DataFrame.</li>
            <li>The cosine similarity between the input movie and all other movies is calculated.</li>
            <li>The most similar movies (excluding the input movie itself) are sorted based on their similarity scores and the top 5 are printed.</li>
        </ul>
    </li>
</ol>
<p>In summary, the code first prepares the data by stemming the words and creating a term frequency matrix. Then, it calculates the similarity between movies based on their feature vectors. Finally, it provides a recommendation function that suggests similar movies based on the input movie title.</p>

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
