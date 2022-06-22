### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def user_user_prediction(M,S,user_means,u):
        prediction = user_means[u] + (np.sum((M - user_means[:,None]) * (M != 0) * S[u,:,None],axis=0) 
                                      / np.sum((M != 0) * np.abs(S[u,:,None]),axis=0)) + 1e-14
        return prediction