
import streamlit as st
from recommender_engine import recommend_products, product_info

st.set_page_config(page_title="E-commerce Product Recommender", page_icon="🛍️", layout="wide")
st.title("🛍️ E-commerce Product Recommender")
st.markdown("#### Get smart product suggestions instantly")

# Input section
col1, col2 = st.columns([3, 1])
with col1:
    product_id = st.text_input("Enter Product ID:", placeholder="e.g., P1")
with col2:
    num_recommendations = st.number_input("No. of Recommendations", min_value=1, max_value=10, value=5)

# Button
if st.button("🔍 Recommend"):
    results = recommend_products(product_id, num_recommendations)
    if results:
        st.success(f"Top {len(results)} Recommendations for {product_id}")
        
        for i, (pid, score) in enumerate(results, start=1):
            name = product_info.get(pid, {}).get("name", "Unknown Product")
            image_url = product_info.get(pid, {}).get("image", "")

            with st.container():
                st.markdown(f"""
<div style="border:2px solid #e5e5e5; border-radius:10px; padding:15px; margin-bottom:20px; box-shadow:2px 2px 8px #ddd;">
    <h4 style="margin-bottom:10px;">{i}. {name} <span style='font-size:0.85em;'> (ID: {pid})</span></h4>
    <img src="{image_url}" width="300" style="border-radius:8px; margin-bottom:10px;" />
    <p><b>Similarity Score:</b> {round(score*100, 2)}%</p>
</div>
                """, unsafe_allow_html=True)
    else:
        st.warning("🚫 Product not found or not enough data!")
