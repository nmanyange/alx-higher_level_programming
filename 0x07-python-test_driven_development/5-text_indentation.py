#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of the characters .,? and :

    Args:
        text: Must be a string

    Raises:
        TypeError: If text is not a string

    Returns:
        Text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    lines = []
    line = ''

    for char in text:
        line += char
        if char in punctuation:
            lines.append(line.strip())
            lines.append('')
            line = ''

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
