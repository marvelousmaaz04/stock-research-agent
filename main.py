# main.py
import streamlit as st
import uuid
from agent import stock_research_agent


st.set_page_config(page_title="🤖 Stock Research Agent", page_icon="📈")

# --- 1. Cleaned Header ---
# Replaced the multiple HTML markdowns with cleaner, native components
st.title("🤖 Stock Research Agent")
st.caption("Ask me to research a company (e.g., 'research jio' or 'AAPL')")

# --- 2. Initialize Session State ---
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 4. Handle New User Input ---
if prompt := st.chat_input("Research AAPL or ask about Jio..."):
    
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- 5. Get and Stream Agent Response ---
    with st.chat_message("assistant"):
        
        # --- CRITICAL FIXES HERE ---
        def stream_agent_response(user_prompt, session_id):
            # Use .stream() for conversational streaming
            stream = stock_research_agent.stream(user_prompt, session_id=session_id)
            
            # Filter for 'text' chunks. This prevents printing
            # 'None' from tool calls and other event data.
            for chunk in stream:
                if chunk.type == "text":
                    yield chunk.content
        
        # `st.write_stream` displays the text chunks as they arrive
        response = st.write_stream(stream_agent_response(prompt, st.session_state.session_id))

    # Add the full agent response to history
    st.session_state.messages.append({"role": "assistant", "content": response})