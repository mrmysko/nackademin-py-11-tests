#!/usr/bin/env python

# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.


def stringt(*args, end="\n", sep=" ") -> str:
    """Concatenate a list and return it as a string."""

    # Creates strings from lists and ints from args and appends them to mod_list.
    mod_list = [str(i) for i in args]

    # Joins items in mod_list with sep as separator, concats end at the end.
    return str(sep).join(mod_list) + str(end)

    # return sep.join([str(i) for i in args]) + end  # One-line


if __name__ == "__main__":
    pass
