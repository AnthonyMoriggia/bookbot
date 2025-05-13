import sys
from stats import get_book_text, get_word_count, get_character_count
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print("Book Not Found")
        sys.exit(1)

    word_count = get_word_count(text)
    char_count = get_character_count(text)

    print(f"""
========== BOOKBOT ==========
Analyzing book found at {book_path}...
-------- Word Count ---------
Found {word_count} total words
------ Character Count ------
{char_count}
============ END ===========""")


if __name__ == "__main__":
    main()
