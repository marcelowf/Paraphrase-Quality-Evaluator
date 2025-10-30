#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
import pandas as pd
import numpy as np
import os

def load_sentences(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as f:
        sentences = [line.strip() for line in f if line.strip()]
    return sentences

def create_comparison_table(original: List[str], paraphrased: List[str], 
                          bertscore_results: dict, sbert_results: dict) -> pd.DataFrame:
    data = []
    for i, (orig, para) in enumerate(zip(original, paraphrased)):
        data.append({
            'ID': i + 1,
            'Frase_Original': orig,
            'Frase_Parafraseada': para,
            'BERTScore_Precision': bertscore_results['precision'][i],
            'BERTScore_Recall': bertscore_results['recall'][i],
            'BERTScore_F1': bertscore_results['f1'][i],
            'SBERT_Similarity': sbert_results['similarity'][i]
        })
    
    return pd.DataFrame(data)

def save_results(df: pd.DataFrame, bertscore_results: dict, sbert_results: dict, paraphrased_sentences: List[str]):
    os.makedirs('resultados', exist_ok=True)
    os.makedirs('dados', exist_ok=True)
    
    df.to_csv('resultados/resultados_detalhados.csv', index=False, encoding='utf-8')
    print("Resultados detalhados salvos em 'resultados/resultados_detalhados.csv'")
    
    summary = {
        'Métrica': ['BERTScore Precision', 'BERTScore Recall', 'BERTScore F1', 'SBERT Similarity'],
        'Média': [
            bertscore_results['mean_precision'],
            bertscore_results['mean_recall'],
            bertscore_results['mean_f1'],
            sbert_results['mean_similarity']
        ],
        'Desvio_Padrão': [
            np.std(bertscore_results['precision']),
            np.std(bertscore_results['recall']),
            np.std(bertscore_results['f1']),
            np.std(sbert_results['similarity'])
        ],
        'Mínimo': [
            np.min(bertscore_results['precision']),
            np.min(bertscore_results['recall']),
            np.min(bertscore_results['f1']),
            np.min(sbert_results['similarity'])
        ],
        'Máximo': [
            np.max(bertscore_results['precision']),
            np.max(bertscore_results['recall']),
            np.max(bertscore_results['f1']),
            np.max(sbert_results['similarity'])
        ]
    }
    
    summary_df = pd.DataFrame(summary)
    summary_df.to_csv('resultados/resumo_estatistico.csv', index=False, encoding='utf-8')
    print("Resumo estatístico salvo em 'resultados/resumo_estatistico.csv'")
    
    with open('dados/frases_parafraseadas.txt', 'w', encoding='utf-8') as f:
        for para in paraphrased_sentences:
            f.write(para + '\n')
    print("Frases parafraseadas salvas em 'dados/frases_parafraseadas.txt'")
