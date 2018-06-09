#!/usr/bin/env python
import argparse

from server import Server
from shard import Shard
from distributedDb import DistributedDataBase
from dataSimulator import DataLossSimulator

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="number of virtual servers", type=int)
    parser.add_argument("-r", "--random", action="store_true", help="random mode")
    parser.add_argument("-m", "--mirror", action="store_true", help="mirror mode")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    n = args.n
    servers_obj_list = [Server(chr(65 + x), n) for x in range(0, n)]
    distributed_db = DistributedDataBase(servers_obj_list)

    shards_obj = (Shard(str(i)) for i in range(1, (n * n) // 2 + 1))

    for shard in shards_obj:
        if args.random:
            distributed_db.add_random_data(shard)
        elif args.mirror:
            distributed_db.add_mirror_data(shard)

    dataloss = DataLossSimulator(servers_obj_list)
    print('Killing 2 arbitrary servers results in data loss in {}% cases'\
          .format(dataloss.probability*100))

if __name__ == '__main__':
    main()
