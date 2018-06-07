import random
class DistributedDataBase:
    def __init__(self,server_list):
        self.server_list = server_list
        self.full_servers_set = set()

    def depart_last_replica(self):
        """run when random doesn't work correct
        and impossibility add data to the last server"""
        depart_server_one = list(set(self.server_list)-self.full_servers_set)[0]

        for server in list(self.full_servers_set):
            if server.data[0] not in depart_server_one.data:
                server.data[0],depart_server_one.data[-1] = depart_server_one.data[-1], server.data[0]

    def add_random_data(self,shard):
        for _ in range(2):
            while True:
                random_server = random.choice(self.server_list)
                if random_server.is_not_full_server():
                    if shard not in random_server.data:
                        random_server.add_data(shard)
                        if random_server.is_not_full_server() != True:
                            self.full_servers_set.add(random_server)
                        break

                if len(self.full_servers_set) == len(self.server_list) - 1:
                    self.depart_last_replica()

    def add_mirror_data(self,shard):
        for odd_serv, even_serv in zip(self.server_list[0::2], self.server_list[1::2]):
            if odd_serv.is_not_full_server():
                odd_serv.add_data(shard)
                even_serv.add_data(shard)
                break
