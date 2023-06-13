import streamlit as st
import openai

#API_KEY = "chatgpt API KEY"
openai.api_key =  API_KEY

#functon that connect chatgpt and get responce from it 
def get_responce_from_chatgpt(text):
    prompt = f"Identify and return the sentimental either positive or negative in given text. text: {text}"
    responce=openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{"role":"system","content":"You are a helpful sentiment analyzer that returns consise sentiment"},{"role":"user","content":prompt}
        ],
        temperature=0.1
    )
    sentiment = responce['choices'][0]['message']['content']
    return sentiment


#result = get_responce_from_chatgpt("i am happy")
# print(result)


#strealit web icon and name of header
st.set_page_config(
        page_title="SENTIMENTAL ANALYZER",
        page_icon="icon.png"
    )


# we are using streamlit for gui to interact with user in better way 
st.title("SENTIMENTAL ANALYZER USING CHATGPT")
model = 'gpt-3.5-turbo'
text = st.text_input("Enter Text:", value ="I love technology")

if st.button('Submit'):
    #we create a spinner that continues runs and get responce
    with st.spinner('OpenAI processing in Progress'):
        sentiment = get_responce_from_chatgpt(text)
        st.success("Processing complete")

    st.header(f"{sentiment}")
st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            color: #6c757d;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            CREATED BY MAQSOOD HUSSAIN WANI
        </div>
        """,True
    
    )
