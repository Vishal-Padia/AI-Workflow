from .document_processor import DocumentProcessor
from .model_manager import ModelManager


class QueryProcessor:
    """
    Coordinates document processing and model inference
    """

    def __init__(self):
        self.model_manager = ModelManager()

    def process_query(self, query, documents, model_id):
        """
        Processes a query using the specified model and documents.
        """

        # process all documents and combine their content
        document_content = []
        for document in documents:
            document_content.append(DocumentProcessor().process_document(document))

        # combine documents content into a single context
        context = "\n".join(str(content) for content in document_content)

        # generate response using the model
        response = self.model_manager.generate_response(model_id, context, query)

        return response
