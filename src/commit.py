from datetime import datetime, timedelta

from github import Github

until = datetime.now()
since = until - timedelta(15)

repo = Github().get_repo("Kengxxiao/ArknightsGameData_YoStar")


def get_commit_msg(lang: str) -> str:
    if lang == "en_US":
        flag = lang.split("_")[0].upper()
    else:
        flag = lang.split("_")[1]
    commits = repo.get_commits(
        path=f"{lang}/gamedata",
        since=since,
        until=until,
    ).get_page(0)
    for commit in commits:
        msg = commit.commit.message
        if flag in msg:
            return msg


def get_version(lang: str) -> str | None:
    msg = get_commit_msg(lang)
    if msg is None:
        return
    ver = msg.split("Data:")[-1]
    return ver


if __name__ == "__main__":
    ver = get_version("ko_KR")
    print(ver)
