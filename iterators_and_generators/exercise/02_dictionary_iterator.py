class dictionary_iter:

    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.keys = list(dict_obj)
        self.key_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.key_idx == len(self.keys):
            raise StopIteration
        key = self.keys[self.key_idx]
        value = self.dict_obj[key]
        self.key_idx += 1
        return (key, value)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
