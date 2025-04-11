---

# 语音助手

基于 fast-whisper、Ollama Qwen2.5 和 espeak-ng 的语音助手系统。

## 安装

1. 安装依赖:
```bash
sudo apt update
sudo apt install python3 python3-pip -y

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

pip install -r requirements.txt
```

2. 安装 espeak-ng:
```bash
# Ubuntu/Debian
sudo apt-get install espeak-ng

# MacOS
brew install espeak-ng
```

3. 安装并运行 Ollama:
```bash

curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:0.5b
```

## 使用方法

1. 文件处理模式:
```bash
python main.py --file path/to/audio.wav
```

2. 交互式模式:
```bash
python main.py --interactive
```

## 项目结构

```
src/
├── core/          # 核心功能模块
├── utils/         # 工具函数
└── config.py      # 配置文件
```

## 支持的功能

- 语音识别 (fast-whisper)
- 自然语言处理 (Ollama Qwen2.5)
- 语音合成 (espeak-ng)
- 实时录音对话
