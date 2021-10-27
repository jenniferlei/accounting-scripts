"""Print out all the melons in our inventory."""


from melons import melons


def print_melons(melon_dict):
    """Print each melon with corresponding attribute information."""

    for melon, attributes in melons.items():
        print(melon.upper())
        for attribute, attribute_value in attributes.items():
            print(f"\t{attribute}: {attribute_value}")

print_melons(melons)
