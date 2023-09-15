from pathlib import Path
import json

NB_FILES = 4
len_seg = 30_000

actual = Path.cwd()

foldertonum = {int(connlu.stem.split("_")[1]) // len_seg : connlu for connlu in actual.glob("*.conllu")}


foldertonum = {k: v for k, v in sorted(foldertonum.items(), key=lambda item: item[0])}

count = 0
for num, file in foldertonum.items():
    if num % NB_FILES == 0:
        count += 1

    newfold = actual / f"WAC-{count}"
    newfold.mkdir(exist_ok=True)
    newfile = newfold / file.name

    with open(file, mode="rb") as f:
        with open(newfile, mode="wb") as f2:
            f2.write(f.read())

    print(f"{file.stem} --> {newfold.stem}")

foldlist = list(actual.glob("WAC-*"))
foldlist.sort(key=lambda x: int(x.stem.split("-")[1]))

dictfold = [
    {
        "id": folder.stem,
        "config": "sud",
        "directory": str(folder)
    }
    for folder in foldlist
]

with open(actual / "corpora_list.json", mode="w", encoding="utf-8") as f:
    json.dump(dictfold, f, indent=4, ensure_ascii=False)


