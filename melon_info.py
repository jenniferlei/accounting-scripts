"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices


def melon_dict(names, seedless, prices):
    '''convert current melon data into dictionary'''
    melon_dict = {}
    for key in melon_names:
        melon_dict[names[key]] = {'price': prices[key], 'seedless': seedless[key]}
    return melon_dict

melon_dict = melon_dict(melon_names, melon_seedlessness, melon_prices)
print(melon_dict)

def add_attribute_to_dict(current_dict, new_attributes):
    '''adds new list of attributes with values None to an existing dictionary for each key'''
    for each_item in current_dict:
        for attribute in new_attributes:
            current_dict[each_item][attribute] = None
    return current_dict

new_attr = ['flesh_color', 'rind_color', 'weight']
new_melon_dict = add_attribute_to_dict(melon_dict, new_attr)
print(new_melon_dict)


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
