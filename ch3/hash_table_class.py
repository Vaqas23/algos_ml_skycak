class HashTable:

    def __init__(self, num_buckets):

        self.buckets = []

        for i in range(num_buckets):
            self.buckets.append([])
    
    def hash(self, text):

        lower_text = text.lower()

        # sum of character indices
        reference = "abcdefghijklmnopqrstuvwxyz"
        numerical_value = 0
        for letter in lower_text:
            numerical_value += reference.index(letter)

        # modulo 5 to determine the bucket
        return numerical_value % len(self.buckets)

    def insert(self, key, value):

        bucket_index = self.hash(key)

        # insert add the end of the desired bucket
        self.buckets[bucket_index].append((key,value))

    def find(self, key):

        bucket_index = self.hash(key)

        for tup in self.buckets[bucket_index]:
            if tup[0] == key:
                return tup[1]
        
        return None
    