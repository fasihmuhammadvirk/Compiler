
# Calculate the FIRST sets for the grammar
def first(grammar):
    first_sets = {}
    for lhs, rhs in grammar:
        first_sets[lhs] = set()
        for symbol in rhs:
            if symbol.isupper():
                first_sets[lhs].update(first_sets[symbol])
            else:
                first_sets[lhs].add(symbol)
    return first_sets


# Calculate the FOLLOW sets for the grammar
def follow(grammar, first_sets):
    follow_sets = {}
    for lhs, rhs in grammar:
        follow_sets[lhs] = set()
        for i, symbol in enumerate(rhs):
            if symbol.isupper():
                follow_sets[symbol].update(follow_sets[lhs])
                if "EPSILON" not in first_sets[symbol]:
                    break
            else:
                follow_sets[symbol] = set(symbol)
                break
    return follow_sets



def create_parse_table(grammar, first, follow):
    parse_table = {}
    for lhs, rhs in grammar:
        parse_table[lhs] = {}
        for symbol in follow[lhs]:
            if symbol in first[rhs[0]]:
                parse_table[lhs][symbol] = rhs
            else:
                parse_table[lhs][symbol] = "EPSILON"
    return parse_table

# Example usage
grammar = [("E", "iE"), ("F", "id")]
first_sets = first(grammar)
follow_sets = follow(grammar, first_sets)
print("")
print(f'First Set {first_sets}\nFollow Set {follow_sets}')
parse_table = create_parse_table(grammar, first_sets, follow_sets)
print("\nParse Table")
print(parse_table)
