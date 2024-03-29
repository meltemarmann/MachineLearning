import pandas as pd

df = pd.read_csv('mtsamples.csv')

count=0
MAXCOUNT = 300

dict = {'input_text': [],
        'output_text': []}
for index, row in df.iterrows():
    print(index, end='\n\n')
    dict['input_text'].append("DESCRIPTION:" + str(row.loc['description']) + 
                            #"SAMPLE_NAME:" + str(row.loc['sample_name']) +
                            #"TRANSCRIPTION:" + str(row.loc['transcription']) + 
                            "KEYWORDS:" + str(row.loc['keywords']))
    dict['output_text'].append("MEDICAL_SPECIALITY:" + str(row.loc['medical_specialty']))
    
    print(type(row))
    print()
    if count==MAXCOUNT:
        break
    count+=1
csvDf = pd.DataFrame(dict)
csvDf.to_csv('decsription_to_medical_speciality.csv', index=False)

"""
['input_text', 'output_text']
input_text:
-DESCRIBTION- j.loc['description'] -SAMPLE_NAME- j.loc['sample_name'] 
-TRANSCRIPTION- j.loc['transcription'] -KEYWORDS- j.loc['keywords']

output_text:
j.loc['medical_specialty']


{'input_text':input_text
'output_text': output_text}"""