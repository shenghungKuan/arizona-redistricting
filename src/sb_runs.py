"""
@author: erv2, and all authors of https://github.com/vrdi/shortbursts-gingles/blob/
"""


import geopandas as gpd
import numpy as np
import pickle
from functools import partial
from gerrychain import Graph, GeographicPartition, Partition, Election, accept
from gerrychain.updaters import Tally, cut_edges
from gerrychain import MarkovChain
from gerrychain.proposals import recom
from gerrychain.accept import always_accept
from gerrychain import constraints
from gerrychain.tree import recursive_tree_part
from gingleator import Gingleator

score_functs = {0: None, 
                1: Gingleator.reward_partial_dist, 
                2: Gingleator.reward_next_highest_close,
                3: Gingleator.penalize_maximum_over,
                4: Gingleator.penalize_avg_over}

BURST_LEN = 10 # 10, 50
NUM_DISTRICTS = 30
ITERS = 10
POP_COL = "TOTPOP"
N_SAMPS = 10
SCORE_FUNCT = score_functs[1]
EPS = 0.1
MIN_POP_COL = 'AMINVAP'
THRESHOLD = 0.5 # 5, 10, 20, 30


## Setup graph, updaters, elections, and initial partition

print("Reading in Data/Graph", flush=True)

graph = Graph.from_file("data/AZ_shapefile/AZ.shp")


my_updaters = {"population" : Tally(POP_COL, alias="population"),
               "VAP": Tally("VAP"),
               "AMINVAP": Tally("AMINVAP"),
               "cut_edges": cut_edges}


print("Creating seed plan", flush=True)

total_pop = sum([graph.nodes()[n][POP_COL] for n in graph.nodes()])

init_partition = Partition(graph, assignment="SEND", updaters=my_updaters)


gingles = Gingleator(init_partition, pop_col=POP_COL,
                     threshold=THRESHOLD, score_funct=SCORE_FUNCT, epsilon=EPS,
                     minority_perc_col="{}_perc".format(MIN_POP_COL))

gingles.init_minority_perc_col(MIN_POP_COL, "VAP", 
                               "{}_perc".format(MIN_POP_COL))

num_bursts = int(ITERS/BURST_LEN)

print("Starting Short Bursts Runs", flush=True)

for n in range(N_SAMPS):
    sb_obs = gingles.short_burst_run(num_bursts=num_bursts, num_steps=BURST_LEN, maximize=True, verbose=False)
    print("\tFinished chain {}".format(n), flush=True)

    print("\tSaving results", flush=True)

    print(sb_obs[1])
    f_out = "data/AZ_sb/AZ_sb.npy"
    np.save(f_out, sb_obs[1])

    f_out_part = "data/AZ_sb/AZ_sb_max_part.p"

    max_stats = {"VAP": sb_obs[0][0]["VAP"],
                 "AMINVAP": sb_obs[0][0]["AMINVAP"],
                 }

    print(max_stats)

    with open(f_out_part, "wb") as f_out:
        pickle.dump(max_stats, f_out)
