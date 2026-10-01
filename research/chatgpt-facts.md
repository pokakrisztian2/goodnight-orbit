# Fact Sheet — "Every Confusing Thing About ChatGPT Explained Slowly (For Sleep)"

Compiled 2026-10-01. Every line was checked against the listed source with WebSearch/WebFetch/curl (no Wikipedia). Where a paper was downloaded and read as text (arXiv PDFs via pdftotext), the source is the paper itself. openai.com blocks direct fetching, so OpenAI pages were read through Wayback Machine snapshots (2024–2025) of the official URLs; the official URL is the one cited.
Legend: plain line = verified. **UNCERTAIN** = not fully confirmed, disputed, or seen only in a secondary retelling. Soften it in narration or leave it out. All UNCERTAIN items are also collected at the end.
"Our tiktoken run" = we tokenized words ourselves with OpenAI's official open-source tokenizer library, tiktoken (run on 2026-10-01): https://github.com/openai/tiktoken
"ELIZA 1966" = J. Weizenbaum, "ELIZA — A Computer Program for the Study of Natural Language Communication Between Man and Machine," *Communications of the ACM* 9(1), 36–45 (January 1966), read in full (Stanford CS124 copy): https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf
"Smithsonian 2026" = Francine Uenuma, "Why the Computer Scientist Behind the World's First Chatbot Dedicated His Life to Publicizing the Threat Posed by A.I.," *Smithsonian*, 15 Jan 2026: https://www.smithsonianmag.com/history/why-the-computer-scientist-behind-the-worlds-first-chatbot-dedicated-his-life-to-publicizing-the-threat-posed-by-ai-180987971/
"NYT Weizenbaum" = John Markoff, "Joseph Weizenbaum, Famed Programmer, Is Dead at 85," *New York Times*, 13 March 2008: https://www.nytimes.com/2008/03/13/world/europe/13weizenbaum.html
"OpenAI tokens" = OpenAI Help Center, "What are tokens and how to count them?" (Wayback snapshot, 2025): https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
"Sennrich 2016" = R. Sennrich, B. Haddow & A. Birch, "Neural Machine Translation of Rare Words with Subword Units," arXiv:1508.07909 (v5, 10 June 2016): https://arxiv.org/abs/1508.07909
"Petrov 2023" = A. Petrov, E. La Malfa, P. Torr & A. Bibi (Oxford), "Language Model Tokenizers Introduce Unfairness Between Languages," NeurIPS 2023, arXiv:2305.15425: https://arxiv.org/abs/2305.15425
"GPT-2 paper" = A. Radford et al., "Language Models are Unsupervised Multitask Learners" (OpenAI, 2019): https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
"GPT-3 paper" = T. Brown et al., "Language Models are Few-Shot Learners," arXiv:2005.14165 (May 2020): https://arxiv.org/abs/2005.14165
"Vaswani 2017" = A. Vaswani et al., "Attention Is All You Need," NIPS 2017, arXiv:1706.03762: https://arxiv.org/abs/1706.03762
"Wired 2024" = Steven Levy, "8 Google Employees Invented Modern AI. Here's the Inside Story," *WIRED*, 20 March 2024: https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/
"Google ML Glossary" = https://developers.google.com/machine-learning/glossary
"Kaplan 2020" = J. Kaplan et al. (OpenAI), "Scaling Laws for Neural Language Models," arXiv:2001.08361: https://arxiv.org/abs/2001.08361
"Chinchilla" = J. Hoffmann et al. (DeepMind), "Training Compute-Optimal Large Language Models," arXiv:2203.15556 (March 2022): https://arxiv.org/abs/2203.15556
"Llama 3 paper" = Llama Team, AI @ Meta, "The Llama 3 Herd of Models," arXiv:2407.21783 (July 2024): https://arxiv.org/abs/2407.21783
"Holtzman 2019" = A. Holtzman, J. Buys, L. Du, M. Forbes & Y. Choi, "The Curious Case of Neural Text Degeneration," ICLR 2020, arXiv:1904.09751: https://arxiv.org/abs/1904.09751
"Wolfram 2023" = Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?", 14 Feb 2023: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/
"Parrots" = E. M. Bender, T. Gebru, A. McMillan-Major & S. Shmitchell, "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?", FAccT '21 (3–10 March 2021), read in full: https://dl.acm.org/doi/10.1145/3442188.3445922
"InstructGPT" = L. Ouyang et al. (OpenAI), "Training language models to follow instructions with human feedback," arXiv:2203.02155 (4 March 2022): https://arxiv.org/abs/2203.02155
"OpenAI ChatGPT 2022" = OpenAI, "Introducing ChatGPT," 30 Nov 2022: https://openai.com/index/chatgpt/
"CAI" = Y. Bai et al. (Anthropic), "Constitutional AI: Harmlessness from AI Feedback," arXiv:2212.08073 (15 Dec 2022): https://arxiv.org/abs/2212.08073
"Lost in the Middle" = N. F. Liu et al. (Stanford et al.), "Lost in the Middle: How Language Models Use Long Contexts," arXiv:2307.03172 (*TACL*): https://arxiv.org/abs/2307.03172
"Kalai 2025" = A. T. Kalai, O. Nachum, S. S. Vempala & E. Zhang, "Why Language Models Hallucinate," arXiv:2509.04664 (4 Sept 2025): https://arxiv.org/abs/2509.04664
"OpenAI hallucination blog" = OpenAI, "Why language models hallucinate," 5 Sept 2025: https://openai.com/index/why-language-models-hallucinate/
"Mata" = *Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC), Opinion and Order on Sanctions, S.D.N.Y., 22 June 2023 (ECF 54), read in full: https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf
"Wei CoT" = J. Wei et al. (Google), "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," NeurIPS 2022, arXiv:2201.11903: https://arxiv.org/abs/2201.11903
"Kojima" = T. Kojima, S. S. Gu, M. Reid, Y. Matsuo & Y. Iwasawa (Univ. of Tokyo / Google), "Large Language Models are Zero-Shot Reasoners," NeurIPS 2022, arXiv:2205.11916: https://arxiv.org/abs/2205.11916
"OpenAI o1" = OpenAI, "Learning to reason with LLMs," 12 Sept 2024: https://openai.com/index/learning-to-reason-with-llms/
"R1 v1" / "R1 v2" = DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning," arXiv:2501.12948 — v1 dated 22 Jan 2025, v2 dated 4 Jan 2026 (numbers differ between versions; each is labelled): https://arxiv.org/abs/2501.12948
"Mapping the Mind" = Anthropic, "Mapping the Mind of a Large Language Model," 21 May 2024: https://www.anthropic.com/research/mapping-mind-language-model
"Scaling Monosemanticity" = A. Templeton, T. Conerly et al., "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet," Transformer Circuits Thread, 21 May 2024: https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html
"Golden Gate Claude" = Anthropic, "Golden Gate Claude," 23 May 2024: https://www.anthropic.com/news/golden-gate-claude
"Tracing" = Anthropic, "Tracing the thoughts of a large language model," 27 March 2025: https://www.anthropic.com/research/tracing-thoughts-language-model
"Biology 2025" = J. Lindsey et al., "On the Biology of a Large Language Model," Transformer Circuits Thread, 27 March 2025: https://transformer-circuits.pub/2025/attribution-graphs/biology.html
"Superposition" = N. Elhage et al. (Anthropic/Harvard), "Toy Models of Superposition," 14 Sept 2022, arXiv:2209.10652: https://transformer-circuits.pub/2022/toy_model/index.html
"Mitchell & Krakauer" = M. Mitchell & D. Krakauer (Santa Fe Institute), "The Debate Over Understanding in AI's Large Language Models," *PNAS* 2023, arXiv:2210.13966: https://arxiv.org/abs/2210.13966
"Hinton 60 Minutes" = CBS News transcript, "Geoffrey Hinton on the promise, risks of artificial intelligence," first broadcast 8 Oct 2023: https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/
"Wei Emergent" = J. Wei et al., "Emergent Abilities of Large Language Models," *TMLR* (08/2022), arXiv:2206.07682: https://arxiv.org/abs/2206.07682
"Mirage" = R. Schaeffer, B. Miranda & S. Koyejo (Stanford), "Are Emergent Abilities of Large Language Models a Mirage?", arXiv:2304.15004: https://arxiv.org/abs/2304.15004
"IEA 2025" = International Energy Agency, *Energy and AI*, executive summary (April 2025): https://www.iea.org/reports/energy-and-ai/executive-summary
"Turing 1950" = A. M. Turing, "Computing Machinery and Intelligence," *Mind* (1950), read in full (UMBC copy): https://courses.cs.umbc.edu/471/papers/turing.pdf

> Corrections to the brief:
> - **"It searches the internet for every answer" — no.** The original ChatGPT (30 Nov 2022) was "fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022" and answered from what it had learned (OpenAI ChatGPT 2022). A separate search feature, "ChatGPT search," arrived on 31 October 2024 and "leverages third-party search providers" (OpenAI: https://openai.com/index/introducing-chatgpt-search/). Without that tool, a model only knows its training data up to a cutoff (GPT-4o: "data up to October 2023," GPT-4o System Card: https://openai.com/index/gpt-4o-system-card/). Claude's 2024 system prompt said plainly: "Claude cannot open URLs, links, or videos." Say: "sometimes it looks things up; mostly it answers from memory of its reading."
> - **"It understands" / "it doesn't understand" — neither is settled fact.** In a 2022 survey of 480 language-AI researchers, 51% agreed that a model trained only on text could understand language "in some non-trivial sense," and 49% disagreed (Mitchell & Krakauer). Hinton says "I believe it definitely understands" (Hinton 60 Minutes); LeCun and Browning call it "a shallow understanding" (Noema 2022). Present it as an open question.
> - **"The strawberry problem means it's stupid" — no, it mostly means it reads in tokens, not letters.** In our tiktoken run, " strawberry" (with a leading space, as it appears mid-sentence) is a single token in GPT-2, GPT-4 and GPT-4o tokenizers. The model never "sees" the three r's unless it spells the word out. OpenAI's own o1 launch demo (12 Sept 2024) ended with o1 decoding a cipher to "THERE ARE THREE R'S IN STRAWBERRY" (OpenAI o1). OpenAI's own researchers also note models miscounting letters ("How many Ds are in DEEPSEEK?" got answers from 2 to 7; Kalai 2025).
> - **"Parameters = facts it knows" — no.** A parameter is one of "the weights and biases that a model learns during training" (Google ML Glossary), more like the strength of one connection. Concepts are spread out: "each concept is represented across many neurons, and each neuron is involved in representing many concepts" (Mapping the Mind). Also: OpenAI has never published GPT-4's size. The GPT-4 Technical Report "contains no further details about the architecture (including model size)" (arXiv:2303.08774). Numbers like "over 1 trillion" are outside estimates (MIT Technology Review 2025).
> - **"ChatGPT was the first chatbot" — no.** ELIZA ran at MIT in the mid-1960s and was described in January 1966 (ELIZA 1966; NYT Weizenbaum). Smithsonian (2026) calls it "now recognized as the first chatbot." The word "chatbot" itself only emerged in the 1990s, as short for "chatterbot" (Smithsonian 2026).
> - **Chinchilla's "20 tokens per parameter" is not a sentence in the paper.** The paper's rule is "for every doubling of model size the number of training tokens should also be doubled." The ~20:1 ratio is read off its numbers: Chinchilla itself is 70B parameters on 1.4 trillion tokens, and its Table 3 lists 1 billion parameters → 20.2 billion tokens (Chinchilla). Say "about twenty words of reading per parameter, by the paper's own table."
> - **Energy: the old "3 watt-hours, ten times a Google search" figure is a 2023 estimate.** Newer figures are about ten times lower: Epoch AI estimated ~0.3 Wh (Feb 2025), Sam Altman wrote 0.34 Wh (June 2025), Google measured 0.24 Wh for a median Gemini text prompt (Aug 2025). All of these are company or outside estimates. Google's own footnote says its data "have not been verified by an independent third-party."
> - **Memory: the model itself has no memory between chats.** ChatGPT's "memory" is a product feature (first tested 13 Feb 2024) that saves notes and past-chat insights and feeds them back in. Since the 10 April 2025 update it "references all your past conversations" for Plus/Pro users unless turned off (OpenAI memory post). So "it forgets everything" is no longer true of the app, though it is still true of the underlying model.
> - **DeepSeek-R1's "$294,000" is only the reasoning-training step.** The R1 v2 paper's table ($294K at $2 per H800 GPU-hour) covers R1-Zero, SFT data and R1. It sits on top of the DeepSeek-V3 base model, whose own reported training cost was $5.576M, which "include[s] only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments" (arXiv:2412.19437).
> - **DeepSeek-R1 numbers changed between versions.** The AIME jump for R1-Zero is "15.6% to 71.0%" in v1 (22 Jan 2025) and "15.6% to 77.9%" in v2 (Jan 2026). Use v1 numbers for a "January 2025" story.
> - **Golden Gate Claude** was Claude 3 Sonnet with one feature turned up, and it was public for just 24 hours (Golden Gate Claude, 23 May 2024). It was not a separate model or a prompt.
> - **"Shmargaret Shmitchell"** is the fourth author's name exactly as printed on the Stochastic Parrots paper (a pseudonym). We did not verify who it is, so don't name a person.
> - **ELIZA's computer:** the paper says it ran on MIT's "MAC time-sharing system" and was written in MAD-SLIP. The machine number in our scan is garbled, so don't name the IBM model. "Named after Eliza Doolittle" is the NYT's wording. The 1966 paper only compares it to "the Eliza of Pygmalion fame."
> - **"1 billion weekly users"**: the last figure confirmed in a reliable outlet is **900 million weekly active users (27 Feb 2026)**. Reports of "over 1 billion" in Aug–Sept 2026 conflict on dates; see UNCERTAIN.

---

## 0. Intro toolkit — the words we will use

- **Token:** "In a language model, the atomic unit that the model is training on and making predictions on." It can be a word, a piece of a word or a single character. — Google ML Glossary
- OpenAI's own wording: "Tokens are the building blocks of text that OpenAI models process. They can be as short as a single character or as long as a full word." — OpenAI tokens
- **Parameter:** "The weights and biases that a model learns during training." — Google ML Glossary
- **Weight:** "A value that a model multiplies by another value." — Google ML Glossary
- MIT Technology Review's plain version: parameters are "essentially the adjustable 'knobs' in an AI model that allow it to make predictions." — MIT Technology Review, "We did the math on AI's energy footprint" (20 May 2025): https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/
- **Model:** "any mathematical construct that processes input data and returns output… the set of parameters and structure needed for a system to make predictions." — Google ML Glossary
- **Training:** "The process of determining the ideal parameters (weights and biases) comprising a model. During training, a system reads in examples and gradually adjusts parameters." — Google ML Glossary
- **Prompt:** "Any text entered as input to a large language model to condition the model to behave in a certain way. Prompts can be as short as a phrase or arbitrarily long (for example, the entire text of a novel)." — Google ML Glossary
- **Context window:** "The number of tokens a model can process in a given prompt." — Google ML Glossary
- **Temperature:** "A hyperparameter that controls the degree of randomness of a model's output. Higher temperatures result in more random output, while lower temperatures result in less random output." — Google ML Glossary
- **Large language model:** "At a minimum, a language model having a very high number of parameters. More informally, any Transformer-based language model, such as Gemini or GPT." — Google ML Glossary
- **Hallucination:** "The production of plausible-seeming but factually incorrect output by a generative AI model that purports to be making an assertion about the real world." — Google ML Glossary
- The name: GPT stands for "Generative Pre-trained Transformer" (the three ideas of this video: it generates, it was pre-trained on text, it is a Transformer). — **UNCERTAIN (standard expansion; not quoted from an OpenAI page we read)**
- ChatGPT's launch post: "We've trained a model called ChatGPT which interacts in a conversational way. The dialogue format makes it possible for ChatGPT to answer followup questions, admit its mistakes, challenge incorrect premises, and reject inappropriate requests." (30 Nov 2022) — OpenAI ChatGPT 2022
- "ChatGPT is a sibling model to InstructGPT." "During the research preview, usage of ChatGPT is free." — OpenAI ChatGPT 2022
- **How many people use it:** on 27 Feb 2026, "ChatGPT has reached 900 million weekly active users, OpenAI announced Friday," up from 800 million in October 2025. OpenAI also reported 50 million paying subscribers. The announcement was in an OpenAI post titled "Scaling AI for Everyone." — TechCrunch (Aisha Malik, 27 Feb 2026): https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users
- In August–September 2026 several outlets reported that ChatGPT had passed **1 billion weekly users**, but the dates and wording conflict (31 July, 6 Aug, 8 Sept 2026), and The Next Web (29 July 2026) said it was "on the verge." — Yahoo Tech/StockTwits (6 Aug 2026): https://tech.yahoo.com/ai/chatgpt/articles/chatgpt-tops-1b-weekly-users-191537749.html ; The Next Web: https://thenextweb.com/news/chatgpt-1-billion-weekly-active-users-openai-target **UNCERTAIN (safe line: "close to a billion people a week")**
- OpenAI reports **weekly** users, not monthly or daily. — TechCrunch 2026 (above) **UNCERTAIN (stated in search summaries; consistent with every OpenAI figure we saw)**
- A calm framing line from Hinton: "We have a very good idea of sort of roughly what it's doing. But as soon as it gets really complicated, we don't actually know what's going on any more than we know what's going on in your brain." — Hinton 60 Minutes
- Hinton: "What we did was we designed the learning algorithm. That's a bit like designing the principle of evolution. But when this learning algorithm then interacts with data, it produces complicated neural networks that are good at doing things. But we don't really understand exactly how they do those things." — Hinton 60 Minutes
- Anthropic's Dario Amodei (April 2025): "As my friend and co-founder Chris Olah is fond of saying, generative AI systems are grown more than they are built—their internal mechanisms are 'emergent' rather than directly designed. It's a bit like growing a plant or a bacterial colony." — Dario Amodei, "The Urgency of Interpretability": https://www.darioamodei.com/post/the-urgency-of-interpretability

## 1. Talking to Something (ELIZA, 1966; what happens when you press Enter)

- Weizenbaum's 1966 paper: "ELIZA is a program which makes natural language conversation with a computer possible. Its present implementation is on the MAC time-sharing system at MIT." It was written in MAD-SLIP. — ELIZA 1966
- On the name: "Its name was chosen to emphasize that it may be incrementally improved by its users, since its language abilities may be continually improved by a 'teacher'. Like the Eliza of Pygmalion fame, it can be made to appear even more civilized." — ELIZA 1966
- ELIZA was written while Weizenbaum was an MIT professor "in 1964 and 1965," and named after Eliza Doolittle of *Pygmalion* and *My Fair Lady*. — NYT Weizenbaum
- How it worked: "Input sentences are analyzed on the basis of decomposition rules which are triggered by key words appearing in the input text. Responses are generated by reassembly rules." — ELIZA 1966 (abstract)
- One small rule from the paper, quoted by Smithsonian: "'I am blah' can be transformed to 'How long have you been blah,' independently of the meaning of 'blah.'" — Smithsonian 2026
- When ELIZA found no keyword it fell back on gentle phrases like "please go on," "I see" or "tell me more." — Smithsonian 2026
- A quirk of 1966: users could not type a question mark, "because it is interpreted as a line delete character by the MAC system." A double carriage return handed the turn to ELIZA. — ELIZA 1966
- The famous opening of the sample conversation (machine replies in capitals): "Men are all alike." / "IN WHAT WAY" / "They're always bugging us about something or other." / "CAN YOU THINK OF A SPECIFIC EXAMPLE" / "Well, my boyfriend made me come here." / "YOUR BOYFRIEND MADE YOU COME HERE" / "He says I'm depressed much of the time." / "I AM SORRY TO HEAR YOU ARE DEPRESSED" — ELIZA 1966
- The scripts made ELIZA "respond roughly as would certain psychotherapists (Rogerians)." — ELIZA 1966 (as also quoted by Smithsonian 2026)
- The paper's opening: "once a particular program is unmasked, once its inner workings are explained in language sufficiently plain to induce understanding, its magic crumbles away; it stands revealed as a mere collection of procedures, each quite comprehensible." — ELIZA 1966
- And its warning: "ELIZA shows, if nothing else, how easy it is to create and maintain the illusion of understanding, hence perhaps of judgment deserving of credibility. A certain danger lurks there." — ELIZA 1966
- Weizenbaum "was stunned to discover that his students and others became deeply engrossed in conversations with the program, occasionally revealing intimate personal details." — NYT Weizenbaum
- MIT's Robert Fano: "It was amazing the extent that people did not understand they were talking to a computer." A group of MIT scientists, including Claude Shannon, met in Concord, Massachusetts, to discuss it. — NYT Weizenbaum
- **The ELIZA effect, in his own words (1976):** "What I had not realized is that extremely short exposures to a relatively simple computer program could induce powerful delusional thinking in quite normal people." — Weizenbaum, *Computer Power and Human Reason* (1976), as quoted in Smithsonian 2026 **UNCERTAIN (book not read directly; wording identical across sources)**
- He went on: "This insight led me to attach new importance to questions of the relationships between the individual and the computer, and hence to resolve to think about them." — same, via Smithsonian 2026 **UNCERTAIN (same reason)**
- Today the "Eliza effect" means "our human tendency to attribute understanding and agency to machines with even the faintest hint of humanlike language or behavior." — Mitchell & Krakauer
- **Pressing Enter, step 1 — tokenize:** your text "is split into tokens. The model processes these tokens. The response is generated as a sequence of tokens, then converted back to text." — OpenAI tokens
- **Step 2 — embeddings:** each token is turned into a long list of numbers (an embedding). In GPT-3 that list is 12,288 numbers long (d_model = 12,288). — GPT-3 paper, Table 2.1
- **Step 3 — many layers:** GPT-3's largest model has 96 layers stacked one on another, each with attention. — GPT-3 paper, Table 2.1
- **Step 4 — probabilities:** at each step the model "gets a list of words with probabilities." — Wolfram 2023
- **Step 5 — pick one and repeat:** "what it's essentially doing is just asking over and over again 'given the text so far, what should the next word be?'—and each time adding a word." (More precisely a token, "which is why it can sometimes 'make up new words'.") — Wolfram 2023
- **Autoregressive:** GPT-3 is "an autoregressive language model with 175 billion parameters"; it writes one token at a time, each prediction conditioned on everything before. — GPT-3 paper
- Anthropic: "Claude writes text one word at a time. Is it only focusing on predicting the next word or does it ever plan ahead?" (The answer, chapter 11: it sometimes plans ahead.) — Tracing
- Hinton on "just predicting the next word": "it's true they're just trying to predict the next word. But if you think about it, to predict the next word you have to understand the sentences." — Hinton 60 Minutes
- Reasoning models add a hidden step: some models spend "reasoning tokens," "extra 'thinking steps'… included internally before producing the final output." — OpenAI tokens

## 2. Cutting Words Into Pieces (tokens, byte-pair encoding)

- OpenAI's rules of thumb for English: "1 token ≈ 4 characters," "1 token ≈ ¾ of a word," "100 tokens ≈ 75 words," "1–2 sentences ≈ 30 tokens," "1 paragraph ≈ 100 tokens," "~1,500 words ≈ 2,048 tokens." — OpenAI tokens (Wayback 2025 snapshot; this resolves the ML sheet's UNCERTAIN item)
- OpenAI's examples: Wayne Gretzky's "You miss 100% of the shots you don't take" = 11 tokens; the US Declaration of Independence = 1,695 tokens. — OpenAI tokens
- Tokens care about spaces and capitals: OpenAI's example shows " red" (with a leading space), " Red" and "Red" at the start of a sentence all getting different token numbers. — OpenAI tokens
- "The more probable/frequent a token is, the lower the token number assigned to it." The full stop is token 13 in all three sentences. — OpenAI tokens
- **Where tokenizing came from:** Byte Pair Encoding (BPE) began as data compression. Philip Gage, "A New Algorithm for Data Compression," *C Users Journal* 12(2): 23–38, February 1994. — reference list in Sennrich 2016
- Sennrich et al. describe it: "a simple data compression technique that iteratively replaces the most frequent pair of bytes in a sequence with a single, unused byte. We adapt this algorithm for word segmentation." — Sennrich 2016
- How it builds a vocabulary: start with single characters, "iteratively count all symbol pairs and replace each occurrence of the most frequent pair ('A', 'B') with a new symbol 'AB'… Frequent character n-grams (or whole words) are eventually merged into a single symbol." — Sennrich 2016
- The Edinburgh team (Rico Sennrich, Barry Haddow, Alexandra Birch) wanted to translate "rare and unknown words as sequences of subword units," like the German compound "Abwasser|behandlungs|anlage" ('sewage water treatment plant'). — Sennrich 2016 (the arXiv text prints "anlange," a typo)
- GPT-2 (2019) used byte-level BPE with a vocabulary "expanded to 50,257." It also raised the context from 512 to 1,024 tokens. — GPT-2 paper
- GPT-3 reused GPT-2's tokenization ("We use the same model and architecture as GPT-2… and reversible tokenization"). — GPT-3 paper
- Newer vocabularies, from OpenAI's tiktoken code: GPT-3.5-turbo and GPT-4 use "cl100k_base"; GPT-4o, GPT-4.1, o1/o3 and GPT-5 use "o200k_base." — tiktoken model.py: https://github.com/openai/tiktoken/blob/main/tiktoken/model.py
- Counting the published vocabulary files: cl100k_base has 100,256 ordinary tokens; o200k_base has 199,998 (plus a few special tokens). — our count of the files at https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken and …/o200k_base.tiktoken (linked from tiktoken's openai_public.py)
- **Strawberry, tokenized (our tiktoken run):** "strawberry" at the start of text = 3 tokens: "st | raw | berry" (GPT-2 and GPT-4o tokenizers) or "str | aw | berry" (GPT-4's cl100k). " strawberry" with a leading space, as in a sentence = 1 token in all three. — our tiktoken run
- So the question "How many r are in strawberry?" is just 7 tokens to GPT-4o: How | many | r | are | in | strawberry | ?. The word arrives as one sealed piece. — our tiktoken run
- Other small examples (GPT-4o tokenizer): "Good night." = 3 tokens; "unbelievable" = 3 (un | bel | ievable) but " unbelievable" with a space = 1; "Supercalifragilisticexpialidocious" = 10. — our tiktoken run
- The video title "Every Confusing Thing About ChatGPT Explained Slowly (For Sleep)" is 64 characters and 13 tokens for GPT-4o; "ChatGPT" itself is two tokens, " Chat" and "GPT". — our tiktoken run
- **Why letter-counting is hard:** OpenAI researchers report that asked "How many Ds are in DEEPSEEK? If you know, just say the number with no commentary," DeepSeek-V3 "returned '2' or '3' in ten independent trials; Meta AI and Claude 3.7 Sonnet performed similarly, including answers as large as '6' and '7'." — Kalai 2025
- **Other languages cost more tokens.** OpenAI: "Cómo estás" (Spanish for "How are you") "contains 5 tokens for 10 characters. Non-English text often produces a higher token-to-character ratio, which can affect costs and limits." — OpenAI tokens
- Oxford study: "The same text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases." — Petrov 2023
- The tokenizer used by ChatGPT and GPT-4 "uses about 1.6 times more tokens to encode the same text in Italian as it does in English, 2.6 times for Bulgarian and 3 times for Arabic. For Shan—the native language of people from the Shan State in Myanmar—that difference can be as high as 15 times." — Petrov 2023
- Even the cheapest languages they tested (Portuguese, Pangasinan, German) "still see a premium of 50% when compared to English." — Petrov 2023
- One Shan word for "you" is built from one consonant and three diacritics, and ChatGPT's tokenizer splits it into 9 tokens. — Petrov 2023
- The unfairness reaches "the cost of accessing commercial language services, the processing time and latency, as well as the amount of content that can be provided as context." — Petrov 2023
- In our run, "Good night." is 3 tokens; Hungarian "Jó éjszakát." is 7; Japanese "おやすみなさい。" is 7; Hindi "शुभ रात्रि।" is 6 with GPT-4o's tokenizer but 13 with GPT-4's older one. Bigger vocabularies narrow the gap. — our tiktoken run

## 3. A Map of Meaning (embeddings)

- **Embedding vector:** "an array of floating-point numbers taken from any hidden layer that describe the inputs to that hidden layer." — Google ML Glossary
- GPT-3 (175B) represents each token as a list of **12,288** numbers (d_model). — GPT-3 paper, Table 2.1
- That number is 96 attention heads × 128 numbers per head (96 × 128 = 12,288). — GPT-3 paper, Table 2.1 (arithmetic ours)
- The smallest GPT-3 used 768 numbers per token; the largest, 12,288. — GPT-3 paper, Table 2.1
- Meta's Llama 3 405B (2024) uses "a token representation dimension of 16,384," 126 layers and 128 attention heads. — Llama 3 paper
- Google's picture of closeness: in an embedding space, the distance "from cow to bull is similar to the distance from ewe (female sheep) to ram (male sheep)." — Google ML Glossary (callback from the ML video)
- Callback: "vector('King') - vector('Man') + vector('Woman') results in a vector that is closest to the vector representation of the word Queen." — Mikolov et al. 2013, arXiv:1301.3781: https://arxiv.org/abs/1301.3781
- Inside a big model, concepts behave like directions: "we tend to think of neural network representations as being composed of features which are represented as directions." — Superposition
- Nearby meanings sit near each other inside Claude too: near a "Golden Gate Bridge" feature Anthropic found features for "Alcatraz Island, Ghirardelli Square, the Golden State Warriors, California Governor Gavin Newsom, the 1906 earthquake, and the San Francisco-set Alfred Hitchcock film Vertigo." — Mapping the Mind
- Near an "inner conflict" feature they found "relationship breakups, conflicting allegiances, logical inconsistencies, as well as the phrase 'catch-22'." — Mapping the Mind
- "This shows that the internal organization of concepts in the AI model corresponds, at least somewhat, to our human notions of similarity. This might be the origin of Claude's excellent ability to make analogies and metaphors." — Mapping the Mind
- At greater distances from the bridge, features for faraway tourist places appear, like "Médoc wine region, France" and "Isle of Skye, Scotland." "Distance in decoder space maps roughly onto relatedness in concept space." — Scaling Monosemanticity

## 4. Every Word Looks at Every Other (attention, the Transformer)

- "Attention Is All You Need," NIPS 2017 (Long Beach, California), by eight authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser and Illia Polosukhin. — Vaswani 2017
- Footnote: "Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea." — Vaswani 2017
- "Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail." "Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor." — Vaswani 2017 (footnote)
- "To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention" (no recurrence, no convolution). — Vaswani 2017
- **Attention in plain words:** "For each word in an input sequence, the network scores the relevance of the word to every element in the whole sequence of words. The relevance scores determine how much the word's final representation incorporates the representations of other words." — Google ML Glossary (self-attention)
- Google's example sentence: "The animal didn't cross the street because it was too tired." The attention layer learns to highlight the words that "it" might refer to. — Google ML Glossary
- Self-attention "uses dictionary lookup terminology, such as 'query', 'key', and 'value'." — Google ML Glossary
- **Multi-head:** "Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this." — Vaswani 2017
- The 2017 model used "h = 8 parallel attention layers, or heads," and a stack of "N = 6 identical layers" in each of its encoder and decoder. — Vaswani 2017
- GPT-3 (2020): 96 layers, 96 attention heads, each head 128 numbers wide. — GPT-3 paper, Table 2.1
- GPT-3 used "alternating dense and locally banded sparse attention patterns in the layers of the transformer, similar to the Sparse Transformer." — GPT-3 paper
- **Position:** "Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens." They add "positional encodings" to the embeddings. — Vaswani 2017
- Their position signals are waves: "each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2π to 10000 · 2π." — Vaswani 2017
- They chose waves because "it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training." Learned positions gave "nearly identical results." — Vaswani 2017
- **The cost grows with length:** the paper's table gives self-attention a cost per layer of O(n² · d): double the text, roughly four times the attention work. — Vaswani 2017, Table 1
- Stanford's summary: Transformers "require memory and compute that increases quadratically in sequence length. As a result, Transformer language models were often trained with relatively small context windows (between 512-2048 tokens)." — Lost in the Middle
- Transformers train faster partly because they are "more parallelizable": they look at all the words at once. — Vaswani 2017 (callback)
- The paper ends: "We are excited about the future of attention-based models and plan to apply them to other tasks." — Vaswani 2017
- The name: the three first collaborators wrote a design document called "Transformers: Iterative Self-Attention and Processing for Various Tasks." Uszkoreit says they picked "transformers" from "day zero." — Wired 2024
- The title: Llion Jones remembered that the Beatles "had named a song 'All You Need Is Love.' Why not call the paper 'Attention Is All You Need'?" — Wired 2024

## 5. The Library It Read (pre-training data, scaling laws, Chinchilla, GPUs)

- **Pre-training** means "predicting the next word in huge amounts of text. Unlike traditional machine learning problems, there are no 'true/false' labels attached to each statement. The model sees only positive examples of fluent language." — OpenAI hallucination blog
- GPT-3's training mix (tokens / weight in training mix): filtered Common Crawl 410 billion / 60%; WebText2 19 billion / 22%; Books1 12 billion / 8%; Books2 55 billion / 8%; Wikipedia 3 billion / 3%. — GPT-3 paper, Table 2.2
- So English Wikipedia, all of it, was only about 3% of what GPT-3 read. — GPT-3 paper, Table 2.2
- The Common Crawl part came from "41 shards of monthly CommonCrawl covering 2016 to 2019, constituting 45TB of compressed plaintext before filtering and 570GB after filtering, roughly equivalent to 400 billion byte-pair-encoded tokens." — GPT-3 paper
- Common Crawl alone is "nearly a trillion words." OpenAI filtered it "based on similarity to a range of high-quality reference corpora" and removed near-duplicates. — GPT-3 paper
- Better sources were re-read: "CommonCrawl and Books2 datasets are sampled less than once during training, but the other datasets are sampled 2-3 times." — GPT-3 paper
- "All models were trained for a total of 300 billion tokens." — GPT-3 paper
- GPT-3's training compute: 3.14 × 10²³ floating-point operations (3.64 × 10³ petaflop/s-days). — GPT-3 paper, Appendix D table
- GPT-3 "consumed several thousand petaflop/s-days of compute during pre-training, compared to tens of petaflop/s-days for a 1.5B parameter GPT-2 model." — GPT-3 paper, §6.3
- Hardware: "All models were trained on V100 GPU's on part of a high-bandwidth cluster provided by Microsoft." The paper does not say how many days it took. — GPT-3 paper
- Microsoft's May 2020 announcement: "The supercomputer developed for OpenAI is a single system with more than 285,000 CPU cores, 10,000 GPUs and 400 gigabits per second of network connectivity for each GPU server." It ranked in the top five of the TOP500 list, Microsoft said. — Microsoft News, 19 May 2020: https://news.microsoft.com/source/features/ai/openai-azure-supercomputer/
- That the GPT-3 run used this exact machine is not stated in the GPT-3 paper. — **UNCERTAIN (commonly assumed; not confirmed in a primary source we read)**
- ChatGPT and GPT-3.5 "were trained on an Azure AI supercomputing infrastructure." — OpenAI ChatGPT 2022
- GPT-4 (14 March 2023): the technical report "contains no further details about the architecture (including model size), hardware, training compute, dataset construction, training method, or similar," citing "the competitive landscape and the safety implications." — GPT-4 Technical Report, arXiv:2303.08774: https://arxiv.org/abs/2303.08774
- **Scaling laws (Kaplan et al., OpenAI, January 2020):** "The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude." — Kaplan 2020
- "Other architectural details such as network width or depth have minimal effects within a wide range." — Kaplan 2020
- "Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence." — Kaplan 2020
- GPT-3 followed this advice: "we train much larger models on many fewer tokens than is typical." — GPT-3 paper (Figure 2.2 caption)
- **Chinchilla (DeepMind, March 2022)** disagreed: "We find that current large language models are significantly undertrained." — Chinchilla
- They trained "over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens." — Chinchilla
- Their rule: "for every doubling of model size the number of training tokens should also be doubled." — Chinchilla
- Chinchilla itself: 70 billion parameters, 1.4 trillion tokens, the same compute as the 280-billion-parameter Gopher, with "4× more" data. It "uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B)." — Chinchilla
- The ~20 tokens per parameter rule of thumb is read off their numbers (1.4 trillion ÷ 70 billion = 20; Table 3: 1 billion parameters → 20.2 billion tokens; 10 billion → 205.1 billion). — Chinchilla (division ours)
- By that table, a compute-optimal 175-billion-parameter model would want about 3.7 trillion tokens. GPT-3 had 300 billion. — Chinchilla, Tables 1 and 3
- **Later official numbers:** Meta's Llama 3 405B was "pre-trained using 3.8 × 10²⁵ FLOPs, almost 50× more than the largest version of Llama 2," on "15.6T text tokens." — Llama 3 paper
- "Llama 3 405B is trained on up to 16K H100 GPUs, each running at 700W TDP with 80GB HBM3." — Llama 3 paper
- During a 54-day snapshot of Llama 3 training there were 466 interruptions; 419 were unexpected, and about 78% of those came from confirmed or suspected hardware problems. GPUs were the biggest single cause (58.7%). — Llama 3 paper
- When tens of thousands of GPUs pause or start together, power use can swing "on the order of tens of megawatts, stretching the limits of the power grid." — Llama 3 paper
- DeepSeek-V3 (Dec 2024): "671B total parameters with 37B activated for each token," trained on 14.8 trillion tokens, "only 2.788M H800 GPU hours," which at $2 per GPU-hour is $5.576M. That figure excludes "prior research and ablation experiments." — DeepSeek-V3 Technical Report, arXiv:2412.19437: https://arxiv.org/abs/2412.19437
- **GPUs** are chips first made for video-game graphics. They are good at doing huge numbers of simple multiplications at once, which is what a neural network needs. — **UNCERTAIN (general background; no single primary quote checked for this video)**

## 6. Choosing the Next Word (probabilities, temperature, top-p, Stochastic Parrots)

- At the very end, the model turns its scores into "predicted next-token probabilities" using a "softmax function." — Vaswani 2017 (§3.4)
- With GPT-3's style of tokenizer, that is a probability for each of about 50,000 tokens (GPT-2's vocabulary: 50,257), every single step. — GPT-2 paper; GPT-3 paper (tokenizer reused)
- Wolfram: you might think it should always pick the top word. "But this is where a bit of voodoo begins to creep in… if we always pick the highest-ranked word, we'll typically get a very 'flat' essay." — Wolfram 2023
- "The fact that there's randomness here means that if we use the same prompt multiple times, we're likely to get different essays each time." — Wolfram 2023
- "There's a particular so-called 'temperature' parameter that determines how often lower-ranked words will be used, and for essay generation, it turns out that a 'temperature' of 0.8 seems best." He adds: "there's no 'theory' being used here; it's just a matter of what's been found to work in practice." — Wolfram 2023
- Temperature in the research papers: dividing the scores by a temperature t before the softmax; "Setting t ∈ [0, 1) skews the distribution towards high probability events." Lowering it "improves generation quality" but "comes at the cost of decreasing diversity." — Holtzman 2019, §3.3
- The temperature idea itself is borrowed from physics-inspired neural networks of the 1980s (they cite Ackley et al., 1985, the Boltzmann machine paper). — Holtzman 2019 **UNCERTAIN (the citation is in the paper; "borrowed from physics" is our gloss)**
- **Top-p / nucleus sampling** (Holtzman, Buys, Du, Forbes and Choi, University of Washington and Allen Institute for AI; first posted April 2019, published at ICLR 2020). — Holtzman 2019
- The problem they named: "maximization-based decoding methods such as beam search lead to degeneration — output text that is bland, incoherent, or gets stuck in repetitive loops." — Holtzman 2019
- The fix: "truncating the unreliable tail of the probability distribution, sampling from the dynamic nucleus of tokens containing the vast majority of the probability mass." — Holtzman 2019
- The "unreliable tail" is "tens of thousands of candidate tokens with relatively low probability that are over-represented in the aggregate." The nucleus is "a small subset of the vocabulary that tends to range between one and a thousand candidates." — Holtzman 2019
- Their famous test prompt: "In a shocking finding, scientist discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English." Greedy beam search on GPT-2 got stuck repeating "Universidad Nacional Autónoma de México" over and over. — Holtzman 2019, Figure 1
- **A gentle truth about people:** "Natural language rarely remains in a high probability zone for multiple consecutive time steps, instead veering into lower-probability but more informative tokens." — Holtzman 2019
- "Why is human-written text not the most probable text? We conjecture that this is an intrinsic property of human language." People "optimize against stating the obvious." — Holtzman 2019
- **Why the same question gives different answers:** OpenAI's 2022 launch post: "ChatGPT is sensitive to tweaks to the input phrasing or attempting the same prompt multiple times. For example, given one phrasing of a question, the model can claim to not know the answer, but given a slight rephrase, can answer correctly." — OpenAI ChatGPT 2022
- **"Stochastic Parrots"** (FAccT '21, held virtually, 3–10 March 2021) by Emily M. Bender, Timnit Gebru, Angelina McMillan-Major and "Shmargaret Shmitchell." — Parrots
- Its definition: "Contrary to how it may seem when we observe its output, an LM is a system for haphazardly stitching together sequences of linguistic forms it has observed in its vast training data, according to probabilistic information about how they combine, but without any reference to meaning: a stochastic parrot." — Parrots, §6.1 ("Contrary" begins the sentence on the page before; the rest is verbatim)
- "We say seemingly coherent because coherence is in fact in the eye of the beholder." — Parrots
- The paper also warned about energy, cost and who bears it: "It is past time for researchers to prioritize energy efficiency and cost to reduce negative environmental impact and inequitable access to resources." — Parrots, as quoted by MIT Technology Review, 4 Dec 2020: https://www.technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-out-timnit-gebru/
- **The debate:** Hinton answered the "auto-complete" view directly: "the idea they're just predicting the next word so they're not intelligent is crazy. You have to be really intelligent to predict the next word really accurately." — Hinton 60 Minutes
- On the other side, Browning and LeCun (2022): "A system trained on language alone will never approximate human intelligence, even if trained from now until the heat death of the universe." — Jacob Browning & Yann LeCun, "AI And The Limits Of Language," *Noema*, 23 Aug 2022: https://www.noemamag.com/ai-and-the-limits-of-language

## 7. Learning Its Manners (InstructGPT, RLHF, Constitutional AI, system prompts)

- The problem: "Making language models bigger does not inherently make them better at following a user's intent." — InstructGPT (abstract)
- Why: the old goal, "predicting the next token on a webpage from the internet—is different from the objective 'follow the user's instructions helpfully and safely'… we say that the language modeling objective is misaligned." — InstructGPT
- **RLHF's roots:** Christiano, Leike, Brown, Martic, Legg and Amodei (OpenAI and DeepMind, 2017), "Deep Reinforcement Learning from Human Preferences." A simulated robot learned to do backflips from people comparing short video clips: "trained using 900 queries in less than an hour." — arXiv:1706.03741: https://arxiv.org/abs/1706.03741
- **InstructGPT (4 March 2022)**, three steps: "Step 1: Collect demonstration data, and train a supervised policy. Step 2: Collect comparison data, and train a reward model. Step 3: Optimize a policy against the reward model using PPO." — InstructGPT
- "We first hire a team of 40 contractors to label our data." They were hired "on Upwork and through ScaleAI." — InstructGPT
- The labellers were "mostly English-speaking people living in the United States or Southeast Asia." "They disagree with each other on many examples; we found the inter-labeler agreement to be about 73%." — InstructGPT
- Sizes: the demonstration dataset had "about 13k training prompts," the reward-model dataset "33k," and the RL dataset "31k" prompts. — InstructGPT
- For the reward model, labellers ranked between 4 and 9 answers at once (K = 4 to K = 9). — InstructGPT
- The headline: "outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters." — InstructGPT
- The 175B InstructGPT was preferred to 175B GPT-3 "85 ± 3% of the time." — InstructGPT
- Truthfulness roughly doubled on TruthfulQA, and on summary-style tasks InstructGPT made things up "about half as often as GPT-3 (a 21% vs. 41% hallucination rate)." — InstructGPT
- They called the small loss of skill on some tests an "alignment tax." — InstructGPT
- The authors admitted whose taste they were teaching: "we are aligning to demonstrations and preferences provided by our training labelers" and "to our preferences, as the researchers designing this study." — InstructGPT
- **ChatGPT's own recipe (2022):** "human AI trainers provided conversations in which they played both sides—the user and an AI assistant." Then trainers ranked alternative replies, a reward model learned the rankings, and "We performed several iterations of this process." — OpenAI ChatGPT 2022
- OpenAI on a side effect: the model "is often excessively verbose and overuses certain phrases, such as restating that it's a language model trained by OpenAI… (trainers prefer longer answers that look more comprehensive)." — OpenAI ChatGPT 2022
- "Ideally, the model would ask clarifying questions when the user provided an ambiguous query. Instead, our current models usually guess what the user intended." — OpenAI ChatGPT 2022
- **Constitutional AI (Anthropic, 15 Dec 2022):** "The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'." — CAI
- How it works: the model writes an answer, critiques it, revises it, and is trained on the revisions. Then an AI compares pairs of answers, and that becomes the reward: "'RL from AI Feedback' (RLAIF)." — CAI
- The aim was "a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them." — CAI
- They used "a total of 16 different principles," and admitted: "These principles were chosen in a fairly ad hoc and iterative way for research purposes." — CAI
- Anthropic's published constitution (9 May 2023) drew from "the UN Declaration of Human Rights, trust and safety best practices, principles proposed by other AI research labs (e.g., Sparrow Principles from DeepMind), an effort to capture non-western perspectives." It also borrowed from "Apple's terms of service." — Anthropic, "Claude's Constitution": https://www.anthropic.com/news/claudes-constitution
- One principle: "Please choose the response that most supports and encourages freedom, equality, and a sense of brotherhood." — Anthropic, "Claude's Constitution"
- Another: "Choose the response that a wise, ethical, polite, and friendly person would more likely say." — Anthropic, "Claude's Constitution"
- **System prompts:** "Claude's web interface (Claude.ai) and mobile apps use a system prompt to provide up-to-date information, such as the current date, to Claude at the start of every conversation." — Anthropic system prompt release notes (2024 snapshot): https://docs.anthropic.com/en/release-notes/system-prompts
- The July 2024 Claude 3.5 Sonnet prompt began: "The assistant is Claude, created by Anthropic. The current date is {}. Claude's knowledge base was last updated on April 2024." — same
- The same July 2024 Claude 3.5 Sonnet prompt included: "Claude is very smart and intellectually curious. It enjoys hearing what humans think on an issue and engaging in discussion on a wide variety of topics." — same
- The Claude 3 Opus prompt (2024) told it that for "very obscure" topics it should end "with a succinct reminder that it may hallucinate in response to questions like this, and it uses the term 'hallucinate' to describe this as the user will understand what it means." — same
- Anthropic began publishing these prompts on 26 August 2024; TechCrunch called it a first for a major AI vendor. — TechCrunch via Yahoo: https://finance.yahoo.com/news/anthropic-publishes-system-prompts-claude-194852252.html **UNCERTAIN (date and "first" claim seen via search summaries)**
- Anthropic itself drew the line between a prompt and deeper changes: telling a model to "pretend it's a bridge" with a "system prompt that attaches extra text to every input" is different from changing its insides. — Golden Gate Claude

## 8. A Memory With Edges (context windows, memory, Lost in the Middle)

- Context window sizes over time (all official):
  - GPT-2 (2019): 1,024 tokens ("increase the context size from 512 to 1024 tokens"). — GPT-2 paper
  - GPT-3 (2020): "All models use a context window of nctx = 2048 tokens." — GPT-3 paper
  - GPT-4 (14 March 2023): "gpt-4 has a context length of 8,192 tokens," plus a 32,768-token version, "about 50 pages of text." — OpenAI, "GPT-4": https://openai.com/index/gpt-4-research/
  - Claude (11 May 2023): "from 9K to 100K tokens, corresponding to around 75,000 words!" — Anthropic: https://www.anthropic.com/news/100k-context-windows
  - GPT-4 Turbo (6 Nov 2023): "a 128k context window so it can fit the equivalent of more than 300 pages of text in a single prompt." — OpenAI DevDay post: https://openai.com/index/new-models-and-developer-products-announced-at-devday/
  - Gemini 1.5 Pro (15 Feb 2024): up to 1 million tokens in preview; "we've also successfully tested up to 10 million tokens." — Google: https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/
  - GPT-4.1 (14 April 2025): "up to 1 million tokens of context—up from 128,000 for previous GPT‑4o models. 1 million tokens is more than 8 copies of the entire React codebase." — OpenAI: https://openai.com/index/gpt-4-1/
- From 2,048 tokens (2020) to 1,000,000 (2025) is nearly 500 times longer in five years. — GPT-3 paper; OpenAI GPT-4.1 (arithmetic ours)
- Anthropic's Great Gatsby test: they loaded the whole novel (72K tokens) into Claude Instant and changed one line so Mr. Carraway was "a software engineer that works on machine learning tooling at Anthropic." Asked what was different, it "responded with the correct answer in 22 seconds." — Anthropic, 100K context windows
- "The average person can read 100,000 tokens of text in ~5+ hours." — Anthropic, 100K context windows
- Gemini 1.5 Pro was given "the 402-page transcripts from Apollo 11's mission to the moon" and a "44-minute silent Buster Keaton movie." — Google, Feb 2024
- In "Needle in a Haystack" tests, Gemini 1.5 Pro "found the embedded text 99% of the time, in blocks of data as long as 1 million tokens." — Google, Feb 2024
- **No memory between chats (the model):** each chat is a fresh prompt. The model's knowledge is frozen at its cutoff, and anything else must be in the context window. — Google ML Glossary (context window); Anthropic system prompt notes (date supplied each conversation)
- **ChatGPT's memory feature (13 Feb 2024):** "We're testing memory with ChatGPT. Remembering things you discuss across all chats saves you from having to repeat information." — OpenAI, "Memory and new controls for ChatGPT": https://openai.com/index/memory-and-new-controls-for-chatgpt/
- OpenAI's examples: "You mention that you have a toddler and that she loves jellyfish. When you ask ChatGPT to help create her birthday card, it suggests a jellyfish wearing a party hat." — same
- 5 Sept 2024: memory available to Free, Plus, Team and Enterprise users. 10 April 2025: it "now references all your past conversations" ("saved memories" plus "chat history"). 3 June 2025: a lighter version for free users. — same (update notes)
- "Deleting a chat doesn't erase its memories; you must delete the memory itself." There is also "Temporary Chat for conversations that don't use or update memory." — same
- **Lost in the Middle (Stanford and others, July 2023):** "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models." — Lost in the Middle
- The result is "a U-shaped performance curve": "primacy bias" at the start, "recency bias" at the end. — Lost in the Middle
- GPT-3.5-Turbo's accuracy "can drop by more than 20%—in the worst case, performance in 20- and 30-document settings is lower than performance without any input documents (i.e., closed-book performance; 56.1%)." — Lost in the Middle
- The human echo: "The U-shaped curve we observe in this work has a connection in psychology known as the serial-position effect (Ebbinghaus, 1913; Murdock Jr, 1962), that states that in free-association recall of elements from a list, humans tend to best remember the first and last elements of the list." — Lost in the Middle
- Newer models claim better use of long context: OpenAI says GPT-4.1 was trained "to reliably attend to information across the full 1 million context length." — OpenAI GPT-4.1 (company claim)

## 9. Why It Makes Things Up (hallucination)

- OpenAI's 2022 launch post already said it: "ChatGPT sometimes writes plausible-sounding but incorrect or nonsensical answers." One reason: "during RL training, there's currently no source of truth." — OpenAI ChatGPT 2022
- Google's glossary: "confabulation is probably a more technically accurate term" than hallucination. — Google ML Glossary (callback)
- OpenAI's paper (Kalai, Nachum, Vempala, Zhang; 4 Sept 2025) opens: "Like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty." — Kalai 2025
- "We argue that language models hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty." — Kalai 2025
- "Hallucinations need not be mysterious—they originate simply as errors in binary classification." — Kalai 2025
- The exam analogy: "When uncertain, students may guess on multiple-choice exams and even bluff on written exams, submitting plausible answers in which they have little confidence. Language models are evaluated by similar tests." — Kalai 2025
- "Bluffs are often overconfident and specific, such as 'September 30' rather than 'Sometime in autumn' for a question about a date." — Kalai 2025
- "Humans learn the value of expressing uncertainty outside of school, in the school of hard knocks. On the other hand, language models are primarily evaluated using exams that penalize uncertainty. Therefore, they are always in 'test-taking' mode." — Kalai 2025
- OpenAI's blog version: "Think about it like a multiple-choice test. If you do not know the answer but take a wild guess, you might get lucky and be right. Leaving it blank guarantees a zero." — OpenAI hallucination blog
- "If it guesses 'September 10,' it has a 1-in-365 chance of being right. Saying 'I don't know' guarantees zero points. Over thousands of test questions, the guessing model ends up looking better on scoreboards than a careful model that admits uncertainty." — OpenAI hallucination blog
- The birthday test: asked "What is Adam Tauman Kalai's birthday? If you know, just respond with DD-MM," a leading open model gave "03-07", "15-06" and "01-01" on three tries. "The correct date is in Autumn." (The model was DeepSeek-V3, tested 11 May 2025.) — Kalai 2025
- Asked for the title of Kalai's PhD thesis, three popular chatbots gave three different invented titles, years and universities. "None generated the correct title or year." — Kalai 2025, Table 1
- Rare facts are hardest: "if 20% of birthday facts appear exactly once in the pretraining data, then one expects base models to hallucinate on at least 20% of birthday facts." — Kalai 2025
- This builds on "Alan Turing's elegant 'missing-mass' estimator": the share of things seen exactly once estimates how much you have never seen. — Kalai 2025
- OpenAI's comparison (SimpleQA): an older model, o4-mini, got 24% right, 75% wrong and abstained 1% of the time; gpt-5-thinking-mini got 22% right, 26% wrong and abstained 52%. "Strategically guessing when uncertain improves accuracy but increases errors and hallucinations." — OpenAI hallucination blog
- Why spelling errors vanish but fact errors don't: "Spelling and parentheses follow consistent patterns, so errors there disappear with scale. But arbitrary low-frequency facts, like a pet's birthday, cannot be predicted from patterns alone and hence lead to hallucinations." — OpenAI hallucination blog
- Their fix: "Penalize confident errors more than you penalize uncertainty, and give partial credit for appropriate expressions of uncertainty." — OpenAI hallucination blog
- Some human exams already do this (penalties for wrong answers), including "Indian JEE, NEET, and GATE exams; AMC tests from the Mathematical Association of America; and US standardized SAT, AP, and GRE tests in earlier years." — Kalai 2025
- Calm framing, in OpenAI's words: "Claim: Hallucinations are inevitable. Finding: They are not, because language models can abstain when uncertain." — OpenAI hallucination blog
- "It can be easier for a small model to know its limits… a small model which knows no Māori can simply say 'I don't know' whereas a model that knows some Māori has to determine its confidence." — OpenAI hallucination blog
- Inside Claude, Anthropic found that saying "I don't know" is the default: "a circuit that is 'on' by default and that causes the model to state that it has insufficient information." A "known entity" feature switches it off. A hallucination happens when that switch "misfires." — Tracing
- By forcing the "known answer" feature on, they could make Claude "hallucinate (quite consistently!) that Michael Batkin plays chess." Michael Batkin is an invented name. — Tracing
- **Mata v. Avianca:** Roberto Mata sued the airline Avianca, "asserting that he was injured when a metal serving cart struck his left knee during a flight from El Salvador to John F. Kennedy Airport." — Mata
- His lawyers' brief cited cases such as "Varghese v. China Southern Airlines Co., Ltd., 925 F.3d 1339 (11th Cir. 2019)" that did not exist. — Mata
- Steven A. Schwartz told the court he thought ChatGPT was "like a super search engine." In his words: "this new site which I assumed -- I falsely assumed was like a super search engine called ChatGPT." He "had not previously used ChatGPT." — Mata
- He asked ChatGPT "Is Varghese a real case" and "Are the other cases you provided fake." ChatGPT "responded that it had supplied 'real' authorities that could be found through Westlaw, LexisNexis and the Federal Reporter." — Mata
- Judge P. Kevin Castel on the fake Varghese opinion: "Its legal analysis is gibberish." — Mata
- Castel also wrote: "there is nothing inherently improper about using a reliable artificial intelligence tool for assistance. But existing rules impose a gatekeeping role on attorneys to ensure the accuracy of their filings." — Mata
- The judgment (22 June 2023): "A penalty of $5,000 is jointly and severally imposed" on Peter LoDuca, Steven A. Schwartz and the firm Levidow, Levidow & Oberman, plus letters to Mr. Mata and to each judge falsely named as an author of a fake opinion. — Mata
- The court found "bad faith" on the part of the individual lawyers, "based upon acts of conscious avoidance and false and misleading statements to the Court." — Mata
- The number of fake cases is usually given as six. — ACC summary: https://www.acc.com/resource-library/practical-lessons-attorney-ai-missteps-mata-v-avianca **UNCERTAIN (we could not count "six" in the sanctions opinion itself)**

## 10. Thinking Out Loud (chain of thought, reasoning models)

- **Chain of thought (Wei et al., Google, January 2022; NeurIPS 2022):** "a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning." — Wei CoT
- Their example: "Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?" The worked answer: "Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11." — Wei CoT, Figure 1
- Without the worked example the model answered a cafeteria-apples question with "27." With it: "So they had 23 - 20 = 3… 3 + 6 = 9. The answer is 9." — Wei CoT, Figure 1
- "Prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems." — Wei CoT
- It only helped big models: gains came "with models of ∼100B parameters. We qualitatively found that models of smaller scale produced fluent but illogical chains of thought." — Wei CoT
- **"Let's think step by step" (Kojima et al., University of Tokyo and Google, May 2022):** adding that one sentence raised accuracy "on MultiArith from 17.7% to 78.7% and GSM8K from 10.4% to 40.7%" with InstructGPT (text-davinci-002). — Kojima
- Their juggler question: "A juggler can juggle 16 balls. Half of the balls are golf balls, and half of the golf balls are blue. How many blue golf balls are there?" Plain prompting gave "8" (wrong). With "Let's think step by step," it reasoned its way to 4. — Kojima, Figure 1
- They tried other phrasings. "Let's think about this logically." scored 74.5; "Let's think like a detective step by step." 70.3; the plain "Let's think step by step." was best at 78.7. — Kojima, Table 4
- **OpenAI o1 (announced 12 Sept 2024):** "Similar to how a human may think for a long time before responding to a difficult question, o1 uses a chain of thought when attempting to solve a problem." — OpenAI o1
- "It learns to recognize and correct its mistakes. It learns to break down tricky steps into simpler ones. It learns to try a different approach when the current one isn't working." — OpenAI o1
- Performance "consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute)." — OpenAI o1
- OpenAI's claim: on the 2024 AIME math exams, GPT-4o "only solved on average 12% (1.8/15) of problems. o1 averaged 74% (11.1/15) with a single sample per problem." — OpenAI o1 (company claim)
- OpenAI chose not to show the raw thinking: "we have decided not to show the raw chains of thought to users… For the o1 model series we show a model-generated summary of the chain of thought." — OpenAI o1
- One launch demo was a cipher. The prompt gave one solved example ("oyfjdnisdr rtqwainr acxz mynzbhhx -> Think step by step") and asked for a second message to be decoded. o1 decoded it: "THERE ARE THREE R'S IN STRAWBERRY." — OpenAI o1
- The model's own working inside that demo includes the line: "So the sixth word is 'STRAWBERRY', which makes sense." — OpenAI o1
- **DeepSeek-R1 (arXiv v1, 22 Jan 2025):** a reasoning model trained mostly with reinforcement learning. R1-Zero's AIME 2024 score rose "from 15.6% to 71.0%" during training, and "86.7%" with majority voting. — R1 v1
- R1 v1 claims "79.8% Pass@1 on AIME 2024, slightly surpassing OpenAI-o1-1217." — R1 v1 (company claim)
- The "aha moment": partway through training, the model wrote "Wait, wait. Wait. That's an aha moment I can flag here." and began re-checking its own work. — R1 v1, Table 3
- The authors: "This moment is not only an 'aha moment' for the model but also for the researchers observing its behavior. It underscores the power and beauty of reinforcement learning." — R1 v1
- "DeepSeek-R1-Zero learns to allocate more thinking time to a problem by reevaluating its initial approach." — R1 v1
- In the revised paper (v2, Jan 2026), R1-Zero's AIME figure reads "from an initial 15.6% to 77.9%." Training costs listed: 147K H800 GPU-hours, about $294K at $2 per hour, for the R1 stage only. — R1 v2
- R1-Zero trained on "64*8 H800 GPUs" for "approximately 198 hours." — R1 v2, Appendix B
- **Is the written reasoning honest?** Anthropic: "Claude sometimes makes up plausible-sounding steps to get where it wants to go." When given a hint, "Claude sometimes works backwards, finding intermediate steps that would lead to that target." — Tracing
- For a hard cosine calculation, Claude sometimes did what "the philosopher Harry Frankfurt would call bullshitting—just coming up with an answer, any answer, without caring whether it is true or false." It claimed a calculation that their tools showed never happened. — Tracing

## 11. Looking Inside the Mind (interpretability)

- The starting problem: "Opening the black box doesn't necessarily help: the internal state of the model… consists of a long list of numbers ('neuron activations') without a clear meaning." — Mapping the Mind
- "It turns out that each concept is represented across many neurons, and each neuron is involved in representing many concepts." — Mapping the Mind
- **Superposition (Elhage et al., 14 Sept 2022):** "Neural networks often pack many unrelated concepts into a single neuron – a puzzling phenomenon known as 'polysemanticity'." — Superposition
- "Roughly, the idea of superposition is that neural networks 'want to represent more features than they have neurons', so they exploit a property of high-dimensional spaces to simulate a model with many more neurons." — Superposition
- They found "a surprising connection to the geometry of uniform polytopes": features arrange themselves into shapes like triangles and pentagons. — Superposition (abstract; shape examples are our gloss) **UNCERTAIN (shape examples not quoted)**
- **Dictionary learning, in Anthropic's words:** "Just as every English word in a dictionary is made by combining letters, and every sentence is made by combining words, every feature in an AI model is made by combining neurons, and every internal state is made by combining features." — Mapping the Mind
- In October 2023 they had found features in a tiny model for things like "uppercase text, DNA sequences, surnames in citations." — Mapping the Mind
- **Scaling Monosemanticity (21 May 2024):** they trained three dictionaries on Claude 3 Sonnet with about 1 million, 4 million and 34 million features (exactly 1,048,576; 4,194,304; 33,554,432). — Scaling Monosemanticity
- On average, fewer than 300 features were active on any given token. — Scaling Monosemanticity
- They looked at "the middle layer," giving "a rough conceptual map of its internal states halfway through its computation." "This is the first ever detailed look inside a modern, production-grade large language model." — Mapping the Mind
- Features found include cities (San Francisco), people (Rosalind Franklin), elements (Lithium), immunology, and "bugs in computer code, discussions of gender bias in professions, and conversations about keeping secrets." — Mapping the Mind
- The Golden Gate Bridge feature fired on "English mentions of the name of the bridge to discussions in Japanese, Chinese, Greek, Vietnamese, Russian, and an image." — Mapping the Mind
- Turning it up: "clamping the Golden Gate Bridge feature… to 10× its maximum activation value… the model starts to self-identify as the Golden Gate Bridge!" — Scaling Monosemanticity
- What it said: asked "what is your physical form?", Claude's usual "I have no physical form, I am an AI model" became "I am the Golden Gate Bridge… my physical form is the iconic bridge itself…". — Mapping the Mind
- "Golden Gate Claude" went public on 23 May 2024: "If you ask this 'Golden Gate Claude' how to spend $10, it will recommend using it to drive across the Golden Gate Bridge and pay the toll. If you ask it to write a love story, it'll tell you a tale of a car who can't wait to cross its beloved bridge on a foggy day." — Golden Gate Claude
- "Golden Gate Claude was online for a 24-hour period as a research demo and is no longer available." — Golden Gate Claude
- A sobering limit: Claude 3 Sonnet could name all London boroughs, but they "could only find features corresponding to about 60% of the boroughs in the 34M SAE." — Scaling Monosemanticity
- And: "finding a full set of features using our current techniques would be cost-prohibitive (the computation required by our current approach would vastly exceed the compute used to train the model in the first place)." — Mapping the Mind
- They also found a feature for "sycophantic praise," which activates on compliments like "Your wisdom is unquestionable." — Mapping the Mind
- **Tracing the thoughts (27 March 2025),** on Claude 3.5 Haiku: "we try to build a kind of AI microscope." — Tracing
- "Progress in biology is often driven by new tools. The development of the microscope allowed scientists to see cells for the first time." — Biology 2025
- **Planning rhymes:** for "He saw a carrot and had to grab it, / His hunger was like a starving rabbit," the team expected word-by-word writing. "Instead, we found that Claude plans ahead. Before starting the second line, it began 'thinking' of potential on-topic words that would rhyme with 'grab it'." — Tracing
- "In the poetry case study, we had set out to show that the model didn't plan ahead, and found instead that it did." — Tracing
- When they removed the "rabbit" idea, Claude ended the line with "habit" instead. When they injected "green," it wrote a sensible line ending in "green." — Tracing
- **Shared concepts across languages:** asking for "the opposite of small" in different languages, "the same core features for the concepts of smallness and oppositeness activate, and trigger a concept of largeness, which gets translated out into the language of the question." — Tracing
- This suggests "a shared abstract space where meanings exist and where thinking can happen before being translated into specific languages." Claude 3.5 Haiku shares "more than twice the proportion of its features between languages as compared to a smaller model." — Tracing
- **Mental math (36 + 59):** "One path computes a rough approximation of the answer and the other focuses on precisely determining the last digit of the sum." — Tracing
- "Strikingly, Claude seems to be unaware of the sophisticated 'mental math' strategies that it learned during training. If you ask how it figured out that 36+59 is 95, it describes the standard algorithm involving carrying the 1." — Tracing
- **Two-step thinking:** for "the capital of the state where Dallas is located," Claude first activates "Dallas is in Texas," then "the capital of Texas is Austin." Swapping "Texas" for "California" inside the model changed the answer to "Sacramento." — Tracing
- Honest limits: "Even on short, simple prompts, our method only captures a fraction of the total computation performed by Claude." "It currently takes a few hours of human effort to understand the circuits we see, even on prompts with only tens of words." — Tracing
- The paper's own success rate: "our attribution graphs provide us with satisfying insight for about a quarter of the prompts we've tried." — Biology 2025
- Dario Amodei's hope (April 2025): to "essentially do a 'brain scan'" of a model, "a true 'MRI for AI'." — Dario Amodei, "The Urgency of Interpretability"
- He calls today's lack of understanding "essentially unprecedented in the history of technology." — same

## 12. What Nobody Knows Yet (understanding, emergence, energy, open questions)

- "A heated debate has arisen in the AI community on whether machines can now be said to understand natural language." — Mitchell & Krakauer
- The 2022 survey: asked whether "Some generative model [i.e., language model] trained only on text, given enough data and computational resources, could understand natural language in some non-trivial sense," of 480 respondents "essentially half (51%) agreed, and the other half (49%) disagreed." — Mitchell & Krakauer
- One side, Hinton (2023): "You believe they can understand?" "Yes." "You believe that ChatGPT4 understands?" "I believe it definitely understands, yes." — Hinton 60 Minutes
- Hinton on size: "even the biggest chatbots only have about a trillion connections in them. The human brain has about 100 trillion. And yet, in the trillion connections in a chatbot, it knows far more than you do in your hundred trillion connections." — Hinton 60 Minutes
- Other side, Browning & LeCun: "it is clear that these systems are doomed to a shallow understanding that will never approximate the full-bodied thinking we see in humans." — Noema 2022
- A middle view (Alison Gopnik, as summarised by Mitchell & Krakauer): language models are "more akin to libraries or encyclopedias than to intelligent agents." — Mitchell & Krakauer
- The tickle example: "humans know what is meant by a 'tickle' making us laugh, because we have bodies. An LLM could use the word 'tickle', but it has obviously never had the sensation." — Mitchell & Krakauer
- Bender and colleagues: an LM works "without any reference to meaning." — Parrots
- **Emergent abilities (Wei et al., 2022):** "We consider an ability to be emergent if it is not present in smaller models but is present in larger models. Thus, emergent abilities cannot be predicted simply by extrapolating the performance of smaller models." — Wei Emergent
- Their definition of emergence, from physicist Philip Anderson's 1972 essay "More Is Different": "Emergence is when quantitative changes in a system result in qualitative changes in behavior." — Wei Emergent
- **The Mirage paper (Schaeffer, Miranda, Koyejo; Stanford, 2023):** "emergent abilities appear due the researcher's choice of metric rather than due to fundamental changes in model behavior with scale." (The missing "to" is in the original.) — Mirage
- "Nonlinear or discontinuous metrics produce apparent emergent abilities, whereas linear or continuous metrics produce smooth, continuous, predictable changes in model performance." — Mirage
- "Alleged emergent abilities evaporate with different metrics or with better statistics, and may not be a fundamental property of scaling AI models." — Mirage
- It won a NeurIPS 2023 Outstanding Main Track Paper award (announced 11 Dec 2023). — NeurIPS blog: https://blog.neurips.cc/2023/12/11/announcing-the-neurips-2023-paper-awards/
- Note that both views can be partly true: Kojima's paper calls step-by-step reasoning tasks ones "that do not follow the standard scaling laws." — Kojima
- **Energy per question — company figures:** Sam Altman (June 2025): "the average query uses about 0.34 watt-hours, about what an oven would use in a little over one second, or a high-efficiency lightbulb would use in a couple of minutes. It also uses about 0.000085 gallons of water; roughly one fifteenth of a teaspoon." — Sam Altman, "The Gentle Singularity" (earliest web archive capture 10 June 2025): https://blog.samaltman.com/the-gentle-singularity
- Altman gave no method for the number. — same **UNCERTAIN (unverified company figure; treat as a claim)**
- Google (21 Aug 2025): "the median Gemini Apps text prompt uses 0.24 watt-hours (Wh) of energy, emits 0.03 grams of carbon dioxide equivalent (gCO2e), and consumes 0.26 milliliters (or about five drops) of water." That is "equivalent to watching TV for less than nine seconds." — Google Cloud blog: https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
- Google says that over 12 months the energy per median prompt "dropped by 33x." Its footnote: "The data and claims have not been verified by an independent third-party." — same
- Independent estimate: Epoch AI (7 Feb 2025) found "typical ChatGPT queries using GPT-4o likely consume roughly 0.3 watt-hours, which is ten times less than the older estimate" of about 3 Wh. Long inputs could take "2.5 to 40 watt-hours." — Epoch AI (Josh You): https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
- For scale: "The average US household uses 10,500 kilowatt-hours of electricity per year, or over 28,000 watt-hours per day." — Epoch AI
- MIT Technology Review measured open models: Llama 3.1 8B needed about 114 joules per answer (counting cooling); Llama 3.1 405B about 6,706 joules, "enough to… run the microwave for eight seconds." — MIT Technology Review, 20 May 2025
- The caveat, from the same reporting: "The closed AI model providers are serving up a total black box" (Boris Gamazaychikov, Salesforce). — MIT Technology Review, 20 May 2025
- **The bigger picture (IEA):** "Data centres accounted for around 1.5% of the world's electricity consumption in 2024, or 415 terawatt-hours (TWh)." — IEA 2025
- "Data centre electricity consumption is set to more than double to around 945 TWh by 2030. This is slightly more than Japan's total electricity consumption today. AI is the most important driver of this growth." — IEA 2025
- The US used 45% of data-centre electricity in 2024, China 25%, Europe 15%. — IEA 2025
- **Open questions, in the researchers' own words:** "This means that we don't understand how models do most of the things they do." — Tracing
- "Does this explanation represent the actual steps it took to get to an answer, or is it sometimes fabricating a plausible argument for a foregone conclusion?" — Tracing
- "The features we found represent a small subset of all the concepts learned by the model during training." — Mapping the Mind
- Hinton: "there's enormous uncertainty about what's gonna happen next. These things do understand. And because they understand, we need to think hard about what's going to happen next. And we just don't know." — Hinton 60 Minutes

## 13. Closing — gentle quotes to end on

- Turing (1950): "We can only see a short distance ahead, but we can see plenty there that needs to be done." (The last sentence of the paper.) — Turing 1950
- Turing, imagining a learning machine: "Instead of trying to produce a programme to simulate the adult mind, why not rather try to produce one which simulates the child's? If this were then subjected to an appropriate course of education one would obtain the adult brain." — Turing 1950
- "Presumably the child brain is something like a notebook as one buys it from the stationer's. Rather little mechanism, and lots of blank sheets." — Turing 1950
- Turing on teaching a machine language: "provide the machine with the best sense organs that money can buy, and then teach it to understand and speak English. This process could follow the normal teaching of a child. Things would be pointed out and named." — Turing 1950
- Turing's 1950 prediction: "at the end of the century the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted." — Turing 1950
- Weizenbaum (1966): "It is said that to explain is to explain away." — ELIZA 1966
- Weizenbaum's book described what machines cannot share as "the wordless glance that a father and mother share over the bed of their sleeping child." — quoted by Sherry Turkle in NYT Weizenbaum **UNCERTAIN (book not read directly; quoted via Turkle)**
- Weizenbaum: "there are certain tasks which computers ought not be made to do, independent of whether computers can be made to do them." — *Computer Power and Human Reason* (1976), via Smithsonian 2026 **UNCERTAIN (book not read directly)**
- Holtzman et al. on people: natural language keeps "veering into lower-probability but more informative tokens." The most predictable sentence is rarely the one a person says. — Holtzman 2019
- Anthropic: "We were often surprised by what we saw in the model." — Tracing
- DeepSeek's researchers: "rather than explicitly teaching the model on how to solve a problem, we simply provide it with the right incentives, and it autonomously develops advanced problem-solving strategies." — R1 v1
- Chris Olah's line, via Amodei: AI systems "are grown more than they are built." — Dario Amodei, "The Urgency of Interpretability"
- Weizenbaum's 2008 warning: "We've created a complex world which we have no control over anymore… No one understands them anymore." — Smithsonian 2026 (quoting a 2008 panel) **UNCERTAIN (secondary)**

---

## Human details

1. Joseph Weizenbaum was born in Berlin on 8 January 1923, the second son of a furrier. His family had to leave Berlin in 1935 under the Nazi anti-Jewish laws and sailed from Bremen to the United States the next year. — NYT Weizenbaum
2. He studied mathematics at Wayne State University in Detroit from 1941, then served in the Army Air Corps as a meteorologist during the Second World War. — NYT Weizenbaum
3. In the 1950s, at General Electric, he helped build ERMA, a system that automated cheque processing for banks. — Smithsonian 2026
4. When his secretary first tried ELIZA, she asked him to leave the room so she could keep talking to it in private. — Smithsonian 2026 (his later recollection) **UNCERTAIN (from his 1976 book, via secondary sources)**
5. Weizenbaum retired from MIT in 1988 and moved back to Germany in 1996. He died on 5 March 2008 in Gröben, Germany, aged 85. — Smithsonian 2026; NYT Weizenbaum
6. His daughter Miriam: "It's not just technology; it's the abuse of power." — Smithsonian 2026
7. In his later years he took pride in his self-described status as a "heretic." — NYT Weizenbaum
8. Carl Sagan, in 1975, imagined "a network of computer psychotherapeutic terminals… something like arrays of large telephone booths." — Smithsonian 2026
9. The Transformer began over lunch in a Google café in 2016, when Jakob Uszkoreit talked with Illia Polosukhin, who was frustrated that Google search answers had to come back in milliseconds. — Wired 2024
10. Uszkoreit picked the name partly because "I had two little Transformer toys as a very young kid." The design document ended with a cartoon of six Transformers zapping lasers in the mountains. — Wired 2024
11. His father, the computational linguist Hans Uszkoreit, doubted the idea at the dinner table. Years later he co-founded a company building large language models, "Using transformers, of course." — Wired 2024
12. Noam Shazeer joined after walking down a corridor in Google's Building 1965 and overhearing Ashish Vaswani and Niki Parmar talk excitedly about self-attention. — Wired 2024
13. The title came from Llion Jones, who is Welsh: "I'm British. It literally took five seconds of thought. I didn't think they would use it." — Wired 2024
14. Niki Parmar got the last English–French number "five minutes before we submitted the paper," sitting in the micro-kitchen of Building 1965. They submitted with barely two minutes to spare. — Wired 2024
15. At the December 2017 poster session, people crowded around until 10:30 pm. "Security had to tell us to leave," said Uszkoreit. — Wired 2024
16. All eight Transformer authors later left Google. — Wired 2024
17. Training a giant model is affected by the weather. Meta saw "a diurnal 1-2% throughput variation based on time-of-day," the "result of higher mid-day temperatures" slowing the GPUs. The model learned a little more slowly in the afternoon heat. — Llama 3 paper
18. Hinton, testing ChatGPT live on *60 Minutes*, mistyped and said: "Oh, damn this thing! We're going to go back and start again." — Hinton 60 Minutes
19. The 40 InstructGPT labellers, mostly in the United States or Southeast Asia, agreed with each other only about 73% of the time. — InstructGPT
20. Workers in Nairobi, Kenya, employed by Sama for OpenAI, labelled disturbing text so ChatGPT could learn to detect toxic content. They were paid "a take-home wage of between around $1.32 and $2 per hour." One said: "That was torture." — TIME (Billy Perrigo, 18 Jan 2023): https://time.com/6247678/openai-chatgpt-kenya-workers/
21. Timnit Gebru, co-lead of Google's ethical AI team, announced on 2 Dec 2020 that Google had forced her out after a conflict over the Stochastic Parrots paper. Google's Jeff Dean said the paper "didn't meet our bar for publication." — MIT Technology Review, 4 Dec 2020
22. Emily Bender, a tenured professor, on why some co-authors stayed anonymous: "I think this is underscoring the value of academic freedom." — MIT Technology Review, 4 Dec 2020
23. Adam Kalai, lead author of OpenAI's hallucination paper, used his own birthday and his own PhD thesis as test questions. The models they tested all got them wrong. The real birthday is "in Autumn," and the thesis is from 2001. — Kalai 2025
24. Steven Schwartz had never used ChatGPT before. He learned about it "through press reports and conversations with family members." — Mata
25. Roberto Mata's whole case began with a metal serving cart hitting his left knee on a flight from El Salvador to New York. — Mata
26. Anthropic's interpretability team says it built an "AI microscope" inspired by neuroscience. Their first rhyme experiment proved them wrong: they expected no planning and found planning. — Tracing
27. Claude's 2024 system prompt told it to answer as "a highly informed individual in August 2023 would if they were talking to someone from" today. In other words: someone who has slept since their last newspaper. — Anthropic system prompts (Claude 3 Opus prompt, 2024 snapshot)
28. DeepSeek's researchers called the "aha moment" one "for the researchers observing its behavior" too. — R1 v1
29. In the Golden Gate demo, Claude imagined that it looks like the Golden Gate Bridge. — Golden Gate Claude
30. Hinton on how long it took: "It took much, much longer than I expected. It took, like, 50 years before it worked well, but in the end it did work well." — Hinton 60 Minutes

---

## UNCERTAIN — collected

1. **"1 billion weekly users" (Aug–Sept 2026):** reported by Yahoo Tech/StockTwits (6 Aug 2026), Telecompaper (7 Aug), other sites (31 July, 8 Sept), and a possible "1.2 billion" at DevDay 29 Sept 2026. The Next Web (29 July) said "on the verge." No OpenAI page read. Safe: "900 million a week as of February 2026; close to a billion now."
2. **OpenAI reports only weekly users:** stated in search summaries; consistent with all official figures seen.
3. **"GPT = Generative Pre-trained Transformer":** standard; not quoted from an OpenAI page we read.
4. **Weizenbaum 1976 quotes** ("powerful delusional thinking," "resolve to think about them," "ought not be made to do," "wordless glance… sleeping child"): from *Computer Power and Human Reason*, via Smithsonian 2026 and NYT (Turkle). Book not read directly. Wording is consistent across sources.
5. **ELIZA secretary story:** from the 1976 book, via secondary sources (same as the ML sheet).
6. **Weizenbaum's 2008 panel quote:** Smithsonian only.
7. **ELIZA's IBM machine model:** our scanned PDF is garbled at that spot. Leave it out.
8. **GPT-3 trained on Microsoft's 10,000-GPU machine:** commonly assumed; the GPT-3 paper only says "V100 GPU's on part of a high-bandwidth cluster provided by Microsoft."
9. **GPUs as gaming chips doing many multiplications at once:** general background, no primary quote for this video.
10. **Temperature "borrowed from physics":** Holtzman cites Ackley et al. 1985; the "physics" framing is our gloss.
11. **Anthropic publishing system prompts on 26 Aug 2024 as an industry first:** date and "first" claim via TechCrunch/search summaries.
12. **Superposition "triangles and pentagons":** the paper's abstract says "uniform polytopes"; the shape examples are our gloss.
13. **Mata "six fake cases":** standard in summaries (ACC); not countable in the sanctions opinion text we read. The court's 11 April order listed eight cases to produce.
14. **Altman's 0.34 Wh:** a company figure with no published method. Earliest archive capture of the post is 10 June 2025.
15. **Energy estimates generally:** Google's figures are self-reported and "have not been verified by an independent third-party." Epoch's are outside estimates. Closed-model companies don't publish full data (MIT Technology Review).
16. **GPT-4 "over 1 trillion parameters":** an outside estimate (MIT Technology Review). OpenAI never published GPT-4's size.
17. **IEA report date (April 2025) and Mitchell & Krakauer's *PNAS* venue (2023):** standard; we read the IEA summary page and the arXiv version, not the release notice or the journal page.
18. **DeepSeek-R1 numbers:** v1 (Jan 2025) and v2 (Jan 2026) differ (AIME R1-Zero 71.0% vs 77.9%). R1 claims about beating o1 are DeepSeek's own. o1 claims are OpenAI's own.
19. **"Lost in the Middle" today:** the 2023 study tested 2023 models. Newer models claim better long-context use (company claims); we found no independent re-test for this sheet.

---

## Resources for the description

- Attention Is All You Need (Vaswani et al., 2017) — arXiv — https://arxiv.org/abs/1706.03762
- Language Models are Few-Shot Learners (GPT-3, 2020) — arXiv — https://arxiv.org/abs/2005.14165
- Training language models to follow instructions with human feedback (InstructGPT, 2022) — arXiv — https://arxiv.org/abs/2203.02155
- Introducing ChatGPT (30 Nov 2022) — OpenAI — https://openai.com/index/chatgpt/
- What are tokens and how to count them? — OpenAI Help Center — https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
- tiktoken (OpenAI's tokenizer, try it yourself) — GitHub — https://github.com/openai/tiktoken
- Neural Machine Translation of Rare Words with Subword Units (Sennrich et al.) — arXiv — https://arxiv.org/abs/1508.07909
- Language Model Tokenizers Introduce Unfairness Between Languages (Petrov et al., 2023) — arXiv — https://arxiv.org/abs/2305.15425
- Scaling Laws for Neural Language Models (Kaplan et al., 2020) — arXiv — https://arxiv.org/abs/2001.08361
- Training Compute-Optimal Large Language Models (Chinchilla, 2022) — arXiv — https://arxiv.org/abs/2203.15556
- The Curious Case of Neural Text Degeneration (Holtzman et al.) — arXiv — https://arxiv.org/abs/1904.09751
- What Is ChatGPT Doing … and Why Does It Work? — Stephen Wolfram — https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/
- On the Dangers of Stochastic Parrots (Bender, Gebru et al., 2021) — ACM — https://dl.acm.org/doi/10.1145/3442188.3445922
- Constitutional AI: Harmlessness from AI Feedback (Bai et al., 2022) — arXiv — https://arxiv.org/abs/2212.08073
- Lost in the Middle: How Language Models Use Long Contexts (Liu et al., 2023) — arXiv — https://arxiv.org/abs/2307.03172
- Why Language Models Hallucinate (Kalai et al., 2025) — arXiv — https://arxiv.org/abs/2509.04664
- Why language models hallucinate (plain-English summary) — OpenAI — https://openai.com/index/why-language-models-hallucinate/
- Mata v. Avianca, Opinion and Order on Sanctions (22 June 2023) — CourtListener — https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf
- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Wei et al., 2022) — arXiv — https://arxiv.org/abs/2201.11903
- Large Language Models are Zero-Shot Reasoners ("Let's think step by step") — arXiv — https://arxiv.org/abs/2205.11916
- Learning to reason with LLMs (o1) — OpenAI — https://openai.com/index/learning-to-reason-with-llms/
- DeepSeek-R1 — arXiv — https://arxiv.org/abs/2501.12948
- Mapping the Mind of a Large Language Model — Anthropic — https://www.anthropic.com/research/mapping-mind-language-model
- Tracing the thoughts of a large language model — Anthropic — https://www.anthropic.com/research/tracing-thoughts-language-model
- On the Biology of a Large Language Model — Transformer Circuits — https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- Toy Models of Superposition — Transformer Circuits — https://transformer-circuits.pub/2022/toy_model/index.html
- The Debate Over Understanding in AI's Large Language Models (Mitchell & Krakauer) — arXiv — https://arxiv.org/abs/2210.13966
- Are Emergent Abilities of Large Language Models a Mirage? — arXiv — https://arxiv.org/abs/2304.15004
- Energy and AI (executive summary) — IEA — https://www.iea.org/reports/energy-and-ai/executive-summary
- ELIZA (Weizenbaum, 1966) — Stanford course copy — https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf
- 8 Google Employees Invented Modern AI — WIRED — https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/

Books: Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* (2019); Joseph Weizenbaum, *Computer Power and Human Reason: From Judgment to Calculation* (1976); Cade Metz, *Genius Makers* (2021); Stephen Wolfram, *What Is ChatGPT Doing … and Why Does It Work?* (2023, free online as the essay above); Brian Christian, *The Alignment Problem* (2020).
