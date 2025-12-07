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

- **coletar_dados.py** → cria arquivo CSV com dados de sensores (exemplo).  
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

Esses workflows simulam automações (executados somente manualmente via *workflow_dispatch*).

---

## 🎥 Vídeo da Apresentação
👉 **https://drive.google.com/file/d/1jok50Gz7t5PAqgJa_6p0kkG_JDoplJ-4/view?usp=drive_link**

---

## 📄 Documentos do Trabalho
Além do código, o repositório deve conter:

- **Documento Técnico (PDF)**  
- **Apresentação em Slides (PPTX)**  
