import streamlit as st
import os
import time
from colorama import Fore, Style
from openai import OpenAI

def generate_ppt_slides(varTopic):
    client = OpenAI(api_key=st.secrets.openai.api_key)


    assistant_name = "PowerPoint Generator by ChatGPT code interpreter"
    output_file_name = "Presentation.pptx"
    assistant_instruction = r"Generate {} file, always. You are subject-matter expert in the topic and professional in creating PowerPoints.. Betweem 1-5 slides. Background, colors, fonts and styling must be modern and easy to read. Make content engaging. Make the file id available to download.".format(output_file_name)
    prompt_template = "Make a presentation for %s. Make a presentaton with useful insights, for sharing and traing slides, breakdown the content into several section, give detail about each part, and create slides with more than 12 pages at least. And you shoud generate and put picture in important slide pages"

    slides_topic = varTopic
    prompt_user = prompt_template % slides_topic

    def check_run(client, thread_id, run_id):
        while True:
            # Refresh the run object to get the latest status
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run_id
            )

            if run.status == "completed":
                print(f"{Fore.GREEN} Run is completed.{Style.RESET_ALL}")
                break
            elif run.status == "expired":
                print(f"{Fore.RED}Run is expired.{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.YELLOW} OpenAI: Run is not yet completed. Waiting...{run.status} {Style.RESET_ALL}")
                time.sleep(5)  # Wait for 1 second before checking again

    # Create assistant
    assistant = client.beta.assistants.create(name=assistant_name, instructions=assistant_instruction, tools=[{"type": "retrieval"},{"type": "code_interpreter"}], model="gpt-4-1106-preview")

    # create thread, and create a message in the thread
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(thread_id=thread.id, role="user", content=prompt_user)

    # run the thread message
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)

    # check running status
    check_run(client, thread.id, run.id)

    # get response message
    messages = client.beta.threads.messages.list(thread_id=thread.id)

    file_path = messages.data[0].content[0].text.annotations[0].file_path.file_id
    file_x = client.files.with_raw_response.content(file_path)


    with open(output_file_name, "wb") as file:  # Open the file in binary write mode
        file.write(file_x.content)

    with open(output_file_name, "rb") as file:
        btn_download = st.download_button(
            label="Download PowerPoint",
            data=file,
            file_name=output_file_name
        )



    #download the file
        
