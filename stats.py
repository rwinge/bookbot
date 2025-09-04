def get_num_words(text: str) -> str:
    word_counter = 0
    for word in text.split():
        word_counter += 1
    return f"Found {word_counter} total words"

def get_chars_count(text: str) -> dict:
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars

def sort_char_counts(char_counts: dict) -> list:
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    def by_num(entry):
        return entry["num"]

    sorted_list.sort(key=by_num, reverse=True)
    return sorted_list