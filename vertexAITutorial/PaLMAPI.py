import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.language_models import ChatModel, InputOutputTextPair


def interview(
    temperature: float,
    project_id: str,
    location: str,
) -> str:
    """Ideation example with a Large Language Model"""

    vertexai.init(project=project_id, location=location)
    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        "Give me ten interview questions for the role of program manager.",
        **parameters,
    )
    print(f"Response from Model: {response.text}")

    return response.text


def science_tutoring(temperature: float = 0.2) -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    chat = chat_model.start_chat(
        context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
        examples=[
            InputOutputTextPair(
                input_text="How many moons does Mars have?",
                output_text="The planet Mars has two moons, Phobos and Deimos.",
            ),
        ],
    )

    response = chat.send_message(
        "How many planets are there in the solar system?", **parameters
    )
    print(f"Response from Model: {response.text}")

    return response

if __name__ == "__main__":
    interview( 0.8, "valid-flow-412916", "us-east4")
    print("\n\nscience tutoring:\n\n", science_tutoring().text)
    input()
    print("\n\nscience tutoring:\n\n", science_tutoring().text)