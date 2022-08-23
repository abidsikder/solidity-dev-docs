#!/usr/bin/env python

import os
import shutil

# specifies directory paths
contract_locations = {
    "prb-math" : "contracts",
    "spatial-sol" : "contracts",
    "solidity-trigonometry" : "src"
}

contract_paths = {}
for project in contract_locations:
    location = contract_locations[project]
    contract_paths[project] = os.path.abspath("./projects/"+project+"/"+location)

clean_before_run = ["contracts", "docs", "site", "artifacts", "cache", "typechain-types"]
for target in clean_before_run:
    if os.path.exists(target):
        shutil.rmtree(target)

os.mkdir("docs")
os.mkdir("contracts")

contracts_path = os.path.abspath("contracts")

print("#### Copying over contracts ####")
for project in contract_locations:
    print("### " + project + " ###")

    project_abs = os.path.abspath(project)
    src = os.path.join(project_abs,contract_paths[project])
    dst = "./contracts/" + project
    shutil.copytree(src, dst)

print("#### Deleting Test Files ####")
original_dir = os.getcwd()
for root, subdirs, files in os.walk("contracts"):
    for subdir in subdirs:
        if subdir == "test":
            subdir_abs_path = os.path.join(original_dir, root, subdir)
            shutil.rmtree(subdir_abs_path)


print("#### Creating documentation markdown files ####")
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

print("#### Building site ####")
os.system("mkdocs build")
os.rename("./site/search.html", "./site/index.html")

print("#### Done ####")
