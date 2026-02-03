import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

load_dotenv()

MODEL_NAME = "models/gemma-3-4b-it"

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY is not set")

client = genai.Client(api_key=api_key)

try:
    start = time.time()
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents="Say hello in one sentence. Add an affirmation."
    )
    latency = time.time() - start
except ClientError:
    raise

if not response.text:
    raise RuntimeError("Empty response from model")

print(response.text)
