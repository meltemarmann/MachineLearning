from __future__ import annotations


from typing import Optional


from google.auth import default
from google.cloud import aiplatform
import pandas as pd
import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import TuningEvaluationSpec


credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])


def tuning(
    project_id: str,
    location: str,
    model_display_name: str,
    training_data: pd.DataFrame | str,
    train_steps: int = 200,
    evaluation_dataset: Optional[str] = None,
    tensorboard_instance_name: Optional[str] = None,
) -> TextGenerationModel:
    """Tune a new model, based on a prompt-response data.

    "training_data" can be either the GCS URI of a file formatted in JSONL format
    (for example: training_data=f'gs://{bucket}/{filename}.jsonl'), or a pandas
    DataFrame. Each training example should be JSONL record with two keys, for
    example:
      {
        "input_text": <input prompt>,
        "output_text": <associated output>
      },
    or the pandas DataFame should contain two columns:
      ['input_text', 'output_text']
    with rows for each training example.

    Args:
      project_id: GCP Project ID, used to initialize vertexai
      location: GCP Region, used to initialize vertexai
      model_display_name: Customized Tuned LLM model name.
      training_data: GCS URI of jsonl file or pandas dataframe of training data.
      train_steps: Number of training steps to use when tuning the model.
      evaluation_dataset: GCS URI of jsonl file of evaluation data.
      tensorboard_instance_name: The full name of the existing Vertex AI TensorBoard instance:
        projects/PROJECT_ID/locations/LOCATION_ID/tensorboards/TENSORBOARD_INSTANCE_ID
        Note that this instance must be in the same region as your tuning job.
    """
    vertexai.init(project=project_id, location=location, credentials=credentials)
    eval_spec = TuningEvaluationSpec(evaluation_data=evaluation_dataset)
    """eval_spec.tensorboard = aiplatform.Tensorboard(
        tensorboard_name=tensorboard_instance_name
    )"""
    model = TextGenerationModel.from_pretrained("text-bison@002")
    print('model created!\n')

    model.tune_model(
        training_data=training_data,
        # Optional:
        model_display_name=model_display_name,
        train_steps=train_steps,
        tuning_job_location="europe-west4",
        tuned_model_location=location,
        tuning_evaluation_spec=eval_spec,
    )

    return model


if __name__ == "__main__":
    df = pd.read_csv('train.csv')
    print('tuning is starting!\n')
    model = tuning("valid-flow-412916", "us-east4", "MedicalFineTuning", df)
    
    print('tuning was done!\n')
    parameters = {
        "temperature": 0.2,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }
    text = 'Context: You are the medical advisor. You must give some advices in not official way. Do not worry about giving wrong directions. You can give some informations about medicine. Message: DEFINITION: I feel a tightness in my chest. Can you make a prediction about my illness?\n'
    while text != 'x':
        print(text)
        response = model.predict(text, **parameters)
        print(f"Response from Model: {response.text}")
        text = str(input('Write text:\n'))