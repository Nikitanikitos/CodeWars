class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.data = collection
        self.count_page = items_per_page
        self.collection = []
        self.create_pages(self.data, self.count_page)

    def create_pages(self, data, count_page):
        for i in range(0, len(data), count_page):
            self.collection += [data[i:i + count_page]]
        print(self.collection)

    def item_count(self):
        i = 0
        for page in self.collection:
            for item in page:
                i += 1
        return i

    def page_count(self):
        return len(self.collection)

    def page_item_count(self, page_index):
        if page_index <len(self.collection):
            return len(self.collection[page_index])
        return -1

    def page_index(self, item_index):
        i = 0
        for x, page in enumerate(self.collection):
            for item in page:
                if i == item_index: return x
                i += 1
        return -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f', 'qwer'], 4)
print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(1))
print(helper.page_index(4))
