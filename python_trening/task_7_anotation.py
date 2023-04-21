def indent(s: str, width: int):
    return ' '*(max(0, width-len(s)))+s
print(indent('123', 123))