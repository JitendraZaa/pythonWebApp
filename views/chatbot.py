'''
Copyright  2024 IBM, Author - Jitendra Zaa

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

        https://wwww.jitendraZaa.com

@date          October 2024
@author        Jitendra Zaa
@email         jitendra.zaa@ibm.com | jitendra.zaa+30@gmail.com
@description   TBD
'''
import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Check out my fun YouTube channel 'Jitendra Zaa': https://www.youtube.com/@JitendraZaaInd",
            "Hi! What's up? Don't forget to subscribe to 'Jitendra Zaa': https://www.youtube.com/@JitendraZaaInd",
            "Hello! Need assistance? My YouTube channel 'Jitendra Zaa' is full of great tips: https://www.youtube.com/@JitendraZaaInd",
            "Hey! Got a question? Also, subscribe to 'Jitendra Zaa' for awesome tutorials: https://www.youtube.com/@JitendraZaaInd",
            "Hi there! How can I help? BTW, my channel 'Jitendra Zaa' is super cool: https://www.youtube.com/@JitendraZaaInd",
            "Hello! Looking for help? Check out 'Jitendra Zaa' on YouTube: https://www.youtube.com/@JitendraZaaInd",
            "Hey! Need assistance? 'Jitendra Zaa' YouTube channel has you covered: https://www.youtube.com/@JitendraZaaInd",
            "Hi! Got any coding questions? Don't forget to watch 'Jitendra Zaa': https://www.youtube.com/@JitendraZaaInd",
            "Hello! Need help? 'Jitendra Zaa' on YouTube is a must-see: https://www.youtube.com/@JitendraZaaInd",
            "Hey there! Any questions? My channel 'Jitendra Zaa' rocks: https://www.youtube.com/@JitendraZaaInd",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})