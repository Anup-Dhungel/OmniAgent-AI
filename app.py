import streamlit as st
from dotenv import load_dotenv
from agent import setup_agent

# 1. Setup Streamlit page
st.set_page_config(page_title="OmniAgent AI", page_icon="🤖", layout="centered")
st.title("🤖 OmniAgent AI")
st.markdown("An autonomous AI agent with Web Search, Code Execution, and File I/O.")

# 2. Load Environment Variables
# We only load it once to avoid repeated disk reads
if "env_loaded" not in st.session_state:
    load_dotenv()
    st.session_state.env_loaded = True

# 3. Initialize Agent
# We store the agent in session_state so it's not re-created on every keystroke/message
if "agent_executor" not in st.session_state:
    try:
        st.session_state.agent_executor = setup_agent()
    except ValueError as e:
        st.error(f"Configuration Error: {e}")
        st.warning("Please ensure your API keys (GROQ_API_KEY, TAVILY_API_KEY) are set in your .env file.")
        st.stop()

# 4. Manage Chat History & Thread ID
if "messages" not in st.session_state:
    st.session_state.messages = []

# We use a fixed thread_id for this user session to maintain memory in LangGraph
if "thread_id" not in st.session_state:
    # A simple way to generate a unique thread per browser session
    import uuid
    st.session_state.thread_id = str(uuid.uuid4())

# Configuration for LangGraph checkpointer
config = {"configurable": {"thread_id": st.session_state.thread_id}}

# 5. Display existing chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. Handle New User Input
if prompt := st.chat_input("What would you like me to do?"):
    # Add user message to chat history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        # We use a placeholder to update the text as it streams, or just show a spinner
        message_placeholder = st.empty()
        
        try:
            with st.spinner("Thinking..."):
                # Stream the events from the agent
                events = st.session_state.agent_executor.stream(
                    {"messages": [("user", prompt)]},
                    config=config,
                    stream_mode="values"
                )

                final_response = ""
                for event in events:
                    if "messages" in event:
                        latest_message = event["messages"][-1]
                        # Only show AI responses in the UI
                        if latest_message.type == "ai" and latest_message.content:
                            final_response = latest_message.content
                            message_placeholder.markdown(final_response)
                
                # If there's no textual content, it might just be a tool call.
                if not final_response:
                    final_response = "I performed an action using my tools."
                    message_placeholder.markdown(final_response)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": final_response})
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
