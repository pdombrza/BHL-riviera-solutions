from itertools import permutations
from typing import Dict, Tuple


MAP = {
    ("A", "B"): 2,
    ("A", "D"): 3,
    ("B", "C"): 2,
    ("B", "E"): 4,
    ("C", "F"): 1,
    ("D", "E"): 5,
    ("E", "F"): 3,
    ("C", "G"): 3,
    ("F", "H"): 2,
    ("G", "H"): 1,
}


def get_permutations(zone_map: Dict[Tuple[str, str], int | float], start_element: str):
    items = [tup for tup in zone_map.keys()]
    items_flattened = list({item for subtup in items for item in subtup})
    perms = list(filter(lambda x: x[0] == start_element, permutations(items_flattened)))
    return perms


def main():
    print(get_permutations(MAP, "A"))


if __name__ == "__main__":
    main()
