import os
import hashlib
import json
import datetime
import random
import shutil
from Utils.LZMA import compress

def _(*args):
	print('[INFO]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()


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

    _(f'MasterHash is {MH}\n')

    all_file = iterate_over("Gamefiles")

    for file in all_file:
        _(f'Processing {file} ...')

        if file.endswith('.csv'):
            file_cont = compress(open(file, "rb").read())
        else:
            file_cont = open(file, "rb").read()

        sha = shash(file_cont)
        out["files"].append({"file": FP(file), "sha": sha})


    os.chdir("Patchs")
    shutil.copytree(backup + "/Gamefiles", os.getcwd() + f"/{MH}")
    os.chdir(MH)  # mode write doesnt create file unless this

    all_file = iterate_over('./')

    for file in all_file:
        if file.endswith('.csv'):
            file_cont = compress(open(file, "rb").read())

            with open(file, "wb") as new_file:
                new_file.write(file_cont)
                new_file.close()
        else:
            _(f"Skipping compression for {file}")
            pass


    json_out = open("fingerprint.json", "w")
    json_out.write(str(out).replace("'", '"').replace("\\\\", "\\"))  # WRITE fingerprint.json
    json_out.close()