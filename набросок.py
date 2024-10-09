def is_palindrome(word):
    # Перевірка, чи є слово паліндромом
    return word == word[::-1]

def main():
    # Введення рядка слів
    user_input = input("Введіть рядок слів, розділених пробілами: ")
    
    # Розділення рядка на слова
    words = user_input.split()
    
    if not words:
        print("Ви не ввели жодного слова.")
        return
    
    # Знаходження найкоротшого слова
    shortest_word = min(words, key=len)
    
    # Перевірка, чи є найкоротше слово паліндромом
    if is_palindrome(shortest_word):
        print(f"Найкоротше слово '{shortest_word}' є паліндромом.")
    else:
        print(f"Найкоротше слово '{shortest_word}' не є паліндромом.")

if __name__ == "__main__":
    main()




    def max_repeated_char_string(strings):
    max_string = ""
    max_count = 0

    for s in strings:
        # Створюємо словник для підрахунку символів
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Знаходимо символ з найбільшим повторенням у рядку
        current_max_char = max(char_count, key=char_count.get)
        current_max_count = char_count[current_max_char]

        # Якщо знайдено більше повторень, оновлюємо max_string
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