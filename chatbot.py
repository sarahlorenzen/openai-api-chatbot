# Import Libraries
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI()

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
        "role": "user",
        "content": " "
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

response = client.responses.create(
  model="gpt-4o-mini",
  instructions=instructions,
  input = input_messages,
  store=False,
  text_format="markdown",
  max_tokens=50)

print(response.output_text)
