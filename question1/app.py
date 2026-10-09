import streamlit as st
from agent import InventoryAgent

st.title("📊 Inventory Chat Agent")

agent = InventoryAgent("data/Inventory-Records-Sample-Data.xlsx")

user_query = st.text_input("Ask me about the inventory:")

if user_query:
    response = agent.answer(user_query)
    st.write(response)

