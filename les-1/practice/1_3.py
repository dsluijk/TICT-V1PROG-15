# Variable declaration
str1 = 'Supercalifragilisticexpialidocious';
str2 = 'Antidisestablishmentarianism';
str3 = 'Honorificabilitudinitatibus';
list1 = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'];
sortedList = [];

# A
print(len(str1));

# B
print(str1.count('ice') > 0);

# C
print(len(str2) > len(str3));

# D
sortedList = sorted(list1);
print('First: ' + sortedList[0] + '. Last: ' + sortedList[len(sortedList) - 1] + '.');
