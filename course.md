# LLM 学习路径（2026-08 整理）

## 第 0 步：全貌（先看这个，3.5h，不写代码）
- Deep Dive into LLMs like ChatGPT — Karpathy
  https://www.youtube.com/watch?v=7xTGNNLPyMI

## 第 1 步：Karpathy《Neural Networks: Zero to Hero》（按顺序敲代码）
- 课程主页: https://karpathy.ai/zero-to-hero.html
- 官方播放列表（下载用这个最省事）:
  https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- 单集:
  1. micrograd（反向传播）      https://www.youtube.com/watch?v=VMj-3S1tku0
  2. makemore Part 1（bigram）  https://www.youtube.com/watch?v=PaCmpygFfXo
  3. makemore Part 2（MLP）     https://www.youtube.com/watch?v=TCH_1BHY58I
  4. makemore Part 3（BatchNorm）https://www.youtube.com/watch?v=P6sfmUTpUmc
  5. makemore Part 4（手写backprop）https://www.youtube.com/watch?v=q8SA3rM6ckI
  6. makemore Part 5（WaveNet） https://www.youtube.com/watch?v=t3YJ5hKiMQ0
  7. Let's build GPT from scratch https://www.youtube.com/watch?v=kCc8FmEb1nY
  8. Let's build the GPT Tokenizer https://www.youtube.com/watch?v=zduSFxRajkE
  9. Let's reproduce GPT-2 (124M) https://www.youtube.com/watch?v=l8pRSuU81PU
- 配套代码:
  - https://github.com/karpathy/micrograd
  - https://github.com/karpathy/makemore
  - https://github.com/karpathy/ng-video-lecture  (build GPT)
  - https://github.com/karpathy/minbpe            (tokenizer)
  - https://github.com/karpathy/build-nanogpt     (GPT-2 复现)

## 第 2 步：nanochat（capstone，全栈 tokenizer→pretrain→SFT→GRPO）
- 仓库: https://github.com/karpathy/nanochat
- 讲解视频（Trelis Research）: https://www.youtube.com/watch?v=qra052AchPE
- workshop 版: https://github.com/i-dot-ai/nanochat-workshop

## 第 3 步：Stanford CS336《Language Modeling from Scratch》Spring 2026
- 课程主页: https://stanford-cs336.github.io/
- 作业（开源）: https://github.com/stanford-cs336  (assignment1-basics 等)
- 视频在 Stanford Online 的 YouTube 频道搜 "CS336 Spring 2026"，已确认的单集:
  - Lec 1 Overview, Tokenization  https://www.youtube.com/watch?v=JuoVZkPBiKk
  - Lec 2 PyTorch (einops)        https://www.youtube.com/watch?v=kuYAsz7zspQ
  - Lec 3 Architectures           https://www.youtube.com/watch?v=lVynu4bo1rY
  - Lec 5 GPUs, TPUs              https://www.youtube.com/watch?v=izZba4UA7iY
  - Lec 10 Inference              https://www.youtube.com/watch?v=EfM546A79aM
- 优先看: Lec 1 / 3 / 5 / 10 + Assignment 1

## 第 4 步（可并行，应用层）
- HF LLM Course:  https://huggingface.co/learn/llm-course
- HF smol-course（SFT/对齐/评估）: https://huggingface.co/learn/smol-course
  仓库: https://github.com/huggingface/smol-course
- MS Generative AI for Beginners: https://github.com/microsoft/generative-ai-for-beginners
- MS AI Agents for Beginners:     https://github.com/microsoft/ai-agents-for-beginners

## 第 5 步：post-training 技术报告（学完直接读）
- DeepSeek-R1: https://arxiv.org/abs/2501.12948
- Tülu 3:      https://arxiv.org/abs/2411.15124
- InstructGPT（RLHF 起点）: https://arxiv.org/abs/2203.02155

## 离线下载命令（另一台电脑装 yt-dlp 后执行）
    pip install yt-dlp
    # Karpathy 全套（含 Deep Dive 单集）
    yt-dlp -f "bv*[height<=1080]+ba" -o "%(playlist_index)s-%(title)s.%(ext)s" \
      "https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ"
    yt-dlp "https://www.youtube.com/watch?v=7xTGNNLPyMI"
    # CS336 单集
    yt-dlp JuoVZkPBiKk lVynu4bo1rY izZba4UA7iY EfM546A79aM
    # 代码仓库
    git clone https://github.com/karpathy/nanochat
    git clone https://github.com/stanford-cs336/assignment1-basics
