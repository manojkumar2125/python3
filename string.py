name = input("Enter the Name")

print(name == name[::-1])

count =0;
for i in range(len(name)):
    if('aeiou'.__contains__(name[i])):
        count += 1
print(count)

freq ={}
for char in name:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] =1
print(freq)


duplicate =set()
for char in name:
    if char is not duplicate:
        duplicate.add(char)
print(duplicate)
    