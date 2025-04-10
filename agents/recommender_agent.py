import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'recommender_model.pkl')
with open(model_path, 'rb') as f:
    df, tfidf, similarity_matrix = pickle.load(f)

def get_recommendations(product_name, top_n=3):
    if product_name not in df['product_name'].values:
        return ["Product not found in catalog."]
    idx = df[df['product_name'] == product_name].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    return [df.iloc[i[0]]['product_name'] for i in sim_scores]
