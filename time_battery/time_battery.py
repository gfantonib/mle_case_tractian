#!/usr/bin/env python3

import pandas as pd
from models import draft, optmized_draft

df = pd.read_csv("../data/collects.csv")

i = 0
draft_time = 0
optmized_draft_time = 0
while (i < 10):
	optmized_draft_time += optmized_draft(df)
	draft_time += draft(df)
	i += 1

draft_elapsed_time_mean = draft_time / (i + 1)
optmized_draft_elapsed_time_mean = optmized_draft_time / (i + 1)

print(f"\nDraft elapsed time: {draft_elapsed_time_mean}")
print(f"Optmized draft elapsed time: {optmized_draft_elapsed_time_mean}")
print(f"Time difference: {abs(draft_elapsed_time_mean - optmized_draft_elapsed_time_mean)}")
print(f"The optmized version is {draft_elapsed_time_mean / optmized_draft_elapsed_time_mean}x faster\n")
