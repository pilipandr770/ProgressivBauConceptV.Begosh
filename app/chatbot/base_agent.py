import openai
from ..config import Config

class BaseAgent:
    def __init__(self, direction):
        self.direction = direction
        # OpenAI 0.28.x uses api_key directly, not client
        if Config.OPENAI_API_KEY:
            openai.api_key = Config.OPENAI_API_KEY

    def respond(self, message):
        # Basic fallback
        if 'termin' in message.lower() or 'buchen' in message.lower():
            return "Bitte buchen Sie einen Termin über unsere Website."
        elif 'kontakt' in message.lower() or 'rückruf' in message.lower():
            return "Bitte kontaktieren Sie uns über das Kontaktformular."
        else:
            # Use OpenAI for response
            if openai.api_key:
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": f"Du bist ein hilfreicher Assistent für {self.direction} bei ProgressivBauConcept in Frankfurt am Main. Antworte professionell und hilfreich. Wenn es um Themen außerhalb von {self.direction} geht, leite zum Projekt-Agenten weiter."},
                            {"role": "user", "content": message}
                        ],
                        max_tokens=150
                    )
                    return response.choices[0].message.content.strip()
                except Exception as e:
                    return f"Ich bin der {self.direction}-Agent. Wie kann ich Ihnen helfen? (Fehler: {str(e)})"
            else:
                return f"Ich bin der {self.direction}-Agent. Wie kann ich Ihnen helfen?"

    def is_relevant(self, message):
        # Check if message is relevant to this direction
        # For now, simple check
        return self.direction.lower() in message.lower()