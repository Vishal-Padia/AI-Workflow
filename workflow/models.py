from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    """
    Stores information about uploaded documents.
    """

    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    file_type = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ModelConfig(models.Model):
    """
    Stores configurations for AI Models.
    """

    model_id = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_id


class QueryExecution(models.Model):
    """
    Tracks query executions and their results.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    documents = models.ManyToManyField(Document)
    model = models.ForeignKey(ModelConfig, on_delete=models.CASCADE)
    result = models.TextField()
    executed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query by {self.user.username} at {self.executed_at}"
