import openai
import streamlit as st

# Set up the OpenAI API key
openai.api_key = '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'


# Sidebar for API key status
with st.sidebar:
    st.title('🤖💬 Prof Omkar on Demand;)')
    st.success('API key is configured!', icon='✅')

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handling new user inputs
if prompt := st.chat_input("What is up?"):
    # Save the user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Placeholder for the assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Replace 'your-assistant-id' with the actual ID of your assistant
        assistant_id = 'asst_iU3CyOXPe2CvT0epNFyp0f2f'
        
        # Make an API call to the assistant
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            full_response = response['choices'][0]['message']['content']
        except Exception as e:
            full_response = f"An error occurred: {str(e)}"
        
        # Display the assistant's final response
        message_placeholder.markdown(full_response)
    
    # Save the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": full_response})
