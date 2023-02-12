registers={
	b'\xf0\x9f\x8d\x8c': None,
	b'\xf0\x9f\xa7\x83': None,
	b'\xf0\x9f\xa5\x91': None,
	b'\xf0\x9f\xa9\xb3': None
}

with open('test.cn', "r+b") as f:
    line = f.readline()

lexed = [line[i:i + 4] for i in range(0, len(line), 4)]

if lexed[0] == b'\xf0\x9f\x8d\x8e':
	#1🍎
	pass
if lexed[0] == b'\xf0\x9f\x8c\x88':
	#2🌈
	pass
if lexed[0] == b'\xf0\x9f\x8d\x89':
	#3🍉
	pass
if lexed[0] == b'\xf0\x9f\x8c\xba':
	#4🌺
	pass
if lexed[0] == b'\xf0\x9f\xa5\x9d':
	#5🥝
	pass
if lexed[0] == b'\xf0\x9f\x8d\x87':
	#6🍇
	pass
if lexed[0] == b'\xf0\x9f\x8d\x8a':
	#7🍊
	pass
if lexed[0] == b'\xf0\x9f\x8d\x93':
	#8🍓
	pass
if lexed[0] == b'\xf0\x9f\x8d\x92':
	#9🍒
	pass
if lexed[0] == b'\xf0\x9f\x8d\x88':
	#10🍈
	pass
if lexed[0] == b'\xf0\x9f\x8d\x8d':
	#11⛱️
	pass
if lexed[0] == b'\xf0\x9f\x8d\xb9':
	#12⛵️
	pass
if lexed[0] == b'\xf0\x9f\xa5\xad':
	#13🥭
	pass
if lexed[0] == b'\xf0\x9f\xa4\xbf':
	#14🤿
	pass
if lexed[0] == b'\xf0\x9f\x8f\x9d':
	#15🏝
	pass
if lexed[0] == b'\xf0\x9f\x8c\x8b':
	#16🌋 
	pass
if lexed[0] == b'\xf0\x9f\x8c\x8a':
	pass
if lexed[0] in registers:
	registers[lexed[0]] = eval(b''.join(lexed[i] for i in range(1,len(lexed))))
