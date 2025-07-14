from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file!")
class PromptInput(TypedDict):
    domain: str
    topic: str
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain in simple terms, what is {topic}?')
])

prompt_data: PromptInput = {
    "domain": "science",
    "topic": "black holes"
}

prompt = chat_template.invoke(prompt_data)

response = model.invoke(prompt)
print("Gemini Response:", response.content)
