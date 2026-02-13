import os


def get_solveds() -> set[int]:
    results = set[int]()
    for entry in os.scandir("problems"):
        results.add(int(entry.name.split(".")[0]))
    return results


def move(entry: os.DirEntry):
    if entry.is_dir():
        return
    problem_id = entry.name.split(".")[0]
    if not os.path.exists(dirpath := f"problems/{problem_id}"):
        os.mkdir(dirpath)
    if not str(entry.path).startswith(dirpath):
        os.rename(entry, os.path.join(dirpath, entry.name))


def main():
    for entry in os.scandir("problems"):
        move(entry)


if __name__ == "__main__":
    main()
