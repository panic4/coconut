from sys import argv

registers = {
	b'\xf0\x9f\x8d\x8c': None,	#🍌
	b'\xf0\x9f\xa7\x83': None,		#🧃
	b'\xf0\x9f\xa5\x91': None,	#🥑
	b'\xf0\x9f\xa9\xb3': None	#🩳
}

exec = True

with open('island.cn', "r+b") as f:
	lines = f.readlines()

i = 0
while i  < len(lines):
	lexed = [lines[i][j:j + 4] for j in range(0, len(lines[i]), 4)]
	
	if lexed[0] == b'\xf0\x9f\x8d\x89' and exec == False:
		exec = True

	if exec:
	
		if lexed[0] == b'\xf0\x9f\x8c\x88':
			#🌈 input statement
			registers[lexed[1]] = eval(input())
			
		if lexed[0] == b'\xf0\x9f\x8e\xa3':
			#18🎣 Print statement
			if lexed[1] in registers: 
				print(registers[lexed[1]])
	
		if lexed[0] == b'\xf0\x9f\x8d\x89' and len(lexed)>1:
			# 3🍉 if/endif statement
			if len(lexed) == 2:
				pass
			elif registers[lexed[1]] == False:
				exec = False

		if lexed[0] == b'\xf0\x9f\x8c\xb8':
			# 4🌸 goto
			i = registers[lexed[1]]
			continue
	
		if lexed[0] == b'\xf0\x9f\x8d\x87':
			# 6🍇 Addition Operator
			registers[lexed[3]] = registers[lexed[1]] + registers[lexed[2]]
	
		if lexed[0] == b'\xf0\x9f\x8d\x8a':
			# 7🍊multiplication operator
			registers[lexed[3]] = registers[lexed[1]] * registers[lexed[2]]
	
		if lexed[0] == b'\xf0\x9f\x8d\x93':
			# 8🍓Subtraction Operator
			registers[lexed[3]] = registers[lexed[1]] - registers[lexed[2]]
	
		if lexed[0] == b'\xf0\x9f\x8d\x92':
			# 9🍒 Division operator
			registers[lexed[3]] = registers[lexed[1]] / registers[lexed[2]]
	
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
		
		if lexed[0] in registers:
			registers[lexed[0]] = eval(b''.join(lexed[i] for i in range(1, len(lexed))))
   
		if lexed[0] == b'\xf0\x9f\x8c\xb4':
			break
   
	i += 1
