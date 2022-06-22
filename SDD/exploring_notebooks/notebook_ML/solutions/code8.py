### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

nmf_model = NMF(n_components = 20)
# Matrix factorization R ~ UT.T  (Find two non-negative matrices (U, T) whose product approximates the non- negative matrix X. )
nmf_model.fit(M)
U = nmf_model.transform(M) # user latent factors (U user matrix)
T = nmf_model.components_.T # item latent factors (T is item matrix)
M_pred = U@T.T
M_pred.shape
preds = pd.DataFrame(M_pred,columns = movie_Ids_columns)

already_rated,recommendations = recommend_movies(preds,4,movies,ratings,10)
recommendations