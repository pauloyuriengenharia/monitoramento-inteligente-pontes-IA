import pandas as pd
import os

def criar_exemplo_csv(path="data/exemplo_sensores.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame({
        "sensor_id": ["S1","S1","S2","S2","S3"],
        "valor": [0.5, 0.6, 0.9, 0.85, 0.4]
    })
    df.to_csv(path, index=False)
    return path

if __name__ == "__main__":
    arquivo = criar_exemplo_csv()
    print(f"Arquivo de exemplo criado em: {arquivo}")
