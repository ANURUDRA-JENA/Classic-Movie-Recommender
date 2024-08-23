# importing dependenceies

import nltk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
import pandas as pd

def recommend(movie):
    index = final_merge[final_merge['original_title'] == movie].index[0]
    distances = similarity[index]
    most_similar_movies = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    for i in most_similar_movies:
        print(final_merge.iloc[i[0]].original_title)

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
        
    return " ".join(y)

#importing the dataset
final_merge = pd.read_csv(r"Final_dataset.csv")
final_merge['collection'] = final_merge['collection'].astype(str)

# Creating Porter stemmer object
ps = PorterStemmer()

# applying the stemming process to our collection of data
final_merge['collection'] = final_merge['collection'].apply(stem)

# Creating a vector from our vocabulary of words and removing the common non-relevnt words
cv = CountVectorizer(max_features=5000,stop_words='english')

# Fitting the vector of vocabulary with our collection of words for each individual movie
# its like creating a matrix consisting of movies in each row and every distinct word of
# our vocabulary in the columns and every movie will be having a vector which will go through
# only those columns of which the words descrivbes the movie best
vector = cv.fit_transform(final_merge['collection']).toarray()
vector.shape

# defining a similarity object which will make relations among movies and according to which
# we can have our recommender sustem give similarly vectorised movies with our choice provided.
similarity = cosine_similarity(vector)

inp = ''
while inp != 'none':
    inp = input("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nPlease input your movie of choice: ")
    print('\n')
    if inp != 'none':
        recommend(inp)