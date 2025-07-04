import streamlit as st
import os
import openai
from agents.buffett_agent import run_buffett_agent
from agents.sentiment_agent import run_sentiment_agent
from agents.valuation_agent import run_valuation_agent

# Load OpenAI key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="SimuVest AI", layout="centered")
st.title("📊 SimuVest AI — Ask Legendary Investors")

user_prompt = st.text_input("💬 Ask a stock market question:")
run_button = st.button("Run Analysis")

if run_button and user_prompt:
    st.subheader("🧠 Buffett Agent")
    with st.spinner("Thinking like Warren Buffett..."):
        buffett_response = run_buffett_agent(user_prompt)
        st.markdown(buffett_response)

    st.subheader("📈 Valuation Agent")
    with st.spinner("Calculating intrinsic value..."):
        valuation = run_valuation_agent(user_prompt)
        st.markdown(valuation)

    st.subheader("📰 Sentiment Agent")
    with st.spinner("Reading market sentiment..."):
        sentiment = run_sentiment_agent(user_prompt)
        st.markdown(sentiment)
