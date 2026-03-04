def extract_unique_words(paragraph):
    # Split the paragraph into words and convert them to lowercase
    words = paragraph.lower().split()

    # Create a set to store unique words
    unique_words = set(words)

    return unique_words

# Example paragraph
paragraph1 = "Python is a great programming language. Python is popular and powerful."

# Extracting unique words
unique_words1 = extract_unique_words(paragraph1)
print("Unique words in paragraph 1:", unique_words1)g