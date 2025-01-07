def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    wordlist = file_contents.split()

    print(charactercount(file_contents))
    print(wordcount(wordlist))

def wordcount(text):
    return len(text)

def charactercount(text):
    lowered_text = text.lower()
    characters = sorted(set(lowered_text))
    ##sorted_characters = sorted(characters)
    count = 0
    output = dict.fromkeys(characters, 0)
    
    for character in characters:
        count = lowered_text.count(character)
        output[character] = count

    return output


main()