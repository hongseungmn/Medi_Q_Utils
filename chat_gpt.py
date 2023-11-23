from openai import OpenAI

client = OpenAI(
  api_key='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'
)

content = ' 예) 함수명 : round(값,반올림할 위치),파라미터 : 첫 번째 파라미터(필수) : 숫자 또는 숫자 표현식, 두 번째 파라미터(선택) : 반올림할 소수점의 위치, 리턴값: int or float, 사용 예제:'

completion = client.chat.completions.create(
  model = "gpt-3.5-turbo-1106",
  messages=[
    {"role":"system","content":"very experienced teacher"},
    {"role":"user","content":"Beginner studying Python,"+content+"이 예를 보고 sklearn.model_selection.train_test_split도 같은 형식으로 설명해줘"},
    
  ]
)

print(completion.choices[0].message.content)