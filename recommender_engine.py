
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('data/ecommerce_data.csv')
df.dropna(inplace=True)
df['user_id'] = df['user_id'].astype(str)
df['product_id'] = df['product_id'].astype(str)

# Create user-item matrix
user_item_matrix = df.groupby(['user_id', 'product_id']).size().unstack(fill_value=0)

# Similarity matrix
item_similarity = cosine_similarity(user_item_matrix.T)
similarity_df = pd.DataFrame(item_similarity,
                             index=user_item_matrix.columns,
                             columns=user_item_matrix.columns)

# Dummy product info
product_info = {
    "P1": {"name": "Wireless Headphones", "image": "https://images.unsplash.com/photo-1580894732444-fd7d993b5ad7?auto=format&fit=crop&w=100&q=80"},
    "P2": {"name": "Smartphone X", "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=100&q=80"},
    "P3": {"name": "Laptop Pro", "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=100&q=80"},
    "P4": {"name": "Smart Watch", "image": "https://images.unsplash.com/photo-1516575529573-5fce6c5f2c01?auto=format&fit=crop&w=100&q=80"},
    "P5": {"name": "Gaming Mouse", "image": "https://images.unsplash.com/photo-1587202372775-c5f6f766abc6?auto=format&fit=crop&w=100&q=80"},
}

# Recommendation function
def recommend_products(product_id, num_recommendations=5):
    if product_id not in similarity_df.columns:
        return []
    similar_scores = similarity_df[product_id].sort_values(ascending=False)
    similar_scores = similar_scores.drop(product_id)
    return list(similar_scores.head(num_recommendations).items())
