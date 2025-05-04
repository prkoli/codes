import os
os.listdir()
def mapper(review):
    review = review.lower()
    review = review.split()
    review = "".join(review)
    return review

def reduce(review):
    char_count = {}
    for char in review:
        char_count[char] = review.count(char)
    return char_count
def map_reduce(file_name):
    with open(file_name, "r") as file:
        review = file.read()
    mapped = mapper(review)
    reduced = reduce(mapped)
    
    for char, count in reduced.items():
        print(f"char:{char} -> count:{count}")

map_reduce("ssd.txt")



def mapper(review):
    review = review.strip()
    review = review.lower()
    review = re.findall("[a-z]+", review)
    return review

def reduce(review):
    word_count = {}
    for word in review:
        word_count[word] = review.count(word)
    return word_count

def map_reduce(file_name):
    with open(file_name, "r") as file:
        review = file.read()
        
    mapped = mapper(review)
    reduced = reduce(mapped)
    
    for word, count in reduced.items():
        print(f"word:{word} -> count:{count}")

map_reduce("ssd.txt")
