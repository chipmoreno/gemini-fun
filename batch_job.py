from google import genai
from google.genai import types
client = genai.Client()

inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'Tell me a one-sentence joke. '}],
            'role':'user'
        }]
    },
        {
            'contents':[{
                'parts':[{'text':'Why is the sky blue?'}],
                'role':'user'
            }]
        }
]

inline_batch_job = client.batches.create(
    model="models/gemini-2.0-flash-lite",
    src=inline_requests,
    config={
        'display_name':"inlined-requests-job-1",
    },
)
print(f"Created batch job: {inline_batch_job.name}")
      