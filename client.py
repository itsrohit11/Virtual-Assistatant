from openai import OpenAI

client = OpenAI(
  api_key="sk-proj-0nmrpJYPzq7TyiQB3MvKT3BlbkFJyERh6l14Sh1bDX98fO5E",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant, skilled in general tasks like alexa and google cloud, give short responses please"},
    {"role": "user", "content": "what is programming."}
  ]
)

print(completion.choices[0].message.content)