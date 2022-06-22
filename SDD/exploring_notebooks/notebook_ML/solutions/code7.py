### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

U,D,T = svds(M,k=100)
D = np.diag(D)
predicted_ratings = U@D@T 
preds = pd.DataFrame(predicted_ratings,columns = movie_Ids_columns)
preds.head()