

name = str(input("Enter Your Name: "))
name_file = "name.txt"
open_file = open(name_file, 'w')

print(name, file=open_file)

open_file.close()

read_file = open(name_file, 'r')
print("Your name is {}".format(read_file.read()))
read_file.close()

numbers_file = "num"
open_num = open(numbers_file, 'r')
count = 0
for line in open_num.readline():
    count += int(line)
print(count)

open_num.close()
