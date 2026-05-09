from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
# Access the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")