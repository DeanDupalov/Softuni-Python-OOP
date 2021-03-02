from typing import Optional, List


class PhotoAlbum:
    MAX_SIZE_PAGE = 4
    pages: int

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.get_photos_matrix(pages)

    @staticmethod
    def get_photos_matrix(pages) -> List[List]:
        return [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> Optional['PhotoAlbum']:
        return cls(photos_count // 4)

    def add_photo(self, label: str) -> str:

        for i in range(0, len(self.photos)):
            if len(self.photos[i]) < PhotoAlbum.MAX_SIZE_PAGE:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

        return "No more free spots"

    def display(self):
        result = ''
        for row in self.photos:
            result += '-' * 11 + '\n'
            for index in range(len(row)):
                if index == len(row) - 1:
                    result += '[]'
                else:
                    result += '[] '
            result += '\n'
        result += '-' * 11 + '\n'
        return result



album = PhotoAlbum.from_photos_count(12)
print(album.pages)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))

# print(album.display())
