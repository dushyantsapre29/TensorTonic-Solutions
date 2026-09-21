def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed-size token chunks with the requested overlap.
    """
    # Write code here
    
    chunks = []
    n_tokens = len(tokens)
    
    step_size = chunk_size - overlap

    chunk_start = 0
    chunk_end = chunk_start + chunk_size
    
    while chunk_end < n_tokens:
        chunks.append(tokens[chunk_start:chunk_end])
        chunk_start += step_size
        chunk_end += step_size

    if chunk_start < n_tokens:
        chunks.append(tokens[chunk_start:])

    return chunks