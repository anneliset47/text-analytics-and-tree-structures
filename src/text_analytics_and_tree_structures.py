from __future__ import annotations

import argparse
import re
import string
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import STOPWORDS, WordCloud


@dataclass
class Node:
    title: str
    children: list["Node"] = field(default_factory=list)

    def add_child(self, title: str) -> "Node":
        node = Node(title=title)
        self.children.append(node)
        return node

    def depth_of(self, target_title: str, current_depth: int = 0) -> int | None:
        if self.title == target_title:
            return current_depth
        for child in self.children:
            depth = child.depth_of(target_title, current_depth + 1)
            if depth is not None:
                return depth
        return None

    def height(self) -> int:
        if not self.children:
            return 0
        return 1 + max(child.height() for child in self.children)

    def to_toc_lines(self, level: int = 0, chapter_num: str = "") -> list[str]:
        indent = "  " * level
        prefix = f"{chapter_num}. " if chapter_num else ""
        lines = [f"{indent}{prefix}{self.title}"]
        for idx, child in enumerate(self.children, start=1):
            child_num = f"{chapter_num}.{idx}" if chapter_num else str(idx)
            lines.extend(child.to_toc_lines(level + 1, child_num))
        return lines


def build_sample_toc() -> Node:
    book = Node("Data Science: The Hard Parts")

    chapter_1 = book.add_child("So What? Creating Value with Data Science")
    chapter_2 = book.add_child("Metrics Design")
    chapter_3 = book.add_child("Growth Decompositions")

    chapter_1.add_child("What Is Value?")
    chapter_1.add_child("Understanding the Business")
    chapter_1.add_child("Measuring Value")

    metrics = chapter_2.add_child("Desirable Properties of Metrics")
    metrics.add_child("Measurable")
    metrics.add_child("Actionable")
    metrics.add_child("Relevant")

    chapter_3.add_child("Additive Decomposition")
    chapter_3.add_child("Multiplicative Decomposition")
    return book


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def normalize_text(text: str) -> str:
    lowered = text.lower()
    table = str.maketrans("", "", string.punctuation + "“”‘’—…")
    return lowered.translate(table)


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z]+", text.lower())


def filter_stopwords(tokens: Iterable[str]) -> list[str]:
    stopwords = set(STOPWORDS)
    stopwords.update({"alice", "said", "would", "could", "one"})
    return [token for token in tokens if token not in stopwords]


def letter_frequency(text: str) -> pd.DataFrame:
    counts = Counter(ch for ch in text if ch.isalpha())
    rows = [
        {"letter": chr(code), "count": counts.get(chr(code), 0)}
        for code in range(ord("a"), ord("z") + 1)
    ]
    return pd.DataFrame(rows)


def top_words(tokens: list[str], top_n: int = 40) -> pd.DataFrame:
    counts = Counter(tokens)
    return pd.DataFrame(counts.most_common(top_n), columns=["token", "count"])


def ngrams(tokens: list[str], n: int, top_n: int = 20) -> pd.DataFrame:
    grams = Counter(tuple(tokens[idx : idx + n]) for idx in range(len(tokens) - n + 1))
    data = [(" ".join(gram), count) for gram, count in grams.most_common(top_n)]
    return pd.DataFrame(data, columns=[f"{n}gram", "count"])


def save_letter_chart(df: pd.DataFrame, out_path: Path) -> None:
    plt.figure(figsize=(12, 5))
    plt.bar(df["letter"], df["count"])
    plt.title("Letter Frequency (a-z)")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=200)
    plt.close()


def save_wordcloud_from_frame(
    df: pd.DataFrame,
    token_col: str,
    count_col: str,
    out_path: Path,
    title: str,
) -> None:
    frequencies = dict(zip(df[token_col], df[count_col]))
    cloud = WordCloud(
        width=1400,
        height=700,
        background_color="white",
    ).generate_from_frequencies(frequencies)
    plt.figure(figsize=(12, 6))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=200)
    plt.close()


def run_pipeline(text_path: Path, figures_dir: Path, report_dir: Path) -> None:
    raw = load_text(text_path)
    normalized = normalize_text(raw)
    tokens = tokenize(normalized)
    clean_tokens = filter_stopwords(tokens)

    letters = letter_frequency(normalized)
    words = top_words(clean_tokens, top_n=40)
    bigrams = ngrams(clean_tokens, n=2, top_n=20)
    trigrams = ngrams(clean_tokens, n=3, top_n=20)

    figures_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    save_letter_chart(letters, figures_dir / "letter_frequency.png")
    save_wordcloud_from_frame(
        words,
        "token",
        "count",
        figures_dir / "top_words_wordcloud.png",
        "Top 40 Words",
    )
    save_wordcloud_from_frame(
        bigrams,
        "2gram",
        "count",
        figures_dir / "top_bigrams_wordcloud.png",
        "Top 20 Bigrams",
    )
    save_wordcloud_from_frame(
        trigrams,
        "3gram",
        "count",
        figures_dir / "top_trigrams_wordcloud.png",
        "Top 20 Trigrams",
    )

    letters.to_csv(report_dir / "letter_frequency.csv", index=False)
    words.to_csv(report_dir / "top_40_words.csv", index=False)
    bigrams.to_csv(report_dir / "top_20_bigrams.csv", index=False)
    trigrams.to_csv(report_dir / "top_20_trigrams.csv", index=False)

    toc = build_sample_toc()
    toc_path = report_dir / "table_of_contents.txt"
    toc_path.write_text("\n".join(toc.to_toc_lines()) + "\n", encoding="utf-8")

    print("Pipeline complete.")
    print(f"- Text input: {text_path}")
    print(f"- Figures: {figures_dir}")
    print(f"- Reports: {report_dir}")
    print(f"- Sample depth ('Metrics Design'): {toc.depth_of('Metrics Design')}")
    print(f"- Tree height: {toc.height()}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Text analytics and tree structure pipeline.")
    parser.add_argument(
        "--text",
        type=Path,
        default=Path("data") / "Alice In Wonderland.txt",
        help="Path to source text file.",
    )
    parser.add_argument(
        "--figures-dir",
        type=Path,
        default=Path("figures"),
        help="Directory for generated charts and word clouds.",
    )
    parser.add_argument(
        "--report-dir",
        type=Path,
        default=Path("report") / "generated",
        help="Directory for generated CSV outputs and TOC text.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_pipeline(args.text, args.figures_dir, args.report_dir)


if __name__ == "__main__":
    main()
