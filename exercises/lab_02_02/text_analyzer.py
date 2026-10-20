"""
Text Analyzer - Starter Version
Reads a text file and reports word count, sentence count,
average word length, longest word, and most common word.
"""

import string

TEXT_FILE = "sample_text.txt"


def load_text(filename):
    with open(filename, "r") as file:
        return file.read()


def clean_words(text):
    words = text.split()
    cleaned = []
    for word in words:
        stripped = word.strip(string.punctuation).lower()
        if stripped:
            cleaned.append(stripped)
    return cleaned


def count_sentences(text):
    sentence_endings = [".", "!", "?"]
    count = 0
    for char in text:
        if char in sentence_endings:
            count += 1
    return count


def average_word_length(words):
    total_length = 0
    for word in words:
        total_length += len(word)
    return total_length / len(words)


def find_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def most_common_word(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    most_common = ""
    highest_count = 0
    for word, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_common = word
    return most_common, highest_count


def analyze_text(filename):
    text = load_text(filename)
    words = clean_words(text)

    word_count = len(words)
    sentence_count = count_sentences(text)
    avg_length = average_word_length(words)
    longest_word = find_longest_word(words)
    common_word, common_count = most_common_word(words)

    print("--- Text Analysis Report ---")
    print(f"Total words: {word_count}")
    print(f"Total sentences: {sentence_count}")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Longest word: {longest_word}")
    print(f"Most common word: '{common_word}' (used {common_count} times)")


if __name__ == "__main__":
    analyze_text(TEXT_FILE)
