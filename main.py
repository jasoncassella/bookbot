def main():
    book_path = 'books/frankenstein.txt'

    with open(book_path) as f:
        text = f.read()
    
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)

    letter_list = []

    for letter, count in letter_count.items():
        if letter.isalpha():
            dict = {}
            dict[letter] = count
            letter_list.append(dict)
    
    print(f"--- Begin report of {book_path}")
    print(f'{word_count} words were found in the document\n')

    for dict in letter_list:
        for letter, value in dict.items():
            print(f'The letter {letter} was found: {value} times')

def get_word_count(text):
    words = text.split()
    return (len(words))

def get_letter_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()