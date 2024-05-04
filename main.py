from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.getenv('OPEN_AI_API_KEY'))

def createKeyPoints(prompt):
  response = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[{
         "role": 'system',
         "content": 'You are an ai assisant that makes a list of keypoints from a text that the user will give you. Make sure to format the keypoints like this: 1. Keypoint 1 2. Keypoint 2 and so on. Leave it all as plain text and dont include any bold or heading text'
      }, {
          "role": 'user',
          "content": prompt
      },],
      max_tokens=500,
  )
  print(response.choices[0].message.content)
  return response.choices[0].message.content


def createDefinitions(prompt):
  response = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[{
         "role": 'system',
         "content": 'You are an ai assisant that makes a list of vocab words and their definitions using the text the user will provide. Format it like this: 1. Vocab word - Definition 2. Vocab word - Definition and so on. Leave it all as plain text and dont include any bold or heading text'
      }, {
          "role": 'user',
          "content": prompt
      },],
      max_tokens=500,
  )
  print(response.choices[0].message.content)
  return response.choices[0].message.content