"""
string_util.py
A sample repository for MolSSI Workshop at UF

Misc. string processing functions
"""

def title_case(sentence):
    """
    Convert a string to title case

    Parameters
    ----------
    sentence : string
        String to be converted to title case

    Returns
    -------
    title_case: string
        String converted to title case --> version 1
    ret : string
        String converted to title case --> version 2

    Example
    -------
    >>> title_case('ThIs iS a StrInG to BE ConVerTed.')
        'This Is A String To Be Converted.'
    """
    # Check that input is of type 'string'
    if not isinstance(sentence, str):
        raise TypeError('Invalid input %s - Input must be of type string' %(sentence))
    # Error if empty string
    if len(sentence) == 0:
        raise ValueError('Cannot apply title function to be empty string.')

    split_sentence = sentence.split()
    title_case = ''
    for i in split_sentence:
        i = i.lower()
        title_case += i[0].upper()+i[1:]+" "
    title_case = title_case[:-1]

    ret = sentence[0].upper()
    for i in range(1, len(sentence)):
        if sentence[i-1] == ' ':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()

    return ret, title_case
