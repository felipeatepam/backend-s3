import os
import boto3
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Configuración actualizada para la estructura de carpetas
S3_BUCKET = "kuberocketci-applications-data"
# El "Key" en S3 incluye el nombre de la carpeta
S3_FILE_KEY = "cmtr-0oqfemca/data.txt"

s3_client = boto3.client('s3')

@app.get("/")
def read_root():
    try:
        # Fetch del objeto con el prefijo de la carpeta
        response = s3_client.get_object(Bucket=S3_BUCKET, Key=S3_FILE_KEY)
        content = response['Body'].read().decode('utf-8').strip()

        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
