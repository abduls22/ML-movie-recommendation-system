import pandas as pd
import numpy as np
import bz2file as bz2

credits = pd.read_csv("tmdb_5000_credits.csv")
movies = pd.read_csv("tmdb_5000_movies.csv")

credits.head()
movies.head()

credits_column_renamed = credits.rename(index=str, columns={"movie_id": "id"})
movies_merge = movies.merge(credits_column_renamed, on='id')

movies_cleaned = movies_merge.drop(columns=['homepage', 'title_x', 'title_y', 'status','production_countries'])

from sklearn.feature_extraction.text import TfidfVectorizer
tfv = TfidfVectorizer(min_df=3,  max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

# Fitting the TF-IDF on the 'overview' text
tfv_matrix = tfv.fit_transform(movies_cleaned['overview'].values.astype(str))

from sklearn.metrics.pairwise import sigmoid_kernel

# Computing the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

# Reverse mapping of indices and movie titles
indices = pd.Series(movies_cleaned.index, index=movies_cleaned['original_title']).drop_duplicates()

def setup_recomendations(title):
    idx = indices[title]    
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:11]
    return sig_scores

def give_recomendations(sigs):
    movie_indices = [i[0] for i in sigs]
    return movies_cleaned['original_title'].iloc[movie_indices].to_numpy().tolist()

import dill as pickle
with open('movieRecommendations.pkl', 'wb') as file:
    pickle.dump(give_recomendations, file)
with open('movieRecommendations2.pkl', 'wb') as f:
    pickle.dump(indices, f)
with open('movieRecommendations3.pkl', 'wb') as fi:
    pickle.dump(movies_cleaned, fi)
with open('movieRecommendations4.pkl', 'wb') as fil:
    pickle.dump(setup_recomendations, fil)
with bz2.BZ2File('movieRecommendations5.pkl', 'wb') as new:
    pickle.dump(sig, new)










