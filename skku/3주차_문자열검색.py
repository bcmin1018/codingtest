# sentence = 'David Beckham is one of the English famous soccer player'
# print(sentence.find("is"))
# # print(sentence.index("two"))
# print(sentence.rfind("Beckham"))
# print(sentence.startswith("david"))
# print(sentence.endswith(".reyalp"))



# 문제 1
def find_first(file, key):
    infile = open(file, 'r')
    outfile = open('result.txt', 'w')

    text = infile.read()
    pos = text.find(key)

    if pos == -1:
        outfile.write(key + 'is not found.\n')
    else:
        outfile.write(key + 'is at ' + str(pos) + ".\n")

    outfile.close()
    infile.close()
    print('done')


def find_second(file, key):
    infile = open(file, 'r')
    outfile = open('result.txt', 'w')

    text = infile.read()
    pos = text.find(key)
    pos = text.find(key, pos + 1)

    if pos == -1:
        outfile.write(key + 'is not found.\n')
    else:
        outfile.write(key + 'is at ' + str(pos) + ".\n")

    outfile.close()
    infile.close()
    print('done')
