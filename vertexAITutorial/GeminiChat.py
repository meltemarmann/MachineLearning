import google.generativeai as genai
import pandas as pd

def createData(examples:list):
    df_fine = pd.read_csv ("fineTune.csv")
    for index, row in df_fine.iterrows():
        if index > 35:
            break
        examples.append(tuple(row))
    

genai.configure(api_key='AIzaSyATK-TatU6Xs7Egg3jiE4xGYMXJ2I4Fd4s')

examples = []
createData(examples)

response = genai.chat(
    context="Be a motivational coach who's very inspiring",
    examples=examples,
    messages="I'm too tired to go the gym today")
print(response.last)