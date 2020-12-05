def find_seat_row(boarding) -> (int,int):
    boarding = boarding.strip()
    r_upper, r_lower = 127, 0
    c_upper, c_lower = 7,0

    factor = 128
    for i in range(0,7):
        factor//=2
        if boarding[i] == "F":
            r_upper -= factor
        elif boarding[i] == "B":
            r_lower += factor
        print(f"row: l{r_lower} u{r_upper} column: l{c_lower} u{c_upper}")

    factor = 8
    for i in range(7,10):
        factor //=2
        if boarding[i] == "L":
            c_upper -= factor
        elif boarding[i] == "R":
            c_lower += factor
        print(f"row: l{r_lower} u{r_upper} column: l{c_lower} u{c_upper}")
    return(r_lower, c_lower)


def seat_id(seat_tuple: (int,int)) -> int:
    row, column = seat_tuple
    return row * 8 + column


def test():
    tickets = """BFFFBBFRRR
    FFFBBBFRRR
    BBFFBBFRLL
    """.split("\n")
    tup = find_seat_row(tickets[0])
    id = seat_id(tup)
    assert tup == (70, 7)
    assert id == 567

    tup = find_seat_row(tickets[1])
    id = seat_id(tup)
    assert tup == (14, 7)
    assert id == 119

    tup = find_seat_row(tickets[2])
    id = seat_id(tup)
    assert tup == (102, 4)
    assert id == 820


test()

with open("input") as f:
    tickets = f.read().split("\n")

positions = map(find_seat_row, tickets)
ids = list(map(seat_id, positions))
print(zip(positions, ids))
print(max(ids))

#myseat
ids = sorted(ids)

#This is actually kind of wrong and has false positives
for i in range(len(ids) - 2):
    if ids[i + 2] != ids[i] + 2:
        print(f"found slot i{i}, id{ids[i] + 1}")