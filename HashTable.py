"""
    IMPLEMENTING A HASHTABLE FROM SCRATCH
"""

# creating a class
class HASHTABLE:
    def __init__(self, size):
        self.size = size
        self.hashtable = self.create_buckets() # the main object of this class

    # create an empty list of buckets
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # insert an element into the hash map
    def set_value(self, key, value):
        # here we use the hash function to get the index for the given key
        hashed_key = hash(key) % self.size

        # get the bucket corresponding to that index
        bucket = self.hashtable[hashed_key]

        found_key = False # initializing the found flag
        for idx, record in enumerate(bucket): 
            record_key, record_value = record

            # here we check if the recorded key is same as the 'key' argument
            if record_key == key:
                found_key = True
                break

            """
            If the key wasn't found, then we update the bucket with this new key or 
            if the key was found we just update its value with the new value.
            """
            
            if found_key:
                bucket[idx] = (key, value)
            else:
                bucket.append(key, value)
        
        # get a particular value for the key
        def get_value(self, key):

            # use the hash function to get the index
            hashed_key = hash(key) % self.size

            # Get the bucket corresponding to index
            bucket = self.hashtable(hashed_key)

            # find the key
            found_key = False # initializing the found flag
            for idx, record in enumerate(bucket): 
                record_key, record_value = record

                # here we check if the recorded key is same as the 'key' argument
                if record_key == key:
                    found_key = True
                    break

                if found_key:
                    return record_value

                else:
                    return "No such key and value"

        def delete_value(self, key):
            # use the hash function to get the index
            hashed_key = hash(key) % self.size

            # Get the bucket corresponding to index
            bucket = self.hashtable(hashed_key)

            # find the key
            found_key = False # initializing the found flag
            for idx, record in enumerate(bucket): 
                record_key, record_value = record

                # here we check if the recorded key is same as the 'key' argument
                if record_key == key:
                    found_key = True
                    break

                if found_key:
                    bucket.pop(index)
                return

        # to print the elements of the hash map
        def __str__(self):
            print(" ".join(str(item)) for item in self.hashtable)

            


    