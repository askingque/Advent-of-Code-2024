def main():
    file = "day_3_input.txt"
    with open(file, "r") as f:
        data = f.readlines()

    parsed_data = ""
    for line in data:
        parsed_data += line
    
    numerical = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    curr_line = ""
    left_num = 0
    right_num = 0
    output = 0
    counter = 0
    for char in parsed_data:
        if counter < 60:
            print(f'char: {char}, curr_line: {curr_line}, left_num: {left_num}, right_num: {right_num}')
        counter += 1
        if curr_line == '':
            if char == 'm':
                curr_line += 'm'
        elif curr_line[-1] == 'm':
            if char == 'u':
                curr_line += 'u'
            else: 
                curr_line = ""
        elif curr_line[-1] == 'u':
            if char == 'l':
                curr_line += 'l'
            else:
                curr_line = ""
        elif curr_line[-1] == 'l':
            if char == '(':
                curr_line += '('
            else:
                curr_line = ""
        elif curr_line[-1] == '(':
            if char in numerical:
                
                curr_line += char
                left_num = left_num * 10 + int(char)
            else:
                curr_line = ""
        elif curr_line[-1] in numerical and ',' not in curr_line:
            if char in numerical:
                curr_line += char
                left_num = left_num * 10 + int(char)
            elif char == ',':
                curr_line += ','
            else:
                curr_line = ""
                left_num = 0
                right_num = 0
        elif curr_line[-1] in numerical and ',' in curr_line:
            if char in numerical:
                curr_line += char
                right_num = right_num * 10 + int(char)
            elif char == ')':
                output += left_num * right_num
                curr_line = ""
                left_num = 0
                right_num = 0
            else:
                curr_line = ""
                left_num = 0
                right_num = 0
        elif curr_line[-1] == ',':
            if char in numerical:
                curr_line += char
                right_num = right_num * 10 + int(char)
            else:
                curr_line = ""
                left_num = 0
                right_num = 0
        
    print(output)
        




    

if __name__ == "__main__":
    main()