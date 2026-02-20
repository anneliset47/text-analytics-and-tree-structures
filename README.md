# Text Analytics and Tree Structures

[![CI](https://github.com/anneliset47/text-analytics-and-tree-structures/actions/workflows/ci.yml/badge.svg)](https://github.com/anneliset47/text-analytics-and-tree-structures/actions/workflows/ci.yml)
[![Lint](https://github.com/anneliset47/text-analytics-and-tree-structures/actions/workflows/lint.yml/badge.svg)](https://github.com/anneliset47/text-analytics-and-tree-structures/actions/workflows/lint.yml)

This project showcases two core computer science skills in one reproducible workflow:

1. **Tree data structures** for hierarchical modeling and recursive traversal.
2. **Text analytics** over *Alice’s Adventures in Wonderland* (tokenization, frequencies, n-grams, and visualizations).

It is structured to be portfolio-friendly for recruiters and easy to run end-to-end from the command line.

## Why this project matters

- Demonstrates **algorithmic reasoning** (tree depth/height, n-gram construction).
- Demonstrates **data processing** with clean, script-based execution.
- Demonstrates **reproducibility** with pinned dependencies and deterministic outputs.
- Demonstrates **communication** with generated artifacts + report.

## Project structure

```text
text-analytics-and-tree-structures/
├── README.md
├── requirements.txt
├── Makefile
├── .gitignore
├── data/
│   ├── Alice In Wonderland.txt
│   └── DS Technical Book Link.pdf
├── figures/
├── notebooks/
│   ├── text_analytics_and_tree_structures.ipynb
│   └── text_analytics_and_tree_structures.py   # direct notebook code extraction
├── report/
│   ├── text_analytics_and_tree_structures_report.pdf
│   └── generated/                               # created by pipeline
└── src/
      └── text_analytics_and_tree_structures.py   # production-style CLI pipeline
```

## Quickstart

### 1) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
make install
```

### 3) Run the pipeline

```bash
make run
```

### 4) Run tests

```bash
make test
```

### 5) Run lint checks

```bash
make lint
```

This generates:

- **Figures** in `figures/`
   - `letter_frequency.png`
   - `top_words_wordcloud.png`
   - `top_bigrams_wordcloud.png`
   - `top_trigrams_wordcloud.png`
- **Tabular outputs** in `report/generated/`
   - `letter_frequency.csv`
   - `top_40_words.csv`
   - `top_20_bigrams.csv`
   - `top_20_trigrams.csv`
   - `table_of_contents.txt`

## Main implementation details

### Tree structure module

The `Node` model supports:

- adding child nodes,
- recursive table-of-contents rendering,
- chapter depth lookup,
- full tree height calculation.

### Text analytics module

The CLI pipeline:

- loads source text,
- normalizes and tokenizes content,
- removes stopwords,
- computes letter and token frequencies,
- computes bigrams and trigrams,
- saves both visual and CSV artifacts.

## Complexity (high level)

- Tree traversal: **O(n)**
- Letter counting: **O(n)**
- Token counting with hash maps: **O(n)** average
- N-gram creation: **O(n)**

## Notes for recruiters/reviewers

- The notebook remains available for exploratory review.
- The `src/` script provides a cleaner production-style interface for consistent execution.
- The generated artifacts are deterministic for the same input corpus.
- GitHub Actions runs tests automatically on pushes and pull requests to `main`.

## Quality gates

- **CI workflow**: runs the unit/smoke test suite across multiple Python versions.
- **Lint workflow**: runs `ruff` checks for import order, syntax quality, and style consistency.
- Together, these workflows provide fast feedback and protect `main` from regressions.

