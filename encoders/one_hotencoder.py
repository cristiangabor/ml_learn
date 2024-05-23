from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Column(BaseModel):
    column: int

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values


@app.post("/onehotencode/")
async def encode(column: Column):
    # Transform the input text
    oHe = OneHotEncoder()
    ct = ColumnTransformer(transformers=[('encoder', oHe, [column.column])], remainder='passthrough')
    
    new_X  = np.array(ct.fit_transform(X))

    new_x = new_X.tolist()

    # Return the prediction
    return {"onehotencodeing": json.dumps(new_x), 'initial_data': json.dumps(X.tolist())}