# Weekly Tech Trends Report (2025-10-20)

> This report is automatically generated, tracking 14 trending tech items.


## Other 

### 🔥🔥🔥🔥 dexter

- **Source**: 🐙 Github
- **Metrics**: ⭐ 1701
- **Link**: [github.com](https://github.com/virattt/dexter)


### 🔥🔥🔥 OmniVinci: Enhancing Architecture and Data for Omni-Modal Understanding   LLM

- **Source**: 📜 Arxiv
- **Metrics**: Advancing machine intelligence requires developing the ability to perceive
across multiple modalities, much as humans sense the world. We introduce
OmniVinci, an initiative to build a strong, open-source, omni-modal LLM. We
carefully study the design choices across model architecture and data curation.
For model architecture, we present three key innovations: (i) OmniAlignNet for
strengthening alignment between vision and audio embeddings in a shared
omni-modal latent space; (ii) Temporal Embedding Grouping for capturing
relative temporal alignment between vision and audio signals; and (iii)
Constrained Rotary Time Embedding for encoding absolute temporal information in
omni-modal embeddings. We introduce a curation and synthesis pipeline that
generates 24M single-modal and omni-modal conversations. We find that
modalities reinforce one another in both perception and reasoning. Our model,
OmniVinci, outperforms Qwen2.5-Omni with +19.05 on DailyOmni (cross-modal
understanding), +1.7 on MMAR (audio), and +3.9 on Video-MME (vision), while
using just 0.2T training tokens - a 6 times reduction compared to
Qwen2.5-Omni's 1.2T. We finally demonstrate omni-modal advantages in downstream
applications spanning robotics, medical AI, and smart factory.
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15870v1)


### 🔥🔥🔥 Skyfall-GS: Synthesizing Immersive 3D Urban Scenes from Satellite   Imagery

- **Source**: 📜 Arxiv
- **Metrics**: Synthesizing large-scale, explorable, and geometrically accurate 3D urban
scenes is a challenging yet valuable task in providing immersive and embodied
applications. The challenges lie in the lack of large-scale and high-quality
real-world 3D scans for training generalizable generative models. In this
paper, we take an alternative route to create large-scale 3D scenes by
synergizing the readily available satellite imagery that supplies realistic
coarse geometry and the open-domain diffusion model for creating high-quality
close-up appearances. We propose \textbf{Skyfall-GS}, the first city-block
scale 3D scene creation framework without costly 3D annotations, also featuring
real-time, immersive 3D exploration. We tailor a curriculum-driven iterative
refinement strategy to progressively enhance geometric completeness and
photorealistic textures. Extensive experiments demonstrate that Skyfall-GS
provides improved cross-view consistent geometry and more realistic textures
compared to state-of-the-art approaches. Project page:
https://skyfall-gs.jayinnn.dev/
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15869v1)


### 🔥🔥🔥 PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction

- **Source**: 📜 Arxiv
- **Metrics**: Large language models (LLMs) are moving beyond static uses and are now
powering agents that learn continually during their interaction with external
environments. For example, agents can learn reusable skills while navigating
web pages or toggling new tools. However, existing methods for skill learning
often create skills that are over-specialized to a single website and fail to
generalize. We introduce PolySkill, a new framework that enables agents to
learn generalizable and compositional skills. The core idea, inspired by
polymorphism in software engineering, is to decouple a skill's abstract goal
(what it accomplishes) and its concrete implementation (how it is executed).
Experiments show that our method (1) improves skill reuse by 1.7x on seen
websites and (2) boosts success rates by up to 9.4% on Mind2Web and 13.9% on
unseen websites, while reducing steps by over 20%. (3) In self-exploration
settings without specified tasks, our framework improves the quality of
proposed tasks and enables agents to learn generalizable skills that work
across different sites. By enabling the agent to identify and refine its own
goals, the PolySkill enhances the agent's ability to learn a better curriculum,
leading to the acquisition of more generalizable skills compared to baseline
methods. This work provides a practical path toward building agents capable of
continual learning in adaptive environments. Our findings show that separating
a skill's goal from its execution is a crucial step toward developing
autonomous agents that can learn and generalize across the open web
continuously.
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15863v1)


### 🔥🔥🔥 BLIP3o-NEXT: Next Frontier of Native Image Generation

- **Source**: 📜 Arxiv
- **Metrics**: We present BLIP3o-NEXT, a fully open-source foundation model in the BLIP3
series that advances the next frontier of native image generation. BLIP3o-NEXT
unifies text-to-image generation and image editing within a single
architecture, demonstrating strong image generation and image editing
capabilities. In developing the state-of-the-art native image generation model,
we identify four key insights: (1) Most architectural choices yield comparable
performance; an architecture can be deemed effective provided it scales
efficiently and supports fast inference; (2) The successful application of
reinforcement learning can further push the frontier of native image
generation; (3) Image editing still remains a challenging task, yet instruction
following and the consistency between generated and reference images can be
significantly enhanced through post-training and data engine; (4) Data quality
and scale continue to be decisive factors that determine the upper bound of
model performance. Building upon these insights, BLIP3o-NEXT leverages an
Autoregressive + Diffusion architecture in which an autoregressive model first
generates discrete image tokens conditioned on multimodal inputs, whose hidden
states are then used as conditioning signals for a diffusion model to generate
high-fidelity images. This architecture integrates the reasoning strength and
instruction following of autoregressive models with the fine-detail rendering
ability of diffusion models, achieving a new level of coherence and realism.
Extensive evaluations of various text-to-image and image-editing benchmarks
show that BLIP3o-NEXT achieves superior performance over existing models.
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15857v1)


## AI 

### 🔥🔥🔥 open-agent-builder

- **Source**: 🐙 Github
- **Metrics**: ⭐ 1169
- **Link**: [github.com](https://github.com/firecrawl/open-agent-builder)


### 🔥🔥🔥 LightsOut: Diffusion-based Outpainting for Enhanced Lens Flare Removal

- **Source**: 📜 Arxiv
- **Metrics**: Lens flare significantly degrades image quality, impacting critical computer
vision tasks like object detection and autonomous driving. Recent Single Image
Flare Removal (SIFR) methods perform poorly when off-frame light sources are
incomplete or absent. We propose LightsOut, a diffusion-based outpainting
framework tailored to enhance SIFR by reconstructing off-frame light sources.
Our method leverages a multitask regression module and LoRA fine-tuned
diffusion model to ensure realistic and physically consistent outpainting
results. Comprehensive experiments demonstrate LightsOut consistently boosts
the performance of existing SIFR methods across challenging scenarios without
additional retraining, serving as a universally applicable plug-and-play
preprocessing solution. Project page: https://ray-1026.github.io/lightsout/
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15868v1)


### 🔥🔥🔥 BiomedXPro: Prompt Optimization for Explainable Diagnosis with   Biomedical Vision Language Models

- **Source**: 📜 Arxiv
- **Metrics**: The clinical adoption of biomedical vision-language models is hindered by
prompt optimization techniques that produce either uninterpretable latent
vectors or single textual prompts. This lack of transparency and failure to
capture the multi-faceted nature of clinical diagnosis, which relies on
integrating diverse observations, limits their trustworthiness in high-stakes
settings. To address this, we introduce BiomedXPro, an evolutionary framework
that leverages a large language model as both a biomedical knowledge extractor
and an adaptive optimizer to automatically generate a diverse ensemble of
interpretable, natural-language prompt pairs for disease diagnosis. Experiments
on multiple biomedical benchmarks show that BiomedXPro consistently outperforms
state-of-the-art prompt-tuning methods, particularly in data-scarce few-shot
settings. Furthermore, our analysis demonstrates a strong semantic alignment
between the discovered prompts and statistically significant clinical features,
grounding the model's performance in verifiable concepts. By producing a
diverse ensemble of interpretable prompts, BiomedXPro provides a verifiable
basis for model predictions, representing a critical step toward the
development of more trustworthy and clinically-aligned AI systems.
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15866v1)


### 🔥🔥🔥 PokeeResearch: Effective Deep Research via Reinforcement Learning from   AI Feedback and Robust Reasoning Scaffold

- **Source**: 📜 Arxiv
- **Metrics**: Tool-augmented large language models (LLMs) are emerging as deep research
agents, systems that decompose complex queries, retrieve external evidence, and
synthesize grounded responses. Yet current agents remain limited by shallow
retrieval, weak alignment metrics, and brittle tool-use behavior. We introduce
PokeeResearch-7B, a 7B-parameter deep research agent built under a unified
reinforcement learning framework for robustness, alignment, and scalability.
PokeeResearch-7B is trained by an annotation-free Reinforcement Learning from
AI Feedback (RLAIF) framework to optimize policies using LLM-based reward
signals that capture factual accuracy, citation faithfulness, and instruction
adherence. A chain-of-thought-driven multi-call reasoning scaffold further
enhances robustness through self-verification and adaptive recovery from tool
failures. Among 10 popular deep research benchmarks, PokeeResearch-7B achieves
state-of-the-art performance among 7B-scale deep research agents. This
highlights that careful reinforcement learning and reasoning design can produce
efficient, resilient, and research-grade AI agents. The model and inference
code is open-sourced under MIT license at
https://github.com/Pokee-AI/PokeeResearchOSS.
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15862v1)


### 🔥🔥🔥 InfiMed-ORBIT: Aligning LLMs on Open-Ended Complex Tasks via   Rubric-Based Incremental Training

- **Source**: 📜 Arxiv
- **Metrics**: Large Language Models (LLMs) have shown substantial advances through
reinforcement learning (RL), particularly in domains where rewards can be
programmatically verified, such as mathematics and code. In these areas, models
benefit from a well-defined operational base guided by explicit rule-based
objectives. However, this progress reveals a significant limitation: in
open-ended domains where rewards are ambiguous, subjective, or
context-dependent, such as creative writing, scientific reasoning, and notably
medical consultation, robust reward functions are lacking, making these areas
challenging for current RL strategies. To bridge this gap, we introduce ORBIT,
an open-ended rubric-based incremental training framework specifically designed
for high-stakes medical dialogue. ORBIT integrates syn- thetic dialogue
generation with the dynamic creation of rubrics, employing these rubrics to
direct an incremental RL process. In particular, this approach does not depend
on external medical knowledge or manual rules, instead utilizing rubric-guided
feedback to shape learning. When implemented on the Qwen3-4B-Instruct model,
our method can greatly enhance its performance on the HealthBench-Hard
benchmark from 7.0 to 27.2 using only 2k samples, thus achieving
state-of-the-art results for models of this scale. Our analysis confirms that
rubric-driven RL fos-ters consistent performance gains across diverse
consultation scenarios, going beyond simple numerical improvements. These
findings underscore rubric-based feedback as a scalable strategy for advancing
LLMs in intricate, open-ended tasks.
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15859v1)


## Web 

### 🔥🔥🔥 Skill_Seekers

- **Source**: 🐙 Github
- **Metrics**: ⭐ 1034
- **Link**: [github.com](https://github.com/yusufkaraaslan/Skill_Seekers)


### 🔥 ro

- **Source**: 🐙 Github
- **Metrics**: ⭐ 287
- **Link**: [github.com](https://github.com/samber/ro)


### 🔥 async-react

- **Source**: 🐙 Github
- **Metrics**: ⭐ 180
- **Link**: [github.com](https://github.com/rickhanlonii/async-react)


## Cloud 

### 🔥🔥🔥 Sound Clouds: Exploring ambient intelligence in public spaces to elicit   deep human experience of awe, wonder, and beauty

- **Source**: 📜 Arxiv
- **Metrics**: While the ambient intelligence (AmI) systems we encounter in our daily lives,
including security monitoring and energy-saving systems, typically serve
pragmatic purposes, we wonder how we can design and implement ambient
artificial intelligence experiences in public spaces that elicit deep human
feelings of awe, wonder, and beauty. As a manifestation, we introduce Sound
Clouds, an immersive art installation that generates live music based on
participants' interaction with several human-height spheres. Our installation
serves as a provocation into future ambient intelligence that provokes, not
limits, the future possibilities of AmI.
- **Link**: [arxiv.org](http://arxiv.org/abs/2510.15865v1)



---

**Data Sources**: GitHub Trending Projects | StackOverflow Hot Questions | arXiv Latest Papers