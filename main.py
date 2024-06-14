from openai import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask

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
  text = response.choices[0].message.content
  lines = text.split('\n')

  # Create a list to store the values
  values = []

  # Process each line individually
  for line in lines:
    # Strip leading and trailing whitespace
    line = line.strip()

    # Find the first space after the number, marking the start of the value
    first_space_index = line.find(" ")
    if first_space_index == -1:
      # If no space is found, skip this line
      continue

    # Extract the value after the first space
    value = line[first_space_index + 1:].strip()

    # Add to the list
    values.append(value)
  
  print(values)
  return values



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
  text = response.choices[0].message.content
  word_def_dict = {}

    # Split the input text into lines
  lines = text.split('\n')

    # Process each line individually
  for line in lines:
    # Strip leading and trailing whitespace
    line = line.strip()

    # Find the first occurrence of " - " which separates word and definition
    split_index = line.find(" - ")
    if split_index == -1:
      # If no " - " is found, skip this line
      continue

    # Extract the word and definition
    word = line[line.find(" ") + 1:split_index].strip()
    definition = line[split_index + 3:].strip()

    # Add to the dictionary
    word_def_dict[word] = definition

  print(word_def_dict)
  return word_def_dict

def createQuestions(prompt):
  response = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[{
         "role": 'system',
         "content": """You are an ai assisant that makes a list of questions pertaining to the text the user gives you. Format them like this. 
         Q1: Question
         A: answer
         B: answer - correct
         C: answer
         D: answer
         Q2: Question
         and so on"""
      }, {
          "role": 'user',
          "content": prompt
      },],
      max_tokens=500,
  )
  print(response.choices[0].message.content)
  return(response.choices[0].message.content)


def createFlashcards(prompt):
  response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{
       "role": 'system',
       "content": """You are an ai assistant that makes different informational flashcards relating to the prompt the user has given. You will format the flashcards like this:
       Flashcard 1
       Front of card: Question about topic
       Back of card: Answer

       Flashcard 2
        Front of card: Question about topic
        Back of card: Answer

      Flashcard 3
       Front of card: Question about topic
       Back of card: Answer

      Flashcard 4
       Front of card: Question about topic
       Back of card: Answer

      Flashcard 5
       Front of card: Question about topic
       Back of card: Answer
       """    
      }, {
        "role": 'user',
        "content": prompt
      },],
      max_tokens=500,
)

  print(response.choices[0].message.content)
  return(response.choices[0].message.content)


@app.route('/definitions', methods = ['POST', 'GET'])
def Server_Def:
    transcript = request.form.get('transcript')
    return createDefinitions(transcript)

@app.route('/questions', methods = ['POST', 'GET'])
def Server_Def:
    transcript = request.form.get('transcript')
    return createQuestions(transcript)

@app.route('/keypoints', methods = ['POST', 'GET'])
def Server_Def:
    transcript = request.form.get('transcript')
    return createKeyPoints(transcript)

@app.route('/flashcards', methods = ['POST', 'GET'])
def Server_Def:
    transcript = request.form.get('transcript')
    return createFlashcards(transcript)

if __name__ = "__main__":
    app.run(debug=True, port=5000)