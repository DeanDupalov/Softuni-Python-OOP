# class vowels: ## iterator
#     vowels = {'a', 'e', 'i', 'u', 'y', 'o'}
#     test: str
#
#     def __init__(self, text):
#         self.text = text
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.text):
#             raise StopIteration
#         idx = self.index
#         self.index += 1
#         if self.text[idx].lower() in self.vowels:
#             return self.text[idx]
#         else:
#             return self.__next__()

# def vowels(text): # generator func
#     vowels = {'a', 'e', 'i', 'u', 'y', 'o'}
#     for ch in text:
#         if ch.lower() in vowels:
#             yield ch

def vowels(text):  # generator comprehension
    vowels = {'a', 'e', 'i', 'u', 'y', 'o'}
    return (ch for ch in text if ch.lower() in vowels)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
