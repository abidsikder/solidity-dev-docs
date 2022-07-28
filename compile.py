#!/usr/bin/env python

import os
import shutil

# specifies directory paths
contract_locations = {
    "prb-math" : "contracts",
    "spatial-sol" : "contracts"
}

contract_paths = {}
for project in contract_locations:
    location = contract_locations[project]
    contract_paths[project] = os.path.abspath("./projects/"+project+"/"+location)

if os.path.exists("contracts"):
    shutil.rmtree("contracts")

os.mkdir("contracts")

contracts_path = os.path.abspath("contracts")

for project in contract_locations:
    print("Working on " + project)

    project_abs = os.path.abspath(project)
    src = os.path.join(project_abs,contract_paths[project])
    dst = "./contracts/" + project
    shutil.copytree(src, dst)


os.system("yarn hardhat docgen")

original_dir = os.getcwd()
for root, subdirs, files in os.walk("docs"):
    for doc_file in files:
        doc_abs = os.path.join(original_dir, root, doc_file)
        with open(doc_abs, 'r') as fp:
            lines = fp.readlines()
        with open(doc_abs, 'w') as fp:
            for number, line in enumerate(lines):
                # delete the first line
                if number not in [0]:
                    fp.write(line)

os.system("mkdocs build")
os.rename("./site/search.html", "./site/index.html")

