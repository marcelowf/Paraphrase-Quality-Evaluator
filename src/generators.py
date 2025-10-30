#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re

class SimpleParaphraseGenerator:
    def __init__(self):
        self.substitutions = {
            'é': 'está sendo',
            'são': 'estão sendo',
            'foi': 'estava sendo',
            'foram': 'estavam sendo',
            'tem': 'possui',
            'têm': 'possuem',
            'faz': 'realiza',
            'fazem': 'realizam',
            'vai': 'irá',
            'vão': 'irão',
            'quer': 'deseja',
            'querem': 'desejam',
            'pode': 'consegue',
            'podem': 'conseguem',
            'deve': 'precisa',
            'devem': 'precisam',
            'bom': 'ótimo',
            'boa': 'ótima',
            'bons': 'ótimos',
            'boas': 'ótimas',
            'mau': 'ruim',
            'má': 'ruim',
            'maus': 'ruins',
            'más': 'ruins',
            'grande': 'enorme',
            'grandes': 'enormes',
            'pequeno': 'minúsculo',
            'pequenos': 'minúsculos',
            'pequena': 'minúscula',
            'pequenas': 'minúsculas',
            'novo': 'recente',
            'nova': 'recente',
            'novos': 'recentes',
            'novas': 'recentes',
            'velho': 'antigo',
            'velha': 'antiga',
            'velhos': 'antigos',
            'velhas': 'antigas',
            'muito': 'bastante',
            'muita': 'bastante',
            'muitos': 'bastante',
            'muitas': 'bastante',
            'pouco': 'escasso',
            'pouca': 'escassa',
            'poucos': 'escassos',
            'poucas': 'escassas',
            'sempre': 'constantemente',
            'nunca': 'jamais',
            'hoje': 'neste dia',
            'ontem': 'no dia anterior',
            'amanhã': 'no próximo dia',
            'e': 'além disso',
            'mas': 'porém',
            'porque': 'devido ao fato de que',
            'quando': 'no momento em que',
            'onde': 'no local em que',
            'como': 'da forma que',
            'em': 'dentro de',
            'para': 'com o objetivo de',
            'com': 'junto a',
            'sem': 'na ausência de',
            'sobre': 'acima de',
            'sob': 'abaixo de',
            'ele': 'o indivíduo',
            'ela': 'a pessoa',
            'eles': 'os indivíduos',
            'elas': 'as pessoas',
            'nós': 'nossa equipe',
            'você': 'o senhor/a senhora',
            'vocês': 'os senhores/as senhoras',
        }
    
    def generate_paraphrase(self, text: str) -> str:
        paraphrased = text
        
        for original, replacement in self.substitutions.items():
            pattern = r'\b' + re.escape(original) + r'\b'
            paraphrased = re.sub(pattern, replacement, paraphrased, flags=re.IGNORECASE)
        
        paraphrased = self._apply_structural_changes(paraphrased)
        return paraphrased
    
    def _apply_structural_changes(self, text: str) -> str:
        if text.endswith('.') and len(text.split()) <= 8:
            if random.random() < 0.3:
                words = text[:-1].split()
                if len(words) >= 3:
                    if words[-1] in ['cidade', 'casa', 'carro', 'pessoa', 'coisa', 'lugar', 'tempo', 'dia', 'noite']:
                        words = [words[-1]] + words[:-1]
                        text = ' '.join(words) + '.'
        
        if random.random() < 0.2:
            if text.startswith('O ') or text.startswith('A '):
                text = 'Além disso, ' + text.lower()
            elif text.startswith('Ele ') or text.startswith('Ela '):
                text = 'Por outro lado, ' + text.lower()
        
        return text
