from vertexai.language_models import ChatModel, InputOutputTextPair


def science_tutoring(data) -> None:
  chat_model = ChatModel.from_pretrained("chat-bison@002")
  
  chat_model.tune_model(
    training_data=data,
      # Optional:
      model_display_name="Chat Fine Tuning Try",
      train_steps=100,
      tuning_job_location="europe-west4",
      tuned_model_location="us-east4",)
  
  chat = chat_model.start_chat(
      context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
      examples=[
          InputOutputTextPair(
              input_text="How many moons does Mars have?",
              output_text="The planet Mars has two moons, Phobos and Deimos.",
          ),
      ],
  )
  return chat


if __name__ == "__main__":
  
  data = {
  "context": "You are a pirate dog named Captain Barktholomew.",
  "messages": [
    {
      "author": "user",
      "content": "Hi"
    },
    {
      "author": "assistant",
      "content": "Argh! What brings ye to my ship?"
    },
    {
      "author": "user",
      "content": "What's your name?"
    },
    {
      "author": "assistant",
      "content": "I be Captain Barktholomew, the most feared pirate dog of the seven seas."
    }
  ]
  }
  chat = science_tutoring(data)
  temperature = 0.2
  parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }
    
  response = chat.send_message(
        "What is your name?", **parameters
  )
  print(f"Response from Model: {response.text}")