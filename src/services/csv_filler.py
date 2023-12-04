from src.schemas.analysis_output import AnalysisOutput
from src.schemas.execution import Execution
from src.schemas.score_output import ScoreOutput
import csv
import time
from fastapi import UploadFile
from src.config import get_settings
import os

SETTINGS = get_settings()

class CSVFillerService:
    def add_csv_prediction_sentiment_analysis(self,score_output:ScoreOutput, execution:Execution, fromGPT:bool = None, analysis_output:AnalysisOutput = None) -> None:

        text = execution.original_text
        modelName = SETTINGS.models_names[1]
        apiRevision = SETTINGS.revision
        date_and_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        executionTime = execution.time_in_seconds
        text_chars_length = len(execution.original_text)
        prediction = score_output.label
        score = score_output.score
        embeddings = None
        ner = None
        pos = None
        
        if analysis_output is not None and fromGPT is not None:
            if fromGPT:
                modelName = SETTINGS.models_names[2] + " - " + SETTINGS.models_names[3]
            else:
                modelName = SETTINGS.models_names[0]    
            analysis_output = analysis_output.model_dump()
            embeddings = analysis_output['embeddings']
            pos = analysis_output['part_of_speech_tagging']
            ner = analysis_output['named_entity_recognition']

        
        csv_file_path = SETTINGS.csv_path
        if not os.path.exists(csv_file_path.split("/")[0]):
            os.makedirs(csv_file_path.split("/")[0])
        is_new_file = not os.path.exists(csv_file_path)
        with open(csv_file_path, "a", newline='') as f:
            writer = csv.writer(f)
            if is_new_file:
                header = ["Texto", "Número de carácteres en el texto", "Predicción", "Puntaje","Fecha y Hora", "Tiempo de ejecución", "Modelo", "Versión de la API", "Embeddings", "NER", "POS"]
                writer.writerow(header)
            row=[text,text_chars_length,prediction,score,date_and_time,executionTime,modelName,apiRevision, embeddings, ner, pos]
            writer.writerow(row)