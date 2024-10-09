def is_palindrome(word):
    return word == word[::-1]

def main():
    user_input = input("Введіть речення: ")
    
    words = user_input.split()
    
    if not words:
        print("Ви не ввели жодного слова.")
        return
    
    shortest_word = min(words, key=len)
    
    if is_palindrome(shortest_word):
        print(f"Найкоротше слово '{shortest_word}' є паліндромом.")
    else:
        print(f"Найкоротше слово '{shortest_word}' не є паліндромом.")

if __name__ == "__main__":
    main()