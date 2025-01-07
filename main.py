def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    wordlist = file_contents.split()
    words = wordcount(wordlist)
    characters = charactercount(file_contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for char_info in characters:
        print(f"The {char_info['char']} character was found {char_info['num']} times")
    print("--- End report ---")    

def get_text(path):
    with open(path) as f:
        return f.read()

def wordcount(text):
    return len(text)

def charactercount(text):
    lowered_text = "".join(char for char in text.lower() if char.isalpha())
    characters = set(lowered_text)
    count = 0
    character_count = dict.fromkeys(characters, 0)

    for character in characters:
        count = lowered_text.count(character)
        character_count[character] = count
    
    character_count_list = []

    for char, num in character_count.items():
        new_dict = {'char': char, 'num': num}
        character_count_list.append(new_dict)
    
    character_count_list.sort(reverse=True, key=sort_on)

    return character_count_list

def sort_on(dict):
    return dict["num"]


main()