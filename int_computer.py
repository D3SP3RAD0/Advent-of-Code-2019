

def run(program):
    i = 0
    try:
        while i < len(program):
            instruction = str(program[i])

            if program[i] == 1:
                program[program[i + 3]] = program[program[i + 1]] + program[program [i + 2]]
                i = i + 4
            elif program[i] == 2:
                program[program[i + 3]] = program[program[i + 1]] * program[program [i + 2]]
                i = i + 4
            elif program[i] == 3:
                
            elif program[i] == 99:
                return program[0]
            else:
                return 0
    except Exception as e:
        print(e)
        return 0