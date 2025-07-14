import google.generativeai as genai

# Replace with your real API key
genai.configure(api_key="AIzaSyALNSClL80WbOIatUJ4KEHXWW4AftNNWSg")

# List available models
for model in genai.list_models():
    print(model.name, "supports generateContent:", "generateContent" in model.supported_generation_methods)
