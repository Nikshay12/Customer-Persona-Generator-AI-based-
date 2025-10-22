from sklearn.cluster import KMeans

def generate_personas(df, n_clusters=3):
    """
    Clusters users into personas using KMeans.
    """
    features = df.drop(columns=['user_id'])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['persona'] = kmeans.fit_predict(features)
    return df, kmeans
