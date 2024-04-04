import google.generativeai as genai
import random
import pandas as pd
df = pd.read_csv('fineTune.csv')
base_model = [
    m for m in genai.list_models()
    if "createTunedModel" in m.supported_generation_methods][0]
#base_model

name = f'generate-num-{random.randint(0,10000)}'
operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
    source_model=base_model.name,
    training_data=df,
    id = name,
    epoch_count = 5,
    batch_size=10,
    learning_rate=0.5,
)
print('tunedModels/{name}')
import time

for status in operation.wait_bar():
    print(operation.metadata)
    time.sleep(30)
model = genai.GenerativeModel(f'tunedModels/{name}')
result = model.generate_content('I have headache. What should I do?\n')

print(result.text)