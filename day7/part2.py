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

    def count_required_bags(self):
        s = 1
        for count, bag in self.subs:
            s += count * bag.count_required_bags()
        return s


# rules = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags."""
# Special treatment for our bag to make it easier to track
OWN_BAG = "shiny gold bag"
OWN_OBJECT = Bag("shiny gold bags contain 2 mirrored blue bags, 1 muted brown bag, 3 dim purple bags.")

with open("input") as f:
    rules = f.read().replace("shiny gold bags contain 2 mirrored blue bags, 1 muted brown bag, 3 dim purple bags.\n", "")


bags = [OWN_OBJECT]

for line in rules.splitlines():
    bags.append(Bag(line))

for bag in bags:
    bag.retrofit(bags)


# remove the gold bag
print(OWN_OBJECT.count_required_bags() - 1)

