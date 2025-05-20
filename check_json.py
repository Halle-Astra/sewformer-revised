import json
import os
import glob
import tqdm

root = '/workspace/programs/sewformer/data-sewfactory/sewfactory/'
fs = os.listdir(root)
problem_files = []
bar = tqdm.tqdm(total=len(fs))
for folder in fs:
    folder = os.path.join(root, folder)
    first_jsons = glob.glob(os.path.join(folder, '*.json'))
    first_jsons += glob.glob(os.path.join(folder, '*/*.json'))
    for json_fp in first_jsons:
        with open(json_fp) as f:
            try:
                json.load(f)
            except Exception as e:
                print(f'err: {e}, fpath: {json_fp}')
                problem_files.append(json_fp)
    bar.update()
bar.close()
f = open('./problem_jsons.txt','w')
f.write('\n'.join(problem_files))
f.close()
