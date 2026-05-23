def find_min_max_in_array(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2
    left_min, left_max = find_min_max_in_array(arr[:mid])
    right_min, right_max = find_min_max_in_array(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


if __name__ == "__main__":
    numbers = [7, 11, 8, 99, 7, 43, 55, 28, 52, 79, 16, 14, 5, 55, 9, 11]
    min_val, max_val = find_min_max_in_array(numbers)

    print("Array:", numbers)
    print( f"MIN in array - {min_val}")
    print(f"MAX in array - {max_val}")