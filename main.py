def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(wordcount(file_contents))

def wordcount(text):
    words = text.split()
    return len(words)

main()