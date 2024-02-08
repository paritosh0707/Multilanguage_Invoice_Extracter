from dotenv import load_dotenv
load_dotenv()   # load  all the environment variables from the .env

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

## function to load Gemini Pro Vision Model
model = genai.GenerateModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

