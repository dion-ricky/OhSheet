
def a1_to_dec(a1):
    """Translates A1 notation into decimal number
    
    :param a1: The A1 notation to be translated
    :type a1: str

    :returns: A number of equivalent A1 notation in decimal

    Example:

    >>> a1_to_dec('J')
    10

    """
    a1 = a1.upper()
    
    decimal = 0
    for i in range(len(a1)):
        p = pow(26, len(a1)-i-1)
        o = ord(a1[i])-64
        decimal += p*o

    return decimal

def dec_to_a1(n):
    """Translates decimal number into A1 notation
    
    :param n: The number to be translated
    :type n: int

    :returns: A string containing translated number in A1 notation

    Example:

    >>> dec_to_a1(10)
    'J'

    """
    try:
        n -= 1
        letter = chr(65 + n%26)
        num = n//26
        if num > 0:
            return dec_to_a1(num) + letter
        else:
            return letter
    except (TypeError, ValueError):
        return None

def rowcol_to_a1(row, col):
    """Translates a row and column cell address to A1 notation
    
    :param row: The row of cell to be converted
                Row start at index 1
    :type row: int

    :param col: The column cell to be converted
                Column start at index 1
    :type col: int

    :returns: A string containing the cell's coordinate in A1 notation

    Example:
    >>> rowcol_to_a1(1, 1)
    'A1'

    """
    if row < 1 or col < 1:
        raise ValueError('(%s, %s)' % (row, col))

    return '%s%s' % (dec_to_a1(row), col)

def range_to_a1(pair):
    """Translates array of row-col pairs array into A1 notation
    
    :param pair: The row-col pairs to be translated into A1 notation
    :type pair: array of array

    :returns: A string containing the range coordinates in A1 notation

    Example:

    >>> range_to_a1([ [1, 1], [1, 2] ])
    'A1:A2'

    """
    range_start = rowcol_to_a1( pair[0][0], pair[0][1] )
    range_end = rowcol_to_a1( pair[1][0], pair[1][1] )

    return ('%s:%s' % (range_start, range_end))

def get_empty_array(n):
    """Generate empty array with certain size
    
    :param n: A decimal number that specify generated array size
    :type n: int

    :returns: Array with size of n

    Example:
    >>> get_empty_array(5)
    ['', '', '', '', '']
    
    """
    r = ['' for i in range(n)]
    
    return r