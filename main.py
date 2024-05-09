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

createQuestions("""Background and Tensions: The Alamo, a mission-turned-fortress in San Antonio, Texas, was central to the Texas Revolution against Mexico. In the 1820s and 1830s, many American settlers moved to Mexican Texas, bringing cultural tensions between them and the Mexican government. The settlers sought more autonomy, culminating in the Texas Revolution in 1835.
Siege and Defense Preparations: In February 1836, Mexican General Antonio López de Santa Anna led a large army into Texas to crush the rebellion. Approximately 200 Texan defenders, including prominent figures like James Bowie, William B. Travis, and Davy Crockett, fortified the Alamo. They knew they were outnumbered, but they hoped reinforcements would arrive.
The 13-Day Siege: Santa Anna's forces laid siege to the Alamo for 13 days, bombarding it with artillery fire and cutting off supplies. Despite the overwhelming odds, the Texan defenders held their ground. Tensions escalated as Mexican troops prepared for a final assault.
The Final Assault and Fall of the Alamo: On March 6, 1836, in a pre-dawn attack, Santa Anna's army stormed the Alamo. The Texans fought fiercely but were overwhelmed. Almost all the defenders, including Bowie, Travis, and Crockett, were killed in the assault, with only a few non-combatants surviving.
Aftermath and Legacy: The fall of the Alamo became a rallying cry for Texan independence: "Remember the Alamo!" Just over a month later, Sam Houston led Texan forces to victory at the Battle of San Jacinto, securing Texas' independence from Mexico. The Alamo remains a symbol of courage, sacrifice, and the Texan spirit, honored in historical reenactments, museums, and cultural narratives.""")