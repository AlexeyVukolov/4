import pprint


class h_map:

    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self.sey_buckets(elements)

    def sey_buckets(self, elements):
        for key, data in elements:
            hashed_data = hash(key)
            index = hashed_data % self.bucket_size
            self.buckets[index].append((key, data))

    def give_value(self, key):
        hashed_data = hash(key)
        index = hashed_data % self.bucket_size
        bucket = self.buckets[index]
        for num, data in bucket:
            if num == key:
                return (data)
        return None

    def __str__(self):
        return pprint.pformat(self.buckets)