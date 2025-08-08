from google import genai
from google.genai import types

# Actual function implementations
def wear_a_suit(situation: bool) -> dict:
    """Decision engine of suit wearing
    Args:
        situation: The situation requiring (or not) a suit.)

    Returns:
        Boolean of yes/no.
    """
    return {"status": f"Suit required {'yes' if situation else 'no'}"}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[wear_a_suit]
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="I am going to a barbeque",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
