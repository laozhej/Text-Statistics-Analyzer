import string

def analyze_text(text):
    # 1. Calculate basic counts
    # We strip whitespace to ensure empty inputs don't count as characters
    char_count = len(text)
    
    # Split text into a list of words
    words = text.split()
    word_count = len(words)
    
    # 2. Find word frequency
    word_frequency = {}
    
    # Remove punctuation and normalize to lowercase
    clean_words = []
    for word in words:
        # This removes punctuation like commas or periods attached to words
        clean_word = word.strip(string.punctuation).lower()
        if clean_word:
            clean_words.append(clean_word)
            
    # Count occurrences
    for word in clean_words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
            
    # 3. Sort by most frequent (Top 3)
    # This sorts the dictionary items by value (count) in descending order
    most_common = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:3]
    
    return char_count, word_count, most_common

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Text Statistics Analyzer ---")
    user_text = input("Enter a paragraph of text to analyze:\n")
    
    if user_text:
        chars, words, common = analyze_text(user_text)
        
        print("\n--- Results ---")
        print(f"Total Characters: {chars}")
        print(f"Total Words:      {words}")
        print("Most Common Words:")
        for word, count in common:
            print(f"  - '{word}': {count} times")
    else:
        print("You didn't enter any text!")
