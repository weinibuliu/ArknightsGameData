# 角色信息
import json
from pathlib import Path


cache_path = Path(Path.cwd(), "cache")
build_path = Path(Path.cwd(), "build")


def run():
    with open(
        f"{cache_path}/gamedata/excel/character_table.json", "r", encoding="utf-8"
    ) as js:
        raw: dict = json.load(js)
        raw_items: list[list] = list(raw.items())

    with open(f"{build_path}/character_table_full.json", "w", encoding="utf-8") as ct_f:
        json.dump(raw, ct_f, indent=4, ensure_ascii=False)

    num = 0
    characters: dict = {}
    for data in raw_items:
        info: dict = data[-1]
        id: str = data[0]  # id
        if "char_" not in id:
            continue
        num += 1

        name: str = info.get("name")  # 名称
        rarity: int = info.get("rarity")  # 稀有度 (0 对应 1星干员)
        profession: str = info.get("profession")  # 职业
        subProfessionId: str = info.get("subProfessionId")  # 子职业
        position: str = info.get("position")  # 部署位置

        characters[id] = {
            "name": name,
            "rarity": rarity,
            "profession": profession,
            "subProfessionId": subProfessionId,
            "position": position,
        }

    with open(f"{build_path}/character_table.json", "w", encoding="utf-8") as ct:
        json.dump(characters, ct, indent=4, ensure_ascii=False)

    print(f"Done: Character ({num})")


if __name__ == "__main__":
    run()
