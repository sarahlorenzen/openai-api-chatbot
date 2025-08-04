# Import Libraries
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

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
        "content": " "
    }
]

def ask_ai(input_messages):
    response = client.responses.create(
        model = "gpt-4o-mini",
        instructions = instructions,
        input = input_messages,
        store = False
    )
    return response.output_text

demo = gr.Interface(
    fn=ask_ai,
    inputs="text",
    outputs="text",
    #type="messages",
    title="Product Description Generator"
)

if __name__ == "__main__":
    demo.launch(share=True)