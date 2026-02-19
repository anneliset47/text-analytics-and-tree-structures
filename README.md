# Text Analytics and Tree Structures

Implementation of core data structures and algorithmic text analysis using *Alice’s Adventures in Wonderland* as the source text.

---

## Project Overview

This project demonstrates two primary algorithmic concepts:

1. **Tree Data Structures**
   - Hierarchical representation of a book’s table of contents
   - Recursive traversal
   - Depth and height calculations

2. **Text Analytics**
   - Letter frequency distribution
   - Stopword removal
   - Word frequency analysis
   - Bigram and trigram modeling
   - Word cloud visualization
   - Algorithm complexity analysis (Big-O notation)

The text corpus analyzed is *Alice’s Adventures in Wonderland* by Lewis Carroll.

---

## Part 1: Tree Data Structure – Table of Contents

### Approach

A `Node` class was implemented to represent chapters and subchapters in a hierarchical structure.

Each node:
- Stores a title
- Maintains a list of child nodes
- Uses recursive traversal to print structure
- Supports dynamic insertion at specified levels

### Key Concepts Demonstrated

- Recursive traversal
- Parent-child hierarchical modeling
- Tree depth calculation
- Tree height computation
- Structured class-based design

Time Complexity:
- Traversal: **O(n)**

---

## Part 2: Text Analytics

### 1. Letter Frequency Distribution

- Converted text to lowercase
- Removed punctuation
- Counted occurrences of each letter (a–z)
- Generated frequency table and visualization

Time Complexity:
- **O(n)**

---

### 2. Top 40 Words

- Tokenized text
- Removed stopwords
- Counted unique word frequencies
- Sorted results

Time Complexity:
- **O(w log w)**  
(where w = number of unique words)

---

### 3. Bigram Analysis

- Generated word pairs
- Counted frequency
- Sorted top 20 results
- Created word cloud visualization

Time Complexity:
- **O(w log w)**

---

### 4. Trigram Analysis

- Generated three-word sequences
- Counted frequencies
- Sorted top 20 results
- Created word cloud visualization

Time Complexity:
- **O(w log w)**

---

## Key Findings

- Most common letters: **e, a, t**
- Most common word: **“said”**, reflecting dialogue-heavy structure
- Frequent bigrams: “said Alice”, “Mock Turtle”
- Frequent trigrams: “said Mock Turtle”, “said March Hare”

The distribution patterns reflect standard English writing and the conversational structure of the novel.

---

## Repository Structure

```
text-analytics-and-tree-structures/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   └── text_analytics_and_tree_structures.ipynb
│
├── report/
│   └── text_analytics_report.pdf
│
└── figures/
    ├── letter_distribution.png
    ├── word_cloud.png
    └── ...
```

---

## Concepts Demonstrated

- Object-Oriented Programming
- Recursive Algorithms
- Frequency Counting
- N-gram Modeling
- Sorting Algorithms
- Time Complexity Analysis
- Data Visualization

---

## Reproducibility

Install dependencies:

```
pip install -r requirements.txt
```

Run the notebook in the `notebooks/` directory.

