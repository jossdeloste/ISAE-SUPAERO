### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

S_all_cosine = all_cosine(M)

def recommend_movies(M,S,user_means,userID, movies, original_ratings, num_recommendations=10):
    predictions = pd.DataFrame(user_user_prediction(M,S,user_means,userID))
    predictions.columns = ['movieId']
    sorted_user_predictions = predictions['movieId'].sort_values(ascending=False)
    # Get the user's data and merge in the movie information.
    user_data = original_ratings_df[original_ratings.userId == (userID)]
    user_full = (user_data.merge(movies, how = 'left', left_on = 'movieId', right_on = 'movieId').
                     sort_values(['rating'], ascending=False))
    print('User '+str(userID)+' has already rated '+ str(user_full.shape[0]) +' movies')
    print('Recommending highest '+str(num_recommendations) + ' predicted ratings movies not already seen/rated ')
    # Recommend the highest predicted rating movies that the user hasn't seen yet.
    temp = pd.DataFrame(sorted_user_predictions).reset_index()
    temp.columns = ['movieId','rating']
    recommendations = (movies_df[~movies_df['movieId'].isin(user_full['movieId'])].
         merge(temp, how = 'left',left_on = 'movieId',right_on = 'movieId').rename(columns = {user_row_number: 'predictions'}).
         sort_values('rating', ascending = False).iloc[:num_recommendations, :-1])
    return user_full, recommendations

user_full, recommendations = recommend_movies(M,S_all_cosine,user_means,4,movies,ratings,num_recommendations=10)
recommendations