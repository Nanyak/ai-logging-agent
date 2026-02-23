import os 
from dotenv import load_dotenv
import google.generativeai as genai
 
# load environment variables 
load_dotenv()

# configure gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=api_key)

# create a model instance
model = genai.GenerativeModel("gemini-2.5-flash-lite")

#read log file
with open("logs/sample_app.log", "r") as file:
    logs = file.read()

prompt = f"""You are an expert Devops engineer analyzing application logs.

## Task:
Analyze the following logs and provide:
1. A summary of the issues found in the logs.
2. Possible causes for these issues.
3. Recommendations for resolving the issues.

## Context:
Logs: {logs}

Provide a clear, structured analysis based on the logs provided.
"""

print("Testing log analysis with AI...")
print("-" * 60)

response = model.generate_content(prompt)
print("AI Analysis:")
print(response.text)

print("-" * 60)
print("Setup completed successfully.")
