import openai
# simport yaml

# set the API Key 
# yaml_file = open('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', 'r')  
# p = yaml.load(yaml_file, Loader=yaml.FullLoader)
# openai.api_key = p['api_key']
openai.api_key = 'sk-XXXXXXXX'

# show available models
modellist = openai.Model.list()
for i in modellist.data:
    print(i.id)


def send_openai_request(engine, prompt, max_tokens=1024):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response

# Define the prompt
prompt = "次の平均を求める、70g　68g　72g　74g"
model="text-davinci-003"

# Generate a response
response = send_openai_request(model, prompt)

# Print the response
print(response["choices"][0]["text"])
