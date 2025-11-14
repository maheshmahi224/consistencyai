# print characters present at an even index number
# accept input string from a user
word = input("enter word :")
print("original string : ",word)

#get the length of a string
size = len(word)
# iterate a each character of a string
# start:0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0,2,4
print("printing only even index chars")
for i in range(0,size-1,2):
    print("index[",i,"]",word[i])



# accept input string from a user
word = input("enter word :")
print("original string : ",word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)
