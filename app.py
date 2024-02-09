from dotenv import load_dotenv
load_dotenv()   # load  all the environment variables from the .env

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

## function to load Gemini Pro Vision Model
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        ## Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

        return image_parts
    else:
        raise FileNotFoundError("No file uploaded to upload")
    

## Tomorrow here will initialize our streamlit app
st.set_page_config(page_title="Invoice Extracter")
st.header("Gemini Muntilanguage Invoice Extracter")
input = st.text_input("Ask the question...")
uploaded_file = st.file_uploader("Choose an invoice image...", type=["png","jpg","jpeg"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)

submit = st.button("Tell me abount the invoice")

input_prompt = """
You are an expert in understanding invoices. We will uplaod an image as invoice and you will have to answer any questions based on the uploaded invoice image
"""

## if submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input, image_data, input_prompt)
    # response.resolve()
    # print(response.candidates[0].content.parts)
    st.subheader("The Response is")
    # print(len(response))
    st.write(response.text)