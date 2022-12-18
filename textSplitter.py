def split(text, maxChars):
    words = text.split()
    lines = buildLines(words, maxChars, [])
    return lines

def buildLines(words, maxChars, lines):
    if len(words) == 0:
        return lines
    line = words.pop(0)
    going = True
    while going:
        if len(words) == 0:
            going = False
        elif len(line + ' ' + words[0]) <= maxChars:
            line += ' '
            line += words.pop(0)
        else:
            going = False
    return buildLines(words, maxChars, lines + [line])


if __name__ == '__main__':
    print(split("house too expensive for the \
        character's profession", 16))