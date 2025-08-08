set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Set brightness and color temp of light",
    "parameters":{
        "type":"object",
        "properties":{
            "brightness":{
                "type": "integer",
                "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
            },
            "color_temp":{
                "type": "string",
                "enum": ["daylight","cool","warm"],
                "description":"Color temp of light fixture",
            },
            },
            "required": ["brightness","color_temp"],
        },
    }
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set brightness and color temp of room light. (mock API).

    Args: 
        brightness: light_level 0 to 100, 0 is off, 100 is full.
        color_temp: Color temp of light fixture, can be daylight, cool, or warm.
        
    Returns:
        A dict containing the set brightness and color temp.
        """
    return {"brightness": brightness, "colorTemperature": color_temp}


from google import genai
from google.genai import types
client = genai.Client()
tools = types.Tool(function_declarations=[set_light_values_declaration])
config = types.GenerateContentConfig(tools=[tools])
import base64

contents = [
    types.Content(
        role="user", parts=[types.Part(text="Turn the lights to a level appropriate to a romantic meeting.")]
    )
]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=contents,
    config=config,
)

print(response.candidates[0].content.parts[0].function_call)

tool_call = response.candidates[0].content.parts[0].function_call
if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)
    print(f"Function execution result: {result}")

function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result},
)

contents.append(response.candidates[0].content)
contents.append(types.Content(role="user", parts=[function_response_part]))

final_response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=config,
    contents=contents
)

print(final_response.text)

