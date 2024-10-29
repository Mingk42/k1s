import subprocess
import json
import os

##### 현재 실행중인 blog 컨테이너 수와 CPU 사용량을 가져오는 함수
def get_cpu_use():

    snapshot = subprocess.run(["docker", "stats", "--no-stream", "--format", "json"], capture_output=True)
    snapshot.stdout.decode("utf-8").strip().split("\n")

    containers=dict()

    for container in list(map(json.loads,snapshot.stdout.decode("utf-8").strip().split("\n"))):
        containers[container["Name"]]=container["CPUPerc"]

    cnts = len(list(filter(lambda x:"lb" not in x,containers.keys())))

    cpu_use = containers["samdul-blog-1"]

    return cpu_use, cnts


##### scale in/out 시작
home_path=os.path.expanduser("~")

while True:
    cu, scale_cnt =get_cpu_use()
    print(f"[INFO] 현재 CPU사용량은 {cu}입니다.")
    print(f"[INFO] 현재 container의 수는 {scale_cnt}개입니다.")
    if float(cu.replace("%",""))>1:
        print(f"[INFO] container의 수를 {scale_cnt+1}로 scale out 합니다.")
        os.system(f"docker compose -f {home_path}/code/docker/k1s/docker-compose.yaml up -d --scale blog={scale_cnt+1}")
    elif float(cu.replace("%",""))<0.5:
        if scale_cnt>1:
            print(f"[INFO] container의 수를 {scale_cnt-1}로 scale in 합니다.", end="\n\n")
            os.system(f"docker compose -f {home_path}/code/docker/k1s/docker-compose.yaml up -d --scale blog={scale_cnt-1}")
    print("")
    os.system("sleep 5")
