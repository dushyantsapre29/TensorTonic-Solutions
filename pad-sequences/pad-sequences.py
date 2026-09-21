import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    
    N = len(seqs)
    if N == 0:
        return np.empty((0,0), dtype=int)
    len_seqs = [len(seq) for seq in seqs]

    if max_len is None:
        max_len = max(len_seqs)

    seqs_arr = np.zeros((N, max_len), dtype=int) + pad_value

    for i in range(N):
        for j in range(min(len_seqs[i], max_len)):
            seqs_arr[i][j] = seqs[i][j]

    return seqs_arr