import random
import numpy as np

def genProbabilities(tokens):
  bgrams = {}
  
  for i in range(len(tokens)-2):
    token1 = tokens[i]
    token2 = tokens[i+1]
    tabelaToken1 = bgrams.get(token1, {})
    tabelaToken1[token2] = tabelaToken1.get(token2, 0) + 1
    bgrams[token1] = tabelaToken1
  
  for key in bgrams:
    bgrams[key] = dict(sorted(bgrams[key].items(), key=lambda item: -item[1]))
    total = sum(bgrams[key].values())
    bgrams[key] = dict([(k, bgrams[key][k]/total) for k in bgrams[key]])
  
  return bgrams

def predict(token, probablilities):
    if token in probablilities:
        return random.choices(list(probablilities[token].keys()), weights=probablilities[token].values())[0]
    return None
  
def calculatePerplexity(tokens, probablilities):
    n = len(tokens)
    log_prob_sum = 0

    for bigram in zip(tokens[:-1], tokens[1:]):
        prob = probablilities.get(bigram, 1e-6)

        log_prob_sum += np.log(prob)

    perplexity = np.exp(-log_prob_sum / n)
    return perplexity