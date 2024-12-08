import os
import time
import shutil
import subprocess
from pathlib import Path

from github import Github

from src import avatar, character, char_classisy
from src import cwd, build_path, cache_path

print(os.environ)
lang = os.environ.get("BUILT_LANG")
character.run(lang)
avatar.run(lang)
char_classisy.run(lang)

# 写入版本信息
if lang == "zh_CN":
    with open(f"{build_path}/version", "w", encoding="utf-8") as vs:
        existing_version = None
        if Path(cwd, "version").exists():
            with open(f"{cwd}/version", "r", encoding="utf-8") as ev:
                existing_version = ev.readline().replace("\n", "")
        print(f"Existing Version: {existing_version}")

        with open(f"{cache_path}/version", "r", encoding="utf-8") as cv:
            current_version = cv.readline().replace("\n", "")
            print(f"Current Version: {current_version}")

        ver = current_version.split("-")
        version = f"{ver[0]}{ver[1]}{ver[2]}{ver[3]}{ver[4]}{ver[5]}"

        built_time = time.strftime("%Y-%m-%d %H:%M:%S")
        built_timestamp = int(
            time.mktime(time.strptime(built_time, "%Y-%m-%d %H:%M:%S"))
        )
        vs.write(f"{current_version}\n")
        vs.write(f"{version}\n")
        vs.write(f"built_time: {built_time}\n")
        vs.write(f"built_timestamp: {built_timestamp}")

    shutil.copyfile(Path(build_path, "version"), Path(cwd, "version"))
else:
    pass

# 写入 GITHUB ENV
if os.environ.get("CI"):
    subprocess.check_call(f'echo VERSION={version} >> "$GITHUB_ENV"', shell=True)
    print(f"VERSION = {version}")
    if current_version != existing_version:
        subprocess.check_call(f'echo RELEASE=true >> "$GITHUB_ENV"', shell=True)
        print("env.RELEASE = true")
print("Done: Version")

print("All Done!")
