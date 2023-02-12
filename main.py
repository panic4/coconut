registers={
	b'\xf0\x9f\x8d\x8c': None,
	b'\xf0\x9f\xa7\x83': None,
	b'\xf0\x9f\xa5\x91': None,
	b'\xf0\x9f\xa9\xb3': None
}

with open('test.cn', "r+b") as f:
    line = f.readline()
    lexed = []
    for i in range(len(line) // 4):
        lexed.append(line[4 * i: 4 * i + 4])

if lexed[0] == b'\xf0\x9f\x8d\x8e':
	#1🍎
	print()
if lexed[0] == b'\xf0\x9f\x8c\x88':
	#2🌈
	print()
if lexed[0] == b'\xf0\x9f\x8d\x89':
	#3🍉
	print()
if lexed[0] == b'\xf0\x9f\x8c\xba':
	#4🌺
	print()
if lexed[0] == b'\xf0\x9f\xa5\x9d':
	#5🥝
	print()
if lexed[0] == b'\xf0\x9f\x8d\x87':
	#6🍇
	print()
if lexed[0] == b'\xf0\x9f\x8d\x8a':
	#7🍊
	print()
if lexed[0] == b'\xf0\x9f\x8d\x93':
	#8🍓
	print()
if lexed[0] == b'\xf0\x9f\x8d\x92':
	#9🍒
	print()
if lexed[0] == b'\xf0\x9f\x8d\x88':
	#10🍈
	print()
if lexed[0] == b'\xf0\x9f\x8d\x8d':
	#11⛱️
	print()
if lexed[0] == b'\xf0\x9f\x8d\xb9':
	#12⛵️
	print()
if lexed[0] == b'\xf0\x9f\xa5\xad':
	#13🥭
	print()
if lexed[0] == b'\xf0\x9f\xa4\xbf':
	#14🤿
	print()
if lexed[0] == b'\xf0\x9f\x8f\x9d':
	#15🏝
	print()
if lexed[0] == b'\xf0\x9f\x8c\x8b':
	#16🌋 
	print()
if lexed[0] == b'\xf0\x9f\x8c\x8a':
	#17🌊
	print()