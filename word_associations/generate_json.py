"""
Takes the input.txt file of associations and makes json.
"""
import json

out_json = open("associations.json","w")
out_js = open("associations.js","w")
sets = open("associations.txt").readlines()

associations = {}
for set in sets:
    set = set.strip()
    key = set.split()[0]
    values = set.split()[1:]
    associations[key] = values

out_json.write(json.dumps(associations,indent=2))
out_json.close()

out_js.write("var associations = "+json.dumps(associations,indent=2)+";")
out_js.close()