from dataclasses import dataclass
from io import TextIOBase
from typing import Any, Dict, Iterable, List, Tuple


def parse_single_iftop_log(f: TextIOBase):
    """
    parse single file
    """

    lines: List[str] = iter(f.readlines()[4:])

    htop_cols = ("#", "host/name", "direction", "2s", "10s", "40s", "cumulative")

    res = []

    def key_line(line: str) -> Dict[str, Any]:
        if "=>" in line:
            cols = htop_cols
        else:
            cols = htop_cols[1:]

        values = line.split()
        return dict(zip(cols, values))

    for line in lines:
        if line.startswith("---"):
            break
        else:
            res.append(key_line(line))

    return res


if __name__ == "__main__":
    with open("example.log") as f:
        res = parse_single_iftop_log(f)
        print(res)
