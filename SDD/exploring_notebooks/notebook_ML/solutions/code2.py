### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def all_pearson(M, user_means, common_items_threshold=5):
    M_normed = (M - user_means[:,None])*(M != 0)
    M_col_normed = (M_normed**2) @ (M_normed != 0).T
    common_items = (M!=0).astype(float) @ (M!=0).T
    return (M_normed @ M_normed.T)/(np.sqrt(M_col_normed*M_col_normed.T)+1e-14) * (common_items >= common_items_threshold)

def all_constrained_person(M,neutral_rating, common_items_threshold=5):
    M_normed = (M - neutral_rating)*(M != 0)
    M_col_normed = (M_normed**2) @ (M_normed!=0).T
    common_items = (M!=0).astype(float) @ (M!=0).T
    return (M_normed @ M_normed.T)/(np.sqrt(M_col_normed*M_col_normed.T)+1e-14) * (common_items >= common_items_threshold)

def all_spearman(M,common_items_threshold = 5):
    M_ranked = st.rankdata(M)*(M != 0)
    M_col_ranked = (M_ranked**2) @ (M_ranked!=0).T
    common_items = (M!=0).astype(float) @ (M!=0).T
    return (M_ranked @ M_ranked.T)/(np.sqrt(M_col_ranked*M_col_ranked.T)+1e-14) * (common_items >= common_items_threshold)
    
def all_cosine(M):
    M_normed = np.sqrt((M**2).sum(axis=1))
    return (M @ M.T) / np.outer(M_normed, M_normed)