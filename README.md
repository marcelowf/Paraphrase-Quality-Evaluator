# BERTScore vs SBERT - Comparação de Paráfrases

Sistema que compara BERTScore e Sentence Transformers (SBERT) para avaliar paráfrases geradas automaticamente.

## 🚀 Como Usar

### 1. Configure tudo
```bash
startup.bat
```

### 2. Execute o projeto
```bash
# Experimento completo (51 frases)
run.bat
```

## 📁 Estrutura

```
PJBL_Processamento_de_Linguagem_Natural/
├── dados/                       # Dados de entrada e saída
│   ├── frases.txt              # Frases originais (52 frases)
│   └── frases_parafraseadas.txt # Paráfrases geradas
├── src/                        # Código fonte
│   └── bert_score_simple.py    # Script principal
├── resultados/                 # Resultados dos experimentos
│   ├── resultados_detalhados.csv
│   └── resumo_estatistico.csv
├── startup.bat                # ⭐ Configura tudo
├── run.bat                    # ⭐ Executa o projeto
└── requirements.txt           # Dependências
```

## 📊 O que o sistema faz

1. **Lê** 51 frases originais do arquivo `dados/frases.txt`
2. **Gera paráfrases** usando regras de substituição simples
3. **Calcula BERTScore** (Precision, Recall, F1) entre originais e parafraseadas
4. **Calcula similaridade SBERT** usando Sentence Transformers
5. **Gera tabelas comparativas** em CSV com os resultados

## 📈 Resultados Gerados

- **`resultados/resultados_detalhados.csv`** - Tabela com resultados para cada frase
- **`resultados/resumo_estatistico.csv`** - Estatísticas resumidas (média, desvio, min, max)
- **`dados/frases_parafraseadas.txt`** - Frases parafraseadas geradas

## 🔧 Solução de Problemas

### Python 3 não encontrado
1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente
3. **MARQUE "Add Python to PATH"** durante a instalação
4. Reinicie o PowerShell e execute `startup.bat` novamente

### Erro de dependências
Execute novamente:
```bash
startup.bat
```

## ⚡ Dicas

- **Primeira execução**: Pode demorar devido ao download dos modelos
- **Conexão com internet**: Necessária para downloads
- **Tempo**: Experimento completo leva 10-15 minutos

## 📋 Critérios de Avaliação

- ✅ Uso correto do BERTScore e SBERT
- ✅ Originalidade no processo de geração de paráfrases
- ✅ Complexidade da solução implementada
- ✅ Funcionamento correto de todas as funcionalidades