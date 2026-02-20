"""Auto-extracted code cells from text_analytics_and_tree_structures.ipynb."""

# ---- Code cell 1 ----
class Node:
    def __init__(self, title):
        self.title = title
        self.subchapters = []

    def add_subchapter(self, title):
        # Create a subchapter node and add it to subchapters
        new_node = Node(title)
        self.subchapters.append(new_node)
        return new_node

    def print_toc(self, level=0, chapter_num=None):
        # Print title with indentation and find chapter number
        indent = "  " * level
        current_chapter = f"{chapter_num}. " if chapter_num else ""
        print(f"{indent}{current_chapter}{self.title}")

        # Print subchapters
        for i, subchapter in enumerate(self.subchapters, start=1):
            # Add decimal points between sections
            subchapter.print_toc(level + 1, f"{chapter_num}.{i}" if chapter_num else str(i))

    ### CHALLENGE QUESTION ###
    def depth_of_chapter(self, target_title, current_depth=0):
        # Return current title if the node matches the depth
        if self.title == target_title:
            return current_depth

        # Recursive case: check each subchapter
        for subchapter in self.subchapters:
            depth = subchapter.depth_of_chapter(target_title, current_depth + 1)
            if depth is not None:
                return depth
        # If the target title is not found in this branch, return None
        return None

    def height_of_tree(self):
      # If there are no subchapters, it is a leaf node
      if not self.subchapters:
          return 0

      # Find the height (recursively)
      return 1 + max(subchapter.height_of_tree() for subchapter in self.subchapters)

# Add chapters or subchapters based on level
def add_level_chapter(node, level, title):
    if level == 0:
        return node.add_subchapter(title)
    elif level > 0:
        current = node
        for _ in range(level - 1):
            if current.subchapters:
                # Go to the last subchapter
                current = current.subchapters[-1]
        return current.add_subchapter(title)





if __name__ == "__main__":
    book = Node("Data Science: The Hard Parts")

    chapter1 = add_level_chapter(book, 0, "So What? Creating Value with Data Science")
    chapter2 = add_level_chapter(book, 0, "Metrics Design")
    chapter3 = add_level_chapter(book, 0, "Growth Decompositions: Understanding Tailwinds and Headwinds")
    chapter4 = add_level_chapter(book, 0, "2×2 Designs")
    chapter5 = add_level_chapter(book, 0, "Building Business Cases")
    chapter6 = add_level_chapter(book, 0, "What's In A Lift")
    chapter7 = add_level_chapter(book, 0, "Narratives")
    chapter8 = add_level_chapter(book, 0, "Datavis: Choosing The Right Plot To Deliver A Message")
    chapter9 = add_level_chapter(book, 0, "Simulation and Bootstrapping")
    chapter10 = add_level_chapter(book, 0, "Linear Regression: Going Back To Basics")

    # Sub chapter
    subchapter1_1 = add_level_chapter(chapter1, 1, "What Is Value?")
    subchapter1_2 = add_level_chapter(chapter1, 1, "What: Understanding the Business")
    subchapter1_3 = add_level_chapter(chapter1, 1, "So What: The Gist of Value Creation in DS")
    subchapter1_4 = add_level_chapter(chapter1, 1, "Now What: Be a Go-Getter")
    subchapter1_5 = add_level_chapter(chapter1, 1, "Measuring Value")
    subchapter2_1 = add_level_chapter(chapter2, 1, "Desirable Properties That Metrics Should Have")
    subchapter2_2 = add_level_chapter(chapter2, 1, "Metrics Decomposition")
    subchapter2_3 = add_level_chapter(chapter2, 1, "Example: Another Revenue Decomposition")
    subchapter2_4 = add_level_chapter(chapter2, 1, "Example: Marketplaces")
    subchapter2_5 = add_level_chapter(chapter2, 1, "Key Takeaways")
    subchapter3_1 = add_level_chapter(chapter3, 1, "Why Growth Decompositions?")
    subchapter3_2 = add_level_chapter(chapter3, 1, "Additive Decompositon")
    subchapter3_3 = add_level_chapter(chapter3, 1, "Multiplicative Decomposition")
    subchapter3_4 = add_level_chapter(chapter3, 1, "Mix-Rate Decompositions")
    subchapter3_5 = add_level_chapter(chapter3, 1, "Mathematical Derivations")
    subchapter4_1 = add_level_chapter(chapter4, 1, "The Case for Simplification")
    subchapter4_2 = add_level_chapter(chapter4, 1, "What’s a 2×2 Design?")
    subchapter4_3 = add_level_chapter(chapter4, 1, "Example: Test a Model and a New Feature")
    subchapter4_4 = add_level_chapter(chapter4, 1, "Example: Understanding User Behavior")
    subchapter4_5 = add_level_chapter(chapter4, 1, "Example: Credit Originiation and Acceptance")
    subchapter5_1 = add_level_chapter(chapter5, 1, "Some Principles to Construct Business Cases")
    subchapter5_2 = add_level_chapter(chapter5, 1, "Example: Proactive Retention Strategy")
    subchapter5_3 = add_level_chapter(chapter5, 1, "Fraud Prevention")
    subchapter5_4 = add_level_chapter(chapter5, 1, "Purchasing External Datasets")
    subchapter5_5 = add_level_chapter(chapter5, 1, "Working on a Data Science Project")
    subchapter6_1 = add_level_chapter(chapter6, 1, "Lifts Defined")
    subchapter6_2 = add_level_chapter(chapter6, 1, "Example: Classifier Model")
    subchapter6_3 = add_level_chapter(chapter6, 1, "Self-Selection and Survivorship Biases")
    subchapter6_4 = add_level_chapter(chapter6, 1, "Other Use Cases for Lifts")
    subchapter6_5 = add_level_chapter(chapter6, 1, "Key Takeaways")
    subchapter7_1 = add_level_chapter(chapter7, 1, "What's in a Narrative: Telling a Story with Your Data")
    subchapter7_2 = add_level_chapter(chapter7, 1, "Building a Narrative")
    subchapter7_3 = add_level_chapter(chapter7, 1, "The Last Mile")
    subchapter7_4 = add_level_chapter(chapter7, 1, "Key Takeaways")
    subchapter7_5 = add_level_chapter(chapter7, 1, "Further Readings")
    subchapter8_1 = add_level_chapter(chapter8, 1, "Some Useful and Not-So-Used Data Visualizations")
    subchapter8_2 = add_level_chapter(chapter8, 1, "General Recommendations")
    subchapter8_3 = add_level_chapter(chapter8, 1, "Key Takeaways")
    subchapter8_4 = add_level_chapter(chapter8, 1, "Further Reading")
    subchapter9_1 = add_level_chapter(chapter9, 1, "Basics of Simulation")
    subchapter9_2 = add_level_chapter(chapter9, 1, "Simulating a Linear Model and Linear Regression")
    subchapter9_3 = add_level_chapter(chapter9, 1, "What are Partial Dependence Plots?")
    subchapter9_4 = add_level_chapter(chapter9, 1, "Omitted Variable Bias")
    subchapter9_5 = add_level_chapter(chapter9, 1, "Simulating Classification Problems")
    subchapter10_1 = add_level_chapter(chapter10, 1, "What's in a Coefficient?")
    subchapter10_2 = add_level_chapter(chapter10, 1, "The Frisch-Waugh-Lovell Theorem")
    subchapter10_3 = add_level_chapter(chapter10, 1, "Why Should You Care Aboule FWL")
    subchapter10_4 = add_level_chapter(chapter10, 1, "Confounders")
    subchapter10_5 = add_level_chapter(chapter10, 1, "Additional Variables")

    # Sub sub chapter
    add_level_chapter(subchapter2_1, 1, "Measurable")
    add_level_chapter(subchapter2_1, 1, "Actionable")
    add_level_chapter(subchapter2_1, 1, "Relevance")
    add_level_chapter(subchapter2_1, 1, "Timeliness")
    add_level_chapter(subchapter2_2, 1, "Funnel Analytics")
    add_level_chapter(subchapter2_2, 1, "Stock-Flow Decompositions")
    add_level_chapter(subchapter2_2, 1, "PxQ-Type Decompositions")
    add_level_chapter(subchapter3_1, 1, "Example")
    add_level_chapter(subchapter3_1, 1, "Interpretation and Use Cases")
    add_level_chapter(subchapter3_2, 1, "Example")
    add_level_chapter(subchapter3_2, 1, "Interpretation")
    add_level_chapter(subchapter3_3, 1, "Example")
    add_level_chapter(subchapter3_3, 1, "Interpretation")
    add_level_chapter(subchapter3_4, 1, "Additive Decompositon")
    add_level_chapter(subchapter3_4, 1, "Multiplicative Decomposition")
    add_level_chapter(subchapter3_4, 1, "Mix-Rate Decompositions")
    add_level_chapter(subchapter4_1, 1, "Example: Test a Model and a New Feature")
    add_level_chapter(subchapter7_1, 1, "Clear and to the Point")
    add_level_chapter(subchapter7_1, 1, "Credible")
    add_level_chapter(subchapter7_1, 1, "Memorable")
    add_level_chapter(subchapter7_1, 1, "Actionable")
    add_level_chapter(subchapter7_2, 1, "Science as Storytelling")
    add_level_chapter(subchapter7_2, 1, "What, So What, and Now What?")
    add_level_chapter(subchapter7_3, 1, "Writing TL;DRs")
    add_level_chapter(subchapter7_3, 1, "Tips to Write Memorable TL;DRs")
    add_level_chapter(subchapter7_3, 1, "Example: Writing a TL;DR for This Chapter")
    add_level_chapter(subchapter7_3, 1, "Delivering Powerful ELevator Pitches")
    add_level_chapter(subchapter7_3, 1, "Presenting Your Narrative")
    add_level_chapter(subchapter8_1, 1, "Bar Versus Line Plots")
    add_level_chapter(subchapter8_1, 1, "Slopegraphs")
    add_level_chapter(subchapter8_1, 1, "Waterfall Charts")
    add_level_chapter(subchapter8_1, 1, "Scatterplot Smoothers")
    add_level_chapter(subchapter8_1, 1, "Plotting Distributions")
    add_level_chapter(subchapter8_2, 1, "Choose Your Colors Wisely")
    add_level_chapter(subchapter8_2, 1, "Different Dimensions in a Plot")
    add_level_chapter(subchapter8_2, 1, "Aim for a Large Enough Data-Ink Ratio")
    add_level_chapter(subchapter8_2, 1, "Customization Versus Semiautomation")
    add_level_chapter(subchapter8_2, 1, "Get the Font Size Right from the Beginning")
    add_level_chapter(subchapter9_5, 1, "Latent Variable Models")
    add_level_chapter(subchapter9_5, 1, "Comparing Different Algorithms")

    # Find depth example
    print("Depth of 'Metrics Design Chapter':", book.depth_of_chapter("Metrics Design"))

    # Find height of book
    print("Height of the book tree:", book.height_of_tree())

    # Print the table of contents
    book.print_toc()

# ---- Code cell 2 ----
# Basic code to read a file
# mybook.txt must to be located in your working folder.
# If you are using Google Colab, add it on root of the 'folder' (left menu, folder icon)
# Be aware that this file will be removed once you close your browser.

f = open('/root/Alice In Wonderland.txt')
contents = f.read()
#print(contents)

# you can use any built-in functions for array, string, dictionary and sets.

# ---- Code cell 3 ----
import string

# Storing the sets of punctuation in variable result
result = string.punctuation

# Printing the punctuation values
#print(result)


# initializing string
test_str = contents

# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''

# Removing punctuations in string
# Using loop + punctuation string
for ele in test_str:
    if ele in punc:
        test_str = test_str.replace(ele, "")

# printing result
#print("The string after punctuation filter : " + test_str)

# ---- Code cell 4 ----
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Create a set of stop words
stop_words = set(stopwords.words('english'))

# Define a function to remove stop words from a sentence
def remove_stop_words(sentence):  # Split the sentence into individual words
  # Convert to lowercase and split
  words_lower = sentence.lower()
  words = words_lower.split()


  # Use a list comprehension to remove stop words
  filtered_words = [word for word in words if word not in stop_words]

  # Join the filtered words back into a sentence
  return ' '.join(filtered_words)

# ---- Code cell 5 ----
# remove stop words
filtered_test_str = remove_stop_words(test_str)
print(filtered_test_str)

# ---- Code cell 6 ----
# Identify the distribution of each letter from a to z, including lower and upper cases.
# Convert all text to lowercase
def letter_frequency(text):
    # Convert text to lowercase
    text = test_str.lower()

    # Initialize an empty list to store letter frequencies
    frequencies = []

    # Loop through each unique character in the text
    for char in sorted(set(text)):
      # is.alpha checks for all letters in alphabet
        if char.isalpha():
            count = text.count(char)
            frequencies.append((char, count))

    return frequencies

frequencies = letter_frequency(filtered_test_str)
for letter, freq in frequencies:
    print(f"{letter}: {freq}")

# ---- Code cell 7 ----
# Identify the distribution of each letter from a to z, including lower and upper cases.
def get_count(word_freq_tuple):
    return word_freq_tuple[1]

# Count word frequencies and return the top 40
def word_frequency(filtered_text, top_n=40):
    # Split the filtered text into words
    words = filtered_test_str.split()

    # Initialize an empty list
    word_frequencies = []

    # Loop through each unique word
    for word in sorted(set(words)):
      # Count occurrences of the current word
        count = words.count(word)
        # Append the word as a tuple
        word_frequencies.append((word, count))

    # Sort the word frequencies
    word_frequencies.sort(key=get_count, reverse=True)
    # Return the top 40 items
    return word_frequencies[:top_n]

# Get the top 40
top_words = word_frequency(filtered_test_str)

# Print the top words
print("Top 40 Most Common Words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

# ---- Code cell 8 ----
from collections import Counter

# Split the input string into words (tokens)
words = filtered_test_str.split()

# Create a list to store the bigrams
bigrams = []

# Loop through the words and create bigrams
for i in range(1, len(words)):  # Start from the second word (index 1)
    bigram = (words[i-1], words[i])  # Create a tuple of consecutive words
    bigrams.append(bigram)  # Add the bigram to the list

# Use Counter to count the frequency of each bigram in the list
bigram_counts = Counter(bigrams)

# Get the top 20 most common bigrams, sorted by frequency (in descending order)
top_20_bigrams = bigram_counts.most_common(20)

# Print the top 20 bigrams and their frequencies
print("Top 20 Most Common Bigrams:")
for bigram, count in top_20_bigrams:
    print(f"{bigram}: {count}")

# ---- Code cell 9 ----
# Create a list to store the trigrams
trigrams = []

# Loop through the words and create trigrams
for i in range (len(words)-2):  # Start from the second word (index 1)
    trigram = (words[i], words[i+1], words[i+2])  # Create a tuple of consecutive words
    trigrams.append(trigram)  # Add the trigram to the list

# Use Counter to count the frequency of each trigram in the list
trigram_counts = Counter(trigrams)

# Get the top 20 most common trigrams, sorted by frequency (in descending order)
top_20_trigrams = trigram_counts.most_common(20)

# Print the top 20 trigrams and their frequencies
print("Top 20 Most Common Trigrams:")
for trigram, count in top_20_trigrams:
    print(f"{trigram}: {count}")

# ---- Code cell 10 ----
#Challenge Question: Produce an analysis of word frequency distribution by sentence structure (e.g., average words per sentence, common sentence starters).
#You must determine sentence boundaries and analyze trends in your writer's sentence structure. (This will not be graded)

#contents = text with sentence structure

from collections import defaultdict
from operator import itemgetter

# Split into sentences using `.`, `?`, and `!`
# Replace the sentence-ending punctuation with a period to standardize the split
sentences = contents.replace('!', '.').replace('?', '.').replace('`','').replace("'","").replace("*","").replace(',','').replace('(','').replace(')','').replace('-','').replace('"','').replace('[','').replace(']','').replace('_','').split('.')

# Initialize a dictionary to count word frequencies
first_word_frequency = defaultdict(int)

# Process each sentence
for sentence in sentences:
    # Strip leading/trailing whitespace and check if the sentence is not empty
    sentence = sentence.strip()
    if sentence:
        # Split the sentence by whitespace and get the first word
        words = sentence.split()
        if words:  # Ensure there is at least one word in the sentence
            first_word = words[0].lower()  # Take the first word and make it lowercase
            # Update the frequency dictionary
            first_word_frequency[first_word] += 1

# Sort by frequency in descending order and take the top 40 words
top_40_words = sorted(first_word_frequency.items(), key=itemgetter(1), reverse=True)[:40]

# Display the frequency of the 40 most common starting words
print("Top 40 most common starting words:")
for word, freq in top_40_words:
    print(f"{word}: {freq}")

