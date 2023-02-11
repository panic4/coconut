with open('temp.txt', "r+b") as f:
    line = f.readline()
    lexed = []
    for i in range(len(line) // 4):
        lexed.append(line[4 * i: 4 * i + 4])
        
    if lexed[0] == b'\xf0\x9f\x8d\x8e':
        #1🍎
    if lexed[0] == b'\xf0\x9f\x8c\x88':
        #2🌈
    if lexed[0] == b'\xf0\x9f\x8d\x89':
        #3🍉
    if lexed[0] == b'\xf0\x9f\x8c\xba':
        #4🌺
    if lexed[0] == b'\xf0\x9f\xa5\x9d':
        #5🥝
    if lexed[0] == b'\xf0\x9f\x8d\x87':
        #6🍇
    if lexed[0] == b'\xf0\x9f\x8d\x8a':
        #7🍊
    if lexed[0] == b'\xf0\x9f\x8d\x93':
        #8🍓
    if lexed[0] == b'\xf0\x9f\x8d\x92':
        #9🍒
    if lexed[0] == b'\xf0\x9f\x8d\x88':
        #10🍈
    if lexed[0] == b'\xf0\x9f\x8d\x8d':
        #11⛱️
    if lexed[0] == b'\xf0\x9f\x8d\xb9':
        #12⛵️
    if lexed[0] == b'\xf0\x9f\xa5\xad':
        #13🥭
    if lexed[0] == b'\xf0\x9f\xa4\xbf':
        #14🤿
    if lexed[0] == b'\xf0\x9f\x8f\x9d':
        #15🏝 
    if lexed[0] == b'\xf0\x9f\x8c\x8b':
        #16🌋 
    if lexed[0] == b'\xf0\x9f\x8c\x8a':
        #17🌊