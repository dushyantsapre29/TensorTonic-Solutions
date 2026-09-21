def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    modified_tokens = tokens.copy()
    
    i=0
    while i<len(modified_tokens):
        if modified_tokens[i] in stopwords:
            modified_tokens.pop(i)
            continue
        i += 1

    return modified_tokens