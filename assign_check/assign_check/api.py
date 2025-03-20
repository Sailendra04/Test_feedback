from openai import OpenAI
import os

def feedback(text):
    prompt = f"Grade(out of 100) this student's assignment and provide constructive feedback:\n\n{text}\n\nFeedback:"


    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = os.getenv("API_KEY"),
    print(api_key)
    )

    completion = client.chat.completions.create(
    # model="open-r1/olympiccoder-7b:free",
    model="mistralai/mistral-small-3.1-24b-instruct:free",
    messages=[{"role": "user","content": prompt}]
    )
    
    return completion.choices[0].message.content

    