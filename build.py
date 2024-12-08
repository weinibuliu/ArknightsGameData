import os
import sys
import time
import shutil
import subprocess
from pathlib import Path


from src import avatar, character, char_classisy
from src import cwd, build_path, cache_path
from src.commit import get_version

lang = sys.argv[1]

character.run(lang)
char_classisy.run(lang)
if lang == "zh_CN":
    avatar.run(lang)
else:
    print("Skip to get avatar")

# 写入版本信息
ver = version = existing_version = current_version = None
existing_version_path = Path(cwd, f"version/{lang}/version")

if lang == "zh_CN":
    with open(f"{cache_path}/{lang}/version", "r", encoding="utf-8") as cv:
        current_version = cv.readline().replace("\n", "")
        print(f"Current Version: {current_version}")
else:
    current_version = get_version(lang)

with open(f"{build_path}/version", "w", encoding="utf-8") as vs:
    if existing_version_path.exists():
        with open(existing_version_path, "r", encoding="utf-8") as ev:
            existing_version = ev.readline().replace("\n", "")
    print(f"Existing Version: {existing_version}")

    if current_version is not None:
        ver = current_version.split("-")
        version = f"{ver[0]}{ver[1]}{ver[2]}{ver[3]}{ver[4]}{ver[5]}"

    built_time = time.strftime("%Y-%m-%d %H:%M:%S")
    built_timestamp = int(time.mktime(time.strptime(built_time, "%Y-%m-%d %H:%M:%S")))

    vs.write(f"{current_version}\n")
    vs.write(f"{version}\n")
    vs.write(f"built_time: {built_time}\n")
    vs.write(f"built_timestamp: {built_timestamp}")

shutil.copyfile(Path(build_path, "version"), existing_version_path)

# 写入 GITHUB ENV
if os.environ.get("CI"):
    subprocess.check_call(f'echo VER={current_version} >> "$GITHUB_ENV"', shell=True)
    print(f"VER = {current_version}")
    if current_version is not None and current_version != existing_version:
        subprocess.check_call(f'echo RELEASE=true >> "$GITHUB_ENV"', shell=True)
        print("env.RELEASE = true")
    else:
        print("env.RELEASE = false")
print("Done: Version")

print("All Done!")
