from typing import List, Tuple

class Bag:
    def __init__(self, rule:str):
        own, others = rule.split("contain")
        self.color = own[:-1].strip().replace("bags", "bag")
        self.subs = []
        for subtype in others.split(","):
            subtype:str = subtype.strip().replace(".", "")
            if subtype.startswith("no other"):
                break
            count = int(subtype.split()[0])
            self.subs.append((count, " ".join(subtype.split()[1:]).replace("bags", "bag")))
        #print(f"Created new bag with color {self.color}, with subtypes {self.subs}")

    def retrofit(self, others):
        old = self.subs
        self.subs = []
        for sub in old:
            # linear search in others
            for other in others:
                if other.color == sub[1]:
                    self.subs.append((sub[0], other))

    def __str__(self):
        return f"Bag {self.color}: {self.subs}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return other[1].color == self.color

    def find_child(self, other) -> bool:
        if other in self.subs:
            return True
        for child in self.subs:
            if child[1].find_child(other):
                return True
        return False


rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
OWN_BAG = "shiny gold bag"
OWN_OBJECT = Bag("shiny gold bags contain no other bags.")

with open("input") as f:
    rules = f.read()



bags = [OWN_OBJECT]

for line in rules.splitlines():
    bags.append(Bag(line))
    print(list(map(str, bags)))

for bag in bags:
    bag.retrofit(bags)

options = 0
for bag in bags:
    if bag.find_child(OWN_OBJECT):
        options += 1
print(options)
