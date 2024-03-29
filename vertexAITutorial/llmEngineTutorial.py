from llmengine import Completion

response = Completion.create(
    model="llama-2-7b",
    prompt="I'm opening a pancake restaurant that specializes in unique pancake shapes, colors, and flavors. List 3 quirky names I could name my restaurant.",
    max_new_tokens=100,
    temperature=0.2,
)

print(response.output.text)
