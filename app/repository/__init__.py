class Repository(object):
    def __init__(self, adapter=None):
        self.client = adapter()

    def find_all(self, selector):
        return self.client.find_all(selector)

    def find(self, selector):
        return self.client.find(selector)

    def create(self, shop):
        return self.client.create(shop)

    def update(self, selector, shop):
        return self.client.update(selector, shop)

    def delete(self, selector):
        return self.client.delete(selector)
