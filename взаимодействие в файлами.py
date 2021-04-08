# file = open('data.txt')
# read = file.read()
# print(file.readline())

# with open('data.txt') as file:
#     lines = file.readlines()
#     print(len(lines))
#     lines_ = []
#     for line in lines:
#         lines_.append(line.strip())
#     print(lines_)

# with open('data.txt', 'w') as file:
#     file.write('Hello World')

with open('data.txt', 'a') as file:
    file.write('\nSpider-man')

