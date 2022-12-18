from generateCardArray import generateCardArray
from textSplitter import split
from PIL import Image, ImageFont, ImageDraw

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

if __name__ == '__main__':
    array = generateCardArray('bingoset.csv')
    generateCardImage(array)