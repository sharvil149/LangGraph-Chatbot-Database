import streamlit as st
from langraph_backend import Chatbot
from langchain_core.messages import HumanMessage
import uuid


#****************************************Utility Function ***********************
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id


def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []


def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state["chat_threads"].append(thread_id)

def load_conversation(thread_id):
    state = Chatbot.get_state(config={'configurable':{'thread_id':thread_id}})
    
    if "messages" not in state.values:
        return []
        
    return state.values["messages"]

#****************************************************************************



if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])

#**************************************SlideBar UI****************************************
st.sidebar.text('Langrapph ChatBot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Converstaions')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] =  thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg,HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_messages.append({'role':role , 'content': msg.content})

        st.session_state['message_history'] = temp_messages

# ************************************************************************************
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.chat_input('Type here')
CONFIG = {'configurable':{'thread_id':st.session_state["thread_id"]}}
if user_input:

    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)


    #response = Chatbot.invoke({'messages':[HumanMessage(content = user_input)]},config = CONFIG)
    #ai_message = response['messages'][-1].content
    #st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
        #st.text(ai_message)
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in Chatbot.stream(
                {'messages':[HumanMessage(content=user_input)]},
                config = CONFIG,
                stream_mode = 'messages'
            )
        )
        st.session_state['message_history'].append({'role':'assistant','content':ai_message})