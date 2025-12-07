import pandas as pd

def analisar_dados(csv_path="data/exemplo_sensores.csv"):
    """
    Leitura simples do CSV de exemplo e verificação básica.
    Retorna um dicionário com resultado ilustrativo.
    """
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        return {"erro": "arquivo não encontrado"}

    # coluna 'valor' contém leituras normalizadas (0..1) no exemplo
    media = df["valor"].mean()

    if media > 0.8:
        resultado = {
            "anomalia": True,
            "criticidade": "Alta",
            "media": float(media),
            "detalhes": "Média das leituras acima do limite exemplificativo."
        }
    elif media > 0.6:
        resultado = {
            "anomalia": True,
            "criticidade": "Moderada",
            "media": float(media),
            "detalhes": "Média das leituras em nível moderado."
        }
    else:
        resultado = {
            "anomalia": False,
            "criticidade": "Baixa",
            "media": float(media),
            "detalhes": "Comportamento dentro da normalidade do exemplo."
        }
    return resultado

if __name__ == "__main__":
    res = analisar_dados()
    print(res)
