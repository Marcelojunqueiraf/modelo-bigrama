

def getMostFrequentTokenPair(tokens: list[int]) -> tuple[int, int]:
    frequency = {}
    for i in range(len(tokens)-1):
        frequency[(tokens[i], tokens[i+1])] = frequency.get((tokens[i], tokens[i+1]), 0) + 1
    return max(frequency, key=frequency.get)

def merge(tokens, mostFrequent, newTokenCode):
    newIds = []
    i = 0

    while True:
        if(i >= len(tokens)-1):
            if(i == len(tokens)-1):
                newIds.append(tokens[i])
            break
        if (tokens[i], tokens[i+1]) == mostFrequent:
            newIds.append(newTokenCode)
            i += 2
        else:
            newIds.append(tokens[i])
            i += 1
    return newIds


def BPE(tokens, num_merges):
    newTokens = list(tokens)

    vocab = {idx: bytes([idx]) for idx in range(256)}
    merges = {}
    
    for i in range(num_merges):
        mostFrequent = getMostFrequentTokenPair(newTokens)
        newTokens = merge(newTokens, mostFrequent, 256+i)
        vocab[256+i] = vocab[mostFrequent[0]] + vocab[mostFrequent[1]]
        merges[mostFrequent] = 256+i
        print(f"merge n {i}")

    return newTokens, vocab, merges

def decode(ids, vocab):
    tokens = b"".join(vocab[id] for id in ids)
    return tokens.decode('utf-8', errors='replace')

def encode(ids, merges):
    tokens = list(ids.encode("utf-8"))

    for pair in merges:
        tokens = merge(tokens, pair, merges[pair])
    
    return tokens