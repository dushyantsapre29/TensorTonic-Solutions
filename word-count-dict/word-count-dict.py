def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    count_dict = dict()

    flat_tokens = [item for sublist in sentences for item in sublist]

    for i in range(len(flat_tokens)):
        if flat_tokens[i] in count_dict: 
            count_dict[flat_tokens[i]] += 1
        else:
            count_dict[flat_tokens[i]] = 1

    return count_dict