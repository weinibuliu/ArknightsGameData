from datetime import datetime, timedelta

from github import Github

until = datetime.now()
since = until - timedelta(7)

repo = Github().get_repo("Kengxxiao/ArknightsGameData_YoStar")


def get_commit_msg(lang: str) -> str:
    flag = lang.split("_")[0].upper()
    commits = repo.get_commits(
        path=f"{lang}/gamedata",
        since=since,
        until=until,
    ).get_page(0)

    for commit in commits:
        msg = commit.commit.message
        if flag in msg:
            return msg


def get_version(lang: str) -> str:
    msg = get_commit_msg(lang)
    ver = msg.split("Data:")[-1]
    return ver


if __name__ == "__main__":
    ver = get_version("en_US")
    print(ver)
