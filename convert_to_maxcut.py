import os


def write_maxcut_file(filename):
    with open(os.path.join("data", filename)) as f:
        lines = f.readlines()
    with open(os.path.join("maxcut", filename), mode='w') as f:
        f.write(lines[0])
        for line in lines[1::]:
            u, v = map(int, line.split())
            f.write("{} {} 1\n".format(u + 1, v + 1))


if __name__ == "__main__":
    for filename in os.listdir("data"):
        if (os.path.isfile(os.path.join("data", filename))):
            write_maxcut_file(filename)
