#!/usr/bin/env python3

import numpy as np
import time

max = 100000000 # 100K
nbrlist = [i for i in range(1, max)]
vector = np.arange(1, max)

start_time = time.time()
for nbr in nbrlist:
	nbr / 10
print(f"list time: {time.time() - start_time}")

start_time = time.time()
vector / 10
print(f"vector time: {time.time() - start_time}")