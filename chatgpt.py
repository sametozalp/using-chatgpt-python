import openai

openai.api_key = ""

model_engine = "gpt-3.5-turbo"
prompt = "naber lan"

completion = openai.completions.create(
    model= model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

response = completion.choices[0].text
print(response)