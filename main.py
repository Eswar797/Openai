import openai

openai.api_key = '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'


a=input("Give input")


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": a},
    ]
)

print(response.choices[0].message['content'])
