def matrix_mul(m_a, m_b):
    """Function to multiply two matrices m_a and m_b.
    
    Args:
        m_a (list): First matrix, a list of lists of integers/floats.
        m_b (list): Second matrix, a list of lists of integers/floats.

    Returns:
        list: A new matrix that is the product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats.
        ValueError: If m_a or m_b is empty or cannot be multiplied.
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check if m_a and m_b are empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Check if elements of m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangular (each row has the same number of elements)
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Check if m_a and m_b can be multiplied (number of columns in m_a == number of rows in m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            # Compute the dot product of the row from m_a and the column from m_b
            dot_product = 0
            for k in range(len(m_b)):
                dot_product += m_a[i][k] * m_b[k][j]
            new_row.append(dot_product)
        result.append(new_row)

    return result
