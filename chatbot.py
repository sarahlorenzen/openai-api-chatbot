# Import Libraries
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

#Huggingface provided GPT4 OpenAI API Key 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# Load instructions from a file
with open("prompt.txt", "r", encoding="utf-8") as f:
    instructions = f.read()

input_messages = [
    {
        "role": "developer",
        "content": "The 4 product types are: Stickers, Ornaments, Magnet Individual, and Magnet Sets. " \
        "The GPT will ask for the product type first, then the name of the new product, and finally generate a description based on the product type."
    },
    {
        "role": "assistant",
        "content": "What is the product type?"
    },
    {
        "role": "assistant",
        "content": "What is the name of the new product?"
    },
    {
        "role": "user",
        "content": ""
    }
]

def generate_response(input_messages):
    response = client.responses.create(
        model = "gpt-4o-mini",
        instructions = instructions,
        input = input_messages,
        store = False
    )
    return response.output_text

# Create Gradio interface
demo = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(placeholder="Enter your prompt here...", label="Prompt", lines=10),
    outputs=gr.Textbox(label="Product Description", lines=10),
    title="Product Description Generator"
)

if __name__ == "__main__":
    demo.launch(share=True)
