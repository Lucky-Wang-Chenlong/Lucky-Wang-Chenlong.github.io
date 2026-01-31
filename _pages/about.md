---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
# About me

My name is Chenlong Wang (王臣龙), a third-year undergraduate student in the School of Computer Science and Technology at [HUST](https://english.hust.edu.cn/). I began my research journey while working with Prof. [Yao Wan](http://wanyao.me/) at HUST, and join his undergraduate research team, [ONE Lab](https://oneslab.github.io/).
After that, I have collaborated with Prof. [Tianyi Zhou](https://tianyizhou.github.io/) at [UMD](https://umd.edu/). At present, I have joined the [CCVL Lab at JHU](https://ccvl.jhu.edu/) as an on-site intern, supervised by [Jieneng Chen](https://beckschen.github.io/).

I am currently seeking a Ph.D position in Machine Learning for Fall 2026.

My research interests lie in **Multimodal Intelligence**, especially on
- **World Model**: Video Generation, 3D Vision, Spatial Reasoning, World Model Simulation, Physics
- **Multi Modality**: Unified Multimodal Model (UMM), Multimodal Large Language Model (MLLM)
- **Reasoning**: Reasoning Interpretability, MLLM Reasoning, Efficient Reasoning, Code Reasoning
- **Trustworthy AI**: Mechanical Interpretability, Model Editing

Here is my [CV](https://drive.google.com/file/d/1_jCzKjvowF2Hqxrt3hZ685d-whxR8nja/view?usp=drive_link). Please feel free to contact me!

---

# 🔥 News
- *2025.08*: &nbsp;🎉 Our paper, **NoWait**, has been accepted at **EMNLP 2025 Findings**!
- *2025.05*: &nbsp;🎉 Our paper, **CodeSync**, has been accepted at **ICML 2025**!
- *2025.01*: &nbsp;🎉 One paper, **GUI-World**, has been accepted at **ICLR 2025**!

---
<br>

# 📝 Publications 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025 Findings</div><img src='images/poster/nowait.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Wait, We Don’t Need to “Wait”! Removing Thinking Tokens Improves Reasoning Efficiency** 

[[Arxiv]](https://arxiv.org/abs/2506.08343) 

**Chenlong Wang**, Yuanning Feng, Dongping Chen, Zhaoyang Chu, Ranjay Krishna, Tianyi Zhou†

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/poster/codesync.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale** 

[[Arxiv]](https://arxiv.org/abs/2502.16645) [[Github]](https://github.com/Lucky-Wang-Chenlong/CodeSync)

 **Chenlong Wang**\*, Zhaoyang Chu\*, Zhengxiang Cheng\*, Xuyi Yang, Kaiyue Qiu, Yao Wan†, Zhou Zhao, Xuanhua Shi, Hai Jin, Dongping Chen‡

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/poster/GUI-world.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents** 

[[Arxiv]](https://arxiv.org/pdf/2406.10819) [[Github]](https://github.com/Dongping-Chen/GUI-World) [[Website]](https://gui-world.github.io)

Dongping Chen\*, Yue Huang\*, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, **Chenlong Wang**, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan†, Pan Zhou† Jianfeng Gao, Lichao Sun†

</div>
</div>


**P.S.** \* indicates equal contribution. † indicates corresponding author. ‡ indicates project leaders.

---

<br>

# 🍀 In Submission

[1] **CausalSpatial: A Comprehensive Benchmark for Object-Centric Causal Spatial Reasoning** [[Arxiv](https://arxiv.org/abs/2601.13304)]

Wenxin Ma\*, **Chenlong Wang**\*, Ruishegn Yuan\*, Hao Chen, Nanru Dai, S Kevin Zhou, Yijun Yang, Alan Yuille, Jieneng Chen†

[2] **Quantifying the Gap between Understanding and Generation within Unified Multimodal Models**

**Chenlong Wang**\*, Yuhang Chen\*, Zhihan Hu\*, Dongping Chen, Wenhu Chen, Sarah Wiegreffe, Tianyi Zhou†

**P.S.** \* indicates equal contribution. † indicates corresponding author. ‡ indicates project leaders.

---
<br>

# 📖 Experience

<div style="display: flex; align-items: center; margin-bottom: 25px;">
  <div style="flex: 1; margin-right: 20px;">
    <div style="font-size: 1.1em; font-weight: bold;">Research Intern</div>
    <div style="font-style: italic; color: #666;">2025.09 - Present</div>
    <div><a href="https://ccvl.jhu.edu/">CCVL</a>, Johns Hopkins University,</div>
    <div>Supervised by <a href="https://beckschen.github.io/">Jieneng Chen.</a></div>
    <ul style="margin-top: 5px;">
      <li>Explore the powerful prior knowledge inside of <code>world models</code>.</li>
    </ul>
  </div>
  <div style="width: 30%; max-width: 200px; display: flex; justify-content: center; align-items: center;">
    <img src="images/affiliation/JHU_logo.png" alt="JHU Logo" style="width: 70%; object-fit: contain;">
  </div>
</div>

<div style="display: flex; align-items: center; margin-bottom: 25px;">
  <div style="flex: 1; margin-right: 20px;">
    <div style="font-size: 1.1em; font-weight: bold;">Remote Research Intern</div>
    <div style="font-style: italic; color: #666;">2025.04 - 2025.10</div>
    <div>University of Maryland,</div>
    <div>Supervised by <a href="https://tianyizhou.github.io/">Tianyi Zhou.</a></div>
    <ul style="margin-top: 5px;">
      <li>Investigate the unification and inherent misalignment within <code>unified models</code>.</li>
      <li>Explore the inherent mechanism in large reasoning models and conduct in-depth research on efficient multimodal reasoning with <code>NoWait</code>.</li>
    </ul>
  </div>
  <div style="width: 30%; max-width: 200px; display: flex; justify-content: center; align-items: center;">
    <img src="images/affiliation/UMD_logo.png" alt="UMD Logo" style="width: 80%; object-fit: contain;">
  </div>
</div>

<div style="display: flex; align-items: center; margin-bottom: 25px;">
  <div style="flex: 1; margin-right: 20px;">
    <div style="font-size: 1.1em; font-weight: bold;">B.Eng. in Computer Science and Technology</div>
    <div style="font-style: italic; color: #666;">2022.09 - 2026.06 (expected)</div>
    <div><a href="https://oneslab.github.io/">ONE Lab</a>, Huazhong University of Science and Technology,</div>
    <div>Supervised by <a href="http://wanyao.me/">Yao Wan.</a></div>
    <ul style="margin-top: 5px;">
      <li>Code generation & interpretability on code knowledge updating task. We propose <code>CodeSync</code>, an automated data engine for code knowledge updating.</li>
      <li>Research on LLM-based GUI Agents. We propose a dataset <code>GUI-World</code> focusing on GUI-oriented capabilities in current MLLMs.</li>
    </ul>
  </div>
  <div style="width: 30%; max-width: 200px; display: flex; justify-content: center; align-items: center;">
    <img src="images/affiliation/HUST_logo.png" alt="HUST Logo" style="width: 100%; object-fit: contain;">
  </div>
</div>
