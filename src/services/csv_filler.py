from src.schemas.sentiment_model_output import SentimentModelOutput
import csv
import time
from fastapi import UploadFile
from src.config import get_settings
import os

SETTINGS = get_settings()

class CSVFillerService:
    def add_csv_prediction_sentiment_analysis(self,modelOutput:SentimentModelOutput) -> None:
        text = modelOutput.execution.original_text
        modelName = SETTINGS.models_names[1]
        apiRevision = SETTINGS.revision
        date_and_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        executionTime = modelOutput.execution.time_in_seconds
        text_chars_length = len(modelOutput.execution.original_text)
        prediction = modelOutput.score_output.label
        score = modelOutput.score_output.score
        
        csv_file_path = SETTINGS.csv_path
        if not os.path.exists(csv_file_path.split("/")[0]):
            os.makedirs(csv_file_path.split("/")[0])
        is_new_file = not os.path.exists(csv_file_path)
        with open(csv_file_path, "a", newline='') as f:
            writer = csv.writer(f)
            if is_new_file:
                header = ["Texto", "Número de carácteres en el texto", "Predicción", "Puntaje","Fecha y Hora", "Tiempo de ejecución", "Modelo", "Versión de la API"]
                writer.writerow(header)
            row=[text,text_chars_length,prediction,score,date_and_time,executionTime,modelName,apiRevision]
            writer.writerow(row)