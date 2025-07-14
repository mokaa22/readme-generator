from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputKeyToolsParser
from langchain_core.prompts import ChatPromptTemplate
from typing import TypedDict
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file!")

# Define TypedDict to describe expected JSON output structure
class Explanation(TypedDict):
    topic: str
    explanation: str

# Create Gemini model with JSON structured output
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key,
    convert_system_message_to_human=True,
    tools=[JsonOutputKeyToolsParser(key_name="response")]
)

# Create the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers in JSON format."),
    ("human", "Explain the topic '{topic}' in simple terms. Respond with a JSON containing 'topic' and 'explanation' keys.")
])

# Prepare input data
input_data = {"topic": "Photosynthesis"}

# Format the message with input
formatted_prompt = prompt.invoke(input_data)

# Call Gemini model
response = model.invoke(formatted_prompt)

# Convert response content to Python dict using eval (safe only for trusted outputs)
try:
    json_response: Explanation = eval(response.content)
    print("Topic:", json_response["topic"])
    print("Explanation:", json_response["explanation"])
except Exception as e:
    print("Failed to parse response as JSON:", e)
    print("Raw response:", response.content)
