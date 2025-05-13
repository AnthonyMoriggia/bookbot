def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    return text


def get_word_count(text):
    words = text.split()
    return len(words)

def sort_dict(dict):
    return dict["num"]


def get_character_count(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    formatted_char_counts = '\n'.join(f"{char}: {count}" for char, count in sorted_counts)

    return formatted_char_counts
