arr = [[], [], [], [], []] # the 5 empty buckets

def custom_hash(text): # will not override (hash)

    lower_text = text.lower()

    # sum of character indices
    reference = "abcdefghijklmnopqrstuvwxyz"
    numerical_value = 0
    for letter in lower_text:
        numerical_value += reference.index(letter)

    # modulo 5 to determine the bucket
    return numerical_value % 5
    
def insert(arr, key, value):

    bucket_index = custom_hash(key)

    # insert add the end of the desired bucket
    arr[bucket_index].append((key,value))

def find(arr, key):

    bucket_index = custom_hash(key)

    for tup in arr[bucket_index]:
        if tup[0] == key:
            return tup[1]
    
    return None