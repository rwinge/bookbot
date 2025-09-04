from stats import get_num_words, get_chars_count, sort_char_counts
import sys

def get_book_text(filepath: None) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    book_text = get_book_text(book)
    book_words = get_num_words(book_text)
    chars_count = get_chars_count(book_text)
    sorted_char_counts = sort_char_counts(chars_count)
    print("----------- Word Count ----------")
    print(book_words)
    print("--------- Character Count -------")
    for i in sorted_char_counts:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()