import argparse
import os
import sys
from typing import Dict, List

language_file_extensions: Dict[str, str] = {"python": "py", "go": "go"}

assert "python" in language_file_extensions

parser = argparse.ArgumentParser(
    description="Create subdirectory scaffolding for Advent of Code."
)

parser.add_argument(
    "day",
    type=int,
    choices=range(1, 26),
    help="the day you want to generate the subdirectory for; int in range [1, 25]",
)
parser.add_argument(
    "-l",
    "--language",
    type=str,
    default="python",
    choices=language_file_extensions.keys(),
    help="the programming language to be used; default is Python",
)

args = parser.parse_args()
print(args)

day_str: str = str(args.day).rjust(2, "0")
day_directory: str = f"day{day_str}"

if os.path.exists(day_directory):
    print(f"{day_directory} already exists; quitting")
    sys.exit(1)

os.mkdir(day_directory)

extension: str = language_file_extensions[args.language]
files_to_be_created: List[str] = [
    "input.txt",
    "sample.txt",
    f"day{day_str}_problem.txt",
    f"day{day_str}p1.{extension}",
    f"day{day_str}p2.{extension}",
]
for file in files_to_be_created:
    open(f"{day_directory}/{file}", "a").close()
