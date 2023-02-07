def eliminate_left_factoring(productions):
    # Step 1: Identify left factored productions
    left_factored = []
    for production in productions:
        expansions = production[1].split("|")
        # Check if any two alternatives have a common prefix
        for i, a1 in enumerate(expansions[:-1]):
            for a2 in expansions[i+1:]:
                common_prefix = ""
                for j, c in enumerate(a1):
                    if c != a2[j]:
                        break
                    common_prefix += c
                if len(common_prefix) > 0:
                    left_factored.append(production)
                    break

    # Step 2: Replace left factored productions with new productions
    for production in left_factored:
        common_prefix = ""
        alternatives = production[1].split("|")
        for i, c in enumerate(alternatives[0]):
            if all(a[i] == c for a in alternatives):
                common_prefix += c
            else:
                break
        
        # Add new productions for each alternative
        new_productions = []
        for alternative in alternatives:
            new_nt = f"{alternative}'"
            new_productions.append((production[0], f"{common_prefix}{new_nt}"))
            new_productions.append((new_nt, alternative[len(common_prefix):]))

        # Step 3: Add new productions
        productions += new_productions

    # Step 4: Remove original left factored productions
    productions = [p for p in productions if p not in left_factored]

    return productions


# Example input: a list of productions in the form of tuples (non_terminal, expansion)
productions = [
    ("S", "aAbBcC|aAbBcD|aEbBcC|aEbBcD"),
    ("A", "d|e"),
    ("E", "f|g"),
]

# Eliminate left factoring
eliminated_productions = eliminate_left_factoring(productions)

# Output: a list of productions with left factoring eliminated
print(eliminated_productions)
