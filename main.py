def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)

    print(f'{word_count} words were found in the document')
    print(letter_count)
    
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