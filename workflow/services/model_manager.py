from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import HfApi


class ModelManager:
    """
    Manages AI model loading and inference
    """

    def __init__(self):
        self.loaded_models = {}
        self.api = HfApi()

    def load_model(self, model_id):
        """
        Loads a model from huggingface hub
        """
        if model_id in self.loaded_models:
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModelForCausalLM.from_pretrained(model_id)
            self.loaded_models[model_id] = {"model": model, "tokenizer": tokenizer}
        return self.loaded_models[model_id]

    def generate_response(self, model_id, query, context):
        """
        Generates response using the specified model
        """
        model_info = self.load_model(model_id)
        model = model_info["model"]
        tokenizer = model_info["tokenizer"]

        # Combine query and context
        input_text = f"Context: {context} \nQuery: {query}"

        # Generate response
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=256)
        response = tokenizer.decode(outputs[0])

        return response
