#Atharv Tamrakar

print("Enter the String: ")
str = input()

old_word_list = str.split()
new_word_list = []
j = 0

for i in range(len(old_word_list)):
    if old_word_list[i] not in new_word_list:
        new_word_list.insert(j, old_word_list[i])
        j = j+1

new_str = ""
for i in range(len(new_word_list)):
    new_str = new_str + new_word_list[i] + " "

print("\nNew String =", new_str)