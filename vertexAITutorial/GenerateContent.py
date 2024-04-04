import google.generativeai as genai

model = genai.GenerativeModel(f'tunedModels/{name}')
result = model.generate_content('I have headache. What should I do?\n')

print(result.text)