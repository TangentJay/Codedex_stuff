from openai import OpenAI

client = OpenAI()

prompt = input('prompt: ')

response = client.responses.create(
    input=prompt,
    model='gpt-5'

)

print(response.output_text)