import magic
import pandas as pd

from PyPDF2 import PdfFileReader
from django.core.files.storage import default_storage


class DocumentProcessor:
    """
    Handles the documents processing for different file types.
    """

    @staticmethod
    def process_document(document):
        """
        Process the uploaded document based on its type.
        """
        file_path = default_storage.path(document.file.name)
        file_type = magic.from_file(file_path, mime=True)

        if "pdf" in file_type:
            return DocumentProcessor._process_pdf(file_path)
        elif "csv" in file_type:
            return DocumentProcessor._process_csv(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    @staticmethod
    def _process_pdf(file_path):
        """
        Extract the text from the PDF file.
        """
        reader = PdfFileReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    @staticmethod
    def _process_csv(file_path):
        """
        Read the CSV file and return the data as a DataFrame.
        """
        df = pd.read_csv(file_path)
        return df.to_dict()
