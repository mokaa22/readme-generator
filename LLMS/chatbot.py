from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file!")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

print("Welcome to Moksha's chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))

    try:
        response = model.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))
        print("Moksha's chatbot:", response.content)
    except Exception as e:
        print("Error:", e)
        print("You may have hit your quota or exceeded message limits.")

print(chat_history)
