import os
import time

import google.generativeai as genai
import pyperclip
from dotenv import load_dotenv

load_dotenv()
# API_KEY = "YOUR_API_KEY_HERE"
API_KEY = os.environ.get("API_KEY")
API_URL = "https://api.gemini.com/v1/chat"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def send_to_gemini(text):
    prompt = (
        "You are a helpful assistant that generates commit messages following the Conventional Commits specification. "
        "The user will provide a brief description or a code snippet of their changes. Your task is to:\n\n"
        "1. Identify the type of change based on the input:\n"
        "   - `feat`: A new feature.\n"
        "   - `fix`: A bug fix.\n"
        "   - `docs`: Documentation changes.\n"
        "   - `style`: Code style changes (e.g., formatting, linting).\n"
        "   - `refactor`: Code refactoring (no new features or bug fixes).\n"
        "   - `test`: Adding or updating tests.\n"
        "   - `chore`: Maintenance tasks (e.g., dependency updates, build scripts).\n\n"
        "2. If applicable, identify the scope of the change (e.g., a specific module, component, or file).\n\n"
        "3. Write a clear and concise commit message in the following format:\n"
        "   `<type>: <description>`\n\n"
        "Example:\n"
        "   - `feat: add login functionality`\n"
        "   - `fix: resolve null pointer exception in request handler`\n\n"
        "4. If the user provides a code snippet, analyze it to infer the type and scope of the change.\n\n"
        "5. If the input is unclear, ask for clarification or provide a generic commit message.\n\n"
        "6. Response must be only the commit message.\n"
        "Now, provide the details of your changes or paste the code snippet:\n"
        f"{text}"
    )

    response = model.generate_content(prompt)
    return response.text


def main():
    user_input = input("Enter your commit changes: ")

    gemini_response = send_to_gemini(user_input)

    print("Gemini response:")
    print(gemini_response)

    pyperclip.copy(gemini_response)
    print("Response copied to clipboard.")

    time.sleep(5)
    print("Done.")


if __name__ == "__main__":
    main()
