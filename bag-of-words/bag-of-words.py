import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    # Write code here
    n_vocab = len(vocab)
    n_tokens = len(tokens)
    
    bag_of_words_arr = np.zeros(n_vocab)

    vocab_dict = dict.fromkeys(vocab,0)

    for i in range(n_tokens):
        if tokens[i] in vocab_dict:
            vocab_dict[tokens[i]] += 1

    return np.asarray(list(vocab_dict.values()))