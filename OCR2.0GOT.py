import gradio as gr
import os
import uuid
import shutil
import re
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, low_cpu_mem_usage=True, device_map='cpu', use_safetensors=True)
model = model.eval()

UPLOAD_FOLDER = "./uploads"
RESULTS_FOLDER = "./results"

for folder in [UPLOAD_FOLDER, RESULTS_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)


def run_GOT(image, search_term):
    unique_id = str(uuid.uuid4())
    image_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}.png")
    
  
    shutil.copy(image, image_path)
    
    try:
        
        res = model.chat(tokenizer, image_path, ocr_type='ocr')
        
        highlighted_text = highlight_text(res, search_term)
        
        return highlighted_text, None
    except Exception as e:
        return f"Error: {str(e)}", None
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)


def highlight_text(text, search_term):
    if not search_term:
        return text
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return pattern.sub(lambda m: f'<span style="background-color: yellow;">{m.group()}</span>', text)

title_html = """
<h2> <span class="gradient-text" id="text">General OCR Theory (GOT)</span>: Multi-Language OCR HINDI AND ENGLISH</h2>
"""

with gr.Blocks() as demo:
    gr.HTML(title_html)
    gr.Markdown("""
    ### Instructions
    Upload your respective image below and click "Submit" to extract text in both English and Hindi. If you want you can select the word to be highlighted.
    """)

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="filepath", label="Upload your image")
            search_input = gr.Textbox(label="Enter a word to search", placeholder="Search term")
            submit_button = gr.Button("Submit")
        
        with gr.Column():
            ocr_result = gr.HTML(label="Extracted Text:")

    
    submit_button.click(run_GOT, inputs=[image_input, search_input], outputs=[ocr_result])

if __name__ == "__main__":
    demo.launch()