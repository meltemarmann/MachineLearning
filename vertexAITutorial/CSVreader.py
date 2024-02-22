import pandas as pd

df = pd.read_csv('mtsamples.csv')

a=0
dict = {'input_text': [],
        'output_text': []}
for index, row in df.iterrows():
    print(index, end='\n\n')
    dict['input_text'].append("DESCRIPTION:" + str(row.loc['description']) + 
                              "MEDICAL_SPECIALITY:" + str(row.loc['medical_specialty']) +
                            "TRANSCRIPTION:" + str(row.loc['transcription']) + 
                            "KEYWORDS:" + str(row.loc['keywords']))
    dict['output_text'].append("SAMPLE_NAME:" + str(row.loc['sample_name']))
    
    print(type(row))
    print()
    if a==300:
        break
    a+=1
csvDf = pd.DataFrame(dict)
csvDf.to_csv('train.csv', index=False)

"""
['input_text', 'output_text']
input_text:
-DESCRIBTION- j.loc['description'] -SAMPLE_NAME- j.loc['sample_name'] 
-TRANSCRIPTION- j.loc['transcription'] -KEYWORDS- j.loc['keywords']

output_text:
j.loc['medical_specialty']


{'input_text':input_text
'output_text': output_text}"""