def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, and :
    Args:
        text (str): The text to be processed.
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Traverse each character in the string
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        # Check if the character is one of the specified punctuation marks
        if text[i] in ".?:":
            result += "\n\n"
            # Skip any spaces after the punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Print the result without extra spaces at the beginning or end
    print(result.strip(), end="")
