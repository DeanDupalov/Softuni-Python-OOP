from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def get_category(self, category_id):
        return [category for category in self.categories if category.id == category_id][0]

    def get_topic(self, topic_id):
        return [topic for topic in self.topics if topic.id == topic_id][0]

    def get_document(self, document_id):
        return [document for document in self.documents if document.id == document_id][0]

    def edit_category(self, category_id: int, new_name: str):
        category = self.get_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic: str, new_storage_folder: str):
        topic = self.get_topic(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_document(document_id)
        self.documents.remove(document)

    def __repr__(self):
        result = []
        for doc in self.documents:
            result.append(doc)
        return '\n'.join(map(str, result))


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")

# d1.add_tag("urgent")
# d1.add_tag("work")
# d3 = Document.from_instance(10, c1, t1, 'test')
# print(d3)
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
