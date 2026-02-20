from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import text_analytics_and_tree_structures as project  # noqa: E402


class TestTreeStructure(unittest.TestCase):
    def test_tree_depth_height_and_toc(self) -> None:
        toc = project.build_sample_toc()
        self.assertEqual(toc.depth_of("Metrics Design"), 1)
        self.assertEqual(toc.height(), 3)

        lines = toc.to_toc_lines()
        self.assertTrue(lines[0].startswith("Data Science: The Hard Parts"))
        self.assertTrue(
            any(
                "1. So What? Creating Value with Data Science" in line
                for line in lines
            )
        )


class TestTextAnalyticsHelpers(unittest.TestCase):
    def test_ngrams_counts(self) -> None:
        tokens = ["data", "science", "data", "science", "is", "fun"]
        bigrams = project.ngrams(tokens, n=2, top_n=5)
        self.assertEqual(bigrams.iloc[0]["2gram"], "data science")
        self.assertEqual(int(bigrams.iloc[0]["count"]), 2)


class TestPipelineSmoke(unittest.TestCase):
    def test_pipeline_generates_outputs(self) -> None:
        sample_text = (
            "Alice was beginning to get very tired of sitting by her sister on the bank. "
            "Alice said the book had no pictures. "
            "The rabbit ran close by her."
        )

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            text_path = tmp_path / "sample.txt"
            figures_dir = tmp_path / "figures"
            report_dir = tmp_path / "report"
            text_path.write_text(sample_text, encoding="utf-8")

            project.run_pipeline(
                text_path=text_path,
                figures_dir=figures_dir,
                report_dir=report_dir,
            )

            self.assertTrue((figures_dir / "letter_frequency.png").exists())
            self.assertTrue((figures_dir / "top_words_wordcloud.png").exists())
            self.assertTrue((report_dir / "letter_frequency.csv").exists())
            self.assertTrue((report_dir / "top_20_bigrams.csv").exists())
            self.assertTrue((report_dir / "table_of_contents.txt").exists())


if __name__ == "__main__":
    unittest.main()
