from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

class VertexLLM:
    def __init__(self, model_name="gemini-1.5-pro"):
        self.model = GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text