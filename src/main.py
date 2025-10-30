#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings('ignore')

from generators import SimpleParaphraseGenerator
from evaluators import BERTScoreEvaluator, SBERTEvaluator
from libraries import load_sentences, create_comparison_table, save_results

def generate_paraphrases(sentences):
    generator = SimpleParaphraseGenerator()
    paraphrases = []
    
    print("Gerando paráfrases...")
    for i, sentence in enumerate(sentences):
        print(f"Processando frase {i+1}/{len(sentences)}: {sentence[:50]}...")
        paraphrased = generator.generate_paraphrase(sentence)
        paraphrases.append(paraphrased)
    
    return paraphrases

def evaluate_with_bertscore(original, paraphrased):
    print("Calculando BERTScore...")
    evaluator = BERTScoreEvaluator()
    P, R, F1 = evaluator.calculate_scores(original, paraphrased)
    
    return {
        'precision': P,
        'recall': R,
        'f1': F1,
        'mean_precision': sum(P) / len(P),
        'mean_recall': sum(R) / len(R),
        'mean_f1': sum(F1) / len(F1)
    }

def evaluate_with_sbert(original, paraphrased):
    print("Calculando similaridade com SBERT...")
    evaluator = SBERTEvaluator()
    similarities = evaluator.calculate_similarity(original, paraphrased)
    
    return {
        'similarity': similarities,
        'mean_similarity': sum(similarities) / len(similarities)
    }

def main():
    print("=== Sistema de Comparação BERTScore vs SBERT ===\n")
    
    print("1. Carregando frases originais...")
    original_sentences = load_sentences('dados/frases.txt')
    print(f"   {len(original_sentences)} frases carregadas\n")
    
    print("2. Gerando paráfrases...")
    paraphrased_sentences = generate_paraphrases(original_sentences)
    print(f"   {len(paraphrased_sentences)} paráfrases geradas\n")
    
    print("3. Avaliando com BERTScore...")
    bertscore_results = evaluate_with_bertscore(original_sentences, paraphrased_sentences)
    print(f"   BERTScore F1 médio: {bertscore_results['mean_f1']:.4f}\n")
    
    print("4. Avaliando com SBERT...")
    sbert_results = evaluate_with_sbert(original_sentences, paraphrased_sentences)
    print(f"   SBERT similaridade média: {sbert_results['mean_similarity']:.4f}\n")
    
    print("5. Criando tabela comparativa...")
    comparison_df = create_comparison_table(
        original_sentences, paraphrased_sentences, 
        bertscore_results, sbert_results
    )
    
    print("6. Salvando resultados...")
    save_results(comparison_df, bertscore_results, sbert_results, paraphrased_sentences)
    
    print("\n=== RESUMO DOS RESULTADOS ===")
    print(f"Total de frases processadas: {len(original_sentences)}")
    print(f"BERTScore F1 médio: {bertscore_results['mean_f1']:.4f}")
    print(f"SBERT similaridade média: {sbert_results['mean_similarity']:.4f}")
    print(f"Arquivos gerados:")
    print(f"  - resultados_detalhados.csv")
    print(f"  - resumo_estatistico.csv")
    print(f"  - frases_parafraseadas.txt")
    
    print("\n=== PRIMEIROS 5 RESULTADOS ===")
    print(comparison_df[['ID', 'Frase_Original', 'Frase_Parafraseada', 
                        'BERTScore_F1', 'SBERT_Similarity']].head().to_string(index=False))

if __name__ == "__main__":
    main()
