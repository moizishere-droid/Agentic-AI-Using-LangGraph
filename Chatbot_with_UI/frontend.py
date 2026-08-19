import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage

if "messgaes_history" not in st.session_state:
    st.session_state["messgaes_history"] = []


for messages in st.session_state["messgaes_history"]:
    with st.chat_message(messages["role"]):
        st.text(messages["content"])

user_input = st.chat_input("Type here...",)

if user_input:
    st.session_state["messgaes_history"].append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.text(user_input)
        
    config = {"configurable":{"thread_id":"1"}}
    response = chatbot.invoke({"messages":[HumanMessage(content=user_input)]},config=config)
    ai_messages = response["messages"][-1].content
    st.session_state["messgaes_history"].append({"role":"assistant","content":ai_messages})
    with st.chat_message("assistant"):
        st.text(ai_messages)
    