# AI虚拟伙伴Web版 (AI Virtual Mate Web)

## 简介

**AI虚拟伙伴Web版** 是一款集成了先进人工智能技术的数字人聊天软件，通过Web界面提供用户与虚拟角色进行互动的平台。用户可以在本地或通过局域网访问Web，享受实时的语音交互体验。软件具备丰富的个性化设置，包括虚拟角色名称、人设、语言模型选择等，同时支持多种语音合成引擎和自定义API接入。

## 开源协议

本项目遵循 **GPL-3.0** 开源协议，鼓励社区成员自由地使用、修改和分发代码，同时要求分发的衍生作品也遵循相同的开源协议。

## 功能特点

- **多语言模型支持**：对接着多种预训练的大型语言模型，如GPT-3.5、GPT-4、Gemini等。
- **自定义API支持**：用户可以根据自己的需求配置自定义API，实现与特定大语言模型的对接。
- **多模语音合成**：支持微软云edge-tts、本地pyttsx3和GPT-SoVITS等多种语音合成引擎。
- **实时语音交互**：利用先进的语音识别技术，用户可以通过语音与虚拟伙伴进行实时交流。
- **动态Web界面**：通过Flet和Flask框架实现的Web服务器，为用户提供了一个动态的交互界面。
- **Live2D角色展示**：集成Live2D技术，展示虚拟角色形象，并根据语音合成结果实时变化口型。

## 系统要求

- 操作系统：Windows 10、Windows 11
- Python版本：推荐使用Python 3.10或以上版本
- 其他依赖：详见`requirements.txt`文件

## 安装指南

### 克隆项目

```bash
git clone https://github.com/swordswind/ai_virtual_mate_web.git
```

### 安装依赖

```bash
分别用 pip install xxx 安装 requirements.txt 中的依赖
```

## 使用说明

### 启动应用程序

在项目根目录下运行`main.py`脚本来启动应用程序(需先补全图片文件素材和放入Live2D模型和vosk语音识别模型)：

```bash
python main.py
```

### 软件设置

- 点击启动器右下角的“软件设置”按钮，进入设置界面。
- 配置虚拟伙伴的名称、人设、用户名、密码等信息。
- 设置语音合成引擎、语速、音高以及各种服务的端口号。
- 点击“保存”按钮，重启软件以应用更改。

### 语音交互

- 在启动器主界面中，通过下拉菜单选择“开启”以激活实时语音交互功能。
- 语音输入将自动触发与虚拟伙伴的对话，并实时显示在启动器窗口中。

### 对话界面

- 在对话Web页面中输入文本消息，点击“发送消息”按钮或按回车键发送。
- 虚拟伙伴的回复将显示在聊天框中。

### 角色展示

- 点击“打开角色”按钮，将在默认浏览器中打开Live2D角色展示页面。

### 导出聊天记录

- 点击对话Web页面左下角的“导出记录”按钮，可以将当前的聊天记录导出为文本文件。

### 清空聊天记录

- 点击对话Web页面左下角的“开启新对话”按钮，可以清空当前的聊天记录，开始新的对话。

## 技术栈

- **Python**：主要编程语言。
- **Flask**：Live2D的Web服务器框架。
- **Flet**：构建对话Web界面的Python库。
- **Live2D**：展示虚拟角色形象。
- **OpenAI**：提供预训练的大型语言模型接口。
- **Edge-TTS**：微软的文本到语音转换服务。
- **Pyttsx3**：Python的文本到语音库。
- **Vosk**：本地语音识别引擎。

## 贡献指南

我们欢迎并鼓励社区成员为本项目贡献代码或提出改进建议。在提交贡献之前，请阅读标准贡献指南以了解如何正确提交合并请求。

### 如何贡献

1. Fork本项目到您的GitHub账户。
2. 克隆您的Fork后的仓库到本地。
3. 创建一个新的分支，例如`feature/your-feature`。
4. 在新的分支上进行您的更改。
5. 提交您的更改，并推送到您的远程仓库。
6. 创建一个Pull Request到本项目的主分支。

## 问题反馈

如果在项目使用过程中遇到任何问题，欢迎在[议题](https://github.com/swordswind/ai_virtual_mate_web/issues)中提交Issue。

## 联系方式

- 邮箱：swordswind@qq.com
- Bilibili：[枫影剑wind](https://space.bilibili.com/106439263)

## 版本信息

- 当前版本：v1.0

## 开源项目页面

[AI虚拟伙伴Web版 GitHub页面](https://github.com/swordswind/ai_virtual_mate_web)

## 致谢

特别感谢所有支持我们项目的个人和开源项目，你们的支持和贡献成就了AI虚拟伙伴Web版。
- transformers：https://github.com/huggingface/transformers
- Qwen2：https://github.com/QwenLM/Qwen2
- GPT-SoVITS：https://github.com/RVC-Boss/GPT-SoVITS
- vosk：https://github.com/alphacep/vosk
- pygame：https://github.com/pygame/pygame
- edge-tts：https://github.com/rany2/edge-tts
- pyttsx3：https://github.com/nateshmbhat/pyttsx3
- ollama：https://github.com/ollama/ollama
- flet：https://github.com/flet-dev/flet
- flask：https://github.com/pallets/flask
- live2d：https://github.com/nladuo/live2d-chatbot-demo
