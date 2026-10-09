import streamlit as st
from agent_doc import DocumentAgent

st.title("📄 Document-Aware Support Assistant")

agent = DocumentAgent("data/laundry_business.pdf")

user_query = st.text_input("Ask me about the document:")

if user_query:
    response = agent.answer(user_query)
    st.write(response)
