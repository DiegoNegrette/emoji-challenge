# 👉 : moves the memory pointer to the next cell

# 👈 : moves the memory pointer to the previous cell

# 👆 : increment the memory cell at the current position 

# 👇 : decreases the memory cell at the current position. 

# 🤜 : if the memory cell at the current position is 0, jump just after the corresponding 🤛

# 🤛 : if the memory cell at the current position is not 0, jump just after the corresponding 🤜

# 👊 : Display the current character represented by the ASCII code defined by the current position.

## Notes:
# - As memory cells are bytes, from 0 to 255 value, if you decrease 0 you'll get  255, if you increment 255 you'll get 0.
# - Loops of 🤜 and 🤛 can be nested. 

# Hello
# instructions =  '👇🤜👇👇👇👇👇👇👇👉👆👈🤛👉👇👊👇🤜👇👉👆👆👆👆👆👈🤛👉👆👆👊👆👆👆👆👆👆👆👊👊👆👆👆👊'

# Hello World!
instructions = '👉👆👆👆👆👆👆👆👆🤜👇👈👆👆👆👆👆👆👆👆👆👉🤛👈👊👉👉👆👉👇🤜👆🤛👆👆👉👆👆👉👆👆👆🤜👉🤜👇👉👆👆👆👈👈👆👆👆👉🤛👈👈🤛👉👇👇👇👇👇👊👉👇👉👆👆👆👊👊👆👆👆👊👉👇👊👈👈👆🤜👉🤜👆👉👆🤛👉👉🤛👈👇👇👇👇👇👇👇👇👇👇👇👇👇👇👊👉👉👊👆👆👆👊👇👇👇👇👇👇👊👇👇👇👇👇👇👇👇👊👉👆👊👉👆👊'


def run_hpl(instructions):
    global memory
    memory = [0]
    global pointer_position
    pointer_position = 0
    global instruction
    instruction = 0
    global output
    output = ''

    def move_right():
        global pointer_position
        pointer_position += 1
        try:
            memory[pointer_position]
        except IndexError:
            memory.append(0)

    def move_left():
        global pointer_position
        pointer_position -= 1


    def increment_value():
        global memory
        memory[pointer_position] += 1
        if memory[pointer_position] > 255:
            memory[pointer_position] = 0

    def decrement_value():
        global memory
        memory[pointer_position] -= 1
        if memory[pointer_position] < 0:
            memory[pointer_position] = 255
    
    def move_to_closing_fist():
        if memory[pointer_position] == 0:
            global instruction
            number_of_opening_fist = 1
            number_of_closing_fist = 0
            while number_of_opening_fist != number_of_closing_fist:
                instruction += 1
                current_instruction = instructions[instruction]
                if current_instruction == '🤜':
                    number_of_opening_fist += 1
                elif current_instruction == '🤛':
                    number_of_closing_fist += 1

    def move_to_opening_fist():
        if memory[pointer_position] != 0:
            global instruction
            number_of_opening_fist = 0
            number_of_closing_fist = 1
            while number_of_opening_fist != number_of_closing_fist:
                instruction -= 1
                current_instruction = instructions[instruction]
                if current_instruction == '🤜':
                    number_of_opening_fist += 1
                elif current_instruction == '🤛':
                    number_of_closing_fist += 1

    def update_output_string():
        global output
        output += chr (memory[pointer_position])

    actions_dict = {
        '👉': move_right,
        '👈': move_left,
        '👆': increment_value,
        '👇': decrement_value,
        '🤜': move_to_closing_fist,
        '🤛': move_to_opening_fist,
        '👊': update_output_string,
    }

    while instruction < len(instructions):
        actions_dict[instructions[instruction]]()
        # print(instruction, instructions[instruction], output)
        instruction += 1
    return output

print(run_hpl(instructions))
