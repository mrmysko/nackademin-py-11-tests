# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.
import sys


def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:

    # Recursion...complicated af

    # Create an empty list to store tuples.
    mod_list = []
    if not isinstance(tree, dict):
        sys.exit("Input is not a dict.")

    # Iterate over the dict.
    for key, value in tree.items():
        # Sets the current cordinate + the current key as the coordinate.
        # (variable,) sets a variable to a single-item tuple.
        coords = current_coord + (key,)
        # Check if the value is a nested dict.
        if isinstance(value, dict):
            # Recursion - Call on itself with the nested dict as argument, and key as cordinate.
            mod_list.extend(treecoords(value, coords))

        # If not, this is the end of the "chain", add the cordinates and value to the list.
        else:
            mod_list.append((coords, value))

    # Return a tuple with the total coordinates and the value.
    return tuple(mod_list)

    # .extend vs append - append adds entire tuple as a list item, expand "separates"
    # https://ioflood.com/blog/python-list-extend-method-usage-and-examples/

    #    mod_list.extend(treecoords(value, coords))
    #    mod_list2.append(treecoords(value, coords))
    #    print(mod_list[1])
    #    print(mod_list2[0][1])
    #    Same item

    # OK, what is the base case?...a single tuple with current_coords and the value
    # {'a': 1} - lowest case. This should return as ('a',), 1)


if __name__ == "__main__":
    pass
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
