import sys

# try:
#     print('Hello,', sys.argv[1])
# except IndexError:
#     print('Too Few Arguments.')

# if len(sys.argv) < 2:
#     sys.exit('Too Few Arguments.')
# if len(sys.argv) > 2:
#     sys.exit('Too Many Arguments.')

# print('Hello', sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too Few Arguments.")

for name in sys.argv[1:]:
    print("Hello, My name is", name)
