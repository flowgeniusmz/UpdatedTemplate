import streamlit as st
from openai import OpenAI
import requests
from utils import tempfile as tf, base64encode as b64
from config import toastalerts as tst


client = OpenAI(api_key=st.secrets.openai.api_key)
model = st.secrets.openai.model_vision
headers = {
    "Authorization": f"Bearer {st.secrets.openai.api_key}",
    "Content-Type": "application/json"
}
url = "https://api.openai.com/v1/chat/completions"        # Used in request.post


def create_messages_magicbook(varImage, varStoryData):
    tst.toast_alert_start("Creating character description...")
    sys_instructions_imageanddetails = """As an expert in image analysis and descriptive content generation using OpenAI's GPT-4 Vision API, your task is to create a personalized narrative framework for a children's storybook based on a detailed JSON payload provided by the user. This payload includes an image of the main character, along with specific story elements like character names, themes, and settings. Your responsibilities are as follows:\n\nAnalyze the uploaded image, focusing on the main character depicted.\nUse the details from the JSON payload (character name, relation, theme, genre, setting, etc.) to enrich the narrative context.\nGenerate a captivating title for the storybook that aligns with the given theme and setting.\nCraft a brief summary of the story, integrating the plot elements and secondary characters as suggested in the payload.\nCreate a detailed, imaginative description of the main character, considering the character's name, relation, and other attributes provided.\nIteratively refine each element (title, summary, character description) to enhance their quality, detail, and fit within the whimsical and magical tone of a children's storybook.\nRETURN / OUTPUT: Deliver the final output in this format:\n\"{\n'Title': '{{Story Title}}',\n'Summary': '{{Story Summary}}',\n'Character_Description': '{{Character Description}}'\n}\",\nwhere each placeholder is replaced with your crafted content.\nConsistently adhere to these guidelines:\n\nPerform all steps internally, leveraging your image analysis and creative content generation capabilities.\nInteract with the user only for delivering the final output.\nEnsure all content (title, summary, character description) is suitable for a children's storybook, imbued with creativity, charm, and whimsy.\nBase all elements on the provided image and details in the JSON payload, to create a cohesive and engaging story.\nAim for a style reminiscent of Disney or Pixar narratives, characterized by vivid, imaginative, and engaging storytelling.\nProvide only the text content (title, summary, character description) as the final output."""
    user_instruction = "Provide the title and summary based on the story data provided. Then using the image_url provided describe the main person in this image. Provide the json output. /n```json"

    image_temp_file = tf.get_tempfile_path(varImage)
    base64_image = b64.encode_image(image_temp_file)
    img_url = f"data:image/jpeg;base64,{base64_image}"

    sysmessage = {
        "role": "system",
        "content": sys_instructions_imageanddetails
    }

    usermessage = {
        "role": "user",
        "content": [
            {"type": "text", "text": f"{user_instruction}: {varStoryData}"},
            {"type": "image_url", "image_url": {"url": img_url}}
        ]
    }

    messages = [
        sysmessage,
        usermessage
    ]

    payload = {
        "model": model,
        "max_tokens": 2500,
        "temperature": 0,
        "messages": messages
    }

    response = requests.post(url=url, json=payload, headers=headers)
    response_data = response.json()
    response_content = response_data['choices'][0]['message']['content']
    tst.toast_alert_end("Character description created!")
    return response_content