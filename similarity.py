import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity


data = pd.read_csv("spotify_songs.csv", encoding = "ISO-8859-1")
# data.head()
# print(data)


# PREPROCESSING
data.drop(['acousticness', 'instrumentalness', 'liveness', 'valence' , 'tempo', 'duration_ms', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'playlist_name','playlist_id','track_album_release_date'], axis=1 ,inplace=True)
# data.info()
data.drop_duplicates(subset=['lyrics'], inplace=True)
data.duplicated(subset=['lyrics']).sum()


data.fillna("nan", inplace=True)
# data.isnull().sum()

data['lyrics']= data['lyrics'].apply(lambda x:x.split())
data['playlist_subgenre']= data['playlist_subgenre'].apply(lambda x:x.split())
data['playlist_genre']= data['playlist_genre'].apply(lambda x:x.split())
data['track_artist'] = data['track_artist'].apply(lambda x:x.split())

#creating tags for algorithms
data['tags'] = data['track_artist'] + data['lyrics'] +  data['playlist_genre'] + data['playlist_subgenre']

data['track_artist']=data['track_artist'].apply(lambda x:" ".join(x))
data['track_artist']=data['track_artist'].str.replace("-","")
data['track_name']=data['track_name'].str.replace("-","")
data['lyrics']=data['lyrics'].apply(lambda x:" ".join(x))
data['playlist_genre']=data['playlist_genre'].apply(lambda x:" ".join(x))
data['playlist_subgenre']=data['playlist_subgenre'].apply(lambda x:" ".join(x))

data['tags2']= data['tags']

data['tags']=data['tags'].apply(lambda x : " ".join(x))

data['tags']=data['tags'].apply(lambda x : x.lower())

# VECTORIZATION
cv = CountVectorizer(max_features=1000, stop_words='english')
vectors = cv.fit_transform(data['tags']).toarray()

# ps = PorterStemmer()

# def stem(text):
#     y=[]
#     for i in text.split():
#         y.append(ps.stem(i))
        
#     return  " ".join(y)

# data['tags'] = data['tags'].apply(stem)


# Calculating cosine distance of the song vectors
similarity = cosine_similarity(vectors)
# print(similarity)