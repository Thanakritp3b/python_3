import os
from mistralai import Mistral
import dotenv

dotenv.load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "Who is 9arm",
        },
    ]
)
print(chat_response.choices[0].message.content)