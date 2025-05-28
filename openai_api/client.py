from openai import OpenAI

model_ai:str = 'gpt-3.5-turbo'
client = OpenAI(
   api_key='API_KEY'
)

def get_car_ai_bio(model,brand,year):
   message:str = '''
   Me mostre uma descrição de venda para o carro {} {} {} em no máximo 250 caracteres.
   Fale coisas especificas desse modelo de carro.
   '''
   message= message.format(brand,model,year)
   response = client.chat.completions.create(
      messages=[
         {
            'role':'user',
            'content':message
         }
      ],
      max_tokens=250,
      model=model_ai
   )
   return response.choices[0].message.content