from itertools import permutations, product
from typing import Dict, Tuple, List


class ZoneInfo:
    def __init__(self, name: str, neighbours: list):
        self.name = name
        self.neighbours = neighbours


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

ORDER = ["A", "G", "C", "D"]

prioA = ["a", "c", "h"]
prioB = ["g", "h", "c", "d"]
prioC = ["b", "e"]


def get_individual_zone_names(zone_map: Dict[Tuple[str, str], int | float]):
    items = [tup for tup in zone_map.keys()]
    zone_names = list({item for subtup in items for item in subtup})
    return zone_names


def get_permutations(zone_names, start_element: str):
    perms = list(filter(lambda x: x[0] == start_element, permutations(zone_names)))
    return perms


def create_zone_classes(zone_names, map: dict):
    zone_classes = [ZoneInfo(name, []) for name in zone_names]
    for zone in zone_classes:
        for connection in map.keys():
            if zone.name == connection[0]:
                zone.neighbours.append(connection[1])
            if zone.name == connection[1]:
                zone.neighbours.append(connection[0])
    return zone_classes


def get_neighbours_dict(zone_classes):
    return {zone.name: zone.neighbours for zone in zone_classes}


def main():
    zone_names = get_individual_zone_names(MAP)
    perms = get_permutations(zone_names, "A")
    zones = create_zone_classes(zone_names, MAP)
    neighbours_dict = get_neighbours_dict(zones)
    print(neighbours_dict)
    possible_paths = []
    for perm in perms:
        for i, z_name in enumerate(perm):
            try:
                if perm[i + 1] in neighbours_dict[z_name]:
                    continue
                else:
                    break
            except IndexError:
                possible_paths.append(perm)
    print(possible_paths)
    # print(neighbours_dict)


if __name__ == "__main__":
    main()
