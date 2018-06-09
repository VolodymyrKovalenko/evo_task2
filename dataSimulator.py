import random
class DataLossSimulator:
    def __init__(self,server_list):
        self.server_list = server_list

    @property
    def probability(self):
        data_matches_list = list()
        select_server = random.choice(self.server_list)
        for element in select_server.data:
            for server in self.server_list:
                if element in server.data:
                    data_matches_list.append(server)
                    break
        probability = len(set(data_matches_list)) / float(len(self.server_list) - 1)
        return probability