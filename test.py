from openai import OpenAi
client = OpenAi()

response = client.chat.completions.create(
    model = "gpt-3.5-turbo-0125",
    response_format = {"type": "json_object"},
    messages = [
        {"role": "system", "content": "You are a helpful assistent disigned to output JSON."},
        {"role": "user", "content": "Who won the world cup in 2018?"}
    ]
)

print(response.choices[0].message.content)