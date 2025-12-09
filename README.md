# 🌉 Monitoramento Inteligente de Pontes com IA  
Trabalho da disciplina **Engenharia de Prompt, Mentalidade de IA e Conhecimento Digital**.

Este repositório reúne **todo o conteúdo técnico** do projeto, incluindo:  
códigos de agentes, scripts auxiliares, dados de exemplo, workflows automatizados (GitHub Actions) e configuração MCP.

---

## 👤 Autor
**Paulo Yuri Pugliezi de Carvalho**  
**RA: 188140**

---

## 📘 Conteúdo do Repositório

### 📁 `agents/`
Scripts que simulam agentes inteligentes:

- **analise_estrutural.py** → lê dados de sensores e identifica possível anomalia.  
- **agente_bim.py** → simula a localização das anomalias no modelo BIM/IFC.  
- **relatorios.py** → gera relatório simples com os resultados.

---

### 📁 `scripts/`
Scripts auxiliares:

- **coletar_dados.py** → cria arquivo CSV com dados de sensores 
- **registrar_resultados.py** → registra resultados em arquivo JSON (log).

---

### 📁 `data/`
- **exemplo_sensores.csv** → base fictícia de dados de sensores.

---

### 📁 `mcp/`
- **agents.yaml** → configuração MCP dos agentes (fluxo e prompts).

---

### 📁 `.github/workflows/`
Workflows GitHub Actions de exemplo:

- **analise_diaria.yml**  
- **relatorio_semanal.yml**  
- **atualizar_bim.yml**

Esses workflows simulam automações

---

## 🎥 Vídeo da Apresentação
👉 **https://drive.google.com/file/d/1jok50Gz7t5PAqgJa_6p0kkG_JDoplJ-4/view?usp=drive_link**

---

## 📄 Documentos do Trabalho
Além do código, o repositório deve conter:

- **Documento Técnico (PDF)**  
- **Apresentação em Slides (PPTX)**

  ---

## 📚 Referências Bibliográficas

KUTZ, Myer. **Handbook of Structural Health Monitoring**. 2. ed. New York: Wiley, 2021.

LIU, A.; SMITH, J. **Prompt Engineering Foundations**. Cambridge: MIT Press, 2023.

MOURA, T.; SILVA, R. **Inteligência artificial aplicada à manutenção preditiva em infraestruturas urbanas**. *Revista Brasileira de Engenharia Civil*, São Paulo, v. 29, n. 2, p. 45-59, 2022.

NUSSBAUM, M.; HARRISON, K.; PETERSON, L. **Automação e reprodutibilidade em projetos de IA.** *Journal of Intelligent Systems Engineering*, Londres, v. 11, n. 3, p. 120-138, 2022.

RUSSELL, Stuart; NORVIG, Peter. **Artificial Intelligence: A Modern Approach**. 4. ed. New Jersey: Pearson, 2016.

SUN, L.; SHANG, Z.; XIA, Y.; BHOWMICK, S. Machine-learning-based structural anomaly detection for bridges. **Engineering Structures**, Amsterdam, v. 209, p. 110-118, 2020.

VOLK, R.; STENGEL, J.; SCHULTMANN, F. Building Information Modeling (BIM) for existing buildings. **Automation in Construction**, Amsterdã, v. 38, p. 109-127, 2014.

YE, X.; SU, Y.; HAN, J. **Structural health monitoring using smart sensors**. *Sensor*, Basel, v. 21, n. 4, p. 1-22, 2021.

