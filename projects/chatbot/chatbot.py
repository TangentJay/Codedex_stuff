from openai import OpenAI

client = OpenAI(api_key='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')

prompt = input('prompt: ')

response = client.responses.create(
    input=prompt,
    model='gpt-5'

)

print(response.output_text)