"""
	R1: b'\xf0\x9f\x8d\x8c' -> 🍌
	R2: b'\xf0\x9f\xa7\x83' -> 🧃
	R3: b'\xf0\x9f\xa5\x91' -> 🥑
	R4: b'\xf0\x9f\xa9\xb3' -> 🩳
"""
registers = {
	b'\xf0\x9f\x8d\x8c': None,
	b'\xf0\x9f\xa7\x83': None,
	b'\xf0\x9f\xa5\x91': None,
	b'\xf0\x9f\xa9\xb3': None
}


with open('test.cn', "r+b") as f:
	lines = f.readlines()
	for line in lines:
		lexed = [line[i:i + 4] for i in range(0, len(line), 4)]

		if lexed[0] == b'\xf0\x9f\x8d\x8e':
			# 1🍎
			print()
		if lexed[0] == b'\xf0\x9f\x8c\x88':
			# 2🌈
			print()
		if lexed[0] == b'\xf0\x9f\x8d\x89':
			# 3🍉 if/endif statement
			print()
		if lexed[0] == b'\xf0\x9f\x8c\xba':
			# 4🌺
			print()
		if lexed[0] == b'\xf0\x9f\xa5\x9d':
			# 5🥝
			print()
		if lexed[0] == b'\xf0\x9f\x8d\x87':
			# 6🍇 Addition Operator
			registers[lexed[3]] = registers[lexed[1]] + registers[lexed[2]]
		if lexed[0] == b'\xf0\x9f\x8d\x8a':
			# 7🍊multiplication operator
			registers[lexed[3]] = registers[lexed[1]] * registers[lexed[2]]
		if lexed[0] == b'\xf0\x9f\x8d\x93':
			# 8🍓Subtraction Operator
			registers[lexed[3]] = registers[lexed[1]] - registers[lexed[2]]
			print(registers[lexed[3]])
		if lexed[0] == b'\xf0\x9f\x8d\x92':
			# 9🍒 Division operator
			registers[lexed[3]] = registers[lexed[1]] / registers[lexed[2]]
			print(registers[lexed[3]])
		if lexed[0] == b'\xf0\x9f\x8d\x88':
			# 10🍈 Equal operator
			registers[lexed[3]] = registers[lexed[1]] == registers[lexed[2]]
		if lexed[0] == b'\xf0\x9f\x8d\x8d':
			# 11🍍NOT operator
			registers[lexed[2]] = not registers[lexed[1]]
		if lexed[0] == b'\xf0\x9f\x8d\xb9':
			# 12🍹 OR operator
			registers[lexed[3]] = registers[lexed[1]] or registers[lexed[2]]
		if lexed[0] == b'\xf0\x9f\xa5\xad':
			# 13🥭AND operator
			registers[lexed[3]] = registers[lexed[1]] and registers[lexed[2]]
		if lexed[0] == b'\xf0\x9f\xa4\xbf':
			# 14🤿 > operator
			registers[lexed[3]] =  registers[lexed[1]] > registers[lexed[2]]
		if lexed[0] == b'\xf0\x9f\x8f\x9d':
			# 15🏝 < operator
			registers[lexed[3]] = registers[lexed[1]] < registers[lexed[2]]
		if lexed[0] == b'\xf0\x9f\x8c\x8b':
			# 16🌋
			pass
		if lexed[0] == b'\xf0\x9f\x8c\x8a':
			# 17🌊
			pass
		if lexed[0] == b'\xf0\x9f\x8e\xa3':
			#18🎣 Print statement
			if lexed[1] in registers: 
				print(registers[lexed[1]])
		if lexed[0] in registers:
			registers[lexed[0]] = eval(b''.join(lexed[i]
								for i in range(1, len(lexed))))
