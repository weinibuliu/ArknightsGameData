## 轻量化明日方舟游戏数据 | LowerArknightsGameData

## 简介 | Introduction
本仓库旨在提供体积更小、针对性更强的明日方舟资源数据文件供其他场景使用。使用数据详见 **[数据来源](#数据来源--data-source)** 。

This repository aims to provide smaller and more targeted Arknights data and resource files for use in other scenarios. For details on the using data, see **[Data Source](#数据来源--data-source)** .

## 更新时间 | Update Time
仓库将于 **UTC-7 | UTC+8 | UTC+9** 的 **10:30** 与 **16:30** 运行工作流，检测是否存在更新（通过比对 `version` 文件内容是否一致）。如检测到更新，将创建 **[Release](https://github.com/weinibuliu/ArknightsGameData/releases)** 。这意味着仓库数据 ***不会*** 立即跟进计划外的修复（如临时闪断更新）。如您对数据时效有较高要求，建议 **fork** 仓库后自行修改工作流。

>[!WARNING]
仓库使用 **[Pygithub](https://github.com/PyGithub/PyGithub)** 获取 commit message ，如请求过于频繁，可能会触发 Github API 相关限制。请控制请求频率。

The repository will run the workflow at **10:30** and **16:30** on **UTC-7 | UTC+8 | UTC+9** to detect whether there are any updates (by comparing the contents of the `version` file to see if they are consistent). If an update is detected, a **[Release](https://github.com/weinibuliu/ArknightsGameData/releases)** will be created. This means that the repository datas ***don't*** keep up with unplanned fixes (such as temporary flash updates) immediately. If you have high requirements for data timeliness, it is recommended to **fork** the repository and modify the workflow yourself.

>[!WARNING]
The repository uses **[Pygithub](https://github.com/PyGithub/PyGithub)** to get commit messages. If the request is too frequent, it may trigger Github API related restrictions. Please control the request frequency.

## 文件列表 | Files List
- `version`
- `avatar` (干员头像)
- `character_table.json`（干员信息）
- `char_classisy` (经过分类的干员信息)

## 数据来源 | Data Source
本仓库使用了以下仓库的数据，感谢其维护者与贡献者的贡献。

This repository uses data from the following repositories.Thanks the contributions of their maintainers and contributors.

- **[ArknightsGameResource](https://github.com/yuanyan3060/ArknightsGameResource) (zh_CN | avatar)**
- **[ArknightsGameData_YoStar](https://github.com/Kengxxiao/ArknightsGameData_YoStar) (en_US | ja_JP | ko_KR)**

## 声明 | Statement
本仓库所有静态资源，版权均属于 **[明日方舟](https://ak.hypergryph.com)** 。本仓库仅出于学习与交流目的进行引用。

The copyright of all static resources in this repository belongs to **[Arknights](https://ak.hypergryph.com)**. This repository only quotes them for learning and communication.

## 致谢
### 开源项目 | Library

#### Github 工作流 | Github Workflows
- **[action-gh-release](https://github.com/softprops/action-gh-release)**
- **[add-and-commit](https://github.com/EndBug/add-and-commit)**
- **[checkout](https://github.com/actions/checkout)**
- **[download-artifact](https://github.com/actions/download-artifact)**
- **[upload-artifact](https://github.com/actions/upload-artifact)**
- **[set-timezone](https://github.com/szenius/set-timezone)**
- **[setup-python](https://github.com/actions/setup-python)**

#### 代码 | Code
- **[pygithub](https://github.com/PyGithub/PyGithub)**

#### 数据 | Data
- **[ArknightsGameData_YoStar](https://github.com/Kengxxiao/ArknightsGameData_YoStar)**
- **[ArknightsGameResource](https://github.com/yuanyan3060/ArknightsGameResource)**

### 贡献者 | Contributors
<a href="https://github.com/weinibuliu/ArknightsGameData/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=weinibuliu/ArknightsGameData&max=1000" />
</a>