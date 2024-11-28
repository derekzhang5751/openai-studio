import base64
import json

import gradio as gr

from myopenai import chat_with_gpt_get_info


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def upload_image_to_chat(image_path):
    if image_path is None:
        return json.dumps({"error": "No image uploaded"}, indent=2)

    try:
        base64_image = encode_image(image_path)
    except Exception as e:
        return json.dumps({"error": f"Failed to encode image: {str(e)}"}, indent=2)

    try:
        response = chat_with_gpt_get_info(f"data:image/jpeg;base64,{base64_image}")
        json_response = json.loads(response)
        return json.dumps(json_response, indent=2)
    except json.JSONDecodeError:
        return json.dumps({"error": "Failed to parse JSON response", "raw_response": response}, indent=2)
    except Exception as e:
        return json.dumps({"error": f"An error occurred: {str(e)}"}, indent=2)


with gr.Blocks() as image_reader_block:
    # Choose annotation file
    with gr.Row():
        # Image Picker
        with gr.Column(scale=1, min_width=300):
            target_image = gr.Image(type="filepath", label="Upload an ID Image")

        # file list
        with gr.Column(scale=1, min_width=300):
            json_show = gr.JSON(label="Image Content")

    target_image.upload(upload_image_to_chat, inputs=[target_image], outputs=[json_show])
    pass

image_reader_page = image_reader_block
