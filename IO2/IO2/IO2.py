def main():

    text = input()
    print(BracketPair(text))

def BracketPair(text):
    iparens = iter('()')
    parens = dict(zip(iparens, iparens))
    closing = parens.values()
    stack = []
    for i in text:
        d = parens.get(i, None)
        if d:
            stack.append(d)
        elif i in closing:
            if not stack or i != stack.pop():
                return False
    return not stack


if __name__ == "__main__":
    main()