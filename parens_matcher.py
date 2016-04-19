def parens_match(s, open_index):
    """Given a sentence and the position of an opening parenthesis,
       return the postiion of the corresponding closing parenthesis"""

    open_count = 0

    position = open_index + 1

    for char in s[position:]:
        if char == "(":
            count += 1
        elif char == ")":
            if open_count == 0:
                return position
            else:
                open_count -= 1

        position += 1

    raise Exception("No matching closing parenthesis.")