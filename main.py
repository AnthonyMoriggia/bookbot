from stats import get_book_text, get_word_count, get_character_count
    
def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    char_count = get_character_count(text)

    print(f"""
========== BOOKBOT ==========
Analyzing book found at book/frankenstein.txt...
-------- Word Count ---------
Found {word_count} total words
------ Character Count ------
{char_count}
============ END ===========""")


if __name__ == "__main__":
    main()
