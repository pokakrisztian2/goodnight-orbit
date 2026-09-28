# Fact Sheet — "Every Confusing Thing About Machine Learning Explained Slowly (For Sleep)"

Compiled 2026-09-29. Every line was checked against the listed source with WebSearch/WebFetch/curl (no Wikipedia). Where a PDF was read in full, the source is the paper itself.
Legend: plain line = verified. **UNCERTAIN** = not fully confirmed, disputed, or seen only in a secondary retelling. Soften it in narration or leave it out. All UNCERTAIN items are also collected at the end.
"Nilsson" = Nils J. Nilsson, *The Quest for Artificial Intelligence* (Cambridge UP, 2010), free PDF from Stanford: https://ai.stanford.edu/~nilsson/QAI/qai.pdf
"Nature 2015 review" = LeCun, Bengio & Hinton, "Deep learning," *Nature* 521, 436–444 (28 May 2015): https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf
"Google ML Glossary" = https://developers.google.com/machine-learning/glossary

> Corrections to the brief:
> - **Rosenblatt died in 1971, not 1969.** The Cornell faculty memorial statement says he died on Sunday afternoon, 11 July 1971, his 43rd birthday. Nilsson's book wrongly gives 1969.
> - **Lighthill report: 1972 or 1973.** Chilton Computing (which hosts the report) and Nilsson's notes date it to 1972 (report July 1972). Many writers say 1973, the year the SRC's printed symposium volume is usually dated. We did not verify that 1973 date. Safe wording: "in the early 1970s" or "in 1973, the Lighthill report was published."
> - **"Coined machine learning":** what we can show is that "machine learning" is in the title of Samuel's July 1959 paper. IBM credits him with coining the term. Say "one of the first to use the phrase."
> - **Samuel vs. Nealey:** IBM called Nealey a former Connecticut champion. Jonathan Schaeffer (Univ. of Alberta, who built the program that later solved checkers) says Nealey was *not* a champion at the time. He won the Connecticut title in 1966, four years later. Nilsson calls him "a blind checkers master."
> - **ELIZA's secretary** is not in the 1966 paper. The story comes from Weizenbaum's 1976 book *Computer Power and Human Reason*.
> - **Lee Sedol's move 78 and AlphaGo's move 37:** DeepMind puts both at about "1 in 10,000."
> - **Cheque reading:** "over 10% of all the cheques in the United States" by the late 1990s (LeCun, Bengio & Hinton, *Nature* 2015). The 1998 paper says "several million checks per day." The figure "20 million a day" is not verified.
> - **Hinton's back:** verified. He injured it at 19 moving a heavy heater for his mother, and in 2005 "stopped sitting almost entirely."
> - **AlexNet in the bedroom:** verified by the Computer History Museum.
> - **Minsky's Turing Award** is the 1969 award (MIT News). Cornell Chronicle gives 1970, which may be the year it was presented.

---

## 0. Intro — the words we will use (plain-English toolkit)

- A **model** is "any mathematical construct that processes input data and returns output… the set of parameters and structure needed for a system to make predictions." — Google ML Glossary
- **Parameters** are "the weights and biases that a model learns during training." — Google ML Glossary
- A **weight** is "a value that a model multiplies by another value. Training is the process of determining a model's ideal weights; inference is the process of using those learned weights to make predictions." — Google ML Glossary
- LeCun, Bengio and Hinton describe weights as "'knobs' that define the input–output function of the machine." A typical deep-learning system may have "hundreds of millions of these adjustable weights, and hundreds of millions of labelled examples." — Nature 2015 review
- **Training vs. inference:** training is when the knobs are turned. Inference is when the finished model is simply used, with the knobs left alone. — Google ML Glossary (weight entry)
- **Loss:** during training, the machine computes "an objective function that measures the error (or distance) between the output scores and the desired pattern of scores," then "modifies its internal adjustable parameters to reduce this error." — Nature 2015 review
- **Supervised learning** is "learning from a training set of labeled examples provided by a knowledgable external supervisor." — Sutton & Barto, *Reinforcement Learning: An Introduction* (2nd ed., 2018), ch. 1: http://incompleteideas.net/book/RLbook2020.pdf
- Google compares supervised learning to "learning a subject by studying a set of questions and their corresponding answers." — Google ML Glossary
- **Unsupervised learning** is "typically about finding structure hidden in collections of unlabeled data." — Sutton & Barto, ch. 1
- **Reinforcement learning** is "learning what to do—how to map situations to actions—so as to maximize a numerical reward signal. The learner is not told which actions to take, but instead must discover which actions yield the most reward by trying them." — Sutton & Barto, ch. 1
- Sutton & Barto name "trial-and-error search and delayed reward" as the two most important features of reinforcement learning. — same
- **Overfitting:** "Creating a model that matches the training data so closely that the model fails to make correct predictions on new data." — Google ML Glossary
- Google's gentle analogy: "Overfitting is like strictly following advice from only your favorite teacher. You'll probably be successful in that teacher's class, but you might 'overfit' to that teacher's ideas and be unsuccessful in other classes." — Google ML Glossary
- Overfitting "occurs when a model performs well on training data but poorly on new, unseen data." — Google ML Crash Course: https://developers.google.com/machine-learning/crash-course/overfitting/overfitting
- An **epoch** is "a full training pass over the entire training set such that each example has been processed once." — Google ML Glossary
- A **neuron** (in machine learning) "calculates the weighted sum of input values multiplied by their corresponding weights" and passes that sum through an activation function. — Google ML Glossary
- A **hidden layer** sits between the input layer and the output layer. "A deep neural network contains more than one hidden layer." — Google ML Glossary

## 1. Can a Machine Think? (Turing 1950, Dartmouth 1956)

- A. M. Turing, "Computing Machinery and Intelligence," *Mind* 59 (no. 236), 433–460, October 1950. — Crossref / OUP: https://academic.oup.com/mind/article/LIX/236/433/986238
- First sentence: "I propose to consider the question, 'Can machines think?'" — Turing 1950 (OUP link above; full text: https://courses.cs.umbc.edu/471/papers/turing.pdf)
- The imitation game "is played with three people, a man (A), a woman (B), and an interrogator (C)… The object of the game for the interrogator is to determine which of the other two is the man and which is the woman." Turing then asks what happens when a machine takes the part of A. — Turing 1950
- Turing's prediction: "in about fifty years' time it will be possible to programme computers, with a storage capacity of about 10⁹, to make them play the imitation game so well that an average interrogator will not have more than 70 per cent chance of making the right identification after five minutes of questioning." — Turing 1950
- He also thought that "at the end of the century the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted." — Turing 1950
- He called the original question "too meaningless to deserve discussion." — Turing 1950
- Objection (6), "Lady Lovelace's Objection," quotes her: "The Analytical Engine has no pretensions to originate anything. It can do whatever we know how to order it to perform" (her italics). Turing dates her memoir 1842. The translated memoir with her Notes was published in 1843. — Turing 1950
- Turing's gentle reply: "Machines take me by surprise with great frequency." — Turing 1950
- Turing's learning-machine idea: "Instead of trying to produce a programme to simulate the adult mind, why not rather try to produce one which simulates the child's? If this were then subjected to an appropriate course of education one would obtain the adult brain." — Turing 1950
- The Dartmouth proposal is dated 31 August 1955 and signed by J. McCarthy (Dartmouth), M. L. Minsky (Harvard), N. Rochester (IBM) and C. E. Shannon (Bell Telephone Laboratories). — Stanford (McCarthy's site): http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html
- Its first sentence: "We propose that a 2 month, 10 man study of artificial intelligence be carried out during the summer of 1956 at Dartmouth College in Hanover, New Hampshire." — Dartmouth proposal (above)
- The core conjecture: "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it." — Dartmouth proposal
- Its optimism: "We think that a significant advance can be made in one or more of these problems if a carefully selected group of scientists work on it together for a summer." — Dartmouth proposal
- Dartmouth College credits the 1956 summer project, organised by John McCarthy, as the place where the term "artificial intelligence" was coined and the field established. — Dartmouth: https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth
- ELIZA: Joseph Weizenbaum, "ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and Machine," *Communications of the ACM* 9(1), 36–45, January 1966. — Crossref; paper: https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf
- ELIZA ran on MIT's MAC time-sharing system and was written in MAD-SLIP for the IBM 7094 (the scan's OCR reads "7091"; 7094 is the known machine). Weizenbaum named it after the Eliza of *Pygmalion* fame, because it could be "incrementally improved by its users" as if taught. — Weizenbaum 1966
- Weizenbaum's opening warning: "once a particular program is unmasked, once its inner workings are explained in language sufficiently plain to induce understanding, its magic crumbles away." — Weizenbaum 1966
- Weizenbaum (1923–2008) later argued that "there are certain tasks which computers ought not be made to do, independent of whether computers can be made to do them." — Nilsson, ch. 24, quoting *Computer Power and Human Reason* (1976)

## 2. A Machine That Learns From Mistakes (McCulloch–Pitts 1943, Rosenblatt 1958)

- Warren McCulloch and Walter Pitts, "A Logical Calculus of the Ideas Immanent in Nervous Activity," *Bulletin of Mathematical Biophysics* 5, 115–133 (December 1943). — Crossref (doi 10.1007/BF02478259)
- Their first line of argument: "Because of the 'all-or-none' character of nervous activity, neural events and the relations among them can be treated by means of propositional logic." — McCulloch & Pitts 1943 (reprint, *Bull. Math. Biol.* 52, 1990)
- Nautilus sums up their result: "the brain could implement every possible logical operation and compute anything that could be computed by one of Turing's hypothetical machines." — Nautilus (Amanda Gefter): https://nautil.us/the-man-who-tried-to-redeem-the-world-with-logic-235253
- F. Rosenblatt, "The perceptron: A probabilistic model for information storage and organization in the brain," *Psychological Review* 65(6), 386–408 (1958). — Crossref (doi 10.1037/h0042519)
- Rosenblatt was born 11 July 1928 in New Rochelle, New York. He earned his Cornell A.B. in 1950 and his Ph.D. in 1956, then worked at Cornell Aeronautical Laboratory in Buffalo. — Cornell faculty memorial statement: https://ecommons.cornell.edu/server/api/core/bitstreams/9722f83a-1386-4956-a576-06d29b41c197/content
- In July 1958 the U.S. Office of Naval Research unveiled the perceptron idea on a five-ton, room-sized IBM 704. Fed punch cards, after 50 trials it taught itself to tell cards marked on the left from cards marked on the right. — Cornell Chronicle (2019): https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon
- The New York Times, 8 July 1958 (UPI story dated 7 July): "NEW NAVY DEVICE LEARNS BY DOING; Psychologist Shows Embryo of Computer Designed to Read and Grow Wiser." — AITopics archive copy: https://aitopics.org/doc/news:C85C11EF ; Cornell Chronicle
- The article's lead: the Navy revealed "the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence." — AITopics (NYT archive copy)
- *The New Yorker* called it "the first serious rival to the human brain ever devised." — Cornell Chronicle
- Rosenblatt on his machine: "the first machine which is capable of having an original idea." — Cornell Chronicle
- The Mark I Perceptron was built at Cornell Aeronautical Laboratory, sponsored by the Office of Naval Research and the Rome Air Development Center. It was first publicly demonstrated on 23 June 1960. — Nilsson, §4.2
- The Mark I "used volume controls (called 'potentiometers' by electrical engineers) for weights. These had small motors attached to them" to turn the weights up or down. — Nilsson, §4.2
- It had 400 photosensors, so it "could read an image composed of 20 by 20 pixels and sort it into one of two possible classes." — Hardt & Recht, *Patterns, Predictions, and Actions* (Princeton UP), arXiv:2102.05242: https://arxiv.org/abs/2102.05242
- The Mark I Perceptron is now at the Smithsonian Institution. — Cornell Chronicle
- The perceptron learns only when it is wrong. Rosenblatt's convergence theorem showed the learning rule would find a separating line (a "hyperplane") whenever one exists. — Nilsson, §4.2
- Rosenblatt also built "Tobermory," a speech-recognition perceptron, named after a talking cat in a short story by Saki. — Nilsson, §4.2
- In 1959 Rosenblatt moved to Cornell's Ithaca campus to direct the Cognitive Systems Research Program. — Cornell memorial statement

## 3. The Checkers Player (Samuel 1959)

- Arthur Samuel began thinking about a checkers program in the late 1940s at the University of Illinois. He joined IBM's Poughkeepsie Laboratory in 1949, finished his first working checkers program in 1952 on the IBM 701, and recoded it for the IBM 704 in 1954. — Nilsson, ch. 5
- A. L. Samuel, "Some Studies in Machine Learning Using the Game of Checkers," *IBM Journal of Research and Development* 3(3), 210–229, July 1959. — Crossref (doi 10.1147/rd.33.0210); PDF: https://people.csail.mit.edu/brooks/idocs/Samuel.pdf
- Abstract: "a computer can be programmed so that it will learn to play a better game of checkers than can be played by the person who wrote the program." — Samuel 1959
- It learned this "in a remarkably short period of time (8 or 10 hours of machine-playing time)." It was given only "the rules of the game, a sense of direction, and a redundant and incomplete list of parameters… whose correct signs and relative weights are unknown." — Samuel 1959
- The reason he gave for machine learning: "Programming computers to learn from experience should eventually eliminate the need for much of this detailed programming effort." — Samuel 1959
- Samuel's first learning program was finished in 1955 and shown on television on 24 February 1956. — Nilsson, ch. 5
- John McCarthy recalled that IBM's founder Thomas J. Watson Sr. said the demonstration "would raise the price of IBM stock 15 points. It did." — Nilsson, ch. 5; also Schaeffer, Univ. of Alberta: https://webdocs.cs.ualberta.ca/~chinook/project/legacy.html
- In 1962 the program beat Robert Nealey. IBM says this came after it had played thousands of games against itself. — IBM History: https://www.ibm.com/history/early-games
- Samuel's program learned partly from "book games." It used *Lee's Guide to Checkers* to tune its choices toward moves experts marked as good. — Nilsson, ch. 5 (quoting McCarthy)
- In a rematch the following year, Nealey won one game and drew five. — Schaeffer, Univ. of Alberta (above)
- Against the world-championship players Walter Hellman and Derek Oldbury, the program lost all eight games. — Nilsson (quoting Schaeffer & Lake); Schaeffer. **UNCERTAIN (year: Nilsson says 1965, Schaeffer's page says 1966)**
- Samuel was not the first to write a checkers program. Christopher Strachey's ran on the Ferranti Mark I at Manchester in 1951–52. — Nilsson, ch. 5

## 4. The Long Winter (Minsky–Papert 1969, Lighthill, expert systems)

- In 1969 Marvin Minsky and Seymour Papert published *Perceptrons*, which "proved, among other things, that some versions of Rosenblatt's perceptrons had important limitations." — Nilsson, ch. 16
- Their two best-known examples are *parity* (is the number of lit dots odd or even?) and *connectedness* (is a shape all in one piece?). — MIT Press book page: https://direct.mit.edu/books/monograph/3132/PerceptronsAn-Introduction-to-Computational **UNCERTAIN (seen via search summary of the book; the theorem numbers were not checked)**
- Nilsson doubts that the book alone killed neural-network research. Rosenblatt had moved on to other topics before 1969, and heuristic programming was drawing attention away. — Nilsson, ch. 16
- Minsky co-founded MIT's Artificial Intelligence Laboratory in 1959 and received the A.M. Turing Award in 1969. — MIT News: https://news.mit.edu/2016/marvin-minsky-obituary-0125
- Minsky built "the first neural network simulator" in 1951 as a Princeton graduate student. He also invented the earliest confocal scanning microscope. — MIT News obituary
- Minsky died on 24 January 2016, aged 88. — MIT News obituary
- In Britain, the Science Research Council asked the Cambridge fluid-dynamics expert Sir James Lighthill to review AI. His report, "Artificial Intelligence: A General Survey," split the field into A (advanced automation), B (bridge / building robots) and C (computer-based studies of the central nervous system). — Nilsson, ch. 16; Chilton Computing: http://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm
- Lighthill: "In no part of the field have the discoveries made so far produced the major impact that was then promised." He blamed the "combinatorial explosion." — Nilsson, ch. 16; Chilton Computing
- The report "resulted in a substantial curtailment of AI research in the United Kingdom." Casualties included the FREDDY robot work at Edinburgh. — Nilsson, ch. 16
- Donald Michie later called the cuts "an outrage." — Nilsson, ch. 16
- Expert systems: MYCIN (Stanford, 1970s) advised on infections using IF–THEN rules. It started with 200 rules and had almost 500 by 1978. — Nilsson, ch. 18
- At the 1984 AAAI conference, a panel titled "The 'Dark Ages' of AI – Can We Avoid Them or Survive Them?" warned about an "AI Winter." — Nilsson, §24.4
- The winter came in the mid- to late 1980s. Several AI companies closed. Between 1987 and 1989, DARPA's budget for basic AI and Strategic Computing fell from $47 million to $31 million. — Nilsson, §24.4
- Nilsson's gentle verdict: "the winter endured only for a season – a season not of hibernation but of renewed efforts to carry on." — Nilsson, §24.4

### 4b. The Wide Street — support vector machines (added at coordinator's request)

- Bernhard Boser, Isabelle Guyon and Vladimir Vapnik, "A training algorithm for optimal margin classifiers" (COLT 1992). Guyon and Vapnik were at AT&T Bell Laboratories. — OpenAlex/ACM (doi 10.1145/130385.130401)
- The 1992 abstract gives the key idea: "A training algorithm that maximizes the margin between the training patterns and the decision boundary." — Boser, Guyon & Vapnik 1992
- The name comes from the "supporting patterns": "the subset of training patterns that are closest to the decision boundary." — Boser, Guyon & Vapnik 1992
- In plain words, the SVM draws the widest possible empty street between two groups of points. Only the points on the kerb, the "support vectors," decide where the street goes. (Explanation built from the 1992 abstract above.)
- Corinna Cortes and Vladimir Vapnik (both AT&T), "Support-Vector Networks," *Machine Learning* 20(3), 273–297, September 1995. — Crossref (doi 10.1007/BF00994018): https://link.springer.com/article/10.1007/BF00994018
- The 1995 paper describes "a new learning machine for two-group classification problems." Input vectors are mapped into "a very high-dimension feature space," where a straight (linear) boundary is drawn. It extended the idea to data that cannot be separated perfectly. — Cortes & Vapnik 1995 (abstract, via Springer)
- Head-to-head on handwritten digits (MNIST): an SVM reached 1.1% error and a modified "V-SVM" reached 0.8%. LeNet-5 had 0.95%, or 0.8% with extra distorted training images. — LeCun et al. 1998 (Proc. IEEE): http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf
- Why neural nets fell out of fashion: "In the late 1990s, neural nets and backpropagation were largely forsaken by the machine-learning community… it was commonly thought that simple gradient descent would get trapped in poor local minima." — Nature 2015 review
- **UNCERTAIN (reasonable, but no primary quote found):** "SVMs beat neural nets in the 2000s because they trained reliably with strong theory." Say that SVMs were the fashionable, trusted method, and that deep nets matched them on MNIST.

## 5. Learning Backwards (backprop 1986, gradient descent)

- D. E. Rumelhart, G. E. Hinton & R. J. Williams, "Learning representations by back-propagating errors," *Nature* 323 (issue 6088), 533–536, October 1986. — Nature: https://www.nature.com/articles/323533a0
- Abstract: the procedure "repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the difference between the actual output vector of the net and the desired output vector." — Nature 1986
- The key result: "internal 'hidden' units which are not part of the input or output come to represent important features of the task domain." — Nature 1986
- The abstract says this ability to create new features "distinguishes back-propagation from earlier, simpler methods such as the perceptron-convergence procedure." — Nature 1986
- The **gradient** tells you, "for each weight… by what amount the error would increase or decrease if the weight were increased by a tiny amount. The weight vector is then adjusted in the opposite direction." — Nature 2015 review
- The error "can be seen as a kind of hilly landscape in the high-dimensional space of weight values. The negative gradient vector indicates the direction of steepest descent in this landscape." — Nature 2015 review. (The channel's "hiker walking downhill in fog" is our metaphor for this. The hiker can only feel the slope underfoot.)
- **Stochastic gradient descent** means showing "a few examples," computing the average gradient for them, nudging the weights, and repeating "for many small sets of examples." — Nature 2015 review
- Gradient descent is "a mathematical technique to minimize loss… Gradient descent is older—much, much older—than machine learning." — Google ML Glossary
- **Backpropagation** is "the algorithm that implements gradient descent in neural networks": a forward pass makes a prediction, then a backward pass sends the error back to adjust the weights. — Google ML Glossary
- The fear that a hiker would get stuck in a small hollow (a "poor local minimum") turned out to be overblown: "In practice, poor local minima are rarely a problem with large networks." — Nature 2015 review
- In 1983 Hinton and Terrence Sejnowski invented Boltzmann machines, "one of the first neural networks capable of learning internal representations in neurons that were not part of the input or output." — ACM Turing Award press release, 27 March 2019: https://awards.acm.org/binaries/content/assets/press-releases/2019/march/turing-award-2018.pdf
- ACM: backpropagation "is standard in most neural networks today." — ACM 2019 press release
- LeCun "proposed an early version of the backpropagation algorithm" and a clean derivation of it. — ACM 2019 press release
- **UNCERTAIN / disputed credit:** earlier forms of backpropagation came before 1986 (e.g. Linnainmaa 1970, Werbos 1974). Who "invented" it is argued about, and was not checked here. Say "made famous in 1986."

## 6. Eyes for Machines (LeCun, convolution, MNIST, cheques)

- Y. LeCun et al., "Backpropagation Applied to Handwritten Zip Code Recognition," *Neural Computation* 1(4), 541–551 (1989). It was trained on handwritten zip-code digits "provided by the U.S. Postal Service." — Crossref abstract (doi 10.1162/neco.1989.1.4.541)
- In the late 1980s, "while working at the University of Toronto and Bell Labs, LeCun was the first to train a convolutional neural network system on images of handwritten digits." — ACM 2019 press release
- Convolution in plain words: a small filter slides across the picture looking for the same little pattern everywhere. Without convolutions, a 2K × 2K image would need "4M separate weights." With them, the machine "only has to find weights for every cell in the convolutional filter." — Google ML Glossary (convolution)
- LeCun, Bottou, Bengio & Haffner, "Gradient-based learning applied to document recognition," *Proceedings of the IEEE* 86(11), 2278–2324 (1998). — Crossref (doi 10.1109/5.726791)
- LeNet-5 "contains 340,908 connections, but only 60,000 trainable free parameters," because the filter weights are shared. — LeCun et al. 1998
- MNIST ("modified NIST") was built from NIST Special Databases 1 and 3. It has 60,000 training images, and the experiments used 10,000 test images. — LeCun et al. 1998
- The 1998 check reader "is deployed commercially and reads several million checks per day." — LeCun et al. 1998 (abstract)
- "By the late 1990s this system was reading over 10% of all the cheques in the United States." — Nature 2015 review
- Bengio's probabilistic sequence models "were incorporated into a system used by AT&T/NCR for reading handwritten checks." — ACM 2019 press release
- Even so, "ConvNets were largely forsaken by the mainstream computer-vision and machine-learning communities until the ImageNet competition in 2012." — Nature 2015 review

## 7. The Big Picture Book (ImageNet, AlexNet 2012, GPUs)

- Fei-Fei Li: "together with Professor Kai Li at Princeton University, we launched the ImageNet project in 2007." — Fei-Fei Li, TED2015 transcript: https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures/transcript
- Her reasoning: "by age three, a child would have seen hundreds of millions of pictures of the real world." — TED2015
- "At its peak, ImageNet was one of the biggest employers of the Amazon Mechanical Turk workers: together, almost 50,000 workers from 167 countries around the world helped us to clean, sort and label nearly a billion candidate images." — TED2015
- "In 2009, the ImageNet project delivered a database of 15 million images across 22,000 classes." — TED2015
- The official count today: "14,197,122 images, 21841 synsets indexed," organised by WordNet. — ImageNet: https://www.image-net.org/about.php
- The ImageNet paper appeared at CVPR 2009. In 2019 it won the PAMI Longuet-Higgins Prize as CVPR 2009's most impactful paper. — image-net.org
- A. Krizhevsky, I. Sutskever & G. E. Hinton, "ImageNet Classification with Deep Convolutional Neural Networks," NIPS 2012. The network had "60 million parameters and 650,000 neurons." — NeurIPS proceedings PDF: https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- It was trained on about 1.2 million ImageNet images, which "took five to six days on two NVIDIA GTX 580 3GB GPUs." — AlexNet paper
- One GTX 580 had only 3 GB of memory, so the network was split across two GPUs. — AlexNet paper
- The result was a top-5 test error of 15.3% in ILSVRC-2012, against "26.2% achieved by the second-best entry." — AlexNet paper
- ACM: "Hinton and his students almost halved the error rate for object recognition." The team used "rectified linear neurons and dropout." — ACM 2019 press release
- "The training was done on a computer with two NVIDIA cards in Krizhevsky's bedroom at his parents' house." — Computer History Museum: https://computerhistory.org/blog/chm-releases-alexnet-source-code/
- NVIDIA's CUDA programming system, released in 2007, made GPUs usable beyond 3D graphics. Neural-network training is mostly "repeated matrix multiplications," which GPUs do in parallel. — CHM (above)
- AlexNet was presented at a computer-vision conference in Florence, Italy, in October 2012. — CHM
- Hinton's summary to CHM: "Ilya thought we should do it, Alex made it work, and I got the Nobel Prize." — CHM

## 8. Learning by Playing (TD-Gammon, Atari, AlphaGo)

- Gerald Tesauro, "Temporal Difference Learning and TD-Gammon," *Communications of the ACM* 38(3), 58–68 (March 1995). — Crossref; full text: https://bkgm.com/articles/tesauro/tdl.html
- TD-Gammon, built at IBM, "learned to play excellent backgammon after playing against themselves during millions of games." — Nilsson, §29.6
- One version had 198 inputs, 40 hidden units and 4 outputs, which estimated the chances of each game outcome. — Nilsson, §29.6
- Its hidden weights formed patterns "roughly corresponding to what a knowledge engineer might call useful features," a kind of "automatic feature discovery." — Tesauro 1995
- Version 2.1 came within a whisker of former world champion Bill Robertie over 40 games. Robertie "only in the very last game was… able to pull ahead for an extremely narrow 1-point victory." — Tesauro 1995
- DeepMind's 2013 DQN was "a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels." It was applied to seven Atari 2600 games and "surpassed an expert human player on three of them." — Mnih et al., arXiv:1312.5602: https://arxiv.org/abs/1312.5602
- The 2015 *Nature* version ("Human-level control through deep reinforcement learning," 518, 529–533, 25 Feb 2015) learned 49 classic Atari 2600 games "directly from sensory experience," reaching roughly expert-human level. The reward was the game score. — Nature: https://www.nature.com/articles/nature14236
- Silver et al., "Mastering the game of Go with deep neural networks and tree search," *Nature* 529, 484–489 (online 27 Jan 2016). — Nature: https://www.nature.com/articles/nature16961
- AlphaGo used "value networks" to judge positions and "policy networks" to choose moves. They were trained first on human expert games, then by reinforcement learning from self-play. — Nature 2016
- AlphaGo won 99.8% of games against other Go programs. It beat the European champion (Fan Hui) 5–0 in October 2015, "the first time that a computer program has defeated a human professional player in the full-sized game of Go." — Nature 2016; DeepMind: https://deepmind.google/research/alphago/
- Go has about 10^170 possible board configurations. DeepMind notes this is more than the number of atoms in the known universe. — DeepMind
- AlphaGo beat Lee Sedol 4–1 in Seoul in March 2016. The match was watched by over 200 million people. — DeepMind
- AlphaGo received a 9 dan professional rank, the highest. — DeepMind
- Move 37 (game 2) had about a 1-in-10,000 probability of being played by a human. — DeepMind
- Lee Sedol's move 78 (game 4), a "wedge" in the middle of the board, also had odds of about 1 in 10,000, and it turned the game around. Go players called it "God's Touch." — DeepMind; Wired (Cade Metz, 2016): https://www.wired.com/2016/03/two-moves-alphago-lee-sedol-redefined-future/
- Hassabis told Wired that AlphaGo was unprepared for move 78 "because it didn't think that a human would ever play it." — Wired 2016
- Lee Sedol retired in November 2019: "Even if I become the number one, there is an entity that cannot be defeated." — ABC News (Australia): https://www.abc.net.au/news/2019-11-29/go-grandmaster-lee-se-dol-retires-computers-cannot-be-defeated/11745872

## 9. Words as Points on a Map (embeddings, word2vec)

- In 2000, Bengio's "A Neural Probabilistic Language Model" "introduced high-dimension word embeddings as a representation of word meaning." — ACM 2019 press release
- Mikolov, Chen, Corrado & Dean (Google), "Efficient Estimation of Word Representations in Vector Space," arXiv:1301.3781 (2013). — arXiv: https://arxiv.org/abs/1301.3781
- Their method "takes less than a day to learn high quality word vectors from a 1.6 billion words data set." — Mikolov et al. 2013
- The famous sum: "vector('King') - vector('Man') + vector('Woman') results in a vector that is closest to the vector representation of the word Queen." The word2vec paper credits this finding to Mikolov et al.'s earlier 2013 paper "Linguistic Regularities…" (NAACL). — Mikolov et al. 2013 (arXiv:1301.3781)
- A companion paper: "vec('Madrid') - vec('Spain') + vec('France') is closer to vec('Paris') than to any other word vector." — Mikolov et al., "Distributed Representations of Words and Phrases…," arXiv:1310.4546: https://arxiv.org/abs/1310.4546
- Google's plain version: in an embedding space, the distance "from cow to bull is similar to the distance from ewe (female sheep) to ram (male sheep)." — Google ML Glossary

## 10. Paying Attention (LSTM, then transformers 2017)

- Hochreiter & Schmidhuber, "Long Short-Term Memory," *Neural Computation* 9(8), 1735–1780 (1997). — Crossref; PDF: https://www.bioinf.jku.at/publications/older/2604.pdf
- The problem LSTM solved: learning over long gaps "takes a very long time, mostly because of insufficient, decaying error backflow," as Hochreiter had analysed in 1991. LSTM could bridge "time lags in excess of 1000 discrete-time steps." — LSTM abstract
- Bengio's group "introduced a form of attention mechanism which led to breakthroughs in machine translation." — ACM 2019 press release
- Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser & Polosukhin, "Attention Is All You Need," NIPS 2017 (Long Beach, CA). The authors were at Google Brain, Google Research and the University of Toronto. — arXiv: https://arxiv.org/abs/1706.03762
- Abstract: "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely." — Vaswani et al. 2017
- Footnote: "Equal contribution. Listing order is random." It adds that "Jakob proposed replacing RNNs with self-attention." — Vaswani et al. 2017
- Attention in the paper's words: "mapping a query and a set of key-value pairs to an output… computed as a weighted sum" of the values. In plain words, each word asks a question and looks around at every other word, weighing how much each one matters. — Vaswani et al. 2017
- The big model reached 28.4 BLEU on English→German and 41.8 BLEU on English→French. Training took "3.5 days on eight GPUs" (NVIDIA P100s). The base model trained in 12 hours. — Vaswani et al. 2017
- Transformers train faster partly because they are "more parallelizable": they look at all the words at once instead of one after another. — Vaswani et al. 2017
- Google today: a large language model is, "more informally, any Transformer-based language model, such as Gemini or GPT." — Google ML Glossary

## 11. The Next Word (GPT, scale, tokens, RLHF, hallucination, what's inside)

- GPT-2 (OpenAI, 2019) "is a 1.5B parameter Transformer." It was trained on WebText, text from about 8 million documents (40 GB) gathered from 45 million links shared on Reddit. — Radford et al. 2019: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- GPT-2 was released in stages. The 124-million-parameter model came out in February 2019, larger ones followed through the year, and the full 1.5-billion model came out with the November 2019 report. — Solaiman et al., "Release Strategies and the Social Impacts of Language Models," arXiv:1908.09203: https://arxiv.org/abs/1908.09203
- GPT-3: "an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model." — Brown et al., "Language Models are Few-Shot Learners," arXiv:2005.14165 (May 2020): https://arxiv.org/abs/2005.14165
- "All models were trained for a total of 300 billion tokens." — GPT-3 paper
- Filtered Common Crawl (410 billion tokens) made up 60% of GPT-3's training mix. Wikipedia made up 3%. — GPT-3 paper, Table 2.2
- People trying to tell GPT-3's ~500-word news articles from human ones did "barely above chance at ∼52%." — GPT-3 paper
- **Next-token prediction:** "autoregressive" means the model writes one token at a time, each time predicting what comes next from everything before. — GPT-3 paper (definition of the model); plain gloss ours
- **Tokens:** OpenAI's rule of thumb is that 1 token ≈ 4 characters of English ≈ ¾ of a word, so 100 tokens ≈ 75 words. — OpenAI Help Center: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them **UNCERTAIN (page blocked to our fetcher; wording confirmed via search results only)**
- **RLHF** (InstructGPT): Ouyang et al., "Training language models to follow instructions with human feedback," arXiv:2203.02155 (4 March 2022). — arXiv: https://arxiv.org/abs/2203.02155
- The three steps: (1) labellers write demonstrations and a model is fine-tuned on them; (2) labellers rank outputs and a reward model learns their preferences; (3) the model is optimised against that reward model with reinforcement learning (PPO). — InstructGPT paper
- OpenAI "hire[d] a team of 40 contractors to label" the data. — InstructGPT paper
- "Outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters." — InstructGPT paper
- ChatGPT launched on 30 November 2022, "fine-tuned from a model in the GPT-3.5 series." — OpenAI: https://openai.com/index/chatgpt/ **UNCERTAIN (openai.com blocked our fetcher; wording confirmed via search result only; the date is well established)**
- **Hallucination**: "The production of plausible-seeming but factually incorrect output by a generative AI model." Google notes that "confabulation is probably a more technically accurate term." — Google ML Glossary
- OpenAI researchers (Kalai et al., Sept 2025): "Like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty." — arXiv:2509.04664: https://arxiv.org/abs/2509.04664
- Their explanation: "the training and evaluation procedures reward guessing over acknowledging uncertainty." — Kalai et al. 2025
- Their example: asked for Adam Kalai's birthday "if you know," a model gave three different wrong dates in three tries. — Kalai et al. 2025
- **What's inside:** "We mostly treat AI models as a black box: something goes in and a response comes out, and it's not clear why the model gave that particular response instead of another." — Anthropic, "Mapping the Mind of a Large Language Model" (21 May 2024): https://www.anthropic.com/research/mapping-mind-language-model
- Anthropic found millions of "features" (patterns of neuron activity matching concepts) inside Claude 3 Sonnet. One feature lit up for the Golden Gate Bridge, in English, Japanese, Chinese, Greek, Vietnamese, Russian and even images. — Anthropic 2024
- When researchers turned that feature up, the model became "effectively obsessed with the bridge, bringing it up in answer to almost any query." — Anthropic 2024
- Hinton, on leaving Google: large language models hold far more knowledge than any person with fewer connections than a brain, so "maybe it's actually got a much better learning algorithm than us." — MIT Technology Review, 2 May 2023: https://www.technologyreview.com/2023/05/02/1072528/geoffrey-hinton-google-why-scared-ai/
- Hinton left Google after about a decade so he could "talk about AI safety issues without having to worry about how it interacts with Google's business." — MIT Technology Review 2023

## 12. Closing — what learning means; the prizes

- 27 March 2019: ACM named Bengio, Hinton and LeCun as the 2018 A.M. Turing Award laureates "for conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing." The award carries $1 million. — ACM press release: https://awards.acm.org/binaries/content/assets/press-releases/2019/march/turing-award-2018.pdf
- 8 October 2024: the Nobel Prize in Physics went to John J. Hopfield (Princeton) and Geoffrey Hinton (Toronto) "for foundational discoveries and inventions that enable machine learning with artificial neural networks." — NobelPrize.org: https://www.nobelprize.org/prizes/physics/2024/press-release/
- The Nobel committee: Hopfield "created an associative memory that can store and reconstruct images and other types of patterns in data." Fed a distorted image, the network lowers its "energy" step by step until it finds the closest stored image. — NobelPrize.org
- Hinton "used the Hopfield network as the foundation for a new network… the Boltzmann machine," using "tools from statistical physics." — NobelPrize.org
- Hopfield was born in 1933 in Chicago. Hinton was born in 1947 in London and took his PhD at Edinburgh in 1978. Prize: 11 million Swedish kronor, shared equally. — NobelPrize.org
- The 2024 Nobel Prize in Chemistry went half to David Baker "for computational protein design" and half jointly to Demis Hassabis and John Jumper "for protein structure prediction." — NobelPrize.org: https://www.nobelprize.org/prizes/chemistry/2024/press-release/
- "In 2020, Demis Hassabis and John Jumper presented an AI model called AlphaFold2." It can predict the structure of "virtually all the 200 million proteins that researchers have identified," and has been used by "more than two million people from 190 countries." — NobelPrize.org
- A quiet closing line from Turing: "We can only see a short distance ahead, but we can see plenty there that needs to be done." — Turing 1950 (final sentence)

---

## Human details

1. Walter Pitts, as a boy of about 12, hid from bullies in a Detroit library. He read all of *Principia Mathematica* in three days and wrote to Bertrand Russell about errors he found. At 15 he ran away to Chicago. — Nautilus: https://nautil.us/the-man-who-tried-to-redeem-the-world-with-logic-235253 **UNCERTAIN (a much-retold story; the details come from later recollections)**
2. Pitts later destroyed his dissertation and his unpublished work, and died alone in 1969. — Nautilus (same)
3. Rosenblatt's interests were "exceptionally broad." He composed music, studied astronomy and proposed a new technique to detect "stellar satellites" (bodies orbiting other stars), and applied computers to political statistics for Eugene McCarthy's campaigns. — Cornell memorial statement
4. He bought a $3,000 telescope and built an observatory with his students in his yard in Brooktondale, NY. — Cornell Chronicle
5. Rosenblatt drowned in a sailing accident on Chesapeake Bay on 11 July 1971, his 43rd birthday. — Cornell memorial statement; the Cornell Chronicle names his sloop the *Shearwater*. **UNCERTAIN (boat name; some accounts say "Clearwater")**
6. His colleagues remembered him as "one of the most selfless and sympathetic colleagues, whose good humor and brilliant mind left a deep impression on us all." — Cornell memorial statement
7. The Mark I Perceptron learned by physically turning knobs: little electric motors rotated volume controls. — Nilsson, §4.2
8. Thomas Watson Sr. predicted that Samuel's checkers demo would lift IBM stock by 15 points. "It did." — Nilsson; Schaeffer
9. After losing to Samuel's program in 1962, Nealey wrote: "In the matter of the endgame, I have not had such competition from any human being since 1954, when I lost my last game." — quoted by Schaeffer (Univ. of Alberta) and fierz.ch **UNCERTAIN (quote wording seen via search results; Nealey's "master" status was questioned by Schaeffer)**
10. The Dartmouth founders thought one summer, "2 month, 10 man," would bring "a significant advance." — Dartmouth proposal, 1955
11. Weizenbaum's secretary, who knew ELIZA was just a program, asked him after a few exchanges to leave the room so she could talk to it in private. — Weizenbaum, *Computer Power and Human Reason* (1976), via New Republic: https://newrepublic.com/article/181189/inventor-chatbot-tried-warn-us-ai-joseph-weizenbaum-computer-power-human-reason **UNCERTAIN (secondary source only; the book was not read directly)**
12. Minsky, remembered as the "father of AI," also invented the confocal scanning microscope. — MIT News
13. At the 1984 AAAI conference, AI researchers held a panel on the coming "Dark Ages" and warned of an "AI winter" before it arrived. — Nilsson, §24.4
14. Hinton "never sits down, due to a bulging disc in his spine, dislodged during an attempt at age 19 to move a heavy heater for his mother… in 2005, he stopped sitting almost entirely." — Toronto Life (2018), archived: https://web.archive.org/web/2023/https://torontolife.com/life/ai-superstars-google-facebook-apple-studied-guy/ ; U of T News (31 Jan 2018): "a back problem that prevents him from sitting and makes international travel a week-long affair": https://www.utoronto.ca/news/u-t-s-geoffrey-hinton-toronto-life-looks-man-behind-machines
15. When the Nobel committee called, Hinton was "in a cheap hotel in California, without an internet connection." He said: "I was planning to get an MRI scan today, but I guess I'll have to cancel that." — NobelPrize.org interview: https://www.nobelprize.org/prizes/physics/2024/hinton/interview/
16. AlexNet, the network that changed computer vision, was trained on two gaming graphics cards in Alex Krizhevsky's bedroom at his parents' house. — Computer History Museum
17. "Ilya thought we should do it, Alex made it work, and I got the Nobel Prize." — Hinton to CHM
18. LeCun's convolutional network read handwritten numbers on bank cheques. By the late 1990s it read over 10% of all cheques in the US. — Nature 2015 review
19. After AlphaGo's move 37, Lee Sedol left the match room and took nearly fifteen minutes to answer. The European champion Fan Hui, watching, kept saying, "So beautiful. So beautiful." — Wired (Cade Metz, 2016)
20. ABC News (2019) says Lee Sedol remains the only human ever to beat that program (the 2016 AlphaGo). He retired three years later. — ABC News 2019; DeepMind
21. Fei-Fei Li's ImageNet was built with almost 50,000 crowd workers in 167 countries. — TED2015
22. The Transformer paper's author list is in random order, by the authors' own note. — Vaswani et al. 2017

---

## UNCERTAIN — collected

1. **Lighthill report date:** 1972 (Chilton, Nilsson) vs the commonly cited 1973.
2. **Samuel vs. Hellman/Oldbury:** 1965 (Nilsson) vs 1966 (Schaeffer).
3. **Nealey's status and quote:** IBM's "former Connecticut champion" is wrong per Schaeffer. The endgame quote was seen via search results only.
4. **"Samuel coined 'machine learning'":** IBM says so. We only show the phrase in his 1959 title.
5. **Rosenblatt's boat name:** *Shearwater* (Cornell Chronicle) vs *Clearwater*. Some colleagues questioned whether his death was purely an accident; there is no official record. Leave that out.
6. **Mark I "512 association units, 8 response units, camera":** only in Wikipedia-derived sources. The Mark I operators' manual (DTIC AD0236965, 1960) could not be read. Safe facts: 400 photosensors in a 20×20 grid, motor-driven potentiometers, first demonstrated on 23 June 1960.
7. **"$2,000,000 Weather Bureau IBM 704"** in the 1958 UPI story: snippet only, not used.
8. **Minsky–Papert parity/connectedness details:** seen via summaries only.
9. **Backpropagation priority** (Linnainmaa 1970, Werbos 1974 vs 1986): disputed, not checked.
10. **"SVMs beat neural nets because…":** a soft claim with no primary quote. The MNIST numbers and the Nature 2015 "forsaken" line are verified.
11. **OpenAI token rule of thumb** (4 chars / ¾ word): page blocked, confirmed via search results.
12. **ELIZA secretary story:** secondary sources only (from the 1976 book).
13. **Pitts' library and Russell-letter story:** a retold legend (Nautilus).
14. **"20 million cheques a day"** (web snippet): not verified. Use "over 10% of US cheques" or "several million a day."
15. **Minsky Turing Award year:** 1969 (MIT, ACM) vs 1970 (Cornell Chronicle; probably the presentation year).
16. **Dartmouth workshop exact dates** (summer 1956): not verified. Say "the summer of 1956."
17. **DNNresearch sold to Google in 2013 (auction, ~$44M, from *Genius Makers*):** not verified. Leave it out or flag it.
18. **ChatGPT announcement wording** ("fine-tuned from a model in the GPT-3.5 series"): openai.com blocked, search result only. The 30 Nov 2022 date is safe.

---

## Resources for the description

- Computing Machinery and Intelligence (Turing, 1950, full text) — UMBC course copy — https://courses.cs.umbc.edu/471/papers/turing.pdf
- A Proposal for the Dartmouth Summer Research Project on AI (1955) — Stanford (John McCarthy) — http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html
- Artificial Intelligence Coined at Dartmouth — Dartmouth College — https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth
- The Man Who Tried to Redeem the World with Logic (Walter Pitts) — Nautilus — https://nautil.us/the-man-who-tried-to-redeem-the-world-with-logic-235253
- Professor's perceptron paved the way for AI – 60 years too soon — Cornell Chronicle — https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon
- Some Studies in Machine Learning Using the Game of Checkers (Samuel, 1959) — MIT CSAIL copy — https://people.csail.mit.edu/brooks/idocs/Samuel.pdf
- Early computer games at IBM (Samuel's checkers) — IBM History — https://www.ibm.com/history/early-games
- Arthur Samuel's Legacy — University of Alberta (Jonathan Schaeffer) — https://webdocs.cs.ualberta.ca/~chinook/project/legacy.html
- The Quest for Artificial Intelligence (Nils Nilsson, free book) — Stanford — https://ai.stanford.edu/~nilsson/QAI/qai.pdf
- Marvin Minsky, "father of artificial intelligence," dies at 88 — MIT News — https://news.mit.edu/2016/marvin-minsky-obituary-0125
- The Lighthill Report — Chilton Computing — http://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm
- Learning representations by back-propagating errors (1986) — Nature — https://www.nature.com/articles/323533a0
- Deep learning (LeCun, Bengio & Hinton, 2015 review) — University of Toronto — https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf
- Fei-Fei Li: How we're teaching computers to understand pictures — TED — https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures/transcript
- ImageNet Classification with Deep Convolutional Neural Networks (AlexNet, 2012) — NeurIPS — https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- CHM Releases AlexNet Source Code — Computer History Museum — https://computerhistory.org/blog/chm-releases-alexnet-source-code/
- Human-level control through deep reinforcement learning (Atari, 2015) — Nature — https://www.nature.com/articles/nature14236
- Mastering the game of Go with deep neural networks and tree search (2016) — Nature — https://www.nature.com/articles/nature16961
- AlphaGo — Google DeepMind — https://deepmind.google/research/alphago/
- Efficient Estimation of Word Representations in Vector Space (word2vec) — arXiv — https://arxiv.org/abs/1301.3781
- Attention Is All You Need (2017) — arXiv — https://arxiv.org/abs/1706.03762
- Language Models are Few-Shot Learners (GPT-3, 2020) — arXiv — https://arxiv.org/abs/2005.14165
- Training language models to follow instructions with human feedback (InstructGPT) — arXiv — https://arxiv.org/abs/2203.02155
- Mapping the Mind of a Large Language Model — Anthropic — https://www.anthropic.com/research/mapping-mind-language-model
- The Nobel Prize in Physics 2024 — NobelPrize.org — https://www.nobelprize.org/prizes/physics/2024/press-release/

Books: Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* (2019); Cade Metz, *Genius Makers* (2021); Nils J. Nilsson, *The Quest for Artificial Intelligence* (2010, free PDF above); Richard Sutton & Andrew Barto, *Reinforcement Learning: An Introduction* (2nd ed., 2018, free at incompleteideas.net).
