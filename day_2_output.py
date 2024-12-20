def is_valid(arr):
    incr = None
    saved = None
    for num in arr:
        print(f'save: {saved}, num: {num}, incr: {incr}')
        if saved != None:
            diff = num - saved
            if incr != None:
                if diff < 0 and incr == True:
                    #print('decreased when we were increasing')
                    return False
                if diff > 0 and incr == False:
                    #print('increased when we were decreasing')
                    return False
                
            else:
                if diff < 0:
                    incr = False
                if diff > 0:
                    incr = True
            if diff == 0 or abs(diff) > 3:
                #print('diff is 0 or greater than 3')
                return False
            
        saved = num
    return True
        

def main():
    #read in data
    file = "day_2_input.txt"
    with open(file, "r") as f:
        data = f.readlines()

    #parse data
    parsed_data = []
    for line in data:
        parsed_data.append(int(x) for x in line.split())
    
    #check if line is valid
    valid_count = 0
    for line in parsed_data:
        if is_valid(line):
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    main()
