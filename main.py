import sys
from stats import count_words, count_characters, sorted_dictonaries
def get_book_text(file_path):
    with open(file_path) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_location = sys.argv[1]
    book = get_book_text(file_location)
    num_words = count_words(book)
    counted_characters = count_characters(book)
    result = sorted_dictonaries(counted_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for element in result:
        print(f"{element["char"]}: {element["count"]}")
    print("============= END ===============")
main()
