import pandas as pd
import os
from datetime import datetime

INPUT_PATH = "data/input.csv"
OUTPUT_PATH = "output/output.csv"
LOG_PATH = "logs/pipeline.log"

def log(message):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

try:
    log("Inicio del pipeline")

    df = pd.read_csv(INPUT_PATH)
    log(f"Datos leídos: {len(df)} registros")

    df = df[df["edad"] >= 18]
    log(f"Filtrado aplicado: {len(df)} registros válidos")

    os.makedirs("output", exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    log("Pipeline ejecutado correctamente")

except Exception as e:
    log(f"Error: {str(e)}")
    raise