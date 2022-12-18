import csv, random

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


if __name__ == '__main__':
    print(generateCardArray('bingoset.csv'))
