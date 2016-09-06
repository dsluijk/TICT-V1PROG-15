# A
flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley'];
print(flowers)

# B
print(flowers.count('potato') > 0);

# C
thorny = [flowers[0], flowers[1], flowers[2]];
print(thorny);

# D
poisonous = [flowers[len(flowers) - 1]];
print(poisonous);

# E
dangerous = thorny + poisonous;
print(dangerous);
