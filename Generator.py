
import random

def build_markov_chain(text, n=1):
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)
    
    return markov_chain

def generate_text(chain, n=1, length=50):
    start = random.choice(list(chain.keys()))
    result = list(start)
    
    for _ in range(length - n):
        state = tuple(result[-n:])
        next_words = chain.get(state)
        if not next_words:
            break
        result.append(random.choice(next_words))
    
    return ' '.join(result)

# Load input text
with open("sample.txt", "r") as file:
    input_text = file.read()

chain = build_markov_chain(input_text, n=1)
generated_text = generate_text(chain, n=1, length=50)

print("Generated Text:\n", generated_text)
