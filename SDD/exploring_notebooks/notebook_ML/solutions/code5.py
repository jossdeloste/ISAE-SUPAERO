### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

S_all_cosine = all_cosine(M.T)
M_T = M.T
item_pr = item_item_predict( M_T, S_all_cosine, movie_means,10)
item_pr