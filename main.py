# main.py
import streamlit as st
import uuid
from agent import stock_research_agent
from agno.utils.pprint import pprint_run_response

st.set_page_config(page_title="🤖 Stock Research Agent", page_icon="📈")
st.markdown('<h1 style="text-align:center">🤖 Stock Research Agent</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color: #6c757d;">Ask me to research a company (e.g., "research jio" or "AAPL")</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; margin-top:0.25rem">Tip: Try a ticker like <strong>AAPL</strong> or a query like <strong>research jio</strong>.</p>', unsafe_allow_html=True)

# --- 1. Initialize Session State ---

if "session_id" not in st.session_state:
    # Create a unique ID for this user's session
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    # Store the chat history
    st.session_state.messages = []

# --- 2. Display Chat History ---
# Loop through all stored messages and display them
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 3. Handle New User Input ---
if prompt := st.chat_input("What company do you want to research?"):
    
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- 4. Get and Stream Agent Response ---
    with st.chat_message("assistant"):
        
        def stream_agent_response(user_prompt, session_id):
            # Pass the session_id to Agno.
            # Agno's db will automatically save/load history for this ID.
            stream = stock_research_agent.run(user_prompt, session_id=session_id, stream=True)
            # pprint_run_response(stream, markdown=True)
            for chunk in stream:
                yield chunk.content
        
        # `st.write_stream` displays the text chunks as they arrive
        response = st.write_stream(stream_agent_response(prompt, st.session_state.session_id))

    # Add the full agent response to history
    st.session_state.messages.append({"role": "assistant", "content": response})