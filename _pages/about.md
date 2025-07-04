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

I am a third-year undergraduate student in the School of Computer Science and Technology at [HUST](https://english.hust.edu.cn/). I began my research journey while collaborating with Prof. [Yao Wan](http://wanyao.me/) at HUST, and join his undergraduate team, [ONE Lab](https://oneslab.github.io/).
At present, I am working with Prof. [Tianyi Zhou](https://tianyizhou.github.io/) at [UMD](https://umd.edu/). 
I am currently seeking a Ph.D position in Machine Learning for Fall 2026.

My research interests lie in **Machine Learning** and **Large Language Model**, especially on
- **Reasoning**: reasoning interpretability, MLLM reasoning, reward hack.
- **World Model & Reinforcement Learning**: Self-evolution, RLVR.
- **Trustworthy AI** : interpretability, knowledge editing.

Here is my [CV](https://drive.google.com/file/d/13tjEFEF5Lehm8jajiyQTGLJJwD3h7v7K/view?usp=drive_link). Please feel free to contact me!

---

# 🔥 News
- *2025.05*: &nbsp;🎉 Our paper, **CodeSync**, has been accepted by **ICML 2025**!
- *2025.01*: &nbsp;🎉 One paper, **GUI-World**, has been accepted by **ICLR 2025**!

---
<br>

# 📝 Publications 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/poster/codesync.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale** 

[[PDF]](https://arxiv.org/abs/2502.16645) [[Github]](https://github.com/Lucky-Wang-Chenlong/CodeSync)

 **Chenlong Wang**\*, Zhaoyang Chu\*, Zhengxiang Cheng\*, Xuyi Yang, Kaiyue Qiu, Yao Wan†, Zhou Zhao†, Xuanhua Shi†, Hai Jin†, Dongping Chen‡

</div>
</div>

<!-- 
- ![ICML 2025](https://img.shields.io/badge/ICML-2025-87acc7) [CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](https://arxiv.org/abs/2502.16645)

  **Chenlong Wang**\*, Zhaoyang Chu\*, Zhengxiang Cheng\*, Xuyi Yang, Kaiyue Qiu, Yao Wan†, Zhou Zhao†, Xuanhua Shi†, Hai Jin†, Dongping Chen†
-->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/poster/GUI-world.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents** 

[[PDF]](https://arxiv.org/pdf/2406.10819) [[Github]](https://github.com/Dongping-Chen/GUI-World) [[Website]](https://gui-world.github.io)

Dongping Chen\*, Yue Huang\*, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, **Chenlong Wang**, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan†, Pan Zhou†, Jianfeng Gao†, Lichao Sun†

</div>
</div>

**P.S.** \* indicates equal contribution. † indicates corresponding author. ‡ indicates project leaders.

<!-- 
- ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-e87213) [GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents](https://arxiv.org/abs/2406.10819)

Dongping Chen\*, Yue Huang\*, Siyuan Wu\*, Jingyu Tang\*, Liuyi Chen, Yilin Bai, Zhigang He, **Chenlong Wang**, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan†, Pan Zhou†, Jianfeng Gao†, Lichao Sun†
-->

<!-- 🍀 In Submission -->

---

# 🍀 In Submission
- **Wait, We Don't Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency** [[PDF]](https://arxiv.org/abs/2506.08343)<br>
  **Chenlong Wang**, Yuanning Feng, Dongping Chen‡, Zhaoyang Chu, Ranjay Krishna†, Tianyi Zhou†<br>
  Collaborated with [**Tianyi Zhou**](https://tianyizhou.github.io/) from [UMD](https://umd.edu/) and [**Ranjay Krishna**](https://ranjaykrishna.com/index.html) from [UW](https://www.washington.edu/).

**P.S.** \* indicates equal contribution. † indicates corresponding author. ‡ indicates project leaders.

---
<br>

# 📖 Experience
- ***2025.04 - Present***, Remote Research in **University of Maryland**.
  - Explore the inherent mechanism in large reasoning models and conduct in-depth research on efficient multimodal reasoning with `NoWait`.

- ***2024.04 - Present***, Research Intern in [ONE Lab](https://oneslab.github.io/) at **Huazhong University of Science and Technology**.
  - Code generation & interpertability on code knowledge updating task. We propose `CodeSync`, an automated data engine for code knowledge updating.
  - Research on LLM-based GUI Agents. We propose a dataset `GUI-World` focusing on GUI-oriented capabilities in current MLLMs.
  
- ***2022.09 - 2026.06 (expected)***, BEng., Huazhong University of Science and Technology.

