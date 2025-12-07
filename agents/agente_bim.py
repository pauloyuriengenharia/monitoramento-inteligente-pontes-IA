def localizar_no_ifc(sensor_id):
    """
    Exemplo ilustrativo que 'localiza' um sensor no modelo BIM.
    Retorna uma estrutura com coordenadas fictícias.
    """
    # Em projeto real, aqui seria feita integração com IFC/BIM.
    return {
        "sensor": sensor_id,
        "coordenadas": "(12.40, 5.20, 3.10)",
        "descricao": "Localização fictícia no modelo IFC (exemplo)"
    }

if __name__ == "__main__":
    exemplo = localizar_no_ifc("S1")
    print(exemplo)
