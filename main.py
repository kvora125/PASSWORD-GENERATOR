import random


def generator(wrds):
    min_len = 8
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    combined_list = digits + uppercase_chars + lowercase_chars + symbols
    temp = [random.choice(digits), random.choice(combined_list), random.choice(uppercase_chars),
            random.choice(combined_list), random.choice(lowercase_chars), random.choice(combined_list),
            random.choice(symbols), random.choice(combined_list)]
    random.shuffle(temp)
    pwd = "".join(temp)
    if len(wrds) > 0:
        pwd = random.choice(wrds) + pwd + random.choice(wrds)
    return pwd


if __name__ == "__main__":
    keywords = []
    keywords = input("Enter keywords and separate by spaces else press enter to continue without keywords: ").split()
    print(generator(keywords))