# OCR-2.0-GOT-MODEL

PROJECT DESCRIPTION: 

This project is a web application that performs Optical Character Recognition (OCR) For the uploaded images. It supports English and Hindi language. And a Keyword search is available and the word is highlighted. 

SOFTWARE REQUIREMENTS:

Python: The program requires Python to run, ideally Python 3.8 or later.

Libraries to be installed:

pip install gradio

pip install transformers

pip install torch

pip install safetensors

pip install pillow

pip install verovio 

pip install tiktoken

installation of nvidia driver is must 

MODEL INFO:

This application leverages the CPU version of the GOT (General OCR Theory) model for Optical Character Recognition (OCR). The model and tokenizer are sourced from the Hugging Face model hub:

Model: ucaslcl/GOT-OCR2_0
Tokenizer: ucaslcl/GOT-OCR2_0
While the code includes provisions for running the model on a GPU, this implementation exclusively uses the CPU version due to the constraints of the Hugging Face deployment environment. As a result, processing times may be slower compared to a GPU-enabled setup. However, using the CPU ensures compatibility across a broader range of systems, particularly those without access to a GPU

USEAGE:

1.Set the code in the Google colab and download the prerequisites libraries and run the code. 
Then upload the image and type the search keyword and output is visible. (most preferable)


2.Clone the GitHub repository 







