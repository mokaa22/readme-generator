import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

project_info = {
    "title": "GitHub README Generator",
    "description": "Automatically generates README files using Gemini and LangChain.",
    "installation": "pip install -r requirements.txt",
    "usage": "python main.py",
    "features": "- Gemini-powered README generation\n- LangChain integration\n- Environment variables support",
    "license": "MIT"
}

prompt_template = ChatPromptTemplate.from_template("""
You are a helpful assistant that writes professional GitHub README.md files.

Use the following project info to create a complete README in markdown format:

Project Title: {title}
Description: {description}
Installation: {installation}
Usage: {usage}
Features: {features}
License: {license}

Return only the markdown content.
""")

chain = prompt_template | llm
response = chain.invoke(project_info)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(response.content)

print("✅ README.md generated successfully using Gemini!")
