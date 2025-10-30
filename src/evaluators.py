#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Tuple
from bert_score import score as bert_score
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class BERTScoreEvaluator:
    def __init__(self):
        pass
    
    def calculate_scores(self, references: List[str], candidates: List[str]) -> Tuple[List[float], List[float], List[float]]:
        P, R, F1 = bert_score(candidates, references, lang="pt", verbose=False)
        return P.tolist(), R.tolist(), F1.tolist()

class SBERTEvaluator:
    def __init__(self, model_name: str = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'):
        self.model = SentenceTransformer(model_name)
    
    def calculate_similarity(self, references: List[str], candidates: List[str]) -> List[float]:
        ref_embeddings = self.model.encode(references)
        cand_embeddings = self.model.encode(candidates)
        
        similarities = []
        for ref_emb, cand_emb in zip(ref_embeddings, cand_embeddings):
            sim = cosine_similarity([ref_emb], [cand_emb])[0][0]
            similarities.append(sim)
        
        return similarities
