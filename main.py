import streamlit as st
from agents.customer_agent import customer_agent
from agents.product_agent import get_categories
from agents.recommender_agent import recommender_agent
from agents.coordinator_agent import init_db, get_log

# Initialize database
init_db()

# --- Streamlit App ---
st.title("ShopGenie 🛒")
st.subheader("AI-Powered Personalized Shopping")

user_id = st.text_input("Enter User ID:")
category = st.selectbox("Browse Category:", get_categories())

if st.button("Browse"):
    customer_agent(user_id, category)
    st.success(f"Browsing {category} logged for {user_id}.")

    st.subheader("🔍 Recommended for you:")
    recs = recommender_agent(category)
    for item in recs:
        st.markdown(f"- {item}")

st.markdown("---")
if st.checkbox("Show database log"):
    st.write(get_log())
