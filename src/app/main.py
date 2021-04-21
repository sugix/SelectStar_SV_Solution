import json

import numpy as np
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd
from itertools import groupby
from pyjarowinkler import distance
from sklearn.cluster import AffinityPropagation
import os

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#grouped_names = SqliteDict('./grouped_names.sqlite', encode=json.dumps, autocommit=True)
#intelligently_grouped_names = SqliteDict('./intelligently_grouped_names.sqlite', encode=json.dumps, autocommit=True)

grouped_names = dict()
intelligently_grouped_names = dict()


path = os.getcwd() + "/input"
input_file_path = f"{path}/names.csv"
input_names_df = pd.read_csv(input_file_path, index_col=None, header=None, names=['Name'])
names:List[str] = input_names_df['Name'].tolist()

@app.on_event("startup")
async def startup_event():
    names.sort()
    names_grouped_on_first_prefix = {j:tuple(i) for j, i in groupby(names,lambda a: a.split('_')[0])}

    for group_name, values in names_grouped_on_first_prefix.items():
        grouped_names[group_name] = values

def intelligent_clustering():
    names_np_array = np.asarray(names)
    jaro_winkler_similarity = -1*np.array([[distance.get_jaro_distance(w1, w2, winkler=True, scaling=0.1) for w1 in names_np_array] for w2 in names_np_array])
    affinity_propogation_model = AffinityPropagation(random_state=None)
    affinity_propogation_model.fit(jaro_winkler_similarity)

    for cluster_id in np.unique(affinity_propogation_model.labels_):
        cluster_name = names_np_array[affinity_propogation_model.cluster_centers_indices_[cluster_id]]
        cluster_values = np.unique(names_np_array[np.nonzero(affinity_propogation_model.labels_==cluster_id)])
        intelligently_grouped_names[cluster_name] = list(cluster_values)

@app.post("/perform-intelligent-grouping/")
async def intelligent_grouping(background_tasks: BackgroundTasks):
    background_tasks.add_task(intelligent_clustering)
    return {"message": "Affinity propagation based clustering in background"}

@app.get("/")
def intelligent_grouping_status():
    return {"Intellingent_cluster_status": len(intelligently_grouped_names)}


@app.get("/groups/{group_name}")
async def get_group_items(group_name: str):
    return grouped_names.get(group_name)

@app.get("/group")
async def get_all_groups():
    return grouped_names.items()

@app.get("/intelligent_group")
async def get_all_intelligent_groups():
    return intelligently_grouped_names.items()

@app.get("/names/{name}")
async def get_group_name(name: str):
    group_name = [grp_name for grp_name, list_of_names in grouped_names.items() if any(name in individual_name for individual_name in list_of_names)]
    if len(group_name) == 0:
        raise HTTPException(status_code=404, detail="Name not found in any group")
    return group_name
