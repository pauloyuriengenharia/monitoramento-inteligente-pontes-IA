import json
import os

def registrar(resultado, path="resultados_log.json"):
    """
    Anexa o resultado (dicionário) a um arquivo JSON (lista).
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    # ler arquivo existente
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(resultado)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path

if __name__ == "__main__":
    exemplo = {"anomalia": False, "criticidade": "Baixa"}
    arquivo = registrar(exemplo)
    print(f"Resultado registrado em: {arquivo}")
