class Server:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.data = []

    def is_not_full_server(self):
        if len(self.data) < self.size:
            return True

    def add_data(self, shard_name):
        self.data.append(shard_name)

    def __repr__(self):
        return self.name