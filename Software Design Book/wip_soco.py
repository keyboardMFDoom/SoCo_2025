import sys
import os

file_path = 'C:\\Users\\arsen\\Git_repositories\\SoCo_2025\\Software Design Book'
file_name = os.listdir(file_path)
filenames = [i for i in file_name if i[:4] == "text"]

def same_bytes(left_name, right_name):
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes


def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            print(i_left,i_right)
            if same_bytes(left, right):
                matches.append((left, right))
    return matches


if __name__ == "__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)

trial = find_duplicates(filenames)
print(trial)


def naive_hash(data):
    return sum(data) % 13

example = bytes("hashing", "utf-8")
for i in range(1, len(example) + 1):
    substring = example[:i]
    hash = naive_hash(substring)
    print(f"{hash:2} {substring}")

rs = ["str "+str(i) for i in range(20)]

for j in rs:
    substring= bytes(j, "utf-8")
    hash = naive_hash(substring)
    print(f"{hash:2} {substring}")

