def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)


    # print(f'{word_count} words were found in the document')
    print(letter_count)
    
def get_word_count(string):
    words = string.split()
    return (len(words))

def get_letter_count(string):
    string = string.lower()
    letters = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    dict = {}
    for letter in string:
        if letter in letters:
            dict.update({letter: letters[letter]})
            letters[letter] +=1

    return dict



main()