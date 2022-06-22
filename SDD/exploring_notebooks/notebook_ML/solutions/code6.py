### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

S_all_cosine = all_cosine(M.T)
M_T = M.T
predictions = np.array([item_item_predict(M_T,S_all_cosine,movie_means,i) for i in range(M_T.shape[0])]).T

def recommendation_movies(movie_Ids_columns,userID,predictions,movies,number_recommendations = 10):
    temp = pd.DataFrame(predictions.T)
    rate_user = temp[userID]
    sorted_user= pd.DataFrame(temp[userID].sort_values(ascending=False))
    top10_index = sorted_user[0:10].index.values
    recommendations = [movies[movies['movieId']==movie_Ids_columns[i]]['title'].values[0] for i in top10_index]
    return recommendations

recommendation_movies(movie_Ids_columns,4,predictions,movies)