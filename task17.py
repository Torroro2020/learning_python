genome = input().lower()
print(((genome.count('c') + genome.count('g')) / len(genome)) * 100)

