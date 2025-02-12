import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = "my_file.json"
#%%
with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj)
   #json.dump(obj2save , destination_file)
#%%
json_my_family = json.dumps(my_family)
print(json_my_family)   

#%% make it readable and indented
json_file = "index.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)

#%%
# json_file = 'my_file.json'
with open(json_file, 'r') as file_obj:
    my_family = json.load(file_obj)

print(my_family)    