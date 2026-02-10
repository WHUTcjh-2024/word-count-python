from collections import Counter
import re
from typing import Iterator

def read_lines(path: str) -> Iterator[str]:
    """Read a text file line by line (generator)."""
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')

def tokenize(line: str):
    """Simple tokenizer: keep alphanumerics, lowercase."""
    return re.findall(r"\b\w+\b", line.lower())

def word_count(path: str) -> Counter:
    """Count word frequencies in a text file."""
    cnt = Counter()
    for line in read_lines(path):
        cnt.update(tokenize(line))
    return cnt
