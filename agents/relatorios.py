def gerar_relatorio(res):
    """
    Gera um relatório de texto simples com base no resultado de análise.
    'res' espera dicionário retornado por analisar_dados().
    """
    lines = []
    lines.append("Relatório Automático - Monitoramento de Ponte (Exemplo)\n")
    if "erro" in res:
        lines.append(f"Erro: {res['erro']}\n")
    else:
        lines.append(f"Anomalia detectada: {res.get('anomalia')}\n")
        lines.append(f"Criticidade: {res.get('criticidade')}\n")
        lines.append(f"Média das leituras: {res.get('media')}\n")
        lines.append(f"Detalhes: {res.get('detalhes')}\n")

    texto = "\n".join(lines)
    with open("relatorio_exemplo.txt", "w", encoding="utf-8") as f:
        f.write(texto)
    return "relatorio_exemplo.txt"

if __name__ == "__main__":
    # exemplo de uso
    resultado_exemplo = {"anomalia": True, "criticidade": "Alta", "media": 0.85, "detalhes": "Teste"}
    arquivo = gerar_relatorio(resultado_exemplo)
    print(f"Relatório salvo em: {arquivo}")
