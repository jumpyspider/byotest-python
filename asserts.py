def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("Aa") == 1, "One upper case, one lower case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("aA") == 1, "One lower case, one upper case"
assert count_upper_case("A$") == 1, "One upper case, one special character"
assert count_upper_case("£$%%^") == 0, "Special characters"

print("All the tests passed")