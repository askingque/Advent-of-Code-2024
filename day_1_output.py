def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    left_arr = []
    right_arr = []
    output = 0

    file = "day_1_input.txt"
    with open(file, "r") as f:
        data = f.readlines()

    for row in data:
        left_temp, right_temp = row.split("   ")
        left_arr.append(int(left_temp))
        right_arr.append(int(right_temp))
        

    left_arr = quicksort(left_arr)
    right_arr = quicksort(right_arr)
    for i in range(len(left_arr)):
        diff = left_arr[i] - right_arr[i]
        if diff < 0:
            diff = diff * -1
        output += diff

    print(output)

main()