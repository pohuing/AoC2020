from typing import List, Set


def part1():
    counts = []
    with open("input") as f:
        groups = f.read().split("\n\n")
        for group in groups:
            group.replace("\n", "")
            group = [letter.lower() for letter in group if letter.isalpha()]
            unique = set(group)
            count = len(unique)
            counts.append(count)
            print(count)
    print(sum(counts))

def part2():
    counts: List[int] = []
    with open("input") as f:
        groups: List[str] = f.read().split("\n\n")
        for group in groups:
            group = group.strip()
            people = group.split("\n")
            base: Set[str] = set("abcdefghijklmnopqrstuvwxyz")
            for person in people:
                base &= set(person)
            count = len(base)
            counts.append(count)
            print(count)

    print(sum(counts))
