from rest_framework import serializers
from .models import Document, ModelConfig, QueryExecution


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["id", "name", "file", "file_type", "uploaded_at"]


class ModelConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelConfig
        fields = ["id", "model_id", "description", "is_active"]


class QueryExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryExecution
        fields = ["id", "query", "documents", "model", "result", "executed_at"]
