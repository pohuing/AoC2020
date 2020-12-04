from math import prod


with open("input") as f:
    forest = f.read()
    
def traverse_forest(direction, forest):
    trees = 0
    x_dir, y_dir = direction
    x, y = [0,0]
    forest = forest.splitlines()
    depth = len(forest)
    width = len(forest[0])
    while y < depth-1:
        x += x_dir
        y += y_dir
        curr = forest[y][x%width]
        print(f"{(x,y)}: {curr}")
        if curr == "#":
            trees+=1
            print(f"Encountered tree at {(x,y)}")
    return trees

print(prod((traverse_forest(direction, forest) for direction in ((1,1), (3,1), (5,1), (7,1), (1,2)))))