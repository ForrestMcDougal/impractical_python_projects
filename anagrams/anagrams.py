import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

anagram_list = []

name = input('Imput a SINGLE word or Single name to find its anagram(s): ')
name = name.lower()

name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

print()
if len(anagram_list) == 0:
    print('No anagrams found')
else:
    print("Anagrams =", *anagram_list, sep="\n")
