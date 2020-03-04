def scramble(s1, s2):
    for char in set(s2):
        if s2.count(char) > s1.count(char):
            return False
    return True

print(scramble('ocwiewozvzsqbhuw', 'zqwosizhcoeuwbvw'))
