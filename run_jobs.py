import os
import subprocess


METHODS = [
    "BURER2002",  # MQLibで一番性能高いやつ
    "LAGUNA2009HCE",  # 一番新しい(性能はそこまで高くなさそう)
]
seconds = 600  # 10 minites

if __name__ == "__main__":
    for method in METHODS:
        print("method: {}".format(method), flush=True)
        for filename in os.listdir("maxcut"):
            if (os.path.isfile(os.path.join("maxcut", filename))):
                res = subprocess.check_output(
                    "./bin/MQLib -fM maxcut/{} -h {} -r {}".
                    format(filename, method, seconds),
                    stderr=subprocess.STDOUT,
                    shell=True).decode("ascii").split(",")
                print(res[2:4], flush=True)
