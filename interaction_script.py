import pandas as pd
import json

def get_interaction():
    interaction_df=pd.read_csv("interactions.csv")
    size=len(interaction_df)
    interaction_groupby=interaction_df.groupby(["name"])["sector_id"].agg(lambda x:str("%0.2f" %(x.count()/size*100))).to_frame().reset_index().rename({"sector_id":'total_interaction'}, axis=1)
    interaction_groupby.set_index('name',inplace=True)
    interaction_js=json.dumps(interaction_groupby.to_dict()['total_interaction'])

    return interaction_js

# s=get_interaction()



