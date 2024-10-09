def max_repeated_char_string(strings):
    max_string = ""
    max_count = 0

    for s in strings:
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        current_max_char = max(char_count, key=char_count.get)
        current_max_count = char_count[current_max_char]

        if current_max_count > max_count:
            max_count = current_max_count
            max_string = s

    return max_string

def main():
    N = int(input("Введіть кількість рядків (N): "))
    strings = []

    for _ in range(N):
        string = input("Введіть рядок: ")
        strings.append(string)

    result = max_repeated_char_string(strings)

    if result:
        print("Рядок з найбільшою кількістю однакових символів:", result)
    else:
        print("Не було введено жодного рядка.")

if __name__ == "__main__":
    main()