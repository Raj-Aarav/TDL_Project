import os
import groq  # Install using `pip install groq`
from dotenv import load_dotenv

load_dotenv()
class ContextExpander:
    def __init__(self):
        """ Initialize the Groq LLM client """
        self.client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

    def expand_caption(self, caption):
        """ Expand the given caption using an LLM """
        prompt = f"Imagine you are a tour guide, give me 2-3 lines brief about the context or the tourist place present in the image caption which is provided :\n\n{caption}"

        try:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",  # Groq's Llama 3 model
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Error in expanding caption: {e}")
            return caption  