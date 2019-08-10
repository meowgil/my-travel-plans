def start_K(string):
    if string[0]=="K":
        print("True")
    else:
        print("False")

start_K("Kelly")
start_K("String")

word = "happy"
for num in range(len(word)):
    print(num, word[num])

def word_triangle(string):
    for n in range(len(string)):
        end = len(string)-n
        print(string[0:end])

word_triangle("Kitty")


def middle(a,b,c):
    if b>=a>=c or c>=a>=b:
        return a
    if a>=b>=c or c>=b>=a:
        return b
    if a>=c>=b or b>=c>=a:
        return c



print(True and False)
print(True and True)
print(True or False)
print(False or False)

def good_length(s):
    if len(s)<8:
        return False
    elif len(s)>64:
        return False
    else:
        return True

print(good_length("2short"))
print(good_length("nice length perfect"))
print(good_length("toooooooooooooooooooooooooooooooooooooooooloooooooooooooooooooooooooooooooooooooooooooooooong"))



def total_length(list):
    total = 0
    for chars in list:
        total = total + len(chars)
    return total

print(total_length(["number","mud"]))

def until_dot(sentence):
    counter = 0
    while counter < len(sentence)-1 and sentence[counter] != '.':
        counter += 1
    print(sentence[:counter])


until_dot("meowmeow.wolfwolf")

def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                 break   # does not do what we want!
    return f"{x} * {y} == 512"

print(find_512())


def start_with(long,short):
    if short == long[:len(short)]:
        return True
    else:
        return False


print(start_with("strawberry","straw"))

def starts_with_v1(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True


def starts_with_v2(long, short):
    length = len(short)
    beginning = long[0 : length]
    if beginning == short:
        return True
    else:
        return False

def starts_with_v3(long, short):
    return long[0:len(short)] == short


starts_with_v2("tin", "tinkerbell")
starts_with_v3("tin", "tinkerbell")


def count_substring_v1(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
        index += 1    # <- look here
    return count

def count_substring_v2(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
            index += len(target)   # <- look here
        else:
            index += 1
    return count

print(count_substring_v1('AAAA','AA'))
print(count_substring_v2('AAAA','AA'))

def locate_first(string, sub): 
    index = 0
    while index < (len(string) - len(sub) + 1):
        if long[index : index + len(sub)] == sub:
            return index
        index += 1
    return -1

def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string) - len(sub) + 1:
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches

def breakify(strings):
    return "<br>".join(strings)

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

breakify(lines)

truth = "beauty"
index = 0
letters = []
while index < len(truth):
    letters.append(truth[index])
    index += 2

letters = '-'.join(letters)
print(letters)
