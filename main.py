
import openai

openai.api_key = 'YOUR_API_KEY'

response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt="Translate the following English text to French: 'Hello, how are you?'",
  max_tokens=50
)

print(response.choices[0].text.strip())



response = openai.Completion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]
)

print(response.choices[0].message['content'])