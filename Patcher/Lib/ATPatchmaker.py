import os
import hashlib
import json
import datetime
import sys
import random
import shutil


def Make():
    backup = os.getcwd()

    def FP(arg: str) -> str:  # get filename in like fingerprint.json
        return arg.replace("\\", r"\/").replace("Gamefiles\\/", "")

    def iterate_over(path: str) -> list:  # get all subfiles and files
        r = []
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                if name != 'fingerprint.json':
                    r.append(os.path.join(root, name))
        return r

    def shash(inp) -> str:  # get hash sha1
        hash_object = hashlib.sha1(inp)
        pbHash = hash_object.hexdigest()
        return pbHash

    def MasterHasher():

        time = str(int(datetime.datetime.timestamp(datetime.datetime.now())))
        by = shash(time.encode()).encode()
        return by

    MH = MasterHasher().decode()
    base = '''{ "files": [],
      "sha": "''' + MH + '",' + '''
      "version": "''' + "26.165." + str(random.randint(1, 9)) + '"}'

    out = json.loads(base)

    all_file = iterate_over("Gamefiles")

    for file in all_file:
        file_cont = open(file, "rb").read()
        sha = shash(file_cont)
        out["files"].append({"file": FP(file), "sha": sha})

    os.chdir("Patchs")
    shutil.copytree(backup + "/Gamefiles", os.getcwd() + f"/{MH}")
    os.chdir(MH)  # mode write doesnt create file unless this

    json_out = open("fingerprint.json", "w")
    json_out.write(str(out).replace("'", '"').replace("\\\\", "\\"))  # WRITE fingerprint.json
    json_out.close()