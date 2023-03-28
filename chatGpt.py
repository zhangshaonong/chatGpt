import requests
import json

# Replace YOUR_API_KEY with your OpenAI API key
headers = {
  'Content-Type': 'application/json',
  "Authorization": "Bearer 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"
}

# Define the parameters for the request
params = {
  'model': 'text-davinci-003',
  # 'model': 'text-curie-001', # 動作テスト用（料金的に）
  'prompt': "写篇诗词描叙大雨",
  "max_tokens": 150, # 出力される文章量の最大値（トークン数） max:4096
  "temperature": 1, # 単語のランダム性 min:0.1 max:2.0
  "top_p": 1, # 単語のランダム性 min:-2.0 max:2.0
  "frequency_penalty": 0.0, # 単語の再利用 min:-2.0 max:2.0
  "presence_penalty": 0.6, # 単語の再利用 min:-2.0 max:2.0
  "stop": [" Human:", " AI:"] # 途中で生成を停止する単語
}

# Send the request to the OpenAI API
# Sresponse = requests.get("https://api.openai.com/v1/completions", headers=headers, params=params)
response = requests.post('https://api.openai.com/v1/completions', headers=headers, data=json.dumps(params))

# Print the response from the API

response_data = response.json()
print(response_data['choices'][0]['text'].strip())
