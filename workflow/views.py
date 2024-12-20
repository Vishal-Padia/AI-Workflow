from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Document, ModelConfig, QueryExecution
from .serializers import (
    DocumentSerializer,
    ModelConfigSerializer,
    QueryExecutionSerializer,
)
from .services.query_processor import QueryProcessor
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny


class CanvasView(TemplateView):
    template_name = "workflow/canvas.html"
    permission_classes = [AllowAny]


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ModelConfigViewSet(viewsets.ModelViewSet):
    queryset = ModelConfig.objects.all()
    serializer_class = ModelConfigSerializer


class QueryExecutionViewSet(viewsets.ModelViewSet):
    queryset = QueryExecution.objects.all()
    serializer_class = QueryExecutionSerializer

    @action(detail=False, methods=["post"])
    def execute(self, request):
        """
        Executes a query using the specified documents and model
        """
        query = request.data.get("query")
        document_ids = request.data.get("document_ids", [])
        model_id = request.data.get("model_id")

        # Validate inputs
        if not all([query, document_ids, model_id]):
            return Response(
                {"error": "Missing required parameters"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Get documents
            documents = Document.objects.filter(id__in=document_ids)
            model_config = ModelConfig.objects.get(id=model_id)

            # Process query
            processor = QueryProcessor()
            result = processor.process_query(query, documents, model_config.model_id)

            # Save execution
            execution = QueryExecution.objects.create(
                user=request.user, query=query, model=model_config, result=result
            )
            execution.documents.set(documents)

            return Response({"result": result, "execution_id": execution.id})

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
