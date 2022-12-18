import csv, random
from PIL import Image, ImageFont, ImageDraw

def generateCardArray(csvFile):
    prompts = []
    with open(csvFile, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            prompts.append(row[0])
    selection = random.choices(prompts, k=24)
    selection.insert(12, "Free Space")
    card = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(selection[i*5 + j])
        card.append(row)
    return card

def generateCardImage(array):
    cardPreset = Image.open('bingocard.png')
    #font = ImageFont.load_default()
    font = ImageFont.truetype("Arial.ttf", 20)
    for i in range(5):
        for j in range(5):
            text = array[i][j]
            lines = split(text, 16)
            editable = ImageDraw.Draw(cardPreset)
            for k in range(len(lines)):
                editable.text((55+(207*i),545+(20*k)-(10*len(lines))+(207*j)), lines[k], (0, 0, 0), font=font)
    #draw.text(( 20, 32), "text_string", (255,0,0), font=font)
    cardPreset.save("result.jpg")

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
    array = generateCardArray('bingoset.csv')
    generateCardImage(array)
