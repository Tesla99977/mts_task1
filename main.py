from io import StringIO

import pandas as pd
from fastapi import FastAPI, UploadFile, File
from sqlalchemy import create_engine

app = FastAPI()

DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/task' ### ввести URL на db в облаке
engine = create_engine(DATABASE_URL)

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    # Чтение содержимого файла в DataFrame
    contents = await file.read()
    df = pd.read_csv(pd.io.common.BytesIO(contents))
    df.to_sql('your_table_name', con=engine, if_exists='replace', index=False)  # Замените на свое имя таблицы
    return {"message": "Data uploaded successfully"}
