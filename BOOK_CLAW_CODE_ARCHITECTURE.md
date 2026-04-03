# Claw Code — Architecture of an AI Agent Harness
**A technical book about the Python reimplementation of the Claude Code agent harness architecture**

---

## Table of Contents

1. Chapter 1: Introduction and Background Story
2. Chapter 2: Ethics and Law of AI Reimplementation
3. Chapter 3: High-Level Architecture
4. Chapter 4: The CLI Entry Point
5. Chapter 5: Data Models & Type System
6. Chapter 6: The Command and Tool Catalog
7. Chapter 7: The Runtime Environment
8. Chapter 8: The Query Engine
9. Chapter 9: Session Management & Persistence
10. Chapter 10: Setup, Bootstrap & Initialization
11. Chapter 11: Execution Layer & Runtime Modes
12. Chapter 12: The Subsystem Architecture
13. Chapter 13: Parity Checking & Quality Assurance
14. Chapter 14: Summary and Outlook

---

# Chapter 1: Introduction and Background Story

## 1.1 What Is Claw Code?

Claw Code is a standalone Python reimplementation of the agent harness architecture of Claude Code -- Anthropic's command-line agent system. The project did not arise as an academic exercise, not as a prototype, and not as a slowly grown hobby. It arose in a single night, under pressure, with the goal of replicating the core architecture of one of the most advanced AI agent systems in the world in Python before morning broke.

To understand the context, one must first grasp what Claude Code actually is. Claude Code is Anthropic's official command-line interface for the Claude language model. It is not a simple chat interface, but rather a complete agent system: a so-called *harness* that wires tools, orchestrates tasks, manages runtime context, checks permissions, persists sessions, and intelligently routes prompts to the appropriate commands and tools. The original implementation is written in TypeScript and comprises a complex web of subsystems -- from the bootstrap phase through tool execution to session management.

Claw Code replicates exactly these architectural patterns. It is not a fork, not a copy-paste, not a wrapper around existing code. It is a complete reimplementation in Python that uses the same design decisions, the same layering, and the same orchestration patterns -- but builds on an entirely different codebase. The project uses exclusively the Python standard library and has zero external dependencies.

Expressed in numbers, Claw Code at the time of publication comprises:

- **66 Python files** in the source directory `src/`
- **207 mirrored commands** from the archived TypeScript original
- **184 mirrored tools** from the archived TypeScript original
- **30 subsystem packages** that mirror the directory structure of the original
- **24 CLI commands** callable via `python3 -m src.main`
- **0 external dependencies** -- everything runs with the Python standard library

These numbers are not arbitrary. They reflect a deliberate decision: The goal was not to build a minimal proof of concept, but to map the full surface of the original system in Python -- every command, every tool, every subsystem. The 207 commands and 184 tools are stored as JSON snapshots in `src/reference_data/` and are loaded at runtime, cataloged, and used for routing decisions.

## 1.2 The Night It All Began

On March 31, 2026, at 4 AM, Sigrid Jin -- the author of this project -- was awakened by a flood of notifications on the phone. The Claude Code source code had been exposed. Not through an official release, not through a planned open-source release, but through a leak. The entire developer community was in uproar.

The situation was double-edged. On one hand, for the first time, the complete architecture of one of the most capable AI agent systems lay exposed. For anyone interested in harness engineering -- that is, the question of how agent systems wire tools, steer tasks, and manage their runtime context -- this was an unprecedented insight. On the other hand, the code was proprietary. Simply possessing it, let alone using or redistributing it, immediately raised legal questions.

Jin's girlfriend in Korea was seriously worried. The mere fact that the code was on his machine could trigger legal action from Anthropic. So Jin made a decision that many engineers would make under pressure when they are simultaneously fascinated and concerned: He sat down, studied the architecture -- not the code itself, but the patterns, the layers, the wiring -- and began to rebuild the whole thing from scratch in Python.

The porting session lasted the entire night. From the first reading of the harness structure through designing the Python directory tree to writing the first tests, everything was completed in a single, continuous sprint. Before the sun rose, the first functional Python rewrite was pushed to GitHub.

This pace would not have been possible without a crucial tool: oh-my-codex.

## 1.3 The Role of oh-my-codex (OmX)

oh-my-codex -- OmX for short -- is a workflow orchestration layer developed by Yeachan Heo (known as `@bellman_ych` on X). OmX builds on OpenAI's Codex and provides an infrastructure for coordinated, parallel, and persistent AI-assisted development workflows. For the Claw Code porting effort, OmX was not just a useful aid -- it was the backbone of the entire process.

Two OmX modes were decisive:

### The `$team` Mode: Parallel Code Review

The `$team` mode allows multiple AI agents to be deployed simultaneously on the same code -- for parallel review, architectural feedback, and quality control. During the porting night, this meant that Jin was not working alone against the clock. Multiple agents could simultaneously check the emerging Python structure for consistency, completeness, and architectural correctness.

Imagine: One agent verifies whether the command catalog mirroring is complete. A second agent checks whether tool registration works correctly. A third agent verifies whether session persistence maps the same lifecycle as the original. All of this happens in parallel, coordinated by OmX, while the main developer writes the next component.

### The `$ralph` Mode: Persistent Execution Loops

The `$ralph` mode goes one step further. It provides persistent execution loops with architecture-level verification. This means: An agent does not run once and return a result, but stays active, repeatedly runs tests, checks the results, and reports deviations. For the Claw Code porting effort, this was indispensable. The `$ralph` mode ensured that every newly written Python file was not only syntactically correct but architecturally fit into the overall picture.

The entire porting session -- from reading the original harness structure to creating a working Python directory tree with tests -- was steered through OmX orchestration. Jin works actively with Yeachan Heo today, the creator of OmX, to continue developing the project.

## 1.4 Sigrid Jin and the 25 Billion Tokens

Who is the person behind Claw Code? To understand that, it is worth looking at an article that appeared in the Wall Street Journal on March 21, 2026 -- ten days before the porting night. The article bore the title *"The Trillion Dollar Race to Automate Our Entire Lives"* and dealt with the growing community of power users who push AI agent systems like Claude Code to their limits.

Sigrid Jin was highlighted as one of the most active users:

> AI startup employee Sigrid Jin, who attended the dinner in Seoul, single-handedly consumed 25 billion Claude Code tokens over the past year. At the time, usage limits were looser, allowing early enthusiasts to reach tens of billions of tokens at very low cost.

25 billion tokens. This number is not just impressive in its magnitude -- it is an indicator of the depth of engagement with the system. Anyone who consumes that many tokens is not experimenting occasionally. He or she lives in the system, understands its limits, knows its weaknesses, and knows where the architecture gives way under load.

The article also made clear that Jin is not a dogmatic adherent of a single AI lab. The various available tools -- Claude Code, Codex, and others -- have different strengths and weaknesses. Codex was said to be better at logical reasoning, while Claude Code generates cleaner, more shareable code. This pragmatic stance -- choosing the best tool for the task at hand rather than remaining loyal to a single provider -- is also reflected in the architecture of Claw Code, which replicates Claude Code's structures but is deliberately conceived as an independent, vendor-agnostic Python project.

In February 2026, Jin flew to San Francisco for the first birthday party of Claude Code, where attendees stood in line to exchange ideas with the developer team. Among the guests were a practicing cardiologist from Belgium who had developed a patient navigation app, and a California lawyer who was automating building permits. Jin described the event as a "sharing party": lawyers, doctors, dentists -- people without software engineering backgrounds who were using AI agents as tools for their own fields.

This experience -- the observation that AI agent systems have long outgrown the boundaries of traditional software development -- is a key driving force behind Claw Code. The project aims not only to create a technical reference implementation but also to make the underlying architectural patterns accessible to a broader community.

## 1.5 The Clean-Room Approach

A central principle of Claw Code is the so-called clean-room approach. This term originally comes from the semiconductor industry and refers to a procedure in which a product is rebuilt without directly using the original source code. Instead, one studies the architecture, the interfaces, and the behavior of the original and then reimplements everything from scratch.

For Claw Code, this concretely means:

1. **Replicate architectural patterns, not copy code.** The Python implementation mirrors the layering of the original -- bootstrap phase, tool wiring, prompt routing, session management -- but the actual source code is entirely rewritten.

2. **JSON snapshots as reference data.** The 207 commands and 184 tools of the original are captured as JSON files in `src/reference_data/`. These snapshots contain the name, source hint, and responsibility of each command and tool, but no executable code from the original. They serve as a metadata catalog, not as code duplication.

3. **Standalone data models.** The data classes in `models.py` -- `Subsystem`, `PortingModule`, `PortingBacklog`, `UsageSummary`, `PermissionDenial` -- are standalone Python definitions built on `dataclasses`. They model the same concepts as the original but with an idiomatic Python API.

4. **No external dependencies.** The entire project runs exclusively with the Python standard library. It uses `json`, `argparse`, `dataclasses`, `pathlib`, `uuid`, `platform`, `sys`, `functools`, and `collections` -- all modules available in every standard Python installation. No `pip install` steps, no third-party libraries, no hidden dependencies.

5. **Legal and ethical cleanliness.** Jin has intensively engaged with the legal and ethical questions surrounding the use of the exposed code. The repository even contains a detailed essay titled *"Is Legal the Same as Legitimate? AI Reimplementation and the Erosion of Copyleft"*, which illuminates these questions from various perspectives. The exposed snapshot is no longer part of the tracked repository state. The project focuses exclusively on the Python porting work.

This clean-room approach is not merely a legal safeguard. It forces the developer to make every architectural decision consciously rather than blindly adopting it from the original. The result is a project that uses the same patterns but was built from its own understanding -- and is thereby often clearer and more readable than the original.

## 1.6 Summary

Claw Code is more than a port. It is a case study in harness engineering: the art of not just building AI agents, but wiring them correctly. It shows how an experienced practitioner -- armed with 25 billion tokens of experience, an OmX orchestration system, and a single night -- can replicate the core architecture of one of the most advanced AI agent systems in the world in Python without copying a single line of proprietary code.

In the following chapters, we will examine each layer of this architecture in detail: the mirror layer with its JSON snapshots, the orchestration layer with prompt routing and session management, the infrastructure layer with setup, permissions, and persistence, and finally the 30 subsystems that round out the overall picture.



# Chapter 2: Ethics and Law of AI Reimplementation

## 2.1 Introduction: When Machines Rewrite the Code

On March 9, 2026, the South Korean software developer and open-source activist Hong Minhee published an essay that immediately sparked heated discussions in the developer community. The title -- *Is Legal the Same as Legitimate: AI Reimplementation and the Erosion of Copyleft* -- posed a question that reaches far beyond the specific occasion: Is what is legally permissible also what is socially and ethically justifiable? Hong Minhee's text takes a single incident as its starting point -- the AI-assisted reimplementation of a widely used Python library -- and unfolds from it a fundamental critique of the way the open-source world is dealing with the emergence of generative AI systems.

For this book, this essay is of particular significance because the Claw Code project itself operates precisely in the field of tension that Hong Minhee describes. Claw Code is a reimplementation of the Claude Code agent harness architecture -- first in Python, later in Rust -- that arose after the Claude Code source code was exposed on March 31, 2026. The question of whether such a reimplementation is legally permissible, ethically justifiable, and socially legitimate directly concerns this project. This chapter therefore undertakes the attempt to present Hong Minhee's argumentation in detail, critically assess it, and apply it to the specific situation of Claw Code.

## 2.2 The chardet Case: Anatomy of a License Change

### 2.2.1 What Happened

Dan Blanchard, the maintainer of chardet -- a Python library for detecting text encodings that is downloaded by approximately 130 million projects per month -- published version 7.0 of his library in early March 2026. This version was 48 times faster than its predecessor, supported multi-core processing, and was redesigned from the ground up. In the list of contributors, an unusual name appeared: Anthropic's Claude. The license had changed from the LGPL (GNU Lesser General Public License) to the MIT license.

Blanchard's account: He had not directly examined the existing source code. Instead, he had only passed the API specification and the test suite to Claude and asked the AI system to reimplement the library from scratch. The resulting code showed less than 1.3 percent similarity to any previous version according to a JPlag analysis. His conclusion: It constituted an independent new work, and he was not obligated to continue the LGPL.

Mark Pilgrim, the original author of the library, publicly objected via a GitHub issue. The LGPL requires that modifications be distributed under the same license. A reimplementation created with extensive knowledge of the existing codebase could not, in Pilgrim's view, qualify as a clean-room implementation.

### 2.2.2 Why This Case Is Paradigmatic

The chardet case concentrates several developments that would be significant individually, but in combination create a qualitatively new situation:

First, *speed*: What previously would have required months or years of manual programming work happened within hours or days. The reimplementation of a library with 130 million monthly downloads is no longer a theoretical scenario but a practically demonstrated process.

Second, *scalability*: If a single person with the help of an AI system can reimplement such a widely used library, then this is fundamentally possible for any copyleft-protected software. The costs of reimplementation, which previously represented a practical barrier to circumventing copyleft, have dropped dramatically.

Third, the *legal gray zone*: The question of whether an AI-assisted reimplementation qualifies as a derivative work under copyright law is legally unresolved. The low JPlag similarity provides a quantitative argument for the independence of the new work, but quantitative similarity measures do not necessarily capture the adoption of architectural decisions, algorithmic strategies, or test logic.

Fourth, the *license direction*: The switch from LGPL to MIT means that subsequent derivative works are no longer required to disclose their source code. An obligation that applied to a library with 130 million monthly downloads has been eliminated in one stroke.

## 2.3 The GNU Analogy and Why It Points in the Wrong Direction

### 2.3.1 The Argument from Antirez

Salvatore Sanfilippo, better known as Antirez and creator of Redis, published a detailed defense of AI reimplementation. His central argument rests on historical precedent: When the GNU project reimplemented the UNIX userspace, it was lawful. Likewise Linux. Copyright protects concrete expressions -- the actual code, its structure, its specific mechanisms -- but not ideas or behaviors. AI-assisted reimplementation moves on the same legal ground. Therefore, it is lawful.

### 2.3.2 Hong Minhee's Counterargument: The Direction of the Vector

Hong Minhee does not dispute the legal analysis. What he disputes is the leap from the legal to the social conclusion -- and he does so with an elegant argumentative maneuver: He takes the GNU analogy seriously and shows that it proves the opposite of what Antirez intends.

When GNU reimplemented the UNIX userspace, the vector ran from proprietary to free. Stallman used the limits of copyright to transform proprietary software into free software. The ethical force of this project came not from its legal permissibility -- it came from the direction in which it moved: It expanded the commons.

In the chardet case, the vector runs in the opposite direction. Software that was protected by a copyleft license -- a license that guarantees users the right to study, modify, and redistribute derivative works under the same terms -- was reimplemented under a permissive license that contains no such guarantee. This is not a reimplementation that expands the commons. It is one that removes the fence that protected the commons.

Hong Minhee's formulation is precise: Antirez invokes the GNU precedent, but this precedent is a counterexample to his conclusion, not a supporting one.

### 2.3.3 Assessment of the Vector Argument

The strength of Hong Minhee's argument lies in its structural clarity. He does not dispute the formal analogy -- yes, both are reimplementations -- but shows that the formal analogy conceals the decisive difference: the direction of the ethical transfer.

One could object that the direction of the vector is a matter of perspective. From the perspective of a developer who wants to use chardet in an MIT-licensed project, the vector also runs from restrictive to free. But this argument confuses individual convenience with collective freedom. The LGPL does not protect the freedom of the individual developer to do whatever they want with code, but rather the freedom of all users to inspect and modify the code and its derivatives. When this guarantee disappears, it is precisely the users without their own development resources who bear the damage in the long run.

## 2.4 The Illusion of the "Friendlier" Permissive License

### 2.4.1 Ronacher's Position

Armin Ronacher, the creator of Flask, expressly welcomed the relicensing. He disclosed that he has a personal interest in the outcome: He himself had wished for years that chardet stood under a non-GPL license. He considers the GPL to be a contradiction to the spirit of sharing because it restricts what can be done with code.

### 2.4.2 What the GPL Actually Prohibits -- and What It Does Not

Hong Minhee points out that Ronacher's claim rests on a fundamental misunderstanding of the GPL.

The GPL does not prohibit keeping source code private. It imposes no restrictions whatsoever on the private modification and use of GPL software. The conditions of the GPL are triggered only by distribution. Anyone who distributes modified code or offers it as a network service must make the source code available under the same terms.

This is not a restriction on sharing. It is a condition attached to sharing: If you share, you must share alike. The requirement to give improvements back to the commons is not a mechanism that suppresses sharing -- it is a mechanism that makes sharing recursive and self-reinforcing.

The contrast with the MIT license clarifies the point: Under MIT, anyone may take code, improve it, and enclose it in a proprietary product. One can receive from the commons without giving anything back. When Ronacher calls this structure "more sharing-friendly," he uses a concept of sharing with a built-in direction: Sharing flows toward those who have more capital and more engineers to benefit from it.

### 2.4.3 The Historical Testimony

Hong Minhee supports his argument with a historical reference: In the 1990s, companies routinely absorbed GPL code into proprietary products -- not because they had chosen permissive licenses, but because copyleft enforcement was lax. The strengthening of copyleft mechanisms closed this gap. For individual developers and small projects without the resources to compete on anything other than reciprocity, copyleft was what made the exchange approximately fair.

This historical point is essential for evaluating the chardet case. The LGPL was not an arbitrarily chosen detail, but the mechanism that ensured contributions to the library did not disappear into proprietary products without users having access to the improved code.

### 2.4.4 The Self-Refuting Example

Perhaps the sharpest piece in Hong Minhee's essay is his analysis of a detail that Ronacher mentions in passing: Vercel reimplemented GNU Bash with the help of AI and published the result. Subsequently, Vercel reacted visibly upset when Cloudflare reimplemented Next.js in the same way.

Next.js is under the MIT license. Cloudflare's vinext violated no license -- it did exactly what Ronacher calls a contribution to the culture of openness, applied to a permissively licensed codebase. Vercel's reaction had nothing to do with license violation; it was purely competitive and territorial.

The implicit position reads: The reimplementation of GPL software as MIT is a victory for sharing, but the reimplementation of one's own MIT software by a competitor is grounds for outrage. This is what the claim that permissive licensing is "more sharing-friendly" than copyleft looks like in practice. The spirit of sharing flows, as it turns out, only in one direction: from oneself outward.

Hong Minhee's observation on this is cutting: When one presents evidence that speaks against one's own position, acknowledges it, and then proceeds unchanged to the original conclusion, that is a signal that the conclusion preceded the argument.

## 2.5 Legal Permissibility Versus Social Legitimacy

### 2.5.1 The Central Distinction

Hong Minhee's essay culminates in a distinction that is fundamental to the entire debate about AI reimplementation: Law sets a floor. Clearing that floor does not mean the behavior is right.

Both -- Antirez and Ronacher -- treat legal permissibility as a proxy for social legitimacy. Antirez concludes his careful legal analysis as if it settles the matter. Ronacher concedes that "there is an obvious moral question here, but it doesn't necessarily interest me." Both treat legal permissibility as a sufficient condition. But the law only says which behavior it will not prevent -- it does not certify that behavior as right.

Hong Minhee draws parallels: Aggressive tax minimization that never crosses into illegality can nevertheless be widely considered antisocial. A pharmaceutical company that legally acquires a patent on a long-generic drug and increases the price a hundredfold has done something legal, but that does not make it right. Legality is a necessary condition; it is not a sufficient one.

### 2.5.2 The Breach of the Social Compact

In the chardet case, the distinction is even sharper. What the LGPL protected was not Blanchard's work alone. It was a social compact to which everyone who contributed to the library over twelve years had agreed. The terms of that compact were: If you take this and build upon it, you share back under the same terms.

This compact functioned as a legal instrument, but it was also the foundation of trust that made contributions rational. The fact that a reimplementation might legally qualify as a new work, and the fact that it represents a breach of trust toward the original contributors, are separate questions. If a court ultimately rules in favor of Blanchard, that ruling tells us what the law allows. It does not tell us that the action was right.

Zoe Kooyman, executive director of the Free Software Foundation, put it succinctly: "Refusing to grant others the rights you yourself received as a user is highly antisocial, regardless of the method used to do so."

### 2.5.3 The Positionality Problem

Hong Minhee poses a question that is rarely asked in technical debates: From what position are the participants arguing?

Antirez created Redis. Ronacher created Flask. Both are figures at the center of the open-source ecosystem, with large audiences and established reputations. For them, declining costs of AI reimplementation mean something specific: It becomes easier to reimplement things in a different form that better suits them. Ronacher says explicitly that he had begun reimplementing GNU Readline precisely because of its copyleft conditions.

For the people who contributed to a library like chardet over the years, the same cost shift means something entirely different: The copyleft protection around their contributions can be removed.

When positional asymmetry of this kind is ignored and the argument is presented as universal analysis, one does not get analysis but rationalization. Both authors arrive at conclusions that align precisely with their own interests. Hong Minhee asks readers to keep this fact in mind.

## 2.6 What the Debate Means for the Future of Copyleft

### 2.6.1 Bruce Perens and the End of the Old Economy

Bruce Perens, who wrote the original Open Source Definition, told The Register: "The entire economy of software development is dead, over, finished, broken!" He meant it as an alarm. Antirez draws from a similar assessment of the situation the conclusion: Adapt. Ronacher says he finds the direction exciting.

Hong Minhee observes that none of the three reactions answers the central question: If copyleft becomes technically easier to circumvent, does that make it less necessary -- or more necessary?

His answer: more necessary. What the GPL protected was not the scarcity of code but the freedom of users. The fact that the production of code has become cheaper does not make it acceptable to use that code as a vehicle for the erosion of freedom. When the friction of reimplementation disappears, so does the friction of stripping copyleft from everything that remains exposed.

### 2.6.2 From Training Copyleft to Specification Copyleft

Hong Minhee had proposed a Training Copyleft (TGPL) as the next step in this evolutionary line in earlier writings. The chardet situation suggests that the argument must go even further: to a specification copyleft that covers the layer beneath the source code.

If source code can now be generated from a specification, then the specification is the locus where the essential intellectual substance of a GPL project resides. Blanchard's own claim -- that he worked only from the test suite and the API without reading the source code -- is, paradoxically, an argument for protecting that test suite and API specification under copyleft terms.

The history of the GPL is the history of licensing tools that evolve in response to new forms of exploitation: GPLv2 to GPLv3, then AGPL. What drove each evolution was not a court ruling but a community that first made a value judgment and then sought legal instruments to express it. The same sequence is now available.

## 2.7 Claw Code in the Mirror of the Debate

### 2.7.1 The Parallel

Now we turn our gaze to the project that this book documents. Claw Code arose after the Claude Code source code was exposed on March 31, 2026. The project description in the README is explicit: The creator, Sigrid Jin, sat down, ported the core functions from scratch to Python, and pushed everything before the sun rose. The work was orchestrated with oh-my-codex (OmX), a workflow layer based on OpenAI's Codex. The result is described as a "clean Python rewrite that captures the architectural patterns of Claude Code's agent harness without copying proprietary source code."

The structural parallel to the chardet case is obvious: An existing software system is reimplemented with AI assistance. The background story of the project expressly mentions the concern about legal action from Anthropic. The solution was to create an independent implementation that relies on architectural patterns, not on copied code.

### 2.7.2 The Differences

However, there are significant differences from the chardet case, and they deserve an honest analysis:

*The initial situation*: chardet was an open-source library under a copyleft license. Claude Code was proprietary software whose source code was unintentionally exposed. The ethical vector here is different: The reimplementation of a proprietary system as an open-source project runs -- in Hong Minhee's terminology -- from proprietary to free. That is structurally closer to the GNU analogy than to the chardet case.

*The licensing question*: With chardet, the issue was the switch from copyleft to permissive within the open-source ecosystem. With Claw Code, the question is whether the reimplementation of proprietary architectural patterns is permissible at all. That is a different legal and ethical question.

*The motivation*: Blanchard reimplemented an existing open-source library that he himself maintained and changed its license. Claw Code arose as a reaction to an unintentional exposure, with the declared goal of understanding and rebuilding the architectural patterns, not of copying the proprietary code.

### 2.7.3 The Remaining Questions

Despite the differences, the existence of Claw Code raises questions that Hong Minhee's analysis directly addresses:

*Where does the boundary run between architectural pattern and protected expression?* The Claw Code project repeatedly emphasizes that it replicates architectural patterns, not copies code. But architectural patterns -- the organization into subsystems, the bootstrap phases, the tool wiring, the trust-gating model -- are the result of considerable intellectual work. Hong Minhee's argument for a specification copyleft suggests that precisely this level -- the architecture, the API, the test suite -- is the locus where the essential intellectual substance resides.

*Is the use of AI systems for reimplementation a relevant fact?* Blanchard's defense rested on the claim that he had not directly examined the code but had only passed the API and the test suite to Claude. The Claw Code background story describes a similar process: Reading the original harness structure, then creating a Python directory tree with tests, steered through AI orchestration. The question of whether an AI system can function as a filter between the original and the reimplementation that reduces the developer's legal responsibility is the same question being asked in the chardet case.

*Who owns the architecture?* The Claw Code README contains an explicit disclaimer: "This repository makes no claim of ownership over the original Claude Code source material." But it also states that it is a Python replica of the architectural patterns that mirrors a command and tool catalog of approximately 150 commands and 100 tools. The question of how much architecture one can replicate before the replica itself becomes a derivative work is exactly the question that Hong Minhee identifies as central.

### 2.7.4 The Relationship to the Commons

There is one aspect in which Claw Code distinguishes itself positively from chardet 7.0: It adds to the commons. Where Blanchard replaced a copyleft license with a permissive one, thereby reducing the protection of the commons, Claw Code creates a new open-source project that did not exist before. The proprietary Claude Code was not delicensed; it was reimplemented and published as open source.

However, this assessment is also not uncomplicated. The reimplementation relies on knowledge derived from the unintentional exposure of proprietary code. The README formulates this openly: "I originally studied the exposed codebase to understand the harness, the tool wiring, and the agent workflow." The fact that the tracked source tree now contains only the Python port does not change the fact that the knowledge on which the port is based stems from insight into proprietary code.

## 2.8 The Deeper Layer: Values That Need No Ruling

### 2.8.1 Community Norms Beyond the Law

Hong Minhee closes his essay with an observation that reaches beyond the specific case: Law is made slowly, after the fact, and reflects existing power relations. The norms that open-source communities built over decades did not wait for judicial approval. People chose the GPL when the law gave them no guarantee of its enforcement, because it expressed the values of the communities they wanted to belong to.

This observation is significant for anyone working in the field of AI-assisted software development. Courts will eventually rule on the permissibility of AI reimplementations. But the question that must be answered first is not a legal one but a social one: Do those who take from the commons owe something back?

Hong Minhee's answer is clear: Yes. This judgment needs no court ruling.

### 2.8.2 What Antirez and Ronacher Make Visible

The last sentence of Hong Minhee's essay deserves to be quoted in full: "What makes the pieces by Antirez and Ronacher worth reading is not that they are right. It is that they make visible with unusual clarity what they choose not to see. When legality is used as a substitute for a value judgment, the question that actually matters is buried in the footnotes of a law they have already outgrown."

This critique is not directed at the intellectual honesty of the two authors -- Hong Minhee expressly respects both. It is directed at an argumentative structure that is widespread in the technology industry: the use of legal permissibility as an escape route from ethical responsibility.

## 2.9 Conclusions for Practice

### 2.9.1 Five Guiding Questions for AI Reimplementation Projects

From Hong Minhee's analysis, five questions can be derived that every AI reimplementation project -- including Claw Code -- should ask itself:

1. **The direction question**: In which direction does the vector run? From proprietary to free (expansion of the commons) or from copyleft to permissive (erosion of the commons)?

2. **The compact question**: Is a social compact being broken to which original contributors had agreed? Did people contribute under certain license expectations that are now being undermined?

3. **The positionality question**: From what position am I arguing? Do I myself benefit from the cost reduction of reimplementation while others bear the damage?

4. **The specification question**: If I claim to have reimplemented only the specification and not the code -- is the specification itself not the locus where the essential intellectual substance resides?

5. **The future question**: If my approach becomes the norm, what world emerges? One in which copyleft-protected projects are systematically converted into permissively licensed ones?

### 2.9.2 What Claw Code Does Right -- and Where Questions Remain Open

Claw Code does several things right in terms of this analysis: It operates in the direction from proprietary to free. It is transparent about its origins. It keeps the original proprietary code out of the tracked repository. It offers a disclaimer.

But the open questions remain: The boundary between architectural pattern and protected expression is unresolved. The role of AI as an intermediary layer between proprietary original and reimplementation raises the same questions as in the chardet case. And the fact that the project is based on insight into unintentionally exposed proprietary code adds an additional ethical dimension that goes beyond Hong Minhee's analysis.

## 2.10 Outlook

The debate that Hong Minhee initiated will not be resolved by a single court ruling or a single blog post. It is part of a broader reassessment of the relationship between AI systems, intellectual property, and the social norms of software development.

For the Claw Code project, this means that the technical work -- the porting, the Rust reimplementation, the parity checks -- cannot be considered in isolation from these questions. Every technical decision is also an ethical decision. The choice of license, the handling of the exposed source material, the transparency about the origin of the knowledge -- all of these are answers to the question that Hong Minhee poses.

The next chapters of this book will examine the technical architecture of Claw Code in detail. But the questions raised in this chapter accompany every line of code. For as Hong Minhee writes: Whatever courts ultimately decide about AI reimplementation, the question we must answer first is not a legal one. It is a social one. Do those who take from the commons owe something back? I think yes. This judgment needs no court ruling.

---

*Sources for this chapter: Hong Minhee, "Is Legal the Same as Legitimate: AI Reimplementation and the Erosion of Copyleft", March 9, 2026; Claw Code Repository (github.com/instructkr/claw-code), README.md and ANLEITUNG.md; the contributions referenced therein by Salvatore Sanfilippo (antirez) and Armin Ronacher as well as the statements by Zoe Kooyman (FSF) and Bruce Perens.*


# Chapter 3: High-Level Architecture

## 3.1 Introduction and Guiding Principle

The architecture of Claw Code follows a clear design principle: **Immutability on the outside, state management on the inside**. The entire system is built as a three-layer model in which each layer carries a clearly delineated responsibility. The lowest layer provides infrastructure -- environment detection, filesystem context, and persistence. The middle layer orchestrates the actual flow: It routes user inputs to the appropriate commands and tools, manages sessions, and controls the token budget. The topmost layer -- the so-called mirror layer -- loads the archived reference data from JSON snapshots and provides them as immutable Python tuples.

This chapter describes each layer in detail, presents the dependencies between modules, and traces the data flow from CLI input to formatted output. Three ASCII diagrams visually illustrate the relationships.

## 3.2 Overall Architecture at a Glance

Before we examine the individual layers in detail, the following diagram provides an overall view of all three layers, the cross-cutting modules, and their relationships to one another:

**CLI Entry Point: main.py** (argparse) -- `build_parser()` --> `main(argv)` --> Dispatch based on `args.command`

### Layer 1 -- Mirror Layer (Spiegelungsschicht)

| Module | Key Elements |
|--------|-------------|
| **commands.py** | `SNAPSHOT_PATH` --> `commands_snapshot.json`; `load_command_snapshot()` (`@lru_cache(maxsize=1)`); `PORTED_COMMANDS`: tuple (207 PortingModule); `get_command(name)`, `get_commands(filter...)`, `find_commands(query)`, `execute_command(name, p)`, `render_command_index()` |
| **tools.py** | `SNAPSHOT_PATH` --> `tools_snapshot.json`; `load_tool_snapshot()` (`@lru_cache(maxsize=1)`); `PORTED_TOOLS`: tuple (184 PortingModule); `get_tool(name)`, `get_tools(filter...)`, `find_tools(query)`, `execute_tool(name, payload)`, `render_tool_index()` |

### Layer 2 -- Orchestration Layer (Orchestrierungsschicht)

| Module | Key Elements |
|--------|-------------|
| **runtime.py** | `PortRuntime` -- `.route_prompt(prompt, limit)`, `.bootstrap_session(prompt)`, `.run_turn_loop(prompt, ...)`, `._collect_matches(tokens, ...)`, `._score(tokens, module)`, `._infer_permission_denials()`; `RuntimeSession` (dataclass), `RoutedMatch` (dataclass) |
| **query_engine.py** | `QueryEnginePort` -- `.submit_message(...)`, `.stream_submit_message()`, `.compact_messages_...()`, `.persist_session()`, `.render_summary()`; `QueryEngineConfig` -- `max_turns=8`, `max_budget_tokens=2000`, `compact_after_turns=12`, `structured_output=False`; `TurnResult` (dataclass) -- prompt, output, matched_commands/tools, permission_denials, usage, stop_reason |
| **execution_registry.py** | `ExecutionRegistry`, `MirroredCommand`, `MirroredTool`, `build_execution_registry()` |

### Layer 3 -- Infrastructure Layer (Infrastrukturschicht)

| Module | Key Elements |
|--------|-------------|
| **setup.py** | `WorkspaceSetup` -- python_version, implementation, platform_name, test_command, `startup_steps()`; `SetupReport` -- prefetches, deferred_init; `run_setup(cwd, trusted)` |
| **context.py** | `PortContext` -- source_root, tests_root, assets_root, archive_root, python_file_count, archive_available; `build_port_context()`, `render_context()` |
| **session_store.py** | `StoredSession` -- session_id, messages, input_tokens, output_tokens; `save_session()`, `load_session()`; storage in `.port_sessions/` |
| **transcript.py** | `TranscriptStore` -- `.append(entry)`, `.compact(keep_last)`, `.replay()`, `.flush()` |
| **history.py** | `HistoryLog`, `HistoryEvent` -- `.add(title, det.)`, `.as_markdown()` |

### Cross-Cutting Modules (imported by all layers)

| Module | Key Elements |
|--------|-------------|
| **models.py** | `PortingModule`, `PortingBacklog`, `PermissionDenial`, `UsageSummary`, `Subsystem` |
| **permissions.py** | `ToolPermissionContext` -- `.blocks(name)`, `.from_iterables()` |
| **parity_audit.py** | `ParityAuditResult`, `run_parity_audit()` -- progress measurement against TS archive |

## 3.3 Layer 1 -- The Mirror Layer

### 3.3.1 Concept and Motivation

The mirror layer forms the foundation of the entire system. Its name derives from the central design decision: Instead of reimplementing the 207 commands and 184 tools of the original TypeScript project from scratch, they are archived as **JSON snapshots** and loaded at runtime as immutable reference data. These snapshots are located in the directory `src/reference_data/` and contain structured metadata -- name, responsibility, and source hint -- for every single command and tool.

The term "mirroring" aptly describes this process: The Python layer mirrors the surface of the TypeScript original without replicating its internal logic. The result is a **read-only catalog** that can be searched, filtered, and routed by the orchestration layer.

### 3.3.2 commands.py -- The Command Catalog

The module `commands.py` is responsible for loading and providing the mirrored command entries. The core is remarkably simple:

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent / 'reference_data' / 'commands_snapshot.json'

@lru_cache(maxsize=1)
def load_command_snapshot() -> tuple[PortingModule, ...]:
    raw_entries = json.loads(SNAPSHOT_PATH.read_text())
    return tuple(
        PortingModule(
            name=entry['name'],
            responsibility=entry['responsibility'],
            source_hint=entry['source_hint'],
            status='mirrored',
        )
        for entry in raw_entries
    )

PORTED_COMMANDS = load_command_snapshot()
```

Three design decisions are noteworthy here:

1. **`@lru_cache(maxsize=1)`**: The snapshot is loaded exactly once on first access and then held in memory. Repeated calls do not read from the filesystem again. This is a classic singleton pattern via Python's decorator mechanism.

2. **`tuple` instead of `list`**: The result is returned as an immutable tuple. No downstream code can accidentally mutate the reference data -- a central safety principle in an architecture that relies on immutable references.

3. **Module-level constant `PORTED_COMMANDS`**: By assigning at the module level, the snapshot is loaded upon import of the module. Every import of `commands.py` accesses the same cached tuple.

On top of the immutable core, `commands.py` offers a set of access functions:

- `get_command(name)` -- Find a single command by name (case-insensitive)
- `get_commands(cwd, include_plugin_commands, include_skill_commands)` -- Retrieve a filtered command list
- `find_commands(query, limit)` -- Text search across name and `source_hint`
- `execute_command(name, prompt)` -- Execute a mirrored command (produces a `CommandExecution` instance)
- `render_command_index(limit, query)` -- Formatted Markdown output of the command list

The `execute_command` function deserves special attention: Since the commands are only mirrored and not fully ported, it produces a **shim execution** -- a message describing what the original command would do without actually executing the logic. The `CommandExecution` dataclass object contains a `handled` flag indicating whether the command was found in the catalog.

### 3.3.3 tools.py -- The Tool Catalog

`tools.py` follows exactly the same pattern as `commands.py`, but for tools. The parallel is deliberate and greatly facilitates understanding the codebase:

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent / 'reference_data' / 'tools_snapshot.json'
PORTED_TOOLS = load_tool_snapshot()   # 184 Eintraege, tuple[PortingModule, ...]
```

An additional layer of functionality is the integration with the permission system. The function `get_tools` accepts an optional `ToolPermissionContext` that can block certain tools by their name or a name prefix:

```python
def get_tools(
    simple_mode: bool = False,
    include_mcp: bool = True,
    permission_context: ToolPermissionContext | None = None,
) -> tuple[PortingModule, ...]:
```

The `simple_mode` parameter reduces the visible tool surface to three core tools: `BashTool`, `FileReadTool`, and `FileEditTool`. The `include_mcp` parameter filters out MCP-based tools (Model Context Protocol). Both parameters demonstrate how the mirror layer provides **projection logic** -- it shapes the view of the immutable catalog without modifying the catalog itself.

### 3.3.4 Symmetry Between Commands and Tools

The deliberate symmetry between `commands.py` and `tools.py` is an architectural feature that runs through the entire project. Both modules:

- load their data from JSON snapshots under `src/reference_data/`
- use `@lru_cache(maxsize=1)` for one-time loading
- expose a module-level tuple (`PORTED_COMMANDS` and `PORTED_TOOLS` respectively)
- offer identical access operations: `get_*`, `find_*`, `execute_*`, `render_*_index`
- produce their respective execution dataclass (`CommandExecution` and `ToolExecution`)
- create backlog objects via `build_command_backlog()` and `build_tool_backlog()`

This symmetry is not coincidental but a deliberate application of the **Uniform Access Principle**: The orchestration layer can treat commands and tools uniformly because both use the same interface (`PortingModule`) and the same provisioning pattern.

## 3.4 Layer 2 -- The Orchestration Layer

### 3.4.1 runtime.py -- Prompt Routing and Session Bootstrapping

`runtime.py` is the heart of the orchestration layer. It contains two main classes: `PortRuntime` and `RuntimeSession`.

**PortRuntime** is the central control class and offers three public methods:

1. **`route_prompt(prompt, limit)`** -- Token-based routing of a user input
2. **`bootstrap_session(prompt, limit)`** -- Full session bootstrapping
3. **`run_turn_loop(prompt, limit, max_turns, structured_output)`** -- Stateful turn loop

#### The Routing Procedure

The prompt routing in `route_prompt` follows a simple but effective token scoring algorithm:

```python
def route_prompt(self, prompt: str, limit: int = 5) -> list[RoutedMatch]:
    tokens = {token.lower() for token in prompt.replace('/', ' ').replace('-', ' ').split() if token}
    by_kind = {
        'command': self._collect_matches(tokens, PORTED_COMMANDS, 'command'),
        'tool': self._collect_matches(tokens, PORTED_TOOLS, 'tool'),
    }
```

The algorithm works in four steps:

1. **Tokenization**: The prompt is split into lowercase tokens. Slashes and hyphens are treated as separators, so that e.g. `/file-edit` becomes the tokens `{'file', 'edit'}`.

2. **Scoring**: For each module in the command and tool catalog, a score is computed. The `_score` method counts how many tokens appear in the module's name, `source_hint`, or responsibility description:

```python
@staticmethod
def _score(tokens: set[str], module: PortingModule) -> int:
    haystacks = [module.name.lower(), module.source_hint.lower(), module.responsibility.lower()]
    score = 0
    for token in tokens:
        if any(token in haystack for haystack in haystacks):
            score += 1
    return score
```

3. **Preselection**: From each category (commands and tools), the best match is guaranteed to be included in the result list. This ensures that both a command and a tool are represented, provided matches exist.

4. **Backfilling**: The remaining slots up to the `limit` are filled with the next-best matches from both categories, sorted by descending score.

The result is a list of `RoutedMatch` objects, each containing `kind` (command/tool), `name`, `source_hint`, and `score`.

#### Session Bootstrapping

The method `bootstrap_session` performs the complete initialization process of a session. It orchestrates components from all three layers:

1. **Initialize infrastructure**: `build_port_context()` collects filesystem information, `run_setup(trusted=True)` detects the runtime environment
2. **Create history log**: A `HistoryLog` is created and documents every step
3. **Create query engine**: `QueryEnginePort.from_workspace()` builds a fresh engine with manifest
4. **Execute routing**: `route_prompt(prompt, limit)` finds the best matches
5. **Build execution registry**: `build_execution_registry()` creates shim wrappers for all mirrored commands and tools
6. **Execute commands and tools**: The routed matches are executed via the registry
7. **Check permission denials**: `_infer_permission_denials` marks potentially dangerous tools (e.g., `bash`-containing tools)
8. **Generate stream events**: `stream_submit_message` produces an event stream (message_start, command_match, tool_match, permission_denial, message_delta, message_stop)
9. **Execute turn**: `submit_message` processes the prompt in the query engine
10. **Persist session**: `persist_session()` saves the state to disk

The result is a `RuntimeSession` object -- a comprehensive dataclass with 12 fields that contains the entire state of the bootstrapped session. The `as_markdown()` method of `RuntimeSession` can output this state as a structured Markdown report.

#### The Turn Loop

`run_turn_loop` implements a stateful iteration loop:

```python
def run_turn_loop(self, prompt, limit=5, max_turns=3, structured_output=False):
    engine = QueryEnginePort.from_workspace()
    engine.config = QueryEngineConfig(max_turns=max_turns, structured_output=structured_output)
    matches = self.route_prompt(prompt, limit=limit)
    results: list[TurnResult] = []
    for turn in range(max_turns):
        turn_prompt = prompt if turn == 0 else f'{prompt} [turn {turn + 1}]'
        result = engine.submit_message(turn_prompt, command_names, tool_names, ())
        results.append(result)
        if result.stop_reason != 'completed':
            break
    return results
```

The loop runs for a maximum of `max_turns` iterations. In each turn, the prompt (annotated with the turn number from the second turn onward) is passed to the query engine. If the `stop_reason` is not `'completed'` -- for example because the token budget was reached (`'max_budget_reached'`) or the maximum number of messages was exceeded (`'max_turns_reached'`) -- the loop breaks early.

### 3.4.2 query_engine.py -- Session State and Token Budgeting

The `QueryEnginePort` class is the stateful component of the orchestration layer. While `PortRuntime` itself is stateless and functions as a coordinator, `QueryEnginePort` manages the mutable session state:

- **`session_id`**: Unique UUID for each session
- **`mutable_messages`**: List of messages so far (the mutable message buffer)
- **`permission_denials`**: Collected permission denials
- **`total_usage`**: Cumulative token consumption object (`UsageSummary`)
- **`transcript_store`**: Transcript store for replay and compaction

#### Configuration

The `QueryEngineConfig` dataclass defines four central control parameters:

| Parameter | Default Value | Description |
|---|---|---|
| `max_turns` | 8 | Maximum number of messages per session |
| `max_budget_tokens` | 2000 | Token upper limit (sum of input and output) |
| `compact_after_turns` | 12 | Compaction occurs after this message count |
| `structured_output` | False | JSON output instead of plain text |

#### Message Processing

The central method `submit_message` processes a prompt in several steps:

1. **Check turn limit**: If `mutable_messages` has already reached `max_turns`, a `TurnResult` with `stop_reason='max_turns_reached'` is immediately returned.
2. **Create summary**: Prompt, matched commands/tools, and permission denials are formatted into a summary line.
3. **Format output**: Depending on the `structured_output` flag, either plain text or JSON is produced.
4. **Check token budget**: Via `total_usage.add_turn(prompt, output)`, the projected consumption is calculated. If it exceeds `max_budget_tokens`, `stop_reason='max_budget_reached'` is set.
5. **Update state**: The message is added to the `mutable_messages` buffer and the `transcript_store`.
6. **Check compaction**: `compact_messages_if_needed()` trims the buffer and the transcript if they have grown too long.

The token budgeting is deliberately implemented in simplified form: `UsageSummary.add_turn` counts words (via `split()`) as an approximation for token counts:

```python
def add_turn(self, prompt: str, output: str) -> 'UsageSummary':
    return UsageSummary(
        input_tokens=self.input_tokens + len(prompt.split()),
        output_tokens=self.output_tokens + len(output.split()),
    )
```

This word-based approximation is sufficient for the current porting status and can later be replaced by a real tokenizer.

#### Streaming Interface

The method `stream_submit_message` yields a generator that produces Server-Sent-Events-like dictionaries:

```
message_start  -->  command_match  -->  tool_match  -->  permission_denial
                                                              |
                                                              v
                                              message_delta  -->  message_stop
```

Each event is a dictionary with a `type` field and associated data. The `message_stop` event contains the usage summary and the transcript size. This generator architecture enables later integration with real streaming protocols (SSE, WebSockets) without changes to the core logic.

#### Persistence Integration

`QueryEnginePort.persist_session()` first flushes the transcript and then saves the session via `session_store.save_session()`:

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(StoredSession(
        session_id=self.session_id,
        messages=tuple(self.mutable_messages),
        input_tokens=self.total_usage.input_tokens,
        output_tokens=self.total_usage.output_tokens,
    ))
    return str(path)
```

The reverse path -- loading a saved session -- is available via the class method `from_saved_session(session_id)`. It restores the complete state, including the transcript and the token counters.

### 3.4.3 execution_registry.py -- The Execution Layer

The `ExecutionRegistry` module provides a unified interface for executing mirrored commands and tools. It creates `MirroredCommand` and `MirroredTool` wrappers, each offering an `execute` method:

```python
@dataclass(frozen=True)
class MirroredCommand:
    name: str
    source_hint: str

    def execute(self, prompt: str) -> str:
        return execute_command(self.name, prompt).message
```

The function `build_execution_registry()` builds the entire registry upon invocation by wrapping all `PORTED_COMMANDS` and `PORTED_TOOLS` in their respective wrapper types. This decouples the orchestration layer from the details of command execution and enables later extensions, such as replacing shim executions with real implementations.

## 3.5 Layer 3 -- The Infrastructure Layer

### 3.5.1 setup.py -- Environment Detection and Startup

`setup.py` is responsible for detecting the runtime environment and performing the startup steps. It provides two dataclasses:

**`WorkspaceSetup`** holds the static environment information: Python version, implementation (CPython, PyPy, etc.), platform name, and test command. The method `startup_steps()` returns the six defined startup steps as a tuple:

1. Start of top-level prefetch side effects
2. Construction of the workspace context
3. Loading of the mirrored command snapshot
4. Loading of the mirrored tool snapshot
5. Preparation of the parity audit hooks
6. Application of trust-gated deferred initialization

**`SetupReport`** aggregates the setup with the results of the prefetch operations and deferred initialization. The function `run_setup` coordinates three prefetch operations:

- `start_mdm_raw_read()` -- Reads MDM configuration data (Mobile Device Management)
- `start_keychain_prefetch()` -- Preloads keychain data
- `start_project_scan(root)` -- Scans the project directory

The `trusted` parameter controls whether deferred initialization (`deferred_init`) is executed with elevated privileges. This is a central security mechanism: In untrusted mode, certain initialization steps are skipped.

### 3.5.2 context.py -- Workspace Context

`context.py` collects filesystem metadata about the workspace. The `PortContext` dataclass contains:

- Paths to `source_root`, `tests_root`, `assets_root`, and `archive_root`
- Counters for Python files, test files, and asset files
- An `archive_available` flag indicating whether the TypeScript original archive is locally present

`build_port_context()` traverses the filesystem via `Path.rglob('*.py')` and counts files dynamically. This function is called by session bootstrapping and provides the user with an overview of the current state of the porting project.

### 3.5.3 session_store.py -- Persistence

The persistence module is deliberately kept minimal. It defines a `StoredSession` dataclass with four fields:

```python
@dataclass(frozen=True)
class StoredSession:
    session_id: str
    messages: tuple[str, ...]
    input_tokens: int
    output_tokens: int
```

`save_session` serializes a session as a JSON file under `.port_sessions/{session_id}.json`. `load_session` deserializes it back. The directory is automatically created as needed (`mkdir(parents=True, exist_ok=True)`).

### 3.5.4 transcript.py and history.py -- Tracking

**`TranscriptStore`** is a lightweight store for messages with four operations:
- `append(entry)` -- Add a message (sets `flushed=False`)
- `compact(keep_last)` -- Remove old entries, keeping only the last `keep_last`
- `replay()` -- Return all entries as a tuple
- `flush()` -- Set the `flushed` flag

**`HistoryLog`** documents the steps of a session as `HistoryEvent` objects (title + detail). It is primarily used during session bootstrapping to track the progress of initialization.

## 3.6 Cross-Cutting Modules

### 3.6.1 models.py -- Shared Data Classes

`models.py` defines the five central data classes used by all layers:

- **`Subsystem`**: Describes a Python module in the workspace (name, path, file count, notes)
- **`PortingModule`**: The universal unit for mirrored commands and tools (name, responsibility, source hint, status)
- **`PermissionDenial`**: Models an access denial (tool name + reason)
- **`UsageSummary`**: Token consumption counter with the `add_turn` method for incremental updates
- **`PortingBacklog`**: Aggregates a list of `PortingModule` objects under a title with formatted summary lines

All data classes except `PortingBacklog` and `UsageSummary` are declared with `frozen=True`, meaning they are immutable after creation.

### 3.6.2 permissions.py -- Access Control

`ToolPermissionContext` implements a simple deny-list-based permission system:

```python
@dataclass(frozen=True)
class ToolPermissionContext:
    deny_names: frozenset[str] = field(default_factory=frozenset)
    deny_prefixes: tuple[str, ...] = ()

    def blocks(self, tool_name: str) -> bool:
        lowered = tool_name.lower()
        return lowered in self.deny_names or any(lowered.startswith(prefix) for prefix in self.deny_prefixes)
```

The class supports two blocking mechanisms: exact name matching and prefix matching. Both are case-insensitive. The factory method `from_iterables` creates a context from CLI arguments (e.g., `--deny-tool BashTool --deny-prefix mcp_`).

### 3.6.3 parity_audit.py -- Progress Measurement

The parity audit module compares the current Python porting status against the archived TypeScript original. It measures five metrics:

1. **Root File Coverage**: How many of the expected root files already exist in Python?
2. **Directory Coverage**: How many of the expected directories have been created?
3. **Total File Ratio**: Ratio of Python files to archived TypeScript files
4. **Command Entry Ratio**: Mirrored commands vs. expected commands
5. **Tool Entry Ratio**: Mirrored tools vs. expected tools

The function `run_parity_audit()` produces a `ParityAuditResult` that can be output as a formatted report via `to_markdown()`. This module is a pure diagnostic tool and has no influence on runtime operation.

## 3.7 Dependency Graph Between Modules

The following diagram shows the import relationships between all modules. An arrow from A to B means "A imports B":


**Component Hierarchy:**

- **system_init.py** (top level)
  - **setup.py** (coordination)
    - **prefetch.py** — `PrefetchResult`, 3 start functions
    - **deferred_init.py** — `DeferredInitResult`, `run_deferred_init()`
  - **commands.py** — `get_commands()`, `built_in_command_names()`
  - **tools.py** — `get_tools()`
- **bootstrap_graph.py** — standalone, documents the flow
- **context.py** — standalone, builds `PortContext`


Noteworthy is the clear hierarchy: `main.py` imports from all layers, but the layers themselves have ordered dependencies. `runtime.py` imports from the mirror layer and the infrastructure, but never the reverse. `models.py` as a cross-cutting module is imported by almost all other modules but itself imports no other project modules.

## 3.8 Data Flow from CLI Input to Output

The following diagram traces the complete data flow for the exemplary command `turn-loop` -- the most complex path through the architecture:


**Scoring Algorithm Detail:**

For each token from the prompt set:
1. Check if token appears in `module.name` → if yes: score += 1
2. Check if token appears in `module.source_hint` → if yes: already counted
3. Check if token appears in `module.responsibility` → if yes: already counted

> Note: `any()` ensures each token is counted at most once per module.


## 3.9 Interplay of the Layers

The strength of the architecture lies in the controlled interplay of the three layers. Each layer has a clear task and communicates with the others via well-defined interfaces:

### Data Direction: Bottom-Up

Data fundamentally flows from bottom to top:

1. **Infrastructure** provides raw data: file paths, environment information, saved sessions
2. **Mirroring** transforms JSON snapshots into typed Python objects
3. **Orchestration** combines both into session logic, routing, and turn management

### Control Direction: Top-Down

Control, by contrast, flows from top to bottom:

1. **CLI** (`main.py`) determines which mode is activated
2. **Orchestration** decides which commands/tools are routed and how many turns are executed
3. **Infrastructure/Mirroring** performs the concrete operations (loading, saving, searching)

### Immutability as an Architectural Principle

A pervasive principle is the distinction between immutable and mutable data:

**Immutable (frozen=True):**
- `PortingModule`, `PortContext`, `WorkspaceSetup`, `SetupReport`
- `StoredSession`, `PermissionDenial`, `RoutedMatch`, `TurnResult`
- `ToolPermissionContext`, `QueryEngineConfig`
- `PORTED_COMMANDS`, `PORTED_TOOLS` (module-level tuples)

**Mutable:**
- `QueryEnginePort.mutable_messages` (growing message buffer)
- `QueryEnginePort.permission_denials` (collected denials)
- `QueryEnginePort.total_usage` (replaced on every turn)
- `TranscriptStore.entries` (growing transcript)
- `HistoryLog.events` (growing event log)
- `PortingBacklog.modules` (mutable module list)

This pattern -- immutable reference data and configurations, mutable session state -- is typical of event-driven systems and greatly facilitates tracking state changes.

## 3.10 The Entry Point: main.py

`main.py` deserves special consideration as the bracket around the entire architecture. The function `build_parser()` defines 21 subcommands via `argparse`, which can be classified into four categories:

**Report commands** (stateless, read-only):
- `summary`, `manifest`, `parity-audit`, `setup-report`, `command-graph`, `tool-pool`, `bootstrap-graph`, `subsystems`

**Catalog commands** (search the mirror layer):
- `commands`, `tools`, `show-command`, `show-tool`

**Execution commands** (traverse the orchestration layer):
- `route`, `bootstrap`, `turn-loop`, `exec-command`, `exec-tool`

**Persistence commands** (use the infrastructure layer):
- `flush-transcript`, `load-session`

**Remote commands** (extended runtime mode):
- `remote-mode`, `ssh-mode`, `teleport-mode`, `direct-connect-mode`, `deep-link-mode`

The `main()` function uses a simple if-elif cascade for dispatching. Each branch follows the same pattern: create object, call method, output result to stdout, return exit code 0. This pattern keeps the entry point logic flat and easily testable -- every CLI command can be invoked in isolation.

## 3.11 Design Patterns and Conventions

Across the three layers, several recurring design patterns can be identified:

### Factory Methods

`QueryEnginePort.from_workspace()` and `QueryEnginePort.from_saved_session(session_id)` are class methods that serve as named constructors. They encapsulate the creation logic and make the calling code more expressive than a direct `__init__` call.

### Builder Pattern

`build_port_manifest()`, `build_port_context()`, `build_execution_registry()`, `build_system_init_message()` -- all follow the convention `build_*()`. These functions aggregate data from various sources and return a finished, immutable object.

### Markdown-as-Output

Nearly every data class offers a `to_markdown()` or `as_markdown()` method. This is a deliberate design decision: The CLI outputs Markdown-formatted reports that are both readable in the terminal and can be inserted into documentation or issue trackers.

### Defensive Configuration

The `QueryEngineConfig` dataclass with its default values (`max_turns=8`, `max_budget_tokens=2000`) demonstrates the principle of defensive configuration: Without explicit configuration, the system behaves safely and predictably. The user can override these values but does not have to.

## 3.12 Summary

The three-layer architecture of Claw Code separates responsibilities clearly and consistently:

- The **mirror layer** (`commands.py`, `tools.py`) loads 207 commands and 184 tools as immutable reference data from JSON snapshots. Its `@lru_cache`-backed loading functions and the symmetric API for commands and tools form the foundation.

- The **orchestration layer** (`runtime.py`, `query_engine.py`, `execution_registry.py`) implements token-scoring-based prompt routing, session bootstrapping with environment detection, stateful turn loops with token budgeting, and a streaming interface for event-based output.

- The **infrastructure layer** (`setup.py`, `context.py`, `session_store.py`, `transcript.py`, `history.py`) provides environment detection with prefetch operations, filesystem context capture, JSON-based session persistence, and transcript as well as history tracking.

The **cross-cutting modules** (`models.py`, `permissions.py`, `parity_audit.py`) supply the shared data structures, a deny-list-based permission system, and a progress measurement against the TypeScript original.

The result is an architecture that, despite its complexity, remains surprisingly navigable: Every module has a clearly delineated responsibility, the data flow direction is predictable, and the consistent use of immutable data classes minimizes the sources of error in state management.

CHAPTER_4_PLACEHOLDER

# Chapter 4: The CLI Entry Point

## Einleitung

Das Herzstück jeder kommandozeilengesteuerten Anwendung ist ihr Einstiegspunkt — der Ort, an dem Benutzereingaben entgegengenommen, interpretiert und an die jeweils zuständige Verarbeitungslogik weitergeleitet werden. Im Claw-Code-Projekt erfüllt die Datei `src/main.py` genau diese Funktion. Mit 214 Zeilen ist sie bewusst schlank gehalten und folgt einem klaren architektonischen Prinzip: Die CLI-Schicht kennt alle verfügbaren Befehle und deren Argumente, delegiert die eigentliche Arbeit aber vollständig an spezialisierte Module. Diese Trennung von Befehlsparsing und Geschäftslogik ist ein Kennzeichen gut strukturierter Python-Projekte und erleichtert sowohl das Testen als auch die Erweiterbarkeit.

Die Datei gliedert sich in drei klar abgegrenzte Bereiche: einen Importblock (Zeilen 1–18), die Funktion `build_parser()` (Zeilen 21–91) und die Funktion `main()` (Zeilen 94–213). Im Folgenden werden alle drei Bereiche im Detail analysiert.

---

## 4.1 Der Importblock

```python
from __future__ import annotations

import argparse

from .bootstrap_graph import build_bootstrap_graph
from .command_graph import build_command_graph
from .commands import execute_command, get_command, get_commands, render_command_index
from .direct_modes import run_deep_link, run_direct_connect
from .parity_audit import run_parity_audit
from .permissions import ToolPermissionContext
from .port_manifest import build_port_manifest
from .query_engine import QueryEnginePort
from .remote_runtime import run_remote_mode, run_ssh_mode, run_teleport_mode
from .runtime import PortRuntime
from .session_store import load_session
from .setup import run_setup
from .tool_pool import assemble_tool_pool
from .tools import execute_tool, get_tool, get_tools, render_tool_index
```

Die erste Zeile `from __future__ import annotations` aktiviert die sogenannte „postponed evaluation of annotations" (PEP 563). Damit werden Typannotationen als Strings behandelt und erst bei Bedarf aufgelöst. Dies erlaubt die Nutzung moderner Typ-Syntax wie `list[str] | None` auch in älteren Python-Versionen und vermeidet zirkuläre Importprobleme.

Der einzige Standardbibliotheks-Import ist `argparse` — das bewährte Modul der Python-Standardbibliothek zum Parsen von Kommandozeilenargumenten.

Alle weiteren Importe sind relative Importe aus dem eigenen Paket (erkennbar am führenden Punkt). Sie lassen sich thematisch gruppieren:

- **Graphen und Analysen:** `build_bootstrap_graph`, `build_command_graph`, `run_parity_audit`, `assemble_tool_pool`
- **Befehls- und Tool-Verwaltung:** `execute_command`, `get_command`, `get_commands`, `render_command_index`, `execute_tool`, `get_tool`, `get_tools`, `render_tool_index`
- **Laufzeitmodi:** `run_deep_link`, `run_direct_connect`, `run_remote_mode`, `run_ssh_mode`, `run_teleport_mode`
- **Infrastruktur:** `ToolPermissionContext`, `build_port_manifest`, `QueryEnginePort`, `PortRuntime`, `load_session`, `run_setup`

Dieses Importmuster macht auf einen Blick sichtbar, welche Module von der CLI-Schicht abhängen — und umgekehrt, welche Module keinerlei Wissen über die CLI besitzen müssen.

---

## 4.2 Die `build_parser()`-Funktion

```python
def build_parser() -> argparse.ArgumentParser:
```

Diese Funktion erzeugt und konfiguriert den gesamten Argument-Parser. Sie gibt ein `argparse.ArgumentParser`-Objekt zurück, das alle 24 Subcommands kennt. Die Funktion ist eine reine Fabrikfunktion ohne Seiteneffekte — sie liest keine Dateien, greift nicht auf das Netzwerk zu und verändert keinen globalen Zustand.

### 4.2.1 Der Wurzel-Parser und die Subparser-Gruppe

```python
parser = argparse.ArgumentParser(
    description='Python porting workspace for the Claude Code rewrite effort'
)
subparsers = parser.add_subparsers(dest='command', required=True)
```

Der Wurzel-Parser wird mit einer Beschreibung versehen, die beim Aufruf von `--help` angezeigt wird. Entscheidend ist der Aufruf von `add_subparsers()`:

- `dest='command'` legt fest, dass der gewählte Subcommand-Name nach dem Parsen im Attribut `args.command` verfügbar ist. Dies ist der Schlüssel für die gesamte Dispatch-Logik in `main()`.
- `required=True` stellt sicher, dass der Benutzer immer einen Subcommand angeben muss. Ohne Subcommand gibt argparse automatisch eine Fehlermeldung aus.

### 4.2.2 Alle 24 Subcommands im Detail

Im Folgenden werden alle Subcommands in der Reihenfolge ihrer Definition im Quelltext beschrieben und nach funktionalen Kategorien gruppiert.

---

### Kategorie 1: Workspace-Inspektion

Diese vier Befehle dienen der Inspektion des aktuellen Workspace-Zustands. Sie benötigen keine oder nur minimale Argumente und liefern strukturierte Berichte.

#### `summary`

```python
subparsers.add_parser('summary',
    help='render a Markdown summary of the Python porting workspace')
```

Der einfachste aller Subcommands: keine zusätzlichen Argumente. Er erzeugt eine Markdown-Zusammenfassung des gesamten Python-Portierungs-Workspace. In `main()` wird er wie folgt behandelt:

```python
if args.command == 'summary':
    print(QueryEnginePort(manifest).render_summary())
    return 0
```

Es wird ein `QueryEnginePort`-Objekt mit dem zuvor gebauten Manifest instanziiert und dessen `render_summary()`-Methode aufgerufen. Das Ergebnis wird direkt auf die Standardausgabe geschrieben.

#### `manifest`

```python
subparsers.add_parser('manifest',
    help='print the current Python workspace manifest')
```

Ebenfalls ohne Argumente. Er gibt das Workspace-Manifest in Markdown-Form aus:

```python
if args.command == 'manifest':
    print(manifest.to_markdown())
    return 0
```

Das `manifest`-Objekt würde bereits zu Beginn von `main()` durch `build_port_manifest()` erzeugt und steht somit sofort zur Verfügung.

#### `subsystems`

```python
list_parser = subparsers.add_parser('subsystems',
    help='list the current Python modules in the workspace')
list_parser.add_argument('--limit', type=int, default=32)
```

Dieser Befehl listet die Python-Module im Workspace auf. Er besitzt ein optionales Argument `--limit` vom Typ `int` mit dem Standardwert 32, das die Anzahl der angezeigten Module begrenzt. Der Handler:

```python
if args.command == 'subsystems':
    for subsystem in manifest.top_level_modules[: args.limit]:
        for subsystem in manifest.top_level_modules[: args.limit]:
        print(f'{subsystem.name}\t{subsystem.file_count}\t{subsystem.notes}')
    return 0
```

Er iteriert über die im Manifest gespeicherten Top-Level-Module (begrenzt durch das Limit) und gibt für jedes Modul Name, Dateianzahl und Notizen als tabulatorgetrennte Zeilen aus. Dieses Format eignet sich gut für die Weiterverarbeitung in Shell-Pipelines.

#### `setup-report`

```python
subparsers.add_parser('setup-report',
    help='render the startup/prefetch setup report')
```

Keine zusätzlichen Argumente. Der Handler:

```python
if args.command == 'setup-report':
    print(run_setup().as_markdown())
    return 0
```

Hier wird `run_setup()` aus dem Modul `.setup` aufgerufen. Das Ergebnis besitzt eine `as_markdown()`-Methode, die den Bericht als Markdown-Text zurückgibt. Dieser Befehl simuliert den Startup-/Prefetch-Bericht, wie er beim Hochfahren der Laufzeitumgebung erzeugt wird.

---

### Kategorie 2: Befehls- und Tool-Katalog

Diese vier Befehle ermöglichen die Navigation durch den Katalog der gespiegelten Befehle und Tools.

#### `commands`

```python
commands_parser = subparsers.add_parser('commands',
    help='list mirrored command entries from the archived snapshot')
commands_parser.add_argument('--limit', type=int, default=20)
commands_parser.add_argument('--query')
commands_parser.add_argument('--no-plugin-commands', action='store_true')
commands_parser.add_argument('--no-skill-commands', action='store_true')
```

Dies ist einer der komplexesten Subcommands in Bezug auf die Argument-Konfiguration. Er verfügt über vier optionale Argumente:

- `--limit` (int, Standard 20): Maximale Anzahl angezeigter Einträge.
- `--query` (String, optional): Ein Suchbegriff zur Filterung der Befehle.
- `--no-plugin-commands` (Boolean-Flag): Wenn gesetzt, werden Plugin-Befehle ausgeschlossen.
- `--no-skill-commands` (Boolean-Flag): Wenn gesetzt, werden Skill-Befehle ausgeschlossen.

Der Handler implementiert eine Verzweigung je nachdem, ob eine Query angegeben würde:

```python
if args.command == 'commands':
    if args.query:
        print(render_command_index(limit=args.limit, query=args.query))
    else:
        commands = get_commands(
            include_plugin_commands=not args.no_plugin_commands,
            include_skill_commands=not args.no_skill_commands
        )
        output_lines = [f'Command entries: {len(commands)}', '']
        output_lines.extend(
            f'- {module.name} — {module.source_hint}'
            for module in commands[: args.limit]
        )
        print('\n'.join(output_lines))
    return 0
```

Wenn eine Query vorhanden ist, wird `render_command_index()` aufgerufen — eine Funktion, die vermutlich eine durchsuchbare Indexdarstellung liefert. Ohne Query wird `get_commands()` aufgerufen, wobei die beiden Boolean-Flags invertiert übergeben werden (beachte die `not`-Negation: `--no-plugin-commands` setzt `include_plugin_commands` auf `False`). Die Ausgabe besteht aus einer Kopfzeile mit der Gesamtanzahl, gefolgt von einer Aufzählung mit Name und Herkunftshinweis.

#### `tools`

```python
tools_parser = subparsers.add_parser('tools',
    help='list mirrored tool entries from the archived snapshot')
tools_parser.add_argument('--limit', type=int, default=20)
tools_parser.add_argument('--query')
tools_parser.add_argument('--simple-mode', action='store_true')
tools_parser.add_argument('--no-mcp', action='store_true')
tools_parser.add_argument('--deny-tool', action='append', default=[])
tools_parser.add_argument('--deny-prefix', action='append', default=[])
```

Der tool-reichste Subcommand mit sechs optionalen Argumenten:

- `--limit` (int, Standard 20): Begrenzung der Ausgabe.
- `--query` (String, optional): Suchbegriff.
- `--simple-mode` (Boolean-Flag): Aktiviert einen vereinfachten Modus.
- `--no-mcp` (Boolean-Flag): Schließt MCP-Tools (Model Context Protocol) aus.
- `--deny-tool` (Liste, wiederholbar): Explizites Verbot einzelner Tools nach Name. Durch `action='append'` können mehrere `--deny-tool`-Angaben kumuliert werden.
- `--deny-prefix` (Liste, wiederholbar): Verbot ganzer Tool-Familien nach Namenspräfix.

Der Handler:

```python
if args.command == 'tools':
    if args.query:
        print(render_tool_index(limit=args.limit, query=args.query))
    else:
        permission_context = ToolPermissionContext.from_iterables(
            args.deny_tool, args.deny_prefix
        )
        tools = get_tools(
            simple_mode=args.simple_mode,
            include_mcp=not args.no_mcp,
            permission_context=permission_context
        )
        output_lines = [f'Tool entries: {len(tools)}', '']
        output_lines.extend(
            f'- {module.name} — {module.source_hint}'
            for module in tools[: args.limit]
        )
        print('\n'.join(output_lines))
    return 0
```

Besonders bemerkenswert ist die Verwendung von `ToolPermissionContext.from_iterables()`. Hier werden die vom Benutzer spezifizierten Ablehnungslisten in ein strukturiertes Berechtigungsobjekt umgewandelt, das anschließend an `get_tools()` übergeben wird. Dies zeigt eine saubere Trennung zwischen CLI-Parsing und Geschäftslogik: Die CLI sammelt die Rohdaten, die Domänenschicht interpretiert sie.

#### `show-command`

```python
show_command = subparsers.add_parser('show-command',
    help='show one mirrored command entry by exact name')
show_command.add_argument('name')
```

Ein positionelles Argument `name` — der exakte Befehlsname. Der Handler:

```python
if args.command == 'show-command':
    module = get_command(args.name)
    if module is None:
        print(f'Command not found: {args.name}')
        return 1
    print('\n'.join([module.name, module.source_hint, module.responsibility]))
    return 0
```

Dieser Befehl zeigt die Details eines einzelnen gespiegelten Befehls an. Wird der Befehl nicht gefunden, gibt der Handler eine Fehlermeldung aus und liefert den Exit-Code 1 zurück — ein wichtiges Signal für Skripte und Automatisierungen, die den Exit-Code auswerten.

#### `show-tool`

```python
show_tool = subparsers.add_parser('show-tool',
    help='show one mirrored tool entry by exact name')
show_tool.add_argument('name')
```

Strukturell identisch mit `show-command`, aber für Tools. Der Handler:

```python
if args.command == 'show-tool':
    module = get_tool(args.name)
    if module is None:
        print(f'Tool not found: {args.name}')
        return 1
    print('\n'.join([module.name, module.source_hint, module.responsibility]))
    return 0
```

Auch hier wird bei Nichtauffinden des Tools der Exit-Code 1 zurückgegeben.

---

### Kategorie 3: Ausführung

Diese beiden Befehle gehen über die reine Inspektion hinaus und führen tatsächlich Befehls- bzw. Tool-Shims aus.

#### `exec-command`

```python
exec_command_parser = subparsers.add_parser('exec-command',
    help='execute a mirrored command shim by exact name')
exec_command_parser.add_argument('name')
exec_command_parser.add_argument('prompt')
```

Zwei positionelle Argumente: `name` (der exakte Befehlsname) und `prompt` (die Eingabe, die an den Befehl übergeben wird). Der Handler:

```python
if args.command == 'exec-command':
    result = execute_command(args.name, args.prompt)
    print(result.message)
    return 0 if result.handled else 1
```

Die Funktion `execute_command()` liefert ein Ergebnisobjekt zurück, das mindestens die Attribute `message` und `handled` besitzt. Der Exit-Code hängt von `handled` ab: War die Ausführung erfolgreich, wird 0 zurückgegeben, andernfalls 1. Dieses Muster ermöglicht es aufrufenden Skripten, den Erfolg oder Misserfolg programmatisch zu erkennen.

#### `exec-tool`

```python
exec_tool_parser = subparsers.add_parser('exec-tool',
    help='execute a mirrored tool shim by exact name')
exec_tool_parser.add_argument('name')
exec_tool_parser.add_argument('payload')
```

Analog zu `exec-command`, aber mit dem Argument `payload` statt `prompt`. Das Wort „Payload" deutet darauf hin, dass Tools eher strukturierte Eingaben erwarten (z. B. JSON), während Befehle mit natürlichsprachlichen Prompts arbeiten. Der Handler:

```python
if args.command == 'exec-tool':
    result = execute_tool(args.name, args.payload)
    print(result.message)
    return 0 if result.handled else 1
```

Identische Struktur wie bei `exec-command`: Ergebnis ausgeben, Exit-Code basierend auf dem `handled`-Flag setzen.

---

### Kategorie 4: Routing und Sessions

Diese drei Befehle bilden den Kern der Laufzeitinteraktion — vom einfachen Routing über die Session-Initialisierung bis hin zur mehrstufigen Gesprächsschleife.

#### `route`

```python
route_parser = subparsers.add_parser('route',
    help='route a prompt across mirrored command/tool inventories')
route_parser.add_argument('prompt')
route_parser.add_argument('--limit', type=int, default=5)
```

Ein positionelles Argument `prompt` und ein optionales `--limit` (Standard 5). Der Handler:

```python
if args.command == 'route':
    matches = PortRuntime().route_prompt(args.prompt, limit=args.limit)
    if not matches:
        print('No mirrored command/tool matches found.')
        return 0
    for match in matches:
        print(f'{match.kind}\t{match.name}\t{match.score}\t{match.source_hint}')
    return 0
```

Es wird eine neue `PortRuntime`-Instanz erzeugt und deren `route_prompt()`-Methode aufgerufen. Die Ergebnisse werden als tabulatorgetrennte Zeilen ausgegeben, jeweils mit Art (command oder tool), Name, Relevanz-Score und Herkunftshinweis. Werden keine Treffer gefunden, wird eine entsprechende Meldung ausgegeben — der Exit-Code bleibt dennoch 0, da das Fehlen von Treffern kein Fehler ist.

#### `bootstrap`

```python
bootstrap_parser = subparsers.add_parser('bootstrap',
    help='build a runtime-style session report from the mirrored inventories')
bootstrap_parser.add_argument('prompt')
bootstrap_parser.add_argument('--limit', type=int, default=5)
```

Gleiche Argument-Struktur wie `route`. Der Handler:

```python
if args.command == 'bootstrap':
    print(PortRuntime().bootstrap_session(args.prompt, limit=args.limit).as_markdown())
    return 0
```

Hier wird `bootstrap_session()` aufgerufen, das eine vollständige Session-Struktur aufbaut und als Markdown-Bericht ausgibt. Dies entspricht dem Initialisierungsschritt einer Laufzeit-Session, bei dem Befehle und Tools für einen bestimmten Prompt zusammengestellt werden.

#### `turn-loop`

```python
loop_parser = subparsers.add_parser('turn-loop',
    help='run a small stateful turn loop for the mirrored runtime')
loop_parser.add_argument('prompt')
loop_parser.add_argument('--limit', type=int, default=5)
loop_parser.add_argument('--max-turns', type=int, default=3)
loop_parser.add_argument('--structured-output', action='store_true')
```

Der funktionsreichste Befehl in dieser Kategorie mit vier Argumenten:

- `prompt` (positionell): Der initiale Prompt.
- `--limit` (int, Standard 5): Begrenzung der Tool-/Befehlsauswahl.
- `--max-turns` (int, Standard 3): Maximale Anzahl von Gesprächsrunden.
- `--structured-output` (Boolean-Flag): Aktiviert strukturierte Ausgabe.

Der Handler:

```python
if args.command == 'turn-loop':
    results = PortRuntime().run_turn_loop(
        args.prompt,
        limit=args.limit,
        max_turns=args.max_turns,
        structured_output=args.structured_output
    )
    for idx, result in enumerate(results, start=1):
        print(f'## Turn {idx}')
        print(result.output)
        print(f'stop_reason={result.stop_reason}')
    return 0
```

Die `run_turn_loop()`-Methode liefert eine Liste von Ergebnissen zurück — eines pro Gesprächsrunde. Jedes Ergebnis wird mit einer Markdown-Überschrift (`## Turn N`), dem Ausgabetext und dem Abbruchgrund formatiert. Dies ermöglicht die Nachverfolgung des gesamten Gesprächsverlaufs.

---

### Kategorie 5: Session-Verwaltung

Diese beiden Befehle befassen sich mit der Persistierung und dem Laden von Sessions.

#### `flush-transcript`

```python
flush_parser = subparsers.add_parser('flush-transcript',
    help='persist and flush a temporary session transcript')
flush_parser.add_argument('prompt')
```

Ein positionelles Argument `prompt`. Der Handler:

```python
if args.command == 'flush-transcript':
    engine = QueryEnginePort.from_workspace()
    engine.submit_message(args.prompt)
    path = engine.persist_session()
    print(path)
    print(f'flushed={engine.transcript_store.flushed}')
    return 0
```

Hier wird eine `QueryEnginePort`-Instanz über die Klassenmethode `from_workspace()` erzeugt (im Gegensatz zu `summary`, wo das Manifest explizit übergeben wird). Anschließend wird eine Nachricht eingereicht, die Session persistiert, und der Dateipfad sowie der Flush-Status ausgegeben. Die zweite Ausgabezeile dient der Verifikation: `flushed=True` bestätigt, dass das Transkript erfolgreich geschrieben würde.

#### `load-session`

```python
load_session_parser = subparsers.add_parser('load-session',
    help='load a previously persisted session')
load_session_parser.add_argument('session_id')
```

Ein positionelles Argument `session_id`. Der Handler:

```python
if args.command == 'load-session':
    session = load_session(args.session_id)
    print(f'{session.session_id}\n{len(session.messages)} messages\n'
          f'in={session.input_tokens} out={session.output_tokens}')
    return 0
```

Die Funktion `load_session()` aus dem Modul `.session_store` lädt eine zuvor persistierte Session anhand ihrer ID. Die Ausgabe enthält die Session-ID, die Anzahl der Nachrichten und die Token-Statistiken (Eingabe- und Ausgabe-Tokens). Diese kompakte Zusammenfassung eignet sich hervorragend zur schnellen Diagnose.

---

### Kategorie 6: Laufzeitmodi

Fünf Befehle simulieren verschiedene Laufzeit-Verzweigungen. Sie teilen alle dieselbe Argument-Struktur: ein einziges positionelles Argument `target`.

#### `remote-mode`

```python
remote_parser = subparsers.add_parser('remote-mode',
    help='simulate remote-control runtime branching')
remote_parser.add_argument('target')
```

Handler:

```python
if args.command == 'remote-mode':
    print(run_remote_mode(args.target).as_text())
    return 0
```

Simuliert eine Fernsteuerungs-Laufzeitverzweigung. Die Funktion `run_remote_mode()` stammt aus `.remote_runtime`.

#### `ssh-mode`

```python
ssh_parser = subparsers.add_parser('ssh-mode',
    help='simulate SSH runtime branching')
ssh_parser.add_argument('target')
```

Handler:

```python
if args.command == 'ssh-mode':
    print(run_ssh_mode(args.target).as_text())
    return 0
```

Simuliert eine SSH-Laufzeitverzweigung. Auch diese Funktion stammt aus `.remote_runtime`.

#### `teleport-mode`

```python
teleport_parser = subparsers.add_parser('teleport-mode',
    help='simulate teleport runtime branching')
teleport_parser.add_argument('target')
```

Handler:

```python
if args.command == 'teleport-mode':
    print(run_teleport_mode(args.target).as_text())
    return 0
```

Die dritte Variante aus `.remote_runtime`. „Teleport" bezeichnet hier einen spezifischen Verbindungsmodus, bei dem der Kontext direkt an ein entferntes Ziel übertragen wird.

#### `direct-connect-mode`

```python
direct_parser = subparsers.add_parser('direct-connect-mode',
    help='simulate direct-connect runtime branching')
direct_parser.add_argument('target')
```

Handler:

```python
if args.command == 'direct-connect-mode':
    print(run_direct_connect(args.target).as_text())
    return 0
```

Diese und die folgende Funktion stammen aus `.direct_modes` — einem separaten Modul, das sich von `.remote_runtime` unterscheidet. Dies deutet auf eine architektonische Unterscheidung zwischen „entfernten" und „direkten" Verbindungsmodi hin.

#### `deep-link-mode`

```python
deep_link_parser = subparsers.add_parser('deep-link-mode',
    help='simulate deep-link runtime branching')
deep_link_parser.add_argument('target')
```

Handler:

```python
if args.command == 'deep-link-mode':
    print(run_deep_link(args.target).as_text())
    return 0
```

Der fünfte und letzte Laufzeitmodus. Alle fünf Modi folgen demselben Muster: Target entgegennehmen, Handler aufrufen, Ergebnis über `as_text()` formatieren und ausgeben. Diese Konsistenz vereinfacht das Verständnis und die Wartung erheblich.

---

### Kategorie 7: Architekturanalyse

Vier Befehle liefern tiefgreifende Analysen der Projektarchitektur. Keiner benötigt Argumente.

#### `command-graph`

```python
subparsers.add_parser('command-graph',
    help='show command graph segmentation')
```

Handler:

```python
if args.command == 'command-graph':
    print(build_command_graph().as_markdown())
    return 0
```

Erzeugt eine graphbasierte Darstellung der Befehlssegmentierung. Die Funktion `build_command_graph()` aus `.command_graph` liefert ein Objekt mit einer `as_markdown()`-Methode. Dieser Befehl ist besonders nützlich, um die Abhängigkeiten und Gruppierungen innerhalb des Befehlskatalogs zu verstehen.

#### `tool-pool`

```python
subparsers.add_parser('tool-pool',
    help='show assembled tool pool with default settings')
```

Handler:

```python
if args.command == 'tool-pool':
    print(assemble_tool_pool().as_markdown())
    return 0
```

Zeigt den zusammengestellten Tool-Pool mit Standardeinstellungen an. Die Funktion `assemble_tool_pool()` aus `.tool_pool` aggregiert alle verfügbaren Tools und stellt sie in einer strukturierten Übersicht dar.

#### `bootstrap-graph`

```python
subparsers.add_parser('bootstrap-graph',
    help='show the mirrored bootstrap/runtime graph stages')
```

Handler:

```python
if args.command == 'bootstrap-graph':
    print(build_bootstrap_graph().as_markdown())
    return 0
```

Visualisiert die Stufen des Bootstrap-Prozesses — also die Schritte, die beim Hochfahren der Laufzeitumgebung durchlaufen werden.

#### `parity-audit`

```python
subparsers.add_parser('parity-audit',
    help='compare the Python workspace against the local ignored TypeScript archive when available')
```

Handler:

```python
if args.command == 'parity-audit':
    print(run_parity_audit().to_markdown())
    return 0
```

Ein besonders wichtiger Befehl im Kontext des Portierungsprojekts: Er vergleicht den aktuellen Python-Workspace mit dem archivierten TypeScript-Original und identifiziert Abweichungen. Die Methode heißt hier `to_markdown()` (statt `as_markdown()` wie bei den anderen) — eine kleine Inkonsistenz in der Benennung, die aber funktional keinen Unterschied macht.

---

## 4.3 Die `main()`-Funktion

```python
def main(argv: list[str] | None = None) -> int:
```

Die `main()`-Funktion ist der eigentliche Einstiegspunkt der Anwendung. Sie akzeptiert ein optionales `argv`-Argument (eine Liste von Strings), das standardmässig `None` ist. Wenn `None`, verwendet `argparse` automatisch `sys.argv[1:]`. Die Möglichkeit, `argv` explizit zu übergeben, ist entscheidend für die Testbarkeit: In Tests kann die Funktion direkt mit beliebigen Argumentlisten aufgerufen werden, ohne `sys.argv` manipulieren zu müssen.

### 4.3.1 Initialisierung

```python
parser = build_parser()
args = parser.parse_args(argv)
manifest = build_port_manifest()
```

Die ersten drei Zeilen bilden die Initialisierungsphase:

1. Der Parser wird über `build_parser()` erzeugt.
2. Die Kommandozeilenargumente werden geparst. Scheitert dies (z. B. wegen eines unbekannten Subcommands oder fehlender Pflichtargumente), beendet argparse das Programm automatisch mit einer Fehlermeldung.
3. Das Port-Manifest wird gebaut. Dieses Manifest wird von mehreren Befehlen benötigt und wird daher einmalig zu Beginn erzeugt — ein Beispiel für das „Eager Loading"-Muster.

### 4.3.2 Die Dispatch-Logik

Die gesamte Dispatch-Logik besteht aus einer linearen Kette von `if`-Abfragen auf `args.command`. Es wird kein `match`-Statement (Python 3.10+), kein Dictionary-Dispatch und kein anderes Muster verwendet. Die Wahl einer einfachen `if`-Kette hat Vor- und Nachteile:

**Vorteile:**
- Maximale Lesbarkeit: Jeder Befehl ist sofort auffindbar.
- Flexibilität: Jeder Handler kann beliebig komplex sein, ohne in ein einheitliches Schema gepresst zu werden.
- Debuggbarkeit: Breakpoints können einfach an einzelnen Stellen gesetzt werden.

**Nachteile:**
- Skalierbarkeit: Bei deutlich mehr Befehlen würde die Funktion unübersichtlich lang.
- Wiederholung: Das Muster `if args.command == '...': ... return 0` wird 24 Mal wiederholt.

Die Autoren haben sich bewusst für die einfache Variante entschieden, die bei 24 Befehlen noch gut handhabbar ist.

### 4.3.3 Rückgabewerte und Fehlerbehandlung

Jeder Handler gibt explizit einen ganzzahligen Exit-Code zurück:

- **0** signalisiert Erfolg.
- **1** signalisiert einen anwendungsspezifischen Fehler (z. B. „Command not found" bei `show-command` und `show-tool`, oder `handled == False` bei `exec-command` und `exec-tool`).
- **2** wird am Ende der Funktion für unbekannte Befehle zurückgegeben (ein Sicherheitsnetz, das in der Praxis nie erreicht werden sollte, da argparse unbekannte Subcommands bereits abfängt).

```python
parser.error(f'unknown command: {args.command}')
return 2
```

Der Aufruf von `parser.error()` gibt eine formatierte Fehlermeldung aus und beendet das Programm mit Exit-Code 2. Das nachfolgende `return 2` ist technisch unerreichbar, dient aber als Typannotations-Hilfe und Sicherheitsnetz.

### 4.3.4 Der `__main__`-Block

```python
if __name__ == '__main__':
    raise SystemExit(main())
```

Die letzte Zeile der Datei ermöglicht die direkte Ausführung als Skript. `raise SystemExit(main())` wandelt den von `main()` zurückgegebenen Integer in einen Prozess-Exit-Code um. Die Verwendung von `raise SystemExit()` anstelle von `sys.exit()` ist eine bewusste stilistische Wahl: Sie vermeidet den Import von `sys` und macht die Absicht — das Programm mit einem bestimmten Exit-Code zu beenden — expliziter.

---

## 4.4 Architektonische Beobachtungen

### Einheitliche Ausgabemuster

Die Datei zeigt zwei Hauptmuster für die Ausgabeformatierung:

1. **Markdown-Methoden** (`as_markdown()`, `to_markdown()`): Verwendet von `summary`, `manifest`, `setup-report`, `command-graph`, `tool-pool`, `bootstrap-graph`, `bootstrap` und `parity-audit`.
2. **Text-Methoden** (`as_text()`): Verwendet von allen fünf Laufzeitmodi.
3. **Direkte Formatierung**: Verwendet von `subsystems`, `commands`, `tools`, `route`, `turn-loop`, `flush-transcript` und `load-session`.

### Zwei Laufzeit-Objekte

Die Datei verwendet zwei verschiedene Laufzeit-Abstraktionen:

- `QueryEnginePort`: Für Workspace-bezogene Operationen (Summary, Flush).
- `PortRuntime`: Für Routing- und Session-Operationen (Route, Bootstrap, Turn-Loop).

Diese Trennung spiegelt die Architektur des Gesamtsystems wider: Die Query-Engine ist eine Inspektionsschicht, die Runtime eine Ausführungsschicht.

### Testbarkeit durch Design

Die gesamte Datei ist testfreundlich gestaltet: `build_parser()` kann isoliert getestet werden, `main()` akzeptiert ein explizites `argv`, und alle Handler delegieren sofort an importierte Funktionen. Es gibt keinen globalen Zustand und keine Seiteneffekte außerhalb der Handler-Aufrufe.

---

## 4.5 Zusammenfassung

Die Datei `src/main.py` ist der zentrale CLI-Einstiegspunkt des Claw-Code-Projekts. Mit 24 Subcommands, die in sieben funktionale Kategorien fallen, bietet sie einen umfassenden Zugang zu allen Aspekten des Python-Portierungs-Workspace — von der einfachen Inspektion über die Befehlsausführung bis hin zur Architekturanalyse. Die Trennung in `build_parser()` (Konfiguration) und `main()` (Dispatch) ist sauber, die Delegation an spezialisierte Module konsequent, und die Fehlerbehandlung über Exit-Codes folgt Unix-Konventionen. Trotz der Einfachheit der linearen `if`-Kette bleibt der Code übersichtlich und wartbar — ein solides Fundament für die gesamte CLI-Schicht des Projekts.




# Chapter 5: Data Models & Type System

## 5.1 Introduction -- Why Data Models Are the Backbone of Every Architecture

In every non-trivial piece of software, the question arises early: How do we represent the concepts of our domain in code? Claw Code answers this question with a small but thoughtfully layered collection of **Dataclasses** that live in three files:

| File | Classes | Lines |
|---|---|---|
| `src/models.py` | `Subsystem`, `PortingModule`, `PermissionDenial`, `UsageSummary`, `PortingBacklog` | 50 |
| `src/query.py` | `QueryRequest`, `QueryResponse` | 14 |
| `src/Tool.py` | `ToolDefinition`, `DEFAULT_TOOLS` | 16 |

Together, these three files comprise fewer than 80 lines -- and yet they define the entire vocabulary with which all other modules communicate. In this chapter, we will examine every single class, every field, every method, and every design decision in detail.

---

## 5.2 Frozen Dataclasses as Value Objects

### 5.2.1 The Principle of Immutability

Six of the eight classes in the data model carry the decorator `@dataclass(frozen=True)`. What does this mean in practice? Python automatically generates `__setattr__` and `__delattr__` methods for such classes that reject any subsequent modification with a `FrozenInstanceError`:

```python
from src.models import PortingModule

mod = PortingModule(
    name='query_engine',
    responsibility='LLM-Abfragen ausfuehren',
    source_hint='session.ts',
    status='planned',
)

mod.status = 'done'  # -> FrozenInstanceError!
```

This behavior is not accidental but a deliberate design decision. In the terminology of Domain-Driven Design, frozen Dataclasses are **Value Objects**. A Value Object is entirely defined by its attributes -- it possesses no identity of its own that could change independently of its fields. Two `PortingModule` instances with the same fields are *equal*, and they remain equal as long as they exist.

### 5.2.2 Hashing and Use in Sets

Frozen Dataclasses are automatically **hashable**. Python generates a `__hash__` method based on all fields. This allows constructs such as:

```python
seen = set()
seen.add(PortingModule('a', 'Aufgabe A', 'file_a.ts'))
seen.add(PortingModule('a', 'Aufgabe A', 'file_a.ts'))
assert len(seen) == 1  # Duplicate is detected
```

Or as dictionary keys:

```python
stats: dict[PortingModule, int] = {
    PortingModule('query_engine', 'Abfragen', 'session.ts'): 42,
}
```

In a system that discovers, classifies, and processes modules through various phases, the ability to use them in `set` and `dict` structures is enormously valuable. Without `frozen=True`, this would not be possible, since mutable Dataclasses in Python are not hashable by default.

### 5.2.3 Thread Safety and Predictability

Another advantage of immutability: In a system where data flows through multiple processing stages -- from analysis through planning to execution -- frozen objects can safely be passed between functions, modules, and potentially even threads, without requiring a defensive copy. When a function receives a `Subsystem` object, it can be certain that no one will modify it after the fact.

---

## 5.3 Mutable vs. Immutable -- Two Strategies, One Architecture

Of the five classes in `models.py`, exactly **one** is mutable: `PortingBacklog`. This is not an oversight but follows a clear logic.

### Immutable (frozen=True):

- `Subsystem` -- a discovered subsystem does not change; it is *analyzed once, then captured*
- `PortingModule` -- a planned module is a specification; changes produce a new object
- `PermissionDenial` -- a denial is a fact that is recorded
- `UsageSummary` -- token counters; updates produce a *new* Summary (functional style)

### Mutable:

- `PortingBacklog` -- a growing collection of modules that changes during runtime

The decision is pragmatic: A backlog is by its very nature a **mutable list**. Modules are added, reprioritized, removed. A frozen variant would require a complete copy with every change -- that would be unnecessarily cumbersome in Python and would provide no real safety benefit, since the backlog is typically managed at a single central location.

`UsageSummary`, on the other hand, takes the opposite approach: Although it conceptually represents a changing counter, it is `frozen=True` and realizes changes by creating new instances. This follows the functional paradigm and makes it possible to model the history of token usage as a chain of immutable snapshots.

---

## 5.4 The Classes in Detail

### 5.4.1 `Subsystem`

```python
@dataclass(frozen=True)
class Subsystem:
    name: str
    path: str
    file_count: int
    notes: str
```

**Purpose:** Represents a discovered subsystem in the analyzed source code. Created and imported by `port_manifest.py`:

```python
# src/port_manifest.py
from .models import Subsystem
```

**Fields:**

| Field | Type | Description |
|---|---|---|
| `name` | `str` | Human-readable name of the subsystem, e.g. `"CLI-Kern"` |
| `path` | `str` | File path or directory where the subsystem lives |
| `file_count` | `int` | Number of files belonging to the subsystem |
| `notes` | `str` | Free-text notes, e.g. hints about dependencies |

All four fields are required (no defaults). This makes sense: A subsystem without a path or without a file count would be incomplete and should not be created in the first place.

**Typical usage:**

```python
sub = Subsystem(
    name='Session-Management',
    path='src/session/',
    file_count=12,
    notes='Abhaengigkeit zu auth-Modul',
)
```

### 5.4.2 `PortingModule`

```python
@dataclass(frozen=True)
class PortingModule:
    name: str
    responsibility: str
    source_hint: str
    status: str = 'planned'
```

**Purpose:** The central and most versatile data class of the entire project. A `PortingModule` represents a **planned or already implemented unit of work** -- this could be a CLI command, a tool, a utility, or any other functional unit that is to be created as part of the porting effort.

**Fields:**

| Field | Type | Default | Description |
|---|---|---|---|
| `name` | `str` | -- | Identifier of the module, e.g. `"query_engine"` or `"port_manifest"` |
| `responsibility` | `str` | -- | Brief description of the task, e.g. `"LLM-Abfragen ausfuehren"` |
| `source_hint` | `str` | -- | Reference to the source file in the reference project, e.g. `"session.ts"` |
| `status` | `str` | `'planned'` | Current state: `'planned'`, `'in_progress'`, `'done'` etc. |

The field `status` has the default value `'planned'`, which reflects the most common creation scenario: New modules are first planned and later implemented. Thanks to the default value, it suffices to specify only the three required fields when creating:

```python
mod = PortingModule('tool_pool', 'Werkzeugverwaltung', 'tools.ts')
assert mod.status == 'planned'
```

**Universal Representation -- Commands AND Tools:**

A particularly elegant aspect of this class is its dual role. In Claw Code, there is no separate `Command` or `Tool` model class at the domain level. Instead, `PortingModule` is used for both CLI commands and registered tools. The distinction is made purely through the context in which the object is used:

```python
# As CLI command (in commands.py / command_graph.py)
from .models import PortingModule
cmd = PortingModule('plan', 'Porting-Plan erstellen', 'commands.ts')

# As Tool (in tools.py / tool_pool.py)
from .models import PortingModule
tool = PortingModule('port_manifest', 'Workspace zusammenfassen', 'tools.ts')
```

This unification reduces the number of classes, avoids redundancy, and expresses an important architectural insight: From the perspective of the porting system, commands and tools are structurally identical -- they have a name, a responsibility, an origin, and a status. Only at runtime does the system distinguish how they are executed.

The import statistics confirm this central role: `PortingModule` is imported by five different modules -- `commands.py`, `command_graph.py`, `tools.py`, `tool_pool.py`, and `runtime.py`. No other data class is so broadly connected.

### 5.4.3 `PermissionDenial`

```python
@dataclass(frozen=True)
class PermissionDenial:
    tool_name: str
    reason: str
```

**Purpose:** Records a case where tool access was denied. This is relevant for the security architecture: When a user or an automated action attempts to execute a tool for which no permission exists, a `PermissionDenial` object is created and can be evaluated later.

**Fields:**

| Field | Type | Description |
|---|---|---|
| `tool_name` | `str` | Name of the denied tool, e.g. `"file_write"` |
| `reason` | `str` | Human-readable justification, e.g. `"Schreibzugriff nicht erlaubt"` |

Imported by:

```python
# src/query_engine.py
from .models import PermissionDenial
# src/runtime.py
from .models import PermissionDenial
```

The class is deliberately minimalistic. It stores no timestamps, no user IDs, no stack traces -- only the bare fact: *which* tool was denied and *why*. Extended context information can be added in the calling code as needed.

### 5.4.4 `UsageSummary` -- Functional Token Accounting

```python
@dataclass(frozen=True)
class UsageSummary:
    input_tokens: int = 0
    output_tokens: int = 0

    def add_turn(self, prompt: str, output: str) -> 'UsageSummary':
        return UsageSummary(
            input_tokens=self.input_tokens + len(prompt.split()),
            output_tokens=self.output_tokens + len(output.split()),
        )
```

**Purpose:** Tracks the cumulative token consumption across multiple conversation turns. Despite the `frozen=True` declaration, the class offers a method for "updating" -- albeit in a functional style.

**Fields:**

| Field | Type | Default | Description |
|---|---|---|---|
| `input_tokens` | `int` | `0` | Estimated number of input tokens |
| `output_tokens` | `int` | `0` | Estimated number of output tokens |

Both fields default to `0`, which allows creating an empty summary:

```python
summary = UsageSummary()  # input_tokens=0, output_tokens=0
```

**The `add_turn()` method in detail:**

```python
def add_turn(self, prompt: str, output: str) -> 'UsageSummary':
    return UsageSummary(
        input_tokens=self.input_tokens + len(prompt.split()),
        output_tokens=self.output_tokens + len(output.split()),
    )
```

This method is the heart of the functional pattern. It does *not* modify the existing instance (which would be impossible anyway due to `frozen=True`), but instead creates a **new** `UsageSummary` with updated counter values.

**Token estimation via word count:**

The token estimation is performed via `len(prompt.split())` and `len(output.split())` respectively. This is a deliberate simplification: Real tokenizers (such as those from OpenAI or Anthropic) break text into subword units that do not align with word boundaries. A word like "Unveraenderlichkeit" could be split into 3--5 tokens depending on the tokenizer, while `split()` counts it as one word.

Why this simplification? Three reasons:

1. **No dependency:** A real tokenizer would require an external library (e.g. `tiktoken`), which would enlarge the dependency chain.
2. **Sufficient accuracy:** For the purposes of a usage overview -- not an exact billing -- the word count is a serviceable approximation. Typically, the ratio is about 1.3 tokens per word in English.
3. **Speed:** `str.split()` is one of the fastest string operations in Python and causes no appreciable latency.

**Typical usage as a chain:**

```python
summary = UsageSummary()
summary = summary.add_turn("Analysiere das Projekt", "Das Projekt hat 5 Module.")
summary = summary.add_turn("Zeige Details", "Modul A ist fuer X zustaendig.")

print(summary.input_tokens)   # 5 (3 + 2)
print(summary.output_tokens)  # 12 (6 + 6)
```

Each assignment to `summary` overwrites the reference, not the object. The old instances are collected by the garbage collector. This pattern is identical to how immutable strings are handled in Python (`s = s + "x"`) and is intuitively understandable for Python developers.

### 5.4.5 `PortingBacklog` -- The Mutable Exception

```python
@dataclass
class PortingBacklog:
    title: str
    modules: list[PortingModule] = field(default_factory=list)

    def summary_lines(self) -> list[str]:
        return [
            f'- {module.name} [{module.status}] — {module.responsibility} (from {module.source_hint})'
            for module in self.modules
        ]
```

**Purpose:** Manages a named collection of `PortingModule` entries. This is the only mutable data class in `models.py`, recognizable by the absence of `frozen=True`.

**Fields:**

| Field | Type | Default | Description |
|---|---|---|---|
| `title` | `str` | -- | Title of the backlog, e.g. `"Claw Code Porting-Plan"` |
| `modules` | `list[PortingModule]` | `[]` (via `field(default_factory=list)`) | List of planned modules |

Noteworthy is the use of `field(default_factory=list)` instead of a simple `= []`. This is a famously notorious Python pattern: If one were to write `modules: list = []`, *all* instances would share the same list -- a classic and insidious bug. `default_factory=list` ensures that each instance receives its own, empty list.

**The `summary_lines()` method in detail:**

```python
def summary_lines(self) -> list[str]:
    return [
        f'- {module.name} [{module.status}] — {module.responsibility} (from {module.source_hint})'
        for module in self.modules
    ]
```

This method produces a Markdown-compatible representation of all modules in the backlog. Each line follows the schema:

```
- <name> [<status>] — <responsibility> (from <source_hint>)
```

**Example:**

```python
backlog = PortingBacklog(title='Claw Code Hauptplan')
backlog.modules.append(
    PortingModule('query_engine', 'LLM-Abfragen', 'session.ts', 'in_progress')
)
backlog.modules.append(
    PortingModule('tool_pool', 'Werkzeugverwaltung', 'tools.ts')
)

for line in backlog.summary_lines():
    print(line)
```

Output:

```
- query_engine [in_progress] — LLM-Abfragen (from session.ts)
- tool_pool [planned] — Werkzeugverwaltung (from tools.ts)
```

The Markdown format is deliberately chosen: The output can be directly inserted into report files, terminal outputs, or chat responses. The em-dash (`---`) and square brackets around the status create a visually clear, scan-friendly layout.

The method is implemented as a **pure read method** -- it does not modify the list but projects it into a new list of strings. This is a good example of the interplay between mutability and purity: The class itself is mutable (modules can be added), but its query methods produce no side effects.

---

## 5.5 Query Data Models (`src/query.py`)

```python
@dataclass(frozen=True)
class QueryRequest:
    prompt: str

@dataclass(frozen=True)
class QueryResponse:
    text: str
```

These two classes form a classic **Request/Response pair**. Their extreme simplicity -- one single field each -- is not a sign of immaturity but a deliberate decision.

### 5.5.1 `QueryRequest`

| Field | Type | Description |
|---|---|---|
| `prompt` | `str` | The query text sent to the query engine |

Why not just pass a `str`? Because a dedicated class offers several advantages:

1. **Type safety:** A function `def execute(request: QueryRequest)` is more precise than `def execute(prompt: str)`. The type communicates the *intent*.
2. **Extensibility:** Later, fields such as `temperature`, `max_tokens`, or `system_prompt` can be added without changing existing signatures.
3. **Uniformity:** All data in the system flows as typed objects, not as loose strings.

### 5.5.2 `QueryResponse`

| Field | Type | Description |
|---|---|---|
| `text` | `str` | The response text from the query engine |

Here too: The class is an extension point. Future fields such as `token_count`, `model_id`, or `finish_reason` could enrich the response object.

Both classes are `frozen=True`, since neither a request nor a response should be modified after creation. They are facts, not states.

---

## 5.6 Tool Definitions (`src/Tool.py`)

```python
@dataclass(frozen=True)
class ToolDefinition:
    name: str
    purpose: str

DEFAULT_TOOLS = (
    ToolDefinition('port_manifest', 'Summarize the active Python workspace'),
    ToolDefinition('query_engine', 'Render a Python-first porting summary'),
)
```

### 5.6.1 `ToolDefinition`

| Field | Type | Description |
|---|---|---|
| `name` | `str` | Machine-readable identifier of the tool |
| `purpose` | `str` | Human-readable description of the intended use |

The class describes an available tool in the system. It is `frozen=True`, since tool definitions are not modified at runtime -- a tool has a fixed name and a fixed purpose.

### 5.6.2 `DEFAULT_TOOLS`

```python
DEFAULT_TOOLS = (
    ToolDefinition('port_manifest', 'Summarize the active Python workspace'),
    ToolDefinition('query_engine', 'Render a Python-first porting summary'),
)
```

Noteworthy: `DEFAULT_TOOLS` is a **tuple**, not a list. This reinforces the immutability philosophy at the collection level. While `ToolDefinition` instances are protected by `frozen=True`, a `list` would allow adding or removing elements. A `tuple` prevents that as well.

The two default tools -- `port_manifest` and `query_engine` -- reflect the core functionality: workspace analysis and generation of porting summaries.

### 5.6.3 Distinction from `PortingModule`

One might ask: Why does `ToolDefinition` exist alongside `PortingModule`? The difference lies in the level of abstraction:

- `PortingModule` describes a planned or implemented module *in the context of porting* -- with status, responsibility, and source hint.
- `ToolDefinition` describes a *registered tool* in the running system -- with name and purpose, but without porting context.

`PortingModule` is a planning object; `ToolDefinition` is a runtime object. Both can represent the same real module, but from different perspectives.

---

## 5.7 `models.py` as the Shared Foundation

The file `src/models.py` forms the **shared foundation** of the entire project. Every notable module imports at least one class from it:

| Importing Module | Imported Classes |
|---|---|
| `src/commands.py` | `PortingBacklog`, `PortingModule` |
| `src/command_graph.py` | `PortingModule` |
| `src/tools.py` | `PortingBacklog`, `PortingModule` |
| `src/tool_pool.py` | `PortingModule` |
| `src/runtime.py` | `PermissionDenial`, `PortingModule` |
| `src/query_engine.py` | `PermissionDenial`, `UsageSummary` |
| `src/port_manifest.py` | `Subsystem` |

This import pattern shows a star-shaped dependency structure: `models.py` sits at the center and itself has *no* dependencies on other project modules (it imports only `dataclass` and `field` from the standard library). This is a deliberate and important property:

1. **Cycle-free:** Since `models.py` imports nothing from the project, no circular dependencies can arise.
2. **Stability:** Changes to the business logic in `commands.py` or `runtime.py` do not affect the data models.
3. **Testability:** The model classes can be tested in isolation, without mocking or setup.

The `from __future__ import annotations` at the beginning of each file enables the use of forward references in type annotations. In `UsageSummary.add_turn()`, the return type is annotated as the string `'UsageSummary'` -- with the future import, this also becomes possible without quotation marks (in older Python versions before 3.10, this was still necessary).

---

## 5.8 Design Patterns and Summary

The data models of Claw Code follow several established design principles:

**Value Object Pattern:** Frozen Dataclasses are classic Value Objects -- immutable, equality-based, hashable. They represent concepts like "a subsystem" or "a permission denial" as pure data without behavior (aside from `add_turn` and `summary_lines`).

**Immutable-by-Default, Mutable-by-Exception:** The overwhelming majority of classes are `frozen`. Only where mutability corresponds to the natural lifecycle of the object (as with the growing backlog) is `frozen` omitted.

**Functional Update Pattern:** `UsageSummary.add_turn()` demonstrates how immutable objects can be "updated" by creating new instances with modified values. This pattern is known from functional languages and leads to predictable, well-testable code.

**Shared Kernel:** `models.py` serves as a shared kernel that defines the common language of all modules. It is the only file that all others depend on, and it itself depends on nothing.

**Separation of Concerns:** Query data models (`query.py`) and tool definitions (`Tool.py`) live in their own files, even though they each contain only two definitions. This maintains thematic separation: domain objects, query protocol, and tool registration are three different concerns.

With fewer than 80 lines of code, the type system of Claw Code establishes a complete vocabulary that balances clarity, safety, and extensibility. The data models are small enough to be understood at a glance and precise enough to serve as a reliable foundation for the entire architecture above them.


# Chapter 6: The Command and Tool Catalog

## 6.1 Introduction

A CLI agent like Claude Code thrives on two axes of interaction: **Commands**, which the user explicitly invokes, and **Tools**, which the language model autonomously employs during a conversation. In the original implementation of Claude Code, these two catalogs are spread across hundreds of TypeScript files -- React components for presentation, handlers for logic, validation files for input. Claw Code takes a fundamentally different approach: Instead of functionally rebuilding each individual module, all commands and tools are captured as **reference data** in JSON snapshots and made accessible through a thin Python API.

This chapter describes the entire pipeline -- from the JSON file on disk through LRU-cache-backed loading to the filtered assembly of a concrete tool pool for a session. We examine four source code files (`commands.py`, `tools.py`, `permissions.py`, `tool_pool.py`), two JSON snapshots, and the underlying data models.

## 6.2 The JSON Snapshot Structure

### 6.2.1 Structure of an Entry

Both snapshots -- `commands_snapshot.json` and `tools_snapshot.json` -- reside in the directory `src/reference_data/` and follow exactly the same schema. Each file contains a JSON array of objects with three fields:

```json
{
  "name": "add-dir",
  "source_hint": "commands/add-dir/add-dir.tsx",
  "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/add-dir.tsx"
}
```

The three fields in detail:

- **`name`**: The canonical identifier of the command or tool. For Commands, these are kebab-case names like `add-dir`, `branch`, `autofix-pr`, or `backfill-sessions`. For Tools, PascalCase dominates: `AgentTool`, `BashTool`, `FileReadTool`. The name is the primary search key for all lookup operations.

- **`source_hint`**: The relative path within the archived TypeScript codebase from which this module originates. Examples include `commands/add-dir/add-dir.tsx` or `tools/AgentTool/AgentTool.tsx`. This path is not used for execution -- it is a pure back-reference that shows developers where the original implementation would be found. The `source_hint` also plays a central role in filtering: Whether a command counts as a plugin or skill command is determined based on substrings in this field.

- **`responsibility`**: A descriptive sentence summarizing the task of the module. In the current version, this is a generated text following the pattern `"Command module mirrored from archived TypeScript path ..."` or `"Tool module mirrored from archived TypeScript path ..."`. It documents the mirroring status and provides human-readable context.

### 6.2.2 Structure of the Command Snapshots

The file `commands_snapshot.json` spans 1036 lines and contains **207 entries**. An excerpt from the beginning of the file shows the typical structure:

```json
[
  {
    "name": "add-dir",
    "source_hint": "commands/add-dir/add-dir.tsx",
    "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/add-dir.tsx"
  },
  {
    "name": "add-dir",
    "source_hint": "commands/add-dir/index.ts",
    "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/index.ts"
  },
  {
    "name": "validation",
    "source_hint": "commands/add-dir/validation.ts",
    "responsibility": "Command module mirrored from archived TypeScript path commands/add-dir/validation.ts"
  },
  {
    "name": "advisor",
    "source_hint": "commands/advisor.ts",
    "responsibility": "Command module mirrored from archived TypeScript path commands/advisor.ts"
  }
]
```

Note: The same `name` can appear multiple times when the original command consisted of multiple files (such as `add-dir.tsx` and `index.ts`). Each file of the original source is captured as a separate entry. This preserves the granularity of the TypeScript codebase -- a single command like `add-dir` brings its React component, its index export, and its validation logic as three separate `PortingModule` entries.

### 6.2.3 Structure of the Tool Snapshots

The file `tools_snapshot.json` is somewhat more compact at 921 lines and **184 entries**. The tool names follow TypeScript conventions:

```json
[
  {
    "name": "AgentTool",
    "source_hint": "tools/AgentTool/AgentTool.tsx",
    "responsibility": "Tool module mirrored from archived TypeScript path tools/AgentTool/AgentTool.tsx"
  },
  {
    "name": "UI",
    "source_hint": "tools/AgentTool/UI.tsx",
    "responsibility": "Tool module mirrored from archived TypeScript path tools/AgentTool/UI.tsx"
  },
  {
    "name": "agentColorManager",
    "source_hint": "tools/AgentTool/agentColorManager.ts",
    "responsibility": "Tool module mirrored from archived TypeScript path tools/AgentTool/agentColorManager.ts"
  }
]
```

Here too, the entries reflect the directory structure of the original: The `AgentTool` directory contained, in addition to the main component, helper files such as `agentMemory.ts`, `agentDisplay.ts`, and built-in agents (`claudeCodeGuideAgent.ts`, `exploreAgent.ts`, `generalPurposeAgent.ts`). Each of these files is maintained as its own tool entry.

## 6.3 The PortingModule Data Model

Both snapshot loaders convert the JSON entries into instances of the class `PortingModule`, defined in `src/models.py`:

```python
@dataclass(frozen=True)
class PortingModule:
    name: str
    responsibility: str
    source_hint: str
    status: str = 'planned'
```

The class is declared as a `frozen=True` Dataclass -- making it immutable and hashable. The four fields correspond directly to the three JSON fields plus a fourth field `status`, which is always set to `'mirrored'` when loading from the snapshot (the default `'planned'` applies only when modules are created programmatically without explicitly specifying the status).

The immutability is no coincidence here: Since the loaded modules are stored in global tuples and managed through LRU caches, mutability would be a source of errors. An accidental modification of a module would corrupt the cache without this being noticed.

## 6.4 LRU Caching: `load_command_snapshot()` and `load_tool_snapshot()`

### 6.4.1 The Loading Functions

Both modules -- `commands.py` and `tools.py` -- each define a loading function that reads the JSON snapshot from disk and converts it into a tuple of `PortingModule` instances:

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent / 'reference_data' / 'commands_snapshot.json'

@lru_cache(maxsize=1)
def load_command_snapshot() -> tuple[PortingModule, ...]:
    raw_entries = json.loads(SNAPSHOT_PATH.read_text())
    return tuple(
        PortingModule(
            name=entry['name'],
            responsibility=entry['responsibility'],
            source_hint=entry['source_hint'],
            status='mirrored',
        )
        for entry in raw_entries
    )
```

The function `load_tool_snapshot()` in `tools.py` is identically structured; only the path points to `tools_snapshot.json`.

### 6.4.2 Why `@lru_cache(maxsize=1)`?

The decorator `@lru_cache(maxsize=1)` from `functools` causes the function's result to be held in memory after the first call. On every subsequent call, instead of re-reading and parsing the JSON file, the already computed tuple is returned directly.

The choice of `maxsize=1` is precise and well-founded:

1. **Parameterless function**: Both loading functions take no arguments. There is therefore exactly one possible cache key -- the empty argument tuple `()`. A larger cache would be pointless, since there can never be more than one entry.

2. **Avoidance of redundant I/O**: The JSON files together span nearly 2000 lines. Reading and parsing them costs time, especially if it were to happen with every access to a command name. The cache reduces this to a single read operation per process lifetime.

3. **Implicit initialization**: The global constants `PORTED_COMMANDS` and `PORTED_TOOLS` are assigned at module level. When the module is imported, the loading function is called once, and from that point on the cache delivers the result.

4. **Thread safety**: `lru_cache` in CPython is sufficiently protected by the GIL (Global Interpreter Lock). Since the function only performs actual I/O on the first call and thereafter always serves the cache, there is no race condition risk in normal operation.

An important side effect: Since `lru_cache` holds its result as a strong reference, the entire tuple of `PortingModule` instances remains in memory for the lifetime of the process. At 207 and 184 entries respectively, the memory consumption is negligible -- a tuple of a few hundred small Dataclass instances occupies a few kilobytes.

## 6.5 Global Constants: `PORTED_COMMANDS` and `PORTED_TOOLS`

Immediately after the definition of the loading functions, the global constants are set:

```python
PORTED_COMMANDS = load_command_snapshot()   # 207 Eintraege
```

```python
PORTED_TOOLS = load_tool_snapshot()         # 184 Eintraege
```

These tuples form the backbone of the entire catalog subsystem. All subsequent functions -- lookup, filtering, search, execution -- operate on these global constants. Since they are immutable tuples of immutable Dataclasses, they are inherently thread-safe and can be passed to any location without copying.

The number of entries -- 207 commands and 184 tools -- reflects the considerable surface area of the original project. Not every entry corresponds to a standalone command or tool; as described in Section 6.2, helper modules (validation, UI components, utilities) are also captured individually.

Additionally, `commands.py` contains a cached helper function:

```python
@lru_cache(maxsize=1)
def built_in_command_names() -> frozenset[str]:
    return frozenset(module.name for module in PORTED_COMMANDS)
```

This returns a `frozenset` of all command names and enables O(1) membership tests. Here too, `maxsize=1` is the correct choice, since the function is parameterless and the result does not change at runtime.

## 6.6 Lookup Functions: `get_command()` and `get_tool()`

### 6.6.1 Case-Insensitive Linear Search

Both modules provide a `get_*` function that looks up a single `PortingModule` by its name:

```python
def get_command(name: str) -> PortingModule | None:
    needle = name.lower()
    for module in PORTED_COMMANDS:
        if module.name.lower() == needle:
            return module
    return None
```

```python
def get_tool(name: str) -> PortingModule | None:
    needle = name.lower()
    for module in PORTED_TOOLS:
        if module.name.lower() == needle:
            return module
    return None
```

Both functions are **case-insensitive**: The search term and the stored name are each normalized with `.lower()` before comparison. Thus `get_tool("bashtool")` finds the module named `"BashTool"`, and `get_command("Add-Dir")` finds `"add-dir"`.

The search is linear -- O(n) over the entire tuple. At 207 and 184 entries respectively, this is completely unproblematic. A hash table would be over-engineering here: The function is typically called once per user interaction, and even on slow hardware, a linear scan over 200 short strings takes less than a microsecond.

Important: With duplicates (such as the multiply-occurring `add-dir`), `get_command()` returns the **first match**. This is the module with the lowest index in the tuple -- i.e., the one that appears first in the JSON file.

## 6.7 Filtering: `get_commands()` and `get_tools()`

### 6.7.1 Command Filtering

The function `get_commands()` provides a filtered view of the command catalog:

```python
def get_commands(
    cwd: str | None = None,
    include_plugin_commands: bool = True,
    include_skill_commands: bool = True,
) -> tuple[PortingModule, ...]:
    commands = list(PORTED_COMMANDS)
    if not include_plugin_commands:
        commands = [module for module in commands
                    if 'plugin' not in module.source_hint.lower()]
    if not include_skill_commands:
        commands = [module for module in commands
                    if 'skills' not in module.source_hint.lower()]
    return tuple(commands)
```

The filtering logic is elegant in its simplicity: Instead of maintaining a formal taxonomy, it uses **substring matching on the `source_hint`**. A command counts as a plugin command if its `source_hint` contains the substring `"plugin"` (case-insensitive). Analogously, a command counts as a skill command if `"skills"` appears in the `source_hint`.

This approach has advantages and disadvantages. The advantage: No additional classification field needs to be maintained in the JSON file. The directory structure of the original -- `commands/plugin-*`, `commands/skills/*` -- already implicitly encodes the category. The disadvantage: Should a command happen to contain `"plugin"` in its path without being a plugin, it would be incorrectly filtered. In practice, this is not a problem with the existing codebase.

The parameter `cwd` is accepted but not currently evaluated. It serves as a placeholder for future extensions where the command list could depend on the current working directory (e.g., project-specific commands).

### 6.7.2 Tool Filtering

The function `get_tools()` offers richer filtering:

```python
def get_tools(
    simple_mode: bool = False,
    include_mcp: bool = True,
    permission_context: ToolPermissionContext | None = None,
) -> tuple[PortingModule, ...]:
    tools = list(PORTED_TOOLS)
    if simple_mode:
        tools = [module for module in tools
                 if module.name in {'BashTool', 'FileReadTool', 'FileEditTool'}]
    if not include_mcp:
        tools = [module for module in tools
                 if 'mcp' not in module.name.lower()
                 and 'mcp' not in module.source_hint.lower()]
    return filter_tools_by_permission_context(tuple(tools), permission_context)
```

Three filters are stacked here:

1. **Simple Mode**: When activated, the entire catalog is reduced to exactly three tools: `BashTool`, `FileReadTool`, and `FileEditTool`. These are the minimal tools an agent needs to be able to work at all -- reading files, editing files, and executing shell commands. Simple Mode is particularly useful in restricted environments or during debugging, where the full tool palette would be distracting.

2. **MCP Filter**: The Model Context Protocol (MCP) allows integration of external tool servers. When `include_mcp=False` is set, all tools whose name or `source_hint` contains the substring `"mcp"` are removed. This enables purely local operation without dependency on external services.

3. **Permission Filter**: As the final step, `filter_tools_by_permission_context()` is called, which excludes further tools via the `ToolPermissionContext` (see Section 6.8).

The order of filters is significant: First the base set is narrowed (Simple Mode), then MCP tools are removed, and lastly the permission system takes effect. This ensures that the permission check is applied only to the remaining relevant set.

## 6.8 Search Functions: `find_commands()` and `find_tools()`

For interactive scenarios -- such as when a user wants to display an index of available commands -- search functions are provided:

```python
def find_commands(query: str, limit: int = 20) -> list[PortingModule]:
    needle = query.lower()
    matches = [module for module in PORTED_COMMANDS
               if needle in module.name.lower()
               or needle in module.source_hint.lower()]
    return matches[:limit]
```

The search is a **substring search**: The `query` string is converted to lowercase and then checked against both the `name` and the `source_hint` of each module. A query like `find_commands("agent")` would return all commands in whose name or origin path `"agent"` appears.

The parameter `limit` restricts the result set to a default of 20 matches. This is a pragmatic choice for display purposes -- a terminal can only show a limited number of lines simultaneously.

The function `find_tools()` in `tools.py` is identically structured. Both return a `list` (not a `tuple`), which is semantically correct: The result is a fresh, mutable collection that the caller can further process as desired.

For display purposes, `render_command_index()` and `render_tool_index()` also exist, which produce formatted text output:

```python
def render_command_index(limit: int = 20, query: str | None = None) -> str:
    modules = find_commands(query, limit) if query else list(PORTED_COMMANDS[:limit])
    lines = [f'Command entries: {len(PORTED_COMMANDS)}', '']
    if query:
        lines.append(f'Filtered by: {query}')
        lines.append('')
    lines.extend(f'- {module.name} — {module.source_hint}' for module in modules)
    return '\n'.join(lines)
```

This function first displays the total number of entries and then lists the (optionally filtered) modules with name and origin.

## 6.9 CommandExecution and ToolExecution: Shim Execution

### 6.9.1 The Dataclasses

Both modules each define an execution Dataclass:

```python
@dataclass(frozen=True)
class CommandExecution:
    name: str
    source_hint: str
    prompt: str
    handled: bool
    message: str
```

```python
@dataclass(frozen=True)
class ToolExecution:
    name: str
    source_hint: str
    payload: str
    handled: bool
    message: str
```

The difference lies in the third field: Commands receive a `prompt` (the user command), Tools a `payload` (the input data for the tool). Both are `frozen=True` -- the result of an execution is immutable.

### 6.9.2 The Execution Functions

```python
def execute_command(name: str, prompt: str = '') -> CommandExecution:
    module = get_command(name)
    if module is None:
        return CommandExecution(
            name=name, source_hint='', prompt=prompt,
            handled=False,
            message=f'Unknown mirrored command: {name}',
        )
    action = f"Mirrored command '{module.name}' from {module.source_hint} would handle prompt {prompt!r}."
    return CommandExecution(
        name=module.name, source_hint=module.source_hint,
        prompt=prompt, handled=True, message=action,
    )
```

The function does not actually execute the command -- it is a **shim**. A shim (literally: a thin wedge) is a placeholder that replicates the interface of the real implementation without possessing its functionality. Instead, it generates a descriptive message documenting what the real implementation would do.

The `handled` field indicates whether the command was known: `True` if a corresponding `PortingModule` was found, `False` for an unknown name. Callers can use this field to decide how to proceed -- for example, display an error message or trigger a fallback.

The function `execute_tool()` in `tools.py` follows the same pattern with `payload` instead of `prompt`.

This shim design fits the overall philosophy of Claw Code: The complete, functional re-implementation of all 391 modules would be an enormous effort. The shim approach allows mapping the **surface** of the system completely, while the actual logic can be ported incrementally.

## 6.10 ToolPermissionContext: The Permission System

### 6.10.1 The Data Structure

The file `src/permissions.py` defines a compact but powerful permission system in only 21 lines:

```python
@dataclass(frozen=True)
class ToolPermissionContext:
    deny_names: frozenset[str] = field(default_factory=frozenset)
    deny_prefixes: tuple[str, ...] = ()

    @classmethod
    def from_iterables(
        cls,
        deny_names: list[str] | None = None,
        deny_prefixes: list[str] | None = None,
    ) -> 'ToolPermissionContext':
        return cls(
            deny_names=frozenset(name.lower() for name in (deny_names or [])),
            deny_prefixes=tuple(prefix.lower() for prefix in (deny_prefixes or [])),
        )

    def blocks(self, tool_name: str) -> bool:
        lowered = tool_name.lower()
        return (lowered in self.deny_names
                or any(lowered.startswith(prefix)
                       for prefix in self.deny_prefixes))
```

### 6.10.2 Two Blocking Mechanisms

The `ToolPermissionContext` operates on the **deny-list principle**: Everything is permitted unless explicitly blocked. Two complementary mechanisms are available:

1. **`deny_names`**: A `frozenset` of exact tool names (in lowercase). If a tool name is contained in this set, it is blocked. Example: `frozenset({'bashtool', 'filewritetool'})` would block exactly these two tools.

2. **`deny_prefixes`**: A tuple of prefix strings (in lowercase). A tool is blocked if its name starts with one of these prefixes. Example: `('mcp_',)` would block all tools whose name begins with `mcp_` -- thus all MCP tools at once.

The choice of data types is deliberate: `frozenset` for `deny_names` provides O(1) membership tests and is immutable. `tuple` for `deny_prefixes` is immutable and sequentially searchable -- with typically few prefixes (one to three), the linear search with `any()` is entirely sufficient.

### 6.10.3 The `blocks()` Method

The central method `blocks()` combines both checks:

```python
def blocks(self, tool_name: str) -> bool:
    lowered = tool_name.lower()
    return (lowered in self.deny_names
            or any(lowered.startswith(prefix)
                   for prefix in self.deny_prefixes))
```

Here too, the check is case-insensitive. The name is converted to lowercase once and then checked against both lists. The short-circuit evaluation of `or` ensures that the prefix check is skipped if the name was already found in `deny_names`.

### 6.10.4 The Factory Class Method `from_iterables()`

The class method `from_iterables()` offers a convenient construction interface:

```python
ToolPermissionContext.from_iterables(
    deny_names=['BashTool', 'FileWriteTool'],
    deny_prefixes=['mcp_'],
)
```

It accepts regular lists and internally handles the normalization (lowercasing) and conversion into the correct container types. This means callers do not need to construct `frozenset` literals themselves.

### 6.10.5 Interaction with Tool Filtering

The function `filter_tools_by_permission_context()` in `tools.py` applies the context to a tool collection:

```python
def filter_tools_by_permission_context(
    tools: tuple[PortingModule, ...],
    permission_context: ToolPermissionContext | None = None,
) -> tuple[PortingModule, ...]:
    if permission_context is None:
        return tools
    return tuple(
        module for module in tools
        if not permission_context.blocks(module.name)
    )
```

If no permission context is specified (`None`), all tools are passed through -- a sensible default. Otherwise, each tool is individually checked against `blocks()` and only the non-blocked tools are included in the result tuple.

## 6.11 ToolPool: The Assembly of the Tool Pool

### 6.11.1 The `ToolPool` Dataclass

The file `src/tool_pool.py` defines the central abstraction for a concrete session tool set:

```python
@dataclass(frozen=True)
class ToolPool:
    tools: tuple[PortingModule, ...]
    simple_mode: bool
    include_mcp: bool

    def as_markdown(self) -> str:
        lines = [
            '# Tool Pool',
            '',
            f'Simple mode: {self.simple_mode}',
            f'Include MCP: {self.include_mcp}',
            f'Tool count: {len(self.tools)}',
        ]
        lines.extend(
            f'- {tool.name} — {tool.source_hint}'
            for tool in self.tools[:15]
        )
        return '\n'.join(lines)
```

The class bundles the result of the filtering with the parameters that led to that filtering. This is an example of the **Result-with-Context pattern**: The caller receives not only the filtered tools but also the metadata `simple_mode` and `include_mcp`, which document under what conditions the pool was created.

The method `as_markdown()` produces a compact representation that lists at most 15 tools -- sufficient for a quick overview without flooding the output.

### 6.11.2 The Assembly Function

```python
def assemble_tool_pool(
    simple_mode: bool = False,
    include_mcp: bool = True,
    permission_context: ToolPermissionContext | None = None,
) -> ToolPool:
    return ToolPool(
        tools=get_tools(
            simple_mode=simple_mode,
            include_mcp=include_mcp,
            permission_context=permission_context,
        ),
        simple_mode=simple_mode,
        include_mcp=include_mcp,
    )
```

The function `assemble_tool_pool()` is the central entry point for creating a tool pool. It delegates the actual filtering to `get_tools()` and wraps the result in a `ToolPool` instance. All three filter dimensions -- Simple Mode, MCP inclusion, and permission context -- are passed through.

A typical call might look like this:

```python
# Restricted environment: only base tools, no MCP, BashTool blocked
ctx = ToolPermissionContext.from_iterables(deny_names=['BashTool'])
pool = assemble_tool_pool(simple_mode=True, include_mcp=False, permission_context=ctx)
```

In this example, Simple Mode would reduce the 184 tools to three (`BashTool`, `FileReadTool`, `FileEditTool`), then the permission context would remove `BashTool` -- leaving only `FileReadTool` and `FileEditTool`.

## 6.12 Simple Mode: The Minimal Principle

Simple Mode deserves special attention, as it reflects a fundamental design decision. The three tools that remain in Simple Mode constitute the **irreducible core capability** of a code agent:

| Tool | Capability |
|------|-----------|
| `BashTool` | Execute shell commands |
| `FileReadTool` | Read files |
| `FileEditTool` | Edit files |

With these three tools, an agent can in principle accomplish any task -- albeit more laboriously than with specialized tools. `FileReadTool` replaces `Grep`, `Glob`, and every other read tool; `FileEditTool` replaces `Write` and every other write tool; `BashTool` replaces everything else.

Simple Mode is deliberately implemented as a **whitelist** -- it checks `module.name in {'BashTool', 'FileReadTool', 'FileEditTool'}`. This is robust against changes to the overall catalog: New tools are automatically excluded without requiring the Simple Mode logic to be adjusted.

## 6.13 Architectural Summary

The four files together form a three-layered architecture:


**Catalog Architecture (4 layers):**

| Layer | Module | Responsibility |
|-------|--------|---------------|
| Orchestration | `tool_pool.py` | `assemble_tool_pool()` → `ToolPool` |
| Catalog | `commands.py` / `tools.py` | `get_*`, `find_*`, `execute_*` |
| Access Control | `permissions.py` | `ToolPermissionContext.blocks()` |
| Data | `*_snapshot.json` | Static versioned reference data |


The lowest layer consists of the JSON snapshots -- static, versioned data. Above it lies the access control with its deny-list mechanism. The middle layer provides catalog services (lookup, filtering, search, shim execution). At the top, `tool_pool.py` orchestrates the assembly of a concrete tool pool for a session.

This layering ensures clear responsibilities: `permissions.py` knows nothing about JSON files, `tool_pool.py` knows nothing about substring matching in `source_hint` fields, and the snapshots know nothing at all -- they are pure data.

The decision to model 391 modules as reference data rather than executable code is the defining characteristic of this subsystem. It allows Claw Code to map the complete surface of Claude Code without bearing the enormous implementation effort of a 1:1 port. The shim mechanism in `execute_command()` and `execute_tool()` makes this strategy transparent: Every invocation is documented, and the `handled` field signals to the system that the command was recognized but only simulated.


# Chapter 7: The Runtime Environment

## 7.1 Introduction

The file `src/runtime.py` forms the heart of Claw Code. At 193 lines, it is deliberately kept compact, yet it unites all phases of a user interaction: from parsing the entered prompt through routing to matching commands and tools, executing those modules, streaming the results, all the way to persisting the entire session. One can think of `runtime.py` as the conductor of an orchestra -- the individual musicians (context building, setup, query engine, execution registry) play their parts, but only the runtime brings them into the correct order and ensures that the individual pieces become a coherent whole.

In this chapter, we analyze every component of the runtime in detail: the data structures `RoutedMatch` and `RuntimeSession`, the routing logic of the class `PortRuntime`, the complete session lifecycle in `bootstrap_session()`, and the multi-turn loop `run_turn_loop()`. At the end, a flow diagram visually summarizes the routing algorithm.

---

## 7.2 The Data Structure `RoutedMatch`

```python
@dataclass(frozen=True)
class RoutedMatch:
    kind: str
    name: str
    source_hint: str
    score: int
```

`RoutedMatch` is a frozen (immutable) Dataclass that represents a single routing result. Each time the runtime analyzes a prompt and determines that a particular command or tool might be relevant, a `RoutedMatch` object is created. The four fields carry the following meaning:

### 7.2.1 The Field `kind`

The field `kind` is a simple string that can take exactly one of two values: `'command'` or `'tool'`. This distinction is fundamental to the architecture of Claw Code. Commands are standalone actions that the user triggers -- such as starting a test, displaying a summary, or navigating the project structure. Tools, on the other hand, are utilities that the system uses internally -- for example a file reader, a Bash executor, or a Grep tool. The `kind` value later determines in which register the module is looked up and executed: Commands are resolved via `registry.command()`, tools via `registry.tool()`.

### 7.2.2 The Field `name`

The name of the matched module, i.e., the unique identifier under which the command or tool is registered in the system. This name comes directly from the associated `PortingModule` object and is used to find the module in the `ExecutionRegistry`. Examples would be `'grep'`, `'bash'`, `'read_file'`, or `'run_tests'`.

### 7.2.3 The Field `source_hint`

The `source_hint` indicates from which part of the original TypeScript source code this module was ported. It serves primarily for documentation and traceability: When a developer wants to know which original source underlies a particular Python module, they can consult the `source_hint`. In the Markdown output of `RuntimeSession.as_markdown()`, this field is appended to the module name with a dash, so that every routed match makes its origin transparent.

### 7.2.4 The Field `score`

The score is an integer rating indicating how many of the tokens extracted from the prompt were found in the module's metadata. A score of 3 means that three different prompt tokens appear in the module's name, source hint, or responsibility description. The higher the score, the more relevant the module is considered for the given prompt. The scoring mechanism is deliberately kept simple -- it is a token overlap procedure without weighting, TF-IDF, or semantic similarity. This simplicity is intentional: It makes the routing deterministic, easy to follow, and fast.

### 7.2.5 Why `frozen=True`?

The decision to declare `RoutedMatch` as a frozen Dataclass is a deliberate design choice. Routing results should not be modified after their creation. They are collected in lists, sorted, filtered, and passed to various locations -- from the `bootstrap_session()` method to the `ExecutionRegistry`, to the `QueryEnginePort`, and finally into the `RuntimeSession`. Immutability guarantees that a once-computed routing result remains consistent, regardless of how many consumers read it.

---

## 7.3 The Class `PortRuntime`

`PortRuntime` is the central class of the runtime environment. It has no constructor and no internal state -- it is a pure collection of methods that orchestrate the entire lifecycle of a session. One could describe it as a stateless service class.

### 7.3.1 `route_prompt(prompt, limit=5)` -- The Routing Algorithm

The method `route_prompt` is the heart of prompt routing. It takes a natural-language prompt and returns a list of `RoutedMatch` objects representing the most relevant commands and tools for that prompt.

#### Step 1: Tokenization

```python
tokens = {token.lower() for token in prompt.replace('/', ' ').replace('-', ' ').split() if token}
```

The prompt is first normalized: slashes (`/`) and hyphens (`-`) are replaced with spaces. Then the resulting string is split on whitespace. Each token is converted to lowercase, and empty strings are filtered out. The result is a `set` -- a collection without duplicates. This decision has two consequences: First, each token is counted only once, even if it appears multiple times in the prompt. Second, the order of tokens is irrelevant.

Why are `/` and `-` specifically treated as delimiters? Because in a CLI context, path specifications like `src/runtime` or compound terms like `query-engine` occur frequently. By breaking at these characters, the individual components (`src`, `runtime`, `query`, `engine`) become available as independent tokens and can be matched against module names.

#### Step 2: Scoring per Kind

```python
by_kind = {
    'command': self._collect_matches(tokens, PORTED_COMMANDS, 'command'),
    'tool': self._collect_matches(tokens, PORTED_TOOLS, 'tool'),
}
```

The tokenized prompt components are scored against two module collections: `PORTED_COMMANDS` and `PORTED_TOOLS`. Both are tuples of `PortingModule` objects loaded from JSON snapshot files on import and cached via `@lru_cache`. The method `_collect_matches()` (see Section 7.3.4) produces for each collection a list of `RoutedMatch` objects sorted in descending order by score.

#### Step 3: Selecting the Best Matches

```python
selected: list[RoutedMatch] = []
for kind in ('command', 'tool'):
    if by_kind[kind]:
        selected.append(by_kind[kind].pop(0))
```

This step is crucial and implements a kind of "fair-share strategy": From each category, the best match (the one with the highest score) is first selected and removed from the original list. This guarantees that the result contains at least one command and at least one tool -- provided matches exist in the respective category at all. This strategy prevents one category from completely crowding out the other. If, for example, five tools have high scores but only one command, without this logic the command might fall out of the final list.

#### Step 4: Filling Up with Remaining Matches

```python
leftovers = sorted(
    [match for matches in by_kind.values() for match in matches],
    key=lambda item: (-item.score, item.kind, item.name),
)
selected.extend(leftovers[: max(0, limit - len(selected))])
return selected[:limit]
```

All not-yet-selected matches from both categories are merged into a single list and sorted by three criteria: primarily by score (descending, hence the minus sign), secondarily by `kind` (alphabetically, where `'command'` comes before `'tool'`), and tertiarily by `name` (alphabetically, for deterministic ordering in case of ties). From this sorted remainder list, as many matches are taken as there is still room in the limit. The final truncation `selected[:limit]` ensures that never more than `limit` results are returned.

### 7.3.2 `_score(tokens, module)` -- The Scoring Function

```python
@staticmethod
def _score(tokens: set[str], module: PortingModule) -> int:
    haystacks = [module.name.lower(), module.source_hint.lower(), module.responsibility.lower()]
    score = 0
    for token in tokens:
        if any(token in haystack for haystack in haystacks):
            score += 1
    return score
```

The static method `_score` calculates the relevance of a single module for a given set of prompt tokens. It constructs a list of three "haystacks": the module's name, the source hint, and the responsibility description, each in lowercase. Then it iterates over all tokens and checks for each token whether it appears as a substring in at least one of the three haystacks. If so, the score is incremented by 1.

Some important details:

- **Substring matching, not exact matching:** The token `'run'` matches both `'runtime'` and `'run_tests'`. This increases the hit rate but can also lead to false-positive results. In practice, this behavior is desired, since users often type only parts of module names.
- **No weighting:** A match in the `name` field counts the same as a match in `responsibility`. One could argue that name matches should be more relevant, but simplicity of the algorithm was deliberately preferred here.
- **Set-based tokens:** Since `tokens` is a `set`, each token is counted at most once, even if it appears in all three haystacks. The maximum score of a module therefore equals the number of unique prompt tokens.

### 7.3.3 `_collect_matches(tokens, modules, kind)` -- Collecting All Matches

```python
def _collect_matches(self, tokens: set[str], modules: tuple[PortingModule, ...], kind: str) -> list[RoutedMatch]:
    matches: list[RoutedMatch] = []
    for module in modules:
        score = self._score(tokens, module)
        if score > 0:
            matches.append(RoutedMatch(kind=kind, name=module.name, source_hint=module.source_hint, score=score))
    matches.sort(key=lambda item: (-item.score, item.name))
    return matches
```

This method iterates over all modules of a category, computes the score for each, and collects those with a positive score in a list. Modules with a score of 0 -- i.e., those where not a single prompt token was found -- are immediately discarded. The resulting list is sorted by score (descending) and, in case of ties, by name (alphabetically ascending). This sorting is deterministic: Given an identical input prompt, `_collect_matches` always delivers the same ordering.

### 7.3.4 `_infer_permission_denials(matches)` -- Automatic Permission Denials

```python
def _infer_permission_denials(self, matches: list[RoutedMatch]) -> list[PermissionDenial]:
    denials: list[PermissionDenial] = []
    for match in matches:
        if match.kind == 'tool' and 'bash' in match.name.lower():
            denials.append(PermissionDenial(
                tool_name=match.name,
                reason='destructive shell execution remains gated in the Python port'
            ))
    return denials
```

This method implements a simple but important security rule: Every tool whose name contains the substring `'bash'` is automatically given a `PermissionDenial`. The rationale is that destructive shell executions should remain restricted in the Python port.

The `PermissionDenial` Dataclass (defined in `src/models.py`) consists of two fields: `tool_name` and `reason`. These denials are forwarded to the `QueryEnginePort`, which emits them in its stream as `permission_denial` events and returns them in the `TurnResult` as part of the `permission_denials` tuple.

Noteworthy is that the current implementation looks exclusively at the module name. There is no configuration file or database for permission rules -- the logic is hard-coded. This may suffice for the current state of the project, but it points to a future extension point: A rule-based or configurable permission layer would be a natural evolution.

---

## 7.4 `bootstrap_session(prompt, limit=5)` -- The Complete Session Lifecycle

The method `bootstrap_session` is the most extensive method in `runtime.py`. It orchestrates the entire lifecycle of a session in ten clearly delineated steps. Let us examine each individual step in detail:

### Step 1: `build_port_context()` -- Context Building

```python
context = build_port_context()
```

At the beginning, the project context is built. The function `build_port_context()` from `src/context.py` analyzes the workspace and creates a `PortContext` object with information such as the number of Python files, the availability of archives, and further metadata. This context is later stored in the `RuntimeSession` and can be output as Markdown via `render_context()`.

### Step 2: `run_setup(trusted=True)` -- Setup Execution

```python
setup_report = run_setup(trusted=True)
setup = setup_report.setup
```

The setup step performs the workspace initialization. The flag `trusted=True` signals that the environment is classified as trustworthy -- no additional security checks are performed. The `SetupReport` contains a `WorkspaceSetup` object with information about the Python version, the platform, and the configured test command. Additionally, `WorkspaceSetup` provides a method `startup_steps()` that returns the performed initialization steps as a list.

### Step 3: `QueryEnginePort.from_workspace()` -- Engine Initialization

```python
engine = QueryEnginePort.from_workspace()
```

The query engine is created via the class method `from_workspace()`. Internally, `build_port_manifest()` is called, which creates a `PortManifest` object. The engine receives an automatically generated session ID (UUID hex), an empty message list, a fresh `UsageSummary`, and an empty `TranscriptStore`.

### Step 4: History Logging and `route_prompt()`

```python
history = HistoryLog()
history.add('context', f'python_files={context.python_file_count}, archive_available={context.archive_available}')
history.add('registry', f'commands={len(PORTED_COMMANDS)}, tools={len(PORTED_TOOLS)}')
matches = self.route_prompt(prompt, limit=limit)
```

A `HistoryLog` is created and populated with the first entries: the number of Python files and archive availability from the context, as well as the number of registered commands and tools. Then `route_prompt()` is called to determine the most relevant modules for the given prompt. The result is a list of `RoutedMatch` objects.

### Step 5: `build_execution_registry()` -- Registry Construction

```python
registry = build_execution_registry()
```

The `ExecutionRegistry` is built. It contains a `MirroredCommand` object for each `PortingModule` entry in `PORTED_COMMANDS` and a `MirroredTool` object for each entry in `PORTED_TOOLS`. These wrapper objects each provide an `execute()` method that executes the actual command or tool and returns a message as a string.

### Step 6: Execution of All Matched Modules

```python
command_execs = tuple(
    registry.command(match.name).execute(prompt)
    for match in matches if match.kind == 'command' and registry.command(match.name)
)
tool_execs = tuple(
    registry.tool(match.name).execute(prompt)
    for match in matches if match.kind == 'tool' and registry.tool(match.name)
)
```

For each `RoutedMatch` with `kind == 'command'`, the corresponding command is looked up in the registry and executed. The same happens analogously for tools with `kind == 'tool'`. The results -- message strings -- are collected as tuples. Noteworthy is the double check: `registry.command(match.name)` is used both as a guard in the `if` condition and as the call target in `.execute()`. If a module were not found in the registry, it would be silently skipped.

### Step 7: Permission Denials and `stream_submit_message()`

```python
denials = tuple(self._infer_permission_denials(matches))
stream_events = tuple(engine.stream_submit_message(
    prompt,
    matched_commands=tuple(match.name for match in matches if match.kind == 'command'),
    matched_tools=tuple(match.name for match in matches if match.kind == 'tool'),
    denied_tools=denials,
))
```

The automatic permission denials are computed (see Section 7.3.4). Then `stream_submit_message()` is called on the query engine. This generator method emits a sequence of events: `message_start` (with session ID and prompt), optionally `command_match` and `tool_match` (with the names of matched modules), optionally `permission_denial` (with the names of denied tools), `message_delta` (with the formatted output text), and finally `message_stop` (with usage statistics and the stop reason). All events are materialized as a tuple and stored in the session.

### Step 8: `submit_message()` -- Synchronous Message Processing

```python
turn_result = engine.submit_message(
    prompt,
    matched_commands=tuple(match.name for match in matches if match.kind == 'command'),
    matched_tools=tuple(match.name for match in matches if match.kind == 'tool'),
    denied_tools=denials,
)
```

In addition to the stream, `submit_message()` is called, which returns a `TurnResult`. This contains the prompt, the formatted output, the matched commands and tools, the permission denials, the cumulative token usage, and the stop reason. It is important to note that `stream_submit_message()` internally also calls `submit_message()` -- so the prompt is effectively processed twice. This is a design aspect that possibly points to a planned decoupling of the stream and synchronous paths.

### Step 9: `persist_session()` -- Session Persistence

```python
persisted_session_path = engine.persist_session()
```

The engine flushes its transcript store and saves the entire session as a `StoredSession` via the session store. The returned path is stored as a string in the `RuntimeSession`, so the session can later be restored via `QueryEnginePort.from_saved_session()`.

### Step 10: Assembling the `RuntimeSession`

```python
return RuntimeSession(
    prompt=prompt,
    context=context,
    setup=setup,
    setup_report=setup_report,
    system_init_message=build_system_init_message(trusted=True),
    history=history,
    routed_matches=matches,
    turn_result=turn_result,
    command_execution_messages=command_execs,
    tool_execution_messages=tool_execs,
    stream_events=stream_events,
    persisted_session_path=persisted_session_path,
)
```

Finally, all collected information is merged into a `RuntimeSession` object and returned. Additionally, history entries for routing, execution, and the turn result are added. The system init message is also created with `trusted=True` and stored as a field in the session.

---

## 7.5 The Data Structure `RuntimeSession`

`RuntimeSession` is a non-frozen Dataclass with twelve fields that represents the complete state of a concluded session:

| Field | Type | Description |
|------|-----|--------------|
| `prompt` | `str` | The original user prompt |
| `context` | `PortContext` | The workspace context |
| `setup` | `WorkspaceSetup` | The workspace configuration |
| `setup_report` | `SetupReport` | The complete setup report |
| `system_init_message` | `str` | The system initialization message |
| `history` | `HistoryLog` | The chronological execution log |
| `routed_matches` | `list[RoutedMatch]` | The routing results |
| `turn_result` | `TurnResult` | The result of the message processing |
| `command_execution_messages` | `tuple[str, ...]` | The outputs of command executions |
| `tool_execution_messages` | `tuple[str, ...]` | The outputs of tool executions |
| `stream_events` | `tuple[dict[str, object], ...]` | The stream events |
| `persisted_session_path` | `str` | The storage path of the persisted session |

### 7.5.1 `as_markdown()` -- Human-Readable Output

The method `as_markdown()` transforms the entire session into a well-readable Markdown string. It begins with a heading and the prompt, followed by the rendered context. Then follow the setup information (Python version, implementation, platform, test command), the startup steps, the system init message, and the routing results.

For each `RoutedMatch`, a line in the format `- [kind] name (score) -- source_hint` is generated. If no matches are present, `- none` is output instead. Then come the command executions, tool executions, stream events (each with a type prefix), the turn result (as text output), the persisted session path, and finally the history as Markdown.

This method is particularly useful for debugging, logging, and transparency: A developer can at any time have the complete execution flow of a session output as a Markdown document and thus trace which modules were routed and executed, which events were streamed, and what the token usage looked like.

---

## 7.6 `run_turn_loop(prompt, limit, max_turns, structured_output)` -- The Multi-Turn Loop

```python
def run_turn_loop(self, prompt: str, limit: int = 5, max_turns: int = 3,
                  structured_output: bool = False) -> list[TurnResult]:
    engine = QueryEnginePort.from_workspace()
    engine.config = QueryEngineConfig(max_turns=max_turns, structured_output=structured_output)
    matches = self.route_prompt(prompt, limit=limit)
    command_names = tuple(match.name for match in matches if match.kind == 'command')
    tool_names = tuple(match.name for match in matches if match.kind == 'tool')
    results: list[TurnResult] = []
    for turn in range(max_turns):
        turn_prompt = prompt if turn == 0 else f'{prompt} [turn {turn + 1}]'
        result = engine.submit_message(turn_prompt, command_names, tool_names, ())
        results.append(result)
        if result.stop_reason != 'completed':
            break
    return results
```

While `bootstrap_session()` runs through a single round (a single "turn"), `run_turn_loop()` enables the execution of multiple consecutive rounds with the same prompt. This is relevant for iterative tasks where the system needs multiple passes to complete a task.

### 7.6.1 Initialization

A fresh `QueryEnginePort` is created, and its configuration is overwritten by a new `QueryEngineConfig` object with the passed `max_turns` and `structured_output` parameters. The routing is performed once -- the matched commands and tools remain constant across all turns.

### 7.6.2 The Loop

The loop iterates from `0` to `max_turns - 1`. In the first turn, the original prompt is used. From the second turn onward, the prompt is extended with a suffix `[turn N]`, where `N` is the 1-based turn number. Each turn result is added to the results list.

### 7.6.3 Stop Conditions

The loop has three stop conditions:

1. **`max_turns` reached:** When the loop has completed all planned turns, it ends naturally. This is the implicit termination via the `range()` bound.
2. **Stop reason other than `'completed'`:** If a `TurnResult` has a `stop_reason` that is not `'completed'`, the loop is terminated early. Possible reasons are `'max_turns_reached'` (the engine has reached its internal turn limit) or `'max_budget_reached'` (the token budget would be exceeded).
3. **Implicit budget limit:** Within the `QueryEnginePort`, `submit_message()` checks whether the projected token usage exceeds the configured `max_budget_tokens`. If so, the `stop_reason` is set to `'max_budget_reached'`, which leads to termination in the next loop iteration.

Noteworthy is that `run_turn_loop()` does not pass permission denials to the engine (the last argument is an empty tuple `()`). This distinguishes the turn loop from `bootstrap_session()`, where `_infer_permission_denials()` is explicitly called. This may be a deliberate simplification or an area that will be extended in future versions.

### 7.6.4 Return Value

The method returns a list of all `TurnResult` objects. The caller can determine from this how many turns were actually executed, what the respective output was, and why the loop ended.

---

## 7.7 Flow Diagram of the Routing Algorithm

The following diagram shows the complete flow of `route_prompt()` as a text flow chart:


**Scoring Algorithm Detail:**

For each token from the prompt set:
1. Check if token appears in `module.name` → if yes: score += 1
2. Check if token appears in `module.source_hint` → if yes: already counted
3. Check if token appears in `module.responsibility` → if yes: already counted

> Note: `any()` ensures each token is counted at most once per module.


### Scoring Detail (`_score`):


**Scoring Algorithm Detail:**

For each token from the prompt set:
1. Check if token appears in `module.name` → if yes: score += 1
2. Check if token appears in `module.source_hint` → if yes: already counted
3. Check if token appears in `module.responsibility` → if yes: already counted

> Note: `any()` ensures each token is counted at most once per module.


---

## 7.8 Interaction of Components

The runtime functions as the central integration point of the entire Claw Code system. The following overview shows the dependencies:

- **`src/context.py`** provides the `PortContext` (workspace metadata)
- **`src/setup.py`** provides `SetupReport` and `WorkspaceSetup` (platform/Python information)
- **`src/commands.py`** provides `PORTED_COMMANDS` (tuple of `PortingModule` from JSON snapshot)
- **`src/tools.py`** provides `PORTED_TOOLS` (tuple of `PortingModule` from JSON snapshot)
- **`src/models.py`** defines the core data types `PortingModule`, `PermissionDenial`, `UsageSummary`
- **`src/query_engine.py`** provides `QueryEnginePort` (message engine with session management)
- **`src/execution_registry.py`** provides `ExecutionRegistry` (lookup and execution of modules)
- **`src/system_init.py`** provides the system initialization message
- **`src/history.py`** provides `HistoryLog` (chronological execution log)

The runtime itself defines only two data types (`RoutedMatch`, `RuntimeSession`) and one class (`PortRuntime`) with five methods. Its complexity lies not in its own code but in the orchestration of the named subsystems.

---

## 7.9 Design Decisions and Critical Assessment

### Statelessness of `PortRuntime`

The class `PortRuntime` has no constructor and no internal state. Each method creates its own dependencies as needed (e.g., `QueryEnginePort.from_workspace()`). This makes the class easy to test and use, but also means that with each session creation, all dependencies are rebuilt.

### Double Message Processing in `bootstrap_session()`

The prompt is processed through both `stream_submit_message()` and `submit_message()`. Since `stream_submit_message()` internally calls `submit_message()`, the prompt is actually submitted to the engine twice. This leads to a double state mutation (messages are appended twice, usage is updated twice). For production use, decoupling would be advisable here.

### Simplicity of the Scoring Algorithm

The token-overlap approach is deliberately simple. It works well for short, keyword-like prompts but can reach its limits with longer natural-language inputs: A prompt like "I would like to read the files in the directory" would contain many stop words that rarely appear in module names. A possible extension would be a stop-word list or a weighting based on the field in which the match was found.

### Missing Permission Denials in `run_turn_loop()`

As already mentioned, `run_turn_loop()` passes an empty tuple for `denied_tools`. This means that in the multi-turn loop, even Bash tools could be executed without denial. Depending on security requirements, this could be intentional behavior or an open issue.

---

## 7.10 Summary

The file `src/runtime.py` is the hub of Claw Code. With only 193 lines, it orchestrates the entire lifecycle of a user session: from parsing the prompt through a simple but effective token-based routing, the execution of matched modules, the streaming of results, synchronous message processing, all the way to persistence. The `RoutedMatch` Dataclass bridges routing and execution, the `RuntimeSession` Dataclass collects all artifacts of a session, and the `PortRuntime` class ties everything together. The multi-turn loop `run_turn_loop()` extends the basic model with iterative processing and configurable termination conditions. The design consistently favors simplicity and transparency over abstraction -- a philosophy that runs through the entire Claw Code project.


# Chapter 8: The Query Engine

## 8.1 Introduction

The Query Engine forms the heart of the interaction layer of Claw Code. It is the central component that receives incoming user prompts, matches them against registered commands and tools, monitors token consumption, logs permission denials, and ultimately returns a structured result. In doing so, it follows a clear architectural approach: The engine strictly separates the stateful conversation logic (the "Port") from the overlying runtime layer (the "Runtime"), which handles the actual routing.

This chapter analyzes three source files that together form the entire query engine subsystem:

- **`src/query_engine.py`** (194 lines) -- contains the configuration, the data class for turn results, and the complete `QueryEnginePort` class
- **`src/QueryEngine.py`** (20 lines) -- defines the `QueryEngineRuntime` subclass with its `route()` method
- **`src/transcript.py`** (24 lines) -- implements the `TranscriptStore`, which manages the conversation transcript

We will go through each of these components in detail, explain their interconnection, and illustrate with sequence diagrams how messages flow through the system.

---

## 8.2 QueryEngineConfig -- The Configuration Class

The entire behavioral control of the Query Engine is governed by a single, immutable data class (`frozen=True`):

```python
@dataclass(frozen=True)
class QueryEngineConfig:
    max_turns: int = 8
    max_budget_tokens: int = 2000
    compact_after_turns: int = 12
    structured_output: bool = False
    structured_retry_limit: int = 2
```

### 8.2.1 The Individual Parameters

**`max_turns = 8`**

This parameter defines the maximum number of conversation rounds (turns) that a single session may undergo. As soon as the length of `mutable_messages` reaches or exceeds this value, no new turn is processed. Instead, `submit_message()` immediately returns a `TurnResult` with the `stop_reason` `'max_turns_reached'`. The value 8 is deliberately chosen conservatively: It permits a substantial conversation but prevents endless loops that can occur with automated agents.

**`max_budget_tokens = 2000`**

This token budget limits the cumulative consumption of a session. The calculation is performed via the method `UsageSummary.add_turn()`, which uses a simplified word-based estimate (`len(text.split())`). If the sum of `input_tokens` and `output_tokens` after a turn exceeds 2000, the `stop_reason` is set to `'max_budget_reached'`. Important: The turn is still executed -- the budget acts as a soft limit, not a hard block. Only the next turn would be prevented by the `max_turns` check or an explicit check by the caller.

**`compact_after_turns = 12`**

This value controls the compaction strategy. When the number of stored messages exceeds `compact_after_turns` (i.e., more than 12 entries are present), the older entries are discarded and only the last `compact_after_turns` messages are retained. Note the apparent contradiction: `max_turns` is 8, but `compact_after_turns` is 12. This is not a bug -- a session can be restored via `from_saved_session()` with an already populated message history, and compaction should also take effect in those cases. The compaction affects both `mutable_messages` and the `TranscriptStore`.

**`structured_output = False`**

By default, the engine produces simple text output (line-by-line separated by newlines). If `structured_output` is set to `True`, the engine serializes the summary as a JSON object with the keys `summary` and `session_id`. This option is particularly useful when a downstream system needs to parse the output programmatically.

**`structured_retry_limit = 2`**

If JSON serialization fails (for example due to non-serializable objects in the payload), the engine attempts up to `structured_retry_limit` times to produce a sanitized fallback output. With each failed attempt, the payload is reduced to minimal content (`{'summary': ['structured output retry'], 'session_id': ...}`). If the last attempt also fails, a `RuntimeError` is raised.

### 8.2.2 Design Decision: Why `frozen=True`?

The configuration is implemented as a frozen data class. This means: Once created, no attribute can be changed. This decision has two advantages. First: Thread safety. Even though the current system is not explicitly multithreaded, immutability guarantees that a configuration can be safely shared between multiple components. Second: Clarity of responsibility. Configuration changes require the creation of a new instance, which is explicit and traceable in the code.

---

## 8.3 TurnResult -- The Result of a Turn

Every call to `submit_message()` returns a `TurnResult` that encapsulates the complete state of that one processing step:

```python
@dataclass(frozen=True)
class TurnResult:
    prompt: str
    output: str
    matched_commands: tuple[str, ...]
    matched_tools: tuple[str, ...]
    permission_denials: tuple[PermissionDenial, ...]
    usage: UsageSummary
    stop_reason: str
```

### 8.3.1 Fields in Detail

**`prompt`** stores the original prompt that was fed into this turn. This allows downstream systems to associate the result with its trigger without having to carry the context separately.

**`output`** contains the formatted summary of the turn. Depending on the `structured_output` setting, this is either a multi-line string or a JSON document.

**`matched_commands`** and **`matched_tools`** are tuples of strings indicating which registered commands or tools matched the prompt. These are not computed by the engine itself but passed in by the caller -- the engine merely records them.

**`permission_denials`** is a tuple of `PermissionDenial` objects. Each object contains a `tool_name` and a `reason`. This data structure documents which tools were requested but denied for permission reasons -- a central security feature.

**`usage`** is a `UsageSummary` instance with the fields `input_tokens` and `output_tokens`, reflecting the cumulative token consumption of the entire session up to and including this turn.

**`stop_reason`** is a string with one of three possible values:

| Value | Meaning |
|------|-----------|
| `'completed'` | The turn was completed normally |
| `'max_turns_reached'` | The maximum number of allowed turns had already been reached |
| `'max_budget_reached'` | The token budget was exceeded with this turn |

`TurnResult` is also `frozen=True` -- a turn result is an immutable record and should not be manipulable after the fact.

---

## 8.4 The QueryEnginePort Class

`QueryEnginePort` is the central, stateful class of the Query Engine. The name "Port" follows the Ports-and-Adapters pattern (Hexagonal Architecture): The class defines the interface to the outside world without itself making the concrete routing decisions.

### 8.4.1 Fields

```python
@dataclass
class QueryEnginePort:
    manifest: PortManifest
    config: QueryEngineConfig = field(default_factory=QueryEngineConfig)
    session_id: str = field(default_factory=lambda: uuid4().hex)
    mutable_messages: list[str] = field(default_factory=list)
    permission_denials: list[PermissionDenial] = field(default_factory=list)
    total_usage: UsageSummary = field(default_factory=UsageSummary)
    transcript_store: TranscriptStore = field(default_factory=TranscriptStore)
```

**`manifest`** is a `PortManifest` instance that describes the current state of the workspace (which modules are ported, which are still open, etc.). It is the only field without a default value and must be specified at creation.

**`config`** is the `QueryEngineConfig` described above. Through the `default_factory`, each new engine instance automatically receives the default configuration with `max_turns=8` and `max_budget_tokens=2000`.

**`session_id`** is generated via `uuid4().hex` -- a 32-character hex string without hyphens. Each new session receives a unique identifier that serves as the key for persistence and restoration.

**`mutable_messages`** is the central message list. Unlike the frozen data classes, this list is deliberately mutable -- it grows with each turn by one entry and is compacted as needed.

**`permission_denials`** collects all permission denials over the entire lifetime of the session.

**`total_usage`** accumulates the token consumption. Since `UsageSummary` itself is `frozen=True`, a new object is created and assigned with each turn.

**`transcript_store`** is an instance of `TranscriptStore`, which is maintained in parallel with `mutable_messages` but additionally possesses a `flushed` status and has its own methods for compaction and replay.

### 8.4.2 Factory Method: from_workspace()

```python
@classmethod
def from_workspace(cls) -> 'QueryEnginePort':
    return cls(manifest=build_port_manifest())
```

This method creates a completely new session. It calls `build_port_manifest()` to capture the current workspace state and leaves all other fields to their default values. The result is a fresh engine with a new `session_id`, empty message lists, and zero consumption.

### 8.4.3 Factory Method: from_saved_session(session_id)

```python
@classmethod
def from_saved_session(cls, session_id: str) -> 'QueryEnginePort':
    stored = load_session(session_id)
    transcript = TranscriptStore(entries=list(stored.messages), flushed=True)
    return cls(
        manifest=build_port_manifest(),
        session_id=stored.session_id,
        mutable_messages=list(stored.messages),
        total_usage=UsageSummary(stored.input_tokens, stored.output_tokens),
        transcript_store=transcript,
    )
```

This method restores a previously saved session. The procedure:

1. `load_session(session_id)` reads a `StoredSession` object from the file system (by default from `.port_sessions/`).
2. A `TranscriptStore` is initialized with the stored messages and marked as already `flushed` -- after all, the data originates from an already persisted source.
3. The `mutable_messages` and `total_usage` are reconstructed from the stored session.
4. A new `PortManifest` is created, since the workspace may have changed since the last save.

An important detail: The `permission_denials` are not restored. They are lost during saving, since `StoredSession` does not contain them. This is a deliberate design decision -- permission denials are transient and only relevant for the current session.

### 8.4.4 submit_message() -- The Core Method

`submit_message()` is the most important method of the entire Query Engine. It implements the complete processing cycle of a single turn:

```python
def submit_message(
    self,
    prompt: str,
    matched_commands: tuple[str, ...] = (),
    matched_tools: tuple[str, ...] = (),
    denied_tools: tuple[PermissionDenial, ...] = (),
) -> TurnResult:
```

The procedure is divided into eight clearly separated steps:

**Step 1: Check max turns**

```python
if len(self.mutable_messages) >= self.config.max_turns:
    output = f'Max turns reached before processing prompt: {prompt}'
    return TurnResult(
        prompt=prompt,
        output=output,
        matched_commands=matched_commands,
        matched_tools=matched_tools,
        permission_denials=denied_tools,
        usage=self.total_usage,
        stop_reason='max_turns_reached',
    )
```

This step serves as a circuit breaker. If the message list already contains `max_turns` entries, a `TurnResult` with `stop_reason='max_turns_reached'` is immediately returned without further processing the prompt. Noteworthy: The prompt is embedded in the `output` field so that the caller knows which prompt could not be processed.

**Step 2: Format summary**

```python
summary_lines = [
    f'Prompt: {prompt}',
    f'Matched commands: {", ".join(matched_commands) if matched_commands else "none"}',
    f'Matched tools: {", ".join(matched_tools) if matched_tools else "none"}',
    f'Permission denials: {len(denied_tools)}',
]
output = self._format_output(summary_lines)
```

Here the four core aspects of the turn -- prompt, commands, tools, and denials -- are translated into a human-readable summary. The `_format_output()` method then decides, based on `self.config.structured_output`, whether the output is rendered as plaintext or as JSON.

**Step 3: Estimate token consumption**

```python
projected_usage = self.total_usage.add_turn(prompt, output)
```

The `add_turn()` method of the `UsageSummary` class computes a simplified token estimate based on word count. The resulting `projected_usage` contains the cumulative consumption including the current turn.

**Step 4: Check budget**

```python
stop_reason = 'completed'
if projected_usage.input_tokens + projected_usage.output_tokens > self.config.max_budget_tokens:
    stop_reason = 'max_budget_reached'
```

Unlike the `max_turns` check, the budget check does not block the turn. The turn is fully executed, but the `stop_reason` is set to `'max_budget_reached'` to signal to the caller that no further turns should be submitted.

**Step 5: Append to mutable_messages**

```python
self.mutable_messages.append(prompt)
```

The prompt is added to the internal message list. Only the prompt is stored, not the output -- the message list represents the history of user inputs.

**Step 6: Append to transcript_store**

```python
self.transcript_store.append(prompt)
self.permission_denials.extend(denied_tools)
self.total_usage = projected_usage
```

In parallel with the message list, the prompt is also stored in the transcript. Permission denials are added to the cumulative list, and the token consumption is updated.

**Step 7: compact_messages_if_needed()**

```python
self.compact_messages_if_needed()
```

After appending, a check is made whether compaction is needed (details in Section 8.4.6).

**Step 8: Return TurnResult**

```python
return TurnResult(
    prompt=prompt,
    output=output,
    matched_commands=matched_commands,
    matched_tools=matched_tools,
    permission_denials=denied_tools,
    usage=self.total_usage,
    stop_reason=stop_reason,
)
```

The result is returned as an immutable `TurnResult`.

#### Sequence Diagram: submit_message()

```
Aufrufer            QueryEnginePort         TranscriptStore       UsageSummary
   |                      |                       |                    |
   |--- submit_message -->|                       |                    |
   |   (prompt, cmds,     |                       |                    |
   |    tools, denials)   |                       |                    |
   |                      |                       |                    |
   |                      |-- len(messages)       |                    |
   |                      |   >= max_turns?       |                    |
   |                      |   [Ja] -> Return      |                    |
   |                      |   [Nein] -> weiter    |                    |
   |                      |                       |                    |
   |                      |-- _format_output() -->|                    |
   |                      |   (summary_lines)     |                    |
   |                      |<-- output ------------|                    |
   |                      |                       |                    |
   |                      |-- add_turn() -------->|-------------------->|
   |                      |                       |    projected_usage  |
   |                      |<-------------------------------------------+
   |                      |                       |                    |
   |                      |-- Budget prüfen       |                    |
   |                      |   (projected > max?)  |                    |
   |                      |                       |                    |
   |                      |-- messages.append()   |                    |
   |                      |                       |                    |
   |                      |-- append(prompt) ---->|                    |
   |                      |                       |                    |
   |                      |-- compact_messages -->|                    |
   |                      |      _if_needed()     |-- compact() ------>|
   |                      |                       |                    |
   |<-- TurnResult -------|                       |                    |
   |                      |                       |                    |
```

### 8.4.5 stream_submit_message() -- The Streaming Generator

In addition to the synchronous `submit_message()`, the engine offers a generator for incremental output:

```python
def stream_submit_message(
    self,
    prompt: str,
    matched_commands: tuple[str, ...] = (),
    matched_tools: tuple[str, ...] = (),
    denied_tools: tuple[PermissionDenial, ...] = (),
):
    yield {'type': 'message_start', 'session_id': self.session_id, 'prompt': prompt}
    if matched_commands:
        yield {'type': 'command_match', 'commands': matched_commands}
    if matched_tools:
        yield {'type': 'tool_match', 'tools': matched_tools}
    if denied_tools:
        yield {'type': 'permission_denial', 'denials': [d.tool_name for d in denied_tools]}
    result = self.submit_message(prompt, matched_commands, matched_tools, denied_tools)
    yield {'type': 'message_delta', 'text': result.output}
    yield {
        'type': 'message_stop',
        'usage': {'input_tokens': result.usage.input_tokens,
                  'output_tokens': result.usage.output_tokens},
        'stop_reason': result.stop_reason,
        'transcript_size': len(self.transcript_store.entries),
    }
```

The generator emits up to six events in a fixed order:

1. **`message_start`** -- Contains the `session_id` and the prompt. Always emitted.
2. **`command_match`** -- Contains the recognized commands. Only emitted when `matched_commands` is not empty.
3. **`tool_match`** -- Contains the recognized tools. Only emitted when `matched_tools` is not empty.
4. **`permission_denial`** -- Contains the names of denied tools (only the `tool_name` fields, not the full `PermissionDenial` objects). Only emitted when `denied_tools` is not empty.
5. **`message_delta`** -- Contains the formatted output text. Always emitted.
6. **`message_stop`** -- Contains token consumption, stop reason, and transcript size. Always emitted.

This pattern is modeled after the Server-Sent-Events architecture, as commonly used with streaming APIs. It allows a frontend or a downstream agent to react incrementally to the individual phases of processing, instead of having to wait for the complete result.

#### Sequence Diagram: stream_submit_message()

```
Aufrufer            stream_submit_message()        submit_message()
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- message_start -------|                          |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- command_match --------|  (falls vorhanden)      |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- tool_match -----------|  (falls vorhanden)      |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- permission_denial ----|  (falls vorhanden)      |
   |                          |                          |
   |--- next() ------------->|                          |
   |                          |--- submit_message() --->|
   |                          |<-- TurnResult ----------|
   |<-- message_delta --------|                          |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- message_stop ---------|                          |
   |                          |                          |
   |--- next() ------------->|                          |
   |<-- StopIteration -------|                          |
```

A noteworthy detail: The actual `submit_message()` logic is only executed when the consumer of the generator requests the fifth element (`message_delta`). The first three to four events are emitted without side effects. This means: If a consumer aborts the generator after `message_start`, no state mutation occurs -- the session remains unchanged.

### 8.4.6 compact_messages_if_needed()

```python
def compact_messages_if_needed(self) -> None:
    if len(self.mutable_messages) > self.config.compact_after_turns:
        self.mutable_messages[:] = self.mutable_messages[-self.config.compact_after_turns:]
    self.transcript_store.compact(self.config.compact_after_turns)
```

This method implements a sliding-window strategy. If the message list contains more than `compact_after_turns` entries, all entries except the last `compact_after_turns` are discarded. The assignment `self.mutable_messages[:] = ...` ensures that the in-place modification of the existing list occurs, rather than creating a new list. This is important in case other parts of the system hold a reference to the same list.

Subsequently, the `TranscriptStore` is also compacted, using the same `compact_after_turns` value as the `keep_last` parameter. This symmetry ensures that `mutable_messages` and `transcript_store.entries` always contain the same subset of the conversation history.

### 8.4.7 persist_session()

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(
        StoredSession(
            session_id=self.session_id,
            messages=tuple(self.mutable_messages),
            input_tokens=self.total_usage.input_tokens,
            output_tokens=self.total_usage.output_tokens,
        )
    )
    return str(path)
```

The persistence follows a two-step process:

1. **Flush transcript**: By calling `self.flush_transcript()`, `transcript_store.flushed` is set to `True`. This signals that all entries have been secured.

2. **Save session**: A `StoredSession` object is created and stored in the file system via `save_session()`. What is saved: the `session_id`, the messages as an immutable tuple, and the token counters. The return value is the path to the created file.

Not saved are: the `QueryEngineConfig`, the `PortManifest`, and the `permission_denials`. The configuration is recreated with default values upon restoration, the manifest is freshly read from the workspace, and the permission denials are -- as already explained -- transient.

### 8.4.8 render_summary()

```python
def render_summary(self) -> str:
```

This method produces a Markdown-formatted overview report of the current state of the engine. The report includes:

- The workspace manifest (via `self.manifest.to_markdown()`)
- The size of the command and tool backlogs (up to 10 summary lines each)
- The session ID
- The number of stored conversation rounds
- The number of logged permission denials
- The token consumption values
- The configuration parameters `max_turns` and `max_budget_tokens`
- The flush status of the transcript

This report is primarily intended for diagnostic purposes -- it gives developers and operators a quick overview of the state of a running or restored session.

### 8.4.9 Private Helper Methods

**`_format_output(summary_lines)`** is the switch between plaintext and structured output. With `structured_output=False`, the lines are simply joined with newlines. With `structured_output=True`, a dictionary is created and passed to `_render_structured_output()`.

**`_render_structured_output(payload)`** attempts up to `structured_retry_limit` times to serialize the payload as JSON. In case of failure, the payload is reduced to a minimum and retried. This pattern is defensive, but in practice `json.dumps()` is nearly failure-proof with dictionaries containing strings and lists. The defensive code protects against the case where non-serializable objects enter the payload through a programming error.

---

## 8.5 TranscriptStore -- The Conversation Transcript

```python
@dataclass
class TranscriptStore:
    entries: list[str] = field(default_factory=list)
    flushed: bool = False
```

The `TranscriptStore` is a lean but conceptually important class with only four methods:

### 8.5.1 append(entry)

```python
def append(self, entry: str) -> None:
    self.entries.append(entry)
    self.flushed = False
```

Adds an entry and sets `flushed` to `False`. This flag is the central coordination feature: It indicates whether new, not-yet-persisted entries have been added since the last `flush()`.

### 8.5.2 compact(keep_last=10)

```python
def compact(self, keep_last: int = 10) -> None:
    if len(self.entries) > keep_last:
        self.entries[:] = self.entries[-keep_last:]
```

Retains only the last `keep_last` entries. As with `mutable_messages`, the assignment is done in-place. The default value of 10 is in practice overridden by the `compact_after_turns` value from the configuration.

### 8.5.3 replay()

```python
def replay(self) -> tuple[str, ...]:
    return tuple(self.entries)
```

Returns all entries as an immutable tuple. This method is exposed by `QueryEnginePort.replay_user_messages()` and allows external systems to review the conversation history without mutating the internal list.

### 8.5.4 flush()

```python
def flush(self) -> None:
    self.flushed = True
```

Marks the transcript as persisted. The method deliberately does not delete any entries -- it only sets the flag. The actual writing to disk is performed by `QueryEnginePort.persist_session()`, which calls `flush()` as preparation.

### 8.5.5 The flushed Flag as a State Indicator

The `flushed` flag implements minimalistic dirty tracking: `False` means "there are unsaved changes", `True` means "everything is persisted". This flag is displayed in `render_summary()` and could be used by a future auto-save logic to avoid unnecessary write operations.

#### Sequence Diagram: Lifecycle of the TranscriptStore

```
QueryEnginePort              TranscriptStore             Dateisystem
      |                            |                          |
      |-- new TranscriptStore ---->|                          |
      |                     entries=[], flushed=False         |
      |                            |                          |
      |-- submit_message #1 ------>|                          |
      |      append("prompt1")     |                          |
      |                     entries=["p1"], flushed=False      |
      |                            |                          |
      |-- submit_message #2 ------>|                          |
      |      append("prompt2")     |                          |
      |                     entries=["p1","p2"], flushed=False |
      |                            |                          |
      |-- persist_session() ------>|                          |
      |      flush()               |                          |
      |                     entries=["p1","p2"], flushed=True  |
      |                            |                          |
      |-- save_session() -------->|---------------------------->|
      |                            |              session.json  |
      |                            |                          |
      |-- submit_message #3 ------>|                          |
      |      append("prompt3")     |                          |
      |                  entries=["p1","p2","p3"], flushed=False|
      |                            |                          |
```

---

## 8.6 QueryEngineRuntime -- The Routing Subclass

The file `src/QueryEngine.py` (note the capitalization -- a deliberate convention to distinguish the "public" API class from the internal Port class) defines the `QueryEngineRuntime`:

```python
class QueryEngineRuntime(QueryEnginePort):
    def route(self, prompt: str, limit: int = 5) -> str:
        matches = PortRuntime().route_prompt(prompt, limit=limit)
        lines = ['# Query Engine Route', '', f'Prompt: {prompt}', '']
        if not matches:
            lines.append('No mirrored command/tool matches found.')
            return '\n'.join(lines)
        lines.append('Matches:')
        lines.extend(
            f'- [{match.kind}] {match.name} ({match.score}) — {match.source_hint}'
            for match in matches
        )
        return '\n'.join(lines)
```

### 8.6.1 Inheritance and Responsibility

`QueryEngineRuntime` inherits from `QueryEnginePort` and extends it with a single method: `route()`. This gives it automatically all Port capabilities -- session management, turn processing, compaction, persistence -- and adds on top the ability to actively route a prompt against registered commands and tools.

### 8.6.2 The route() Method

The method takes a prompt and an optional limit (default: 5) and delegates the actual search to a `PortRuntime` instance. The routing in `PortRuntime.route_prompt()` performs a token-based search: The prompt is broken into tokens (slashes and hyphens are treated as delimiters), and these tokens are matched against the names of ported commands and tools.

The result is a list of `RoutedMatch` objects with the fields `kind` (either `'command'` or `'tool'`), `name`, `score`, and `source_hint`. These are returned as a Markdown-formatted string.

Noteworthy is that `PortRuntime()` is newly instantiated with each call to `route()`. There is no caching of the runtime instance. This is a deliberate tradeoff: Since the registered commands and tools can change between calls (for example through dynamic module loading), a cache would be potentially inconsistent.

### 8.6.3 Architectural Classification

The separation between `QueryEnginePort` and `QueryEngineRuntime` follows the Open/Closed Principle: The Port class is closed to modifications but open to extensions through subclasses. An alternative runtime could, for example, implement a different routing strategy without needing to touch the core turn-processing logic.

The `__all__` declaration in `QueryEngine.py` exports both classes:

```python
__all__ = ['QueryEnginePort', 'QueryEngineRuntime']
```

This signals that consumers of the module can use both the "raw" Port and the full Runtime.

---

## 8.7 Interaction of Components

### 8.7.1 Complete Lifecycle of a Session

The following sequence diagram shows the typical lifecycle of a query engine session from creation to persistence:

```
Aufrufer              QueryEngineRuntime         PortRuntime        TranscriptStore    Dateisystem
   |                        |                       |                    |                |
   |-- from_workspace() --->|                       |                    |                |
   |<-- neue Instanz -------|                       |                    |                |
   |   (session_id=abc123)  |                       |                    |                |
   |                        |                       |                    |                |
   |-- route("bash ls") --->|                       |                    |                |
   |                        |-- route_prompt() ---->|                    |                |
   |                        |<-- [RoutedMatch] -----|                    |                |
   |<-- Markdown-Report ----|                       |                    |                |
   |                        |                       |                    |                |
   |-- submit_message() --->|                       |                    |                |
   |   ("bash ls",          |                       |                    |                |
   |    cmds=("Bash",),     |                       |                    |                |
   |    tools=())           |                       |                    |                |
   |                        |-- append() ---------->|------------------>|                |
   |                        |-- compact() --------->|------------------>|                |
   |<-- TurnResult ---------|                       |                    |                |
   |   (stop_reason=        |                       |                    |                |
   |    'completed')        |                       |                    |                |
   |                        |                       |                    |                |
   |-- [... weitere Turns]  |                       |                    |                |
   |                        |                       |                    |                |
   |-- persist_session() -->|                       |                    |                |
   |                        |-- flush() ----------->|------------------>|                |
   |                        |-- save_session() ---->|------------------->|-- write() --->|
   |<-- Dateipfad ----------|                       |                    |                |
   |                        |                       |                    |                |
```

### 8.7.2 Restoration and Continuation

```
Aufrufer              QueryEngineRuntime         session_store       TranscriptStore
   |                        |                       |                    |
   |-- from_saved_session ->|                       |                    |
   |   (session_id=abc123)  |                       |                    |
   |                        |-- load_session() ---->|                    |
   |                        |<-- StoredSession -----|                    |
   |                        |                       |                    |
   |                        |-- new TranscriptStore |                    |
   |                        |   (entries=[...],     |------------------->|
   |                        |    flushed=True)      |                    |
   |<-- Instanz (restored) -|                       |                    |
   |                        |                       |                    |
   |-- submit_message() --->|                       |                    |
   |   (neuer Prompt)       |-- append() ---------->|------------------->|
   |                        |              flushed = False               |
   |<-- TurnResult ---------|                       |                    |
```

---

## 8.8 Error Handling and Robustness

### 8.8.1 Lines of Defense

The Query Engine implements several lines of defense against faulty or excessive usage:

1. **Turn limit**: Prevents endless loops by automated agents.
2. **Token budget**: Limits cumulative resource consumption.
3. **Compaction**: Prevents unbounded growth of the message history.
4. **Structured output retries**: Catches serialization errors.
5. **Frozen Dataclasses**: Prevents accidental mutation of configuration and results.

### 8.8.2 Soft vs. Hard Limits

The distinction between soft and hard limits is architecturally noteworthy:

- **`max_turns`** is a **hard limit**: Once reached, the turn is no longer processed.
- **`max_budget_tokens`** is a **soft limit**: The turn is still executed, but the `stop_reason` signals the exceedance. The responsibility to actually end the session lies with the caller.

This design gives the caller flexibility: They can react to a budget signal by ending the session, or they can -- if needed -- still perform a concluding "summary turn" before stopping.

---

## 8.9 Summary

The Query Engine of Claw Code is a well-thought-out subsystem that cleanly separates multiple responsibilities:

| Component | Responsibility | File |
|---|---|---|
| `QueryEngineConfig` | Immutable configuration | `query_engine.py` |
| `TurnResult` | Immutable turn result | `query_engine.py` |
| `QueryEnginePort` | Stateful session management | `query_engine.py` |
| `TranscriptStore` | Conversation transcript with dirty tracking | `transcript.py` |
| `QueryEngineRuntime` | Routing-capable extension | `QueryEngine.py` |

The architecture follows clearly recognizable principles: Hexagonal Architecture (Port/Adapter separation), Open/Closed (extensibility through inheritance), and Defensive Programming (retries, limits, frozen data classes). With merely 238 lines of code distributed across three files, the Query Engine provides a remarkably complete solution for the problem of controlled, budgeted, and logged conversation processing.

# Chapter 9: Session Management & Persistence

## Introduction

One of the central problems of any interactive application built on top of Large Language Models (LLMs) is the question: How do you preserve the state of a conversation beyond the boundaries of a single process lifecycle? Claw Code solves this problem through a three-layered persistence model consisting of the **Session Store**, the **History Log**, and the **Transcript Store**. Each of these layers fulfills a clearly delineated task: The Session Store serializes the complete message history along with token usage statistics to disk. The History Log maintains structured milestones of a running session in memory. And the Transcript Store acts as a compactable ring buffer for the chronological sequence of user inputs.

This chapter walks through the entire source code of the three modules `session_store.py`, `history.py`, and `transcript.py`, explains every class and every function in detail, and concludes by showing how the three layers interact within the complete session lifecycle.

---

## 9.1 The Session Store: `session_store.py`

### 9.1.1 The `StoredSession` Data Class

The heart of the persistence layer is the class `StoredSession`, defined as an immutable data class (`frozen=True`):

```python
@dataclass(frozen=True)
class StoredSession:
    session_id: str
    messages: tuple[str, ...]
    input_tokens: int
    output_tokens: int
```

The decision to use `frozen=True` is deliberate and architecturally significant. A stored session represents a **completed snapshot** -- a point in time at which the state of the conversation was frozen and written to disk. After a `StoredSession` has been created, no attribute may be changed. This protects against an entire class of bugs where an already persisted object is modified in memory after the fact, creating a discrepancy between the stored and actual state.

The four fields in detail:

**`session_id: str`** -- A unique identifier for the session. It is generated elsewhere (in `QueryEnginePort`) via `uuid4().hex`, which produces a 32-character hexadecimal string without hyphens. This identifier also serves as the filename on disk (with the `.json` extension appended), enabling a direct mapping between session object and file.

**`messages: tuple[str, ...]`** -- An immutable tuple of all messages exchanged during the session. The choice of a tuple instead of a list is consistent with the `frozen=True` semantics: Since the data class is immutable, a mutable `list` field would be technically possible (Python only checks assignment to the attribute, not mutation of its contents), but semantically misleading. A tuple signals unambiguously to the reader: "This message sequence is finalized."

**`input_tokens: int`** and **`output_tokens: int`** -- The cumulative token counters for the entire session. They are taken from the `UsageSummary` object that the `QueryEnginePort` maintains during message processing. These values are indispensable for budgeting decisions: When restoring a session, the engine can immediately see how many tokens have already been consumed and calculate its remaining budget accordingly.

### 9.1.2 The Default Directory

```python
DEFAULT_SESSION_DIR = Path('.port_sessions')
```

All sessions are stored by default in a directory named `.port_sessions` relative to the current working directory. The leading dot in the name follows the Unix convention for hidden directories and signals that this is internal data that is not part of the actual project. In a production environment, one would typically add this directory to the `.gitignore` file.

### 9.1.3 The `save_session` Function

```python
def save_session(session: StoredSession, directory: Path | None = None) -> Path:
    target_dir = directory or DEFAULT_SESSION_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f'{session.session_id}.json'
    path.write_text(json.dumps(asdict(session), indent=2))
    return path
```

This function handles the serialization of a `StoredSession` to disk. The flow is straightforward, but thoughtful at every step:

1. **Directory determination:** If no explicit directory is passed, the function falls back to `DEFAULT_SESSION_DIR`. Using the `or` operator instead of an explicit `if` block is idiomatic Python and covers both `None` and other falsy values.

2. **Directory creation:** The call `target_dir.mkdir(parents=True, exist_ok=True)` is defensively programmed. `parents=True` ensures that nested directory structures can be fully created -- for example, if `directory` is passed as `Path('data/sessions/archive')` and none of these directories exist. `exist_ok=True` prevents a `FileExistsError` if the directory already exists. This combination makes the call idempotent: it can be executed any number of times without producing errors.

3. **File path construction:** The path is assembled from the directory and the `session_id`, with the `.json` extension appended. By using the UUID as the filename, collisions are practically impossible.

4. **Serialization:** `dataclasses.asdict(session)` recursively converts the data class into a dictionary-like object. The `messages` tuple is automatically converted into a JSON list. `json.dumps(..., indent=2)` produces formatted JSON text that is also human-readable -- an important feature for debugging purposes.

5. **Return value:** The function returns the complete `Path` of the written file. This allows the caller to log or further process the path without having to reconstruct it.

### 9.1.4 The `load_session` Function

```python
def load_session(session_id: str, directory: Path | None = None) -> StoredSession:
    target_dir = directory or DEFAULT_SESSION_DIR
    data = json.loads((target_dir / f'{session_id}.json').read_text())
    return StoredSession(
        session_id=data['session_id'],
        messages=tuple(data['messages']),
        input_tokens=data['input_tokens'],
        output_tokens=data['output_tokens'],
    )
```

The counterpart to `save_session` reads a session back from disk by its ID. Notable here is the **explicit reconstruction** of the `StoredSession` object: Instead of passing the dictionary directly to the constructor (e.g., via `StoredSession(**data)`), the individual fields are extracted by name. This has three advantages:

First, `data['messages']` is explicitly converted to a `tuple`. JSON only knows arrays, which Python deserializes as `list`. To satisfy the type annotation `tuple[str, ...]` of the data class and preserve the immutability semantics, this conversion is necessary.

Second, the explicit mapping serves as a kind of "runtime schema validation": If the JSON file contains a missing field, Python throws a `KeyError` with the specific field name -- far more informative than a generic `TypeError` with `**data`.

Third, the method protects against unknown fields in the JSON file. If a future format contained additional fields, `StoredSession(**data)` would fail with a `TypeError` ("unexpected keyword argument"), while the explicit mapping simply ignores those fields.

### 9.1.5 The JSON Format on Disk

A saved session file has the following format:

```json
{
  "session_id": "a3f8c91b0e4d47f29a1c6e83d5b72f40",
  "messages": [
    "Erklaere mir die Architektur des Projekts",
    "Welche Module gibt es?"
  ],
  "input_tokens": 1247,
  "output_tokens": 583
}
```

This format is intentionally flat and simple. There is no nesting, no metadata envelopes, no versioning field. This follows the principle of simplicity: As long as the schema does not change, no overhead is necessary. Should a schema migration become necessary in the future, one could add a `"version"` field and extend the `load_session` function with migration logic.

---

## 9.2 The History Log: `history.py`

### 9.2.1 The `HistoryEvent` Data Class

```python
@dataclass(frozen=True)
class HistoryEvent:
    title: str
    detail: str
```

A `HistoryEvent` represents a single milestone within a session. It consists of a short title and a more detailed description text. Here too, `frozen=True` is set: Once a logged event is recorded, it is immutable. This property reflects reality -- past events cannot be modified retroactively.

The simplicity of this class is intentional. A `HistoryEvent` carries no timestamp, no priority, no categorization. It is a pure text building block whose semantics derive exclusively from the content of `title` and `detail`. The responsibility for adhering to naming conventions lies with the calling code.

### 9.2.2 The `HistoryLog` Class

```python
@dataclass
class HistoryLog:
    events: list[HistoryEvent] = field(default_factory=list)

    def add(self, title: str, detail: str) -> None:
        self.events.append(HistoryEvent(title=title, detail=detail))

    def as_markdown(self) -> str:
        lines = ['# Session History', '']
        lines.extend(f'- {event.title}: {event.detail}' for event in self.events)
        return '\n'.join(lines)
```

In contrast to `HistoryEvent`, `HistoryLog` is **mutable** -- it does not have `frozen=True`. This is necessary because the log grows continuously during the session.

**The `add` method** is a convenience function that creates a new `HistoryEvent` and appends it to the internal list. It takes `title` and `detail` as separate strings, rather than expecting a finished `HistoryEvent` object. This decoupling has the advantage that the calling code does not need to depend directly on the `HistoryEvent` class.

**The `as_markdown` method** serializes the entire log into a Markdown document. The format is deliberately simple: A first-level heading (`# Session History`), followed by a bullet list in which each event is formatted as `- title: detail`. This Markdown representation is used in the `as_markdown` method of `RuntimeSession`, where it is embedded as a section in the complete session report.

### 9.2.3 Usage in Practice

In the `PortRuntime.bootstrap_session` method (file `runtime.py`), the `HistoryLog` is populated at several points:

```python
history = HistoryLog()
history.add('context', f'python_files={context.python_file_count}, archive_available={context.archive_available}')
history.add('registry', f'commands={len(PORTED_COMMANDS)}, tools={len(PORTED_TOOLS)}')
history.add('routing', f'matches={len(matches)} for prompt={prompt!r}')
history.add('execution', f'command_execs={len(command_execs)} tool_execs={len(tool_execs)}')
history.add('turn', f'commands=... tools=... denials=... stop={turn_result.stop_reason}')
history.add('session_store', persisted_session_path)
```

One can see the convention: The `title` names the phase of the bootstrapping process (`context`, `registry`, `routing`, `execution`, `turn`, `session_store`), while `detail` contains the concrete metrics of that phase. In this way, a compact but informative protocol is created that is excellent for debugging and traceability. In the Markdown export, this would look like this, for example:

```markdown
# Session History

- context: python_files=42, archive_available=True
- registry: commands=7, tools=5
- routing: matches=3 for prompt='Erklaere die Architektur'
- execution: command_execs=1 tool_execs=2
- turn: commands=1 tools=2 denials=0 stop=completed
- session_store: .port_sessions/a3f8c91b0e4d47f29a1c6e83d5b72f40.json
```

---

## 9.3 The Transcript Store: `transcript.py`

### 9.3.1 Structure of the Class

```python
@dataclass
class TranscriptStore:
    entries: list[str] = field(default_factory=list)
    flushed: bool = False

    def append(self, entry: str) -> None:
        self.entries.append(entry)
        self.flushed = False

    def compact(self, keep_last: int = 10) -> None:
        if len(self.entries) > keep_last:
            self.entries[:] = self.entries[-keep_last:]

    def replay(self) -> tuple[str, ...]:
        return tuple(self.entries)

    def flush(self) -> None:
        self.flushed = True
```

The `TranscriptStore` is a specialized in-memory buffer that distinguishes itself from a simple list through three essential capabilities: **compaction**, **replay**, and **flush tracking**.

### 9.3.2 The `append` Method

Each new entry is appended to the end of the list. At the same time, the `flushed` flag is reset to `False`. This semantics is important: It signals that new data has been added since the last flush and the persisted version on disk may be outdated. In the context of the overall system, `append` is called within `QueryEnginePort.submit_message`, so that every processed message automatically ends up in the transcript.

### 9.3.3 The `compact` Method

```python
def compact(self, keep_last: int = 10) -> None:
    if len(self.entries) > keep_last:
        self.entries[:] = self.entries[-keep_last:]
```

The `compact` method implements a **sliding-window compaction**. When the number of entries exceeds `keep_last`, all entries except the last `keep_last` are discarded. The use of slice assignment `self.entries[:] = ...` instead of `self.entries = ...` is a subtle but important detail: Slice assignment **mutates the existing list in-place**, while a simple assignment would create a **new list** and replace the reference. In this case, the difference makes no semantic difference, since `entries` is a private field anyway. But the in-place mutation is consistent with the slice assignment also used in `QueryEnginePort.compact_messages_if_needed` for `mutable_messages`, and signals the intent: "We are modifying the content, not the identity."

Compaction is a response to a fundamental problem of LLM-based systems: the **context window**. The longer a conversation runs, the more tokens are consumed by historical messages, and the less room remains for new inputs and outputs. By discarding older entries, memory consumption is limited, while the most recent entries are preserved since they are typically the most relevant.

In the `QueryEnginePort`, compaction is controlled by `compact_messages_if_needed`:

```python
def compact_messages_if_needed(self) -> None:
    if len(self.mutable_messages) > self.config.compact_after_turns:
        self.mutable_messages[:] = self.mutable_messages[-self.config.compact_after_turns:]
    self.transcript_store.compact(self.config.compact_after_turns)
```

Here, both the message list and the `TranscriptStore` are compacted with the same `compact_after_turns` value (default: 12). This ensures that both data structures remain in sync.

### 9.3.4 The `replay` Method

```python
def replay(self) -> tuple[str, ...]:
    return tuple(self.entries)
```

`replay` returns an immutable copy of all current entries. The return as a tuple -- not a list -- is a deliberate design decision: The caller receives a snapshot that cannot be accidentally modified. In the `QueryEnginePort`, this method is exposed via `replay_user_messages` and allows passing the conversation so far to external consumers without endangering the internal data structure.

### 9.3.5 The `flush` Method

```python
def flush(self) -> None:
    self.flushed = True
```

`flush` merely sets a boolean flag. It does **not** delete any data and writes **nothing** to disk. Its function is purely signaling: "The current data has been processed by the caller." In the context of the `QueryEnginePort`, `flush` is called immediately before persistence:

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(
        StoredSession(
            session_id=self.session_id,
            messages=tuple(self.mutable_messages),
            input_tokens=self.total_usage.input_tokens,
            output_tokens=self.total_usage.output_tokens,
        )
    )
    return str(path)
```

The flush signals that the transcript content has been transferred into the `StoredSession` and written to disk. Subsequent `append` calls reset the flag to `False`, indicating that persistence would need to occur again.

---

## 9.4 The Interplay: `QueryEnginePort` as Orchestrator

The three modules presented -- `session_store`, `history`, and `transcript` -- are brought together in the class `QueryEnginePort` (file `query_engine.py`). This class is the central orchestrator of session management.

### 9.4.1 Session Creation

When a `QueryEnginePort` is instantiated, a new session ID is automatically generated:

```python
session_id: str = field(default_factory=lambda: uuid4().hex)
```

At the same time, an empty `TranscriptStore` is created:

```python
transcript_store: TranscriptStore = field(default_factory=TranscriptStore)
```

The `HistoryLog` is not managed within the `QueryEnginePort`, but in the parent `RuntimeSession` class (file `runtime.py`), which serves as a facade over the entire session.

### 9.4.2 Message Processing

Within `submit_message`, both the mutable message list and the Transcript Store are updated:

```python
self.mutable_messages.append(prompt)
self.transcript_store.append(prompt)
```

Immediately afterward, a check is made whether compaction is necessary:

```python
self.compact_messages_if_needed()
```

### 9.4.3 Persistence

The `persist_session` method creates a `StoredSession` from the current state and writes it to disk:

```python
def persist_session(self) -> str:
    self.flush_transcript()
    path = save_session(
        StoredSession(
            session_id=self.session_id,
            messages=tuple(self.mutable_messages),
            input_tokens=self.total_usage.input_tokens,
            output_tokens=self.total_usage.output_tokens,
        )
    )
    return str(path)
```

The flow: First the Transcript Store is flushed, then a `StoredSession` is constructed whose `messages` field is fed from the current `mutable_messages` as a tuple. Then `save_session` performs the JSON serialization and file write operation. The returned path is passed on as a string.

### 9.4.4 Restoration

The class method `from_saved_session` restores a complete `QueryEnginePort` from a saved session:

```python
@classmethod
def from_saved_session(cls, session_id: str) -> 'QueryEnginePort':
    stored = load_session(session_id)
    transcript = TranscriptStore(entries=list(stored.messages), flushed=True)
    return cls(
        manifest=build_port_manifest(),
        session_id=stored.session_id,
        mutable_messages=list(stored.messages),
        total_usage=UsageSummary(stored.input_tokens, stored.output_tokens),
        transcript_store=transcript,
    )
```

Notable here is the conversion in both directions: `stored.messages` is a tuple (from `StoredSession`), but is converted to a `list` for both `mutable_messages` and `TranscriptStore.entries`, since both structures need to be mutated during operation. The `TranscriptStore` is initialized with `flushed=True`, since its data was just loaded from disk -- there is no need for re-persistence as long as no new entries are added.

The `manifest` is freshly generated via `build_port_manifest()`, since it should reflect the current state of the workspace, not the state at the time of saving.

---

## 9.5 The Complete Session Lifecycle

In summary, the lifecycle of a session can be divided into five phases:

### Phase 1: Creation

When `QueryEnginePort.from_workspace()` is called or during direct instantiation, a new session ID is generated via `uuid4().hex`. An empty `TranscriptStore` and an empty message list are created. At this point, the session exists exclusively in memory.

In the parent `PortRuntime.bootstrap_session`, a `HistoryLog` is also created and populated with initial context information.

### Phase 2: Message Processing

Each call to `submit_message` adds the prompt to both the message list and the Transcript Store. The engine calculates the token usage, checks budget limits, and produces a `TurnResult`. The History Log is populated in the surrounding `bootstrap_session` method with information about the routing, execution, and result of the turn.

### Phase 3: Transcript Compaction

After each message processing, `compact_messages_if_needed` checks whether the number of messages exceeds the threshold `compact_after_turns` (default: 12). If so, both `mutable_messages` and `transcript_store.entries` are trimmed to the last 12 entries. This mechanism prevents unbounded growth of the data structures and limits token consumption during the next message processing.

### Phase 4: Persistence

The `persist_session` method bundles the current state -- session ID, messages, and token counters -- into an immutable `StoredSession` and delegates the serialization to `save_session`. The result is a JSON file in the `.port_sessions/` directory that represents the complete conversation state.

### Phase 5: Restoration

Via `QueryEnginePort.from_saved_session(session_id)`, the JSON file is read, deserialized into a `StoredSession`, and used as the basis for a new, fully functional `QueryEnginePort`. The restored engine can immediately process new messages, seamlessly continuing from the saved state -- including the token counters that are relevant for budget decisions.

---

## 9.6 Architectural Assessment

### Strengths

**Simplicity:** The entire persistence model comprises fewer than 85 lines of code across three files. There is no database, no ORM, no migration -- just JSON files and data classes. This simplicity reduces the likelihood of errors and makes the system easy to understand.

**Immutability in the right places:** `StoredSession` and `HistoryEvent` are `frozen`, while `HistoryLog`, `TranscriptStore`, and `QueryEnginePort` are mutable. This division follows a clear principle: Data structures that represent snapshots are immutable; data structures that represent active processes are mutable.

**Compaction as a first-class concept:** The fact that compaction is implemented directly in the `TranscriptStore` (and not as an afterthought hack) shows that the authors considered the limitations of LLM context windows from the very beginning.

**Testability:** Since `save_session` and `load_session` accept the target directory as a parameter, tests can easily use temporary directories without polluting the default directory.

### Possible Extensions

**Timestamps:** Neither `StoredSession` nor `HistoryEvent` carry a timestamp. For debugging purposes, a `created_at` field in `StoredSession` and a `timestamp` field in `HistoryEvent` would be useful.

**Compaction strategy:** The current strategy of "keep the last N entries" is simple and effective, but lossy. An extension could be a summarization function that condenses older entries into a compressed overview instead of discarding them entirely.

**Error handling:** `load_session` throws unhandled exceptions when the file does not exist (`FileNotFoundError`) or the JSON format is invalid (`json.JSONDecodeError`). A more robust version could define specific session exceptions.

---

## 9.7 Summary

The session management of Claw Code follows the principle "as simple as possible, but no simpler." Three compact modules -- `session_store.py`, `history.py`, and `transcript.py` -- together cover the entire spectrum of state management: from in-memory logging through compaction to persistence and restoration. The `QueryEnginePort` orchestrates these components and provides with `from_saved_session` and `persist_session` two symmetric methods that cleanly frame the lifecycle of a session. The result is a persistence model that requires no external dependencies, is easily testable, and yet fulfills all requirements of an interactive LLM client.


# Chapter 10: Setup, Bootstrap & Initialization

## Introduction

Every complex software system faces the challenge of organizing its own startup process so that dependencies are correctly resolved, resources are provided in time, and security decisions are made at the right point. In Claw Code, this process is particularly multi-layered: Before the first user query can be processed, the system must inspect its runtime environment, start prefetch processes, make trust decisions, register commands and tools, and finally select the appropriate operating mode. This chapter is devoted entirely to the interplay of the six source files that implement this flow: `setup.py`, `prefetch.py`, `deferred_init.py`, `bootstrap_graph.py`, `context.py`, and `system_init.py`. We will examine every data structure, every function, and every design decision in detail.

---

## 10.1 The Workspace Setup Process (`setup.py`)

The file `src/setup.py` forms the heart of the initialization logic. It imports both the prefetch infrastructure and the deferred-init subsystem and orchestrates their interplay in a single, coherent sequence.

### 10.1.1 The `WorkspaceSetup` Class

```python
@dataclass(frozen=True)
class WorkspaceSetup:
    python_version: str
    implementation: str
    platform_name: str
    test_command: str = 'python3 -m unittest discover -s tests -v'
```

`WorkspaceSetup` is an immutable (frozen) dataclass that captures the basic runtime parameters of the system. The four fields have the following meaning:

- **`python_version`**: A string of the form `"3.12.1"` containing the current Python version in `major.minor.patch` format. It is generated in `build_workspace_setup()` by joining the first three elements of `sys.version_info`.

- **`implementation`**: The name of the Python implementation as returned by `platform.python_implementation()` -- typically `"CPython"`, but `"PyPy"` or `"GraalPy"` would also be conceivable. This field allows the system to issue implementation-specific optimizations or warnings.

- **`platform_name`**: A detailed platform string produced by `platform.platform()` containing information such as operating system, version, and architecture (e.g., `"Linux-6.18.5-x86_64-with-glib2.39"`).

- **`test_command`**: A preconfigured command for running the test suite. The default value `'python3 -m unittest discover -s tests -v'` uses the built-in `unittest` discovery mechanism and recursively searches the `tests` directory for test modules. The `-v` parameter provides verbose output. This value is set as a default but can be overridden at instantiation.

### 10.1.2 The `startup_steps()` Method

```python
def startup_steps(self) -> tuple[str, ...]:
    return (
        'start top-level prefetch side effects',
        'build workspace context',
        'load mirrored command snapshot',
        'load mirrored tool snapshot',
        'prepare parity audit hooks',
        'apply trust-gated deferred init',
    )
```

This method returns a tuple of exactly six strings that name the logical steps of the startup process in the correct order. Each step represents a clearly delineated phase:

1. **`start top-level prefetch side effects`** -- Here the three prefetch operations (`mdm_raw_read`, `keychain_prefetch`, `project_scan`) are started. The term "side effects" is deliberately chosen: These operations have side effects on the system state by preloading data that will be needed later.

2. **`build workspace context`** -- The `PortContext` is built, which captures the directory structure of the project and calculates file counters.

3. **`load mirrored command snapshot`** -- The available commands are loaded from the Command Registry. The term "mirrored" indicates that these commands are to be understood as a mirror (parity copy) of the TypeScript original.

4. **`load mirrored tool snapshot`** -- Analogously, the available tools are loaded.

5. **`prepare parity audit hooks`** -- Audit hooks are prepared that monitor the parity fidelity between the Python port and the TypeScript original.

6. **`apply trust-gated deferred init`** -- The final step performs the trust-dependent deferred initialization. Only when `trusted=True` are plugins, skills, MCP prefetches, and session hooks activated.

The order is not chosen randomly: Prefetches must start first so that their results are available as early as possible. The context must precede the commands and tools, since these may require context information. The parity hooks must be prepared before the deferred init so that the deferred initialization can also be monitored. And the deferred init comes last because it depends on the trust decision, which is only established after CLI parsing.

### 10.1.3 The `SetupReport` Class

```python
@dataclass(frozen=True)
class SetupReport:
    setup: WorkspaceSetup
    prefetches: tuple[PrefetchResult, ...]
    deferred_init: DeferredInitResult
    trusted: bool
    cwd: Path
```

`SetupReport` is the central result structure of the entire setup process. It bundles all the information gathered during initialization:

- **`setup`**: The `WorkspaceSetup` instance with the runtime parameters.
- **`prefetches`**: A tuple of `PrefetchResult` objects -- one for each of the three prefetch operations.
- **`deferred_init`**: The result of the deferred initialization as a `DeferredInitResult`.
- **`trusted`**: A boolean value indicating the trust status of the current session.
- **`cwd`**: The current working directory as a `Path` object.

The `as_markdown()` method generates a human-readable Markdown representation of the entire report. It lists the Python version, platform, trust status, and working directory, followed by the prefetch results and deferred init details. This method is particularly useful for diagnostic and debugging purposes, as it provides a complete overview of the system's startup state.

### 10.1.4 The `run_setup()` Function

```python
def run_setup(cwd: Path | None = None, trusted: bool = True) -> SetupReport:
    root = cwd or Path(__file__).resolve().parent.parent
    prefetches = [
        start_mdm_raw_read(),
        start_keychain_prefetch(),
        start_project_scan(root),
    ]
    return SetupReport(
        setup=build_workspace_setup(),
        prefetches=tuple(prefetches),
        deferred_init=run_deferred_init(trusted=trusted),
        trusted=trusted,
        cwd=root,
    )
```

`run_setup()` is the entry function that executes the entire setup flow. It accepts two optional parameters:

- `cwd`: The working directory. If `None`, the parent directory of the `src` folder is automatically determined -- i.e., the project root directory.
- `trusted`: The trust status, defaulting to `True`.

The function first starts all three prefetch operations in sequence, then builds the `WorkspaceSetup` object and executes the deferred init. All results are collected in a `SetupReport` and returned. Notably, the prefetches are collected as a list and then converted to a tuple -- this ensures the immutability of the `SetupReport`.

---

## 10.2 Prefetch Operations (`prefetch.py`)

The file `src/prefetch.py` defines the prefetch infrastructure: a lightweight mechanism for initiating costly I/O operations early.

### 10.2.1 The `PrefetchResult` Class

```python
@dataclass(frozen=True)
class PrefetchResult:
    name: str
    started: bool
    detail: str
```

Each prefetch result carries three pieces of information:

- **`name`**: A machine-readable identifier such as `"mdm_raw_read"`, `"keychain_prefetch"`, or `"project_scan"`.
- **`started`**: A boolean value indicating whether the operation was successfully started. In the current implementation, this value is always `True`, as these are simulated operations. In a production environment, starting a prefetch could fail -- for example, if a network connection is unavailable.
- **`detail`**: A human-readable description text summarizing the purpose and status of the operation.

### 10.2.2 The Three Prefetch Functions

**`start_mdm_raw_read()`** simulates the preloading of MDM raw data (Mobile Device Management). In a real system, configuration data would be queried from an MDM server here -- such as permitted actions, policy settings, or device information. The prefetch ensures that this data is already in memory when it is needed later, rather than blocking the user with a synchronous network request.

**`start_keychain_prefetch()`** simulates the preloading of keychain data. The keychain contains authentication tokens, API keys, and other security-relevant data. By loading this data early, the first authenticated API call is not delayed by a keychain query. The detail text explicitly refers to the "trusted startup path," suggesting that keychain prefetching is particularly relevant in trusted mode.

**`start_project_scan(root: Path)`** simulates a scan of the project root directory. This step analyzes the directory structure, identifies relevant files, and builds an initial understanding of the project structure. The passed `root` parameter determines which directory is scanned. In the simulated implementation, the path is merely noted in the detail text; in practice, an actual file system scan would take place here.

All three functions follow the same pattern: They create a `PrefetchResult` with a unique name, `started=True`, and a descriptive detail string. This uniform interface makes it easy to add further prefetch operations without having to modify the calling logic in `setup.py` -- it suffices to define a new function that returns a `PrefetchResult` and insert it into the list in `run_setup()`.

---

## 10.3 Deferred Initialization (`deferred_init.py`)

The file `src/deferred_init.py` implements the concept of trust-dependent deferred initialization -- a mechanism that ensures potentially risky subsystems are only activated when the current session has been classified as trusted.

### 10.3.1 The `DeferredInitResult` Class

```python
@dataclass(frozen=True)
class DeferredInitResult:
    trusted: bool
    plugin_init: bool
    skill_init: bool
    mcp_prefetch: bool
    session_hooks: bool
```

This class contains five boolean fields that record the activation status of the four trust-dependent subsystems as well as the trust status itself:

- **`trusted`**: Reflects the passed trust status.
- **`plugin_init`**: Indicates whether plugin initialization was performed. Plugins extend the system's functionality with additional capabilities.
- **`skill_init`**: Indicates whether skills were loaded. Skills are specialized capabilities that can be invoked context-dependently.
- **`mcp_prefetch`**: Indicates whether MCP data (Model Context Protocol) was preloaded. MCP enables communication with external services and tools.
- **`session_hooks`**: Indicates whether session hooks were registered. These hooks allow code to be executed automatically upon certain events during a session.

The `as_lines()` method generates a tuple of formatted strings -- one per subsystem -- displaying the respective activation status. This method is used by the `SetupReport` in its `as_markdown()` method.

### 10.3.2 The `run_deferred_init()` Function

```python
def run_deferred_init(trusted: bool) -> DeferredInitResult:
    enabled = bool(trusted)
    return DeferredInitResult(
        trusted=trusted,
        plugin_init=enabled,
        skill_init=enabled,
        mcp_prefetch=enabled,
        session_hooks=enabled,
    )
```

The logic is deliberately kept simple: The `trusted` parameter is converted to a boolean value (which is a no-op for an already boolean parameter, but makes it more robust against truthy/falsy values), and this value is used for all four subsystems.

**When `trusted=True`**: All four subsystems are activated (`plugin_init=True`, `skill_init=True`, `mcp_prefetch=True`, `session_hooks=True`). The system runs with full functionality.

**When `trusted=False`**: All four subsystems are deactivated. The system runs in a restricted mode in which no plugins are loaded, no skills are initialized, no MCP data is preloaded, and no session hooks are registered. This is a security mechanism: In an untrusted environment, loading plugins or executing hooks could pose a risk.

This binary all-or-nothing logic is a deliberate design decision. In a more differentiated implementation, one could control individual subsystems independently. However, the current implementation favors simplicity and predictability: Either the system is fully trusted or it is not, and the consequences are clearly defined in both cases.

---

## 10.4 The Bootstrap Graph (`bootstrap_graph.py`)

The file `src/bootstrap_graph.py` formalizes the entire startup process as a directed graph with seven successive phases.

### 10.4.1 The `BootstrapGraph` Class

```python
@dataclass(frozen=True)
class BootstrapGraph:
    stages: tuple[str, ...]
```

The class is minimal: It contains only a tuple of stage identifiers. The `as_markdown()` method generates a Markdown listing of all phases, which is useful for documentation and diagnostic purposes.

### 10.4.2 The Seven Phases of the Bootstrap Graph

The function `build_bootstrap_graph()` creates the concrete graph with the following seven phases:

**Phase 1: `top-level prefetch side effects`**

This is the very first phase and has the highest priority. Even before any parsing or validation logic is executed, the prefetch operations are started. The reason: Prefetches typically involve I/O operations (network, file system) that cause latency. The earlier they are started, the greater the probability that their results are already available when they are later queried.

**Phase 2: `warning handler and environment guards`**

In this phase, warning handlers and environment guards are set up. Warning handlers intercept Python warnings and redirect them to the logging system. Environment guards check whether the runtime environment meets the minimum requirements -- such as the correct Python version, required environment variables, or necessary system resources. If a guard condition is not met, the startup process is aborted before further initialization takes place.

**Phase 3: `CLI parser and pre-action trust gate`**

Here the command-line arguments are parsed and the trust decision is made. The CLI parser interprets the passed arguments and flags. The "Trust Gate" is a security barrier that checks whether the current session is trusted before executing any actions. This decision directly influences the later deferred init in Phase 5.

**Phase 4: `setup() + commands/agents parallel load`**

In this phase, two things happen simultaneously: The `run_setup()` function is executed (which collects the prefetch results and builds the `WorkspaceSetup`), and in parallel, the commands and agents are loaded. The parallelization is an important performance gain: Since loading commands and agents is independent of the workspace setup, both processes can overlap.

**Phase 5: `deferred init after trust`**

After the trust decision from Phase 3 is established and the setup from Phase 4 is complete, the deferred initialization is now performed. This is where it is decided whether plugins, skills, MCP prefetches, and session hooks are activated or not.

**Phase 6: `mode routing: local / remote / ssh / teleport / direct-connect / deep-link`**

This phase selects the operating mode of the system. Claw Code supports six different modes:

- **local**: Local execution on the same machine.
- **remote**: Connection to a remote server.
- **ssh**: Execution via an SSH connection.
- **teleport**: A special remote access mode that possibly uses a Teleport-compatible network.
- **direct-connect**: Direct connection without intermediaries.
- **deep-link**: Execution via a deep link that directly targets specific actions or contexts.

The mode routing analyzes the CLI arguments and the environment configuration to select the appropriate mode and directs execution to the corresponding handler.

**Phase 7: `query engine submit loop`**

The last phase starts the main loop of the system: the query engine submit loop. In this loop, the system waits for user queries, submits them to the query engine, receives responses, and displays them. This loop runs until the user ends the session.

### 10.4.3 Diagram of the Seven Bootstrap Phases


**Bootstrap Graph — 7 Phases:**

| Phase | Name | Description |
|-------|------|-------------|
| 1 | Prefetch Side Effects | `start_mdm_raw_read()`, `start_keychain_prefetch()`, `start_project_scan()` |
| 2 | Warning Handler & Guards | Redirect Python warnings, validate environment |
| 3 | CLI Parser & Trust Gate | Parse arguments, determine `trusted = True/False` |
| 4 | Setup + Parallel Load | `run_setup()` runs in parallel with commands/agents loading |
| 5 | Deferred Init After Trust | If trusted: enable plugins, skills, MCP, hooks. If not: disable all |
| 6 | Mode Routing | Select: local / remote / ssh / teleport / direct-connect / deep-link |
| 7 | Query Engine Submit Loop | READ → PROCESS → RENDER → repeat until session ends |


---

## 10.5 The Project Context (`context.py`)

The file `src/context.py` provides the `PortContext` -- a data structure that captures and quantifies the entire project layout.

### 10.5.1 The `PortContext` Class

```python
@dataclass(frozen=True)
class PortContext:
    source_root: Path
    tests_root: Path
    assets_root: Path
    archive_root: Path
    python_file_count: int
    test_file_count: int
    asset_file_count: int
    archive_available: bool
```

The eight fields can be divided into two groups:

**Directory paths:**
- **`source_root`**: The root directory of the source code (`<project>/src`).
- **`tests_root`**: The root directory of the tests (`<project>/tests`).
- **`assets_root`**: The root directory for static resources (`<project>/assets`).
- **`archive_root`**: The directory containing the TypeScript snapshot of the original (`<project>/archive/claude_code_ts_snapshot/src`). This path is particularly revealing: It shows that the project carries an archived copy of the original TypeScript source code, which serves as a reference for the parity check.

**Counters and availability:**
- **`python_file_count`**: The number of `.py` files in `source_root`, counted recursively.
- **`test_file_count`**: The number of `.py` files in `tests_root`, counted recursively.
- **`asset_file_count`**: The number of all files in `assets_root`, counted recursively (without restriction to a specific extension).
- **`archive_available`**: A boolean value indicating whether the archive directory exists at all. This is important because the archive could be optional -- for example, if the repository was cloned without the archive folder.

### 10.5.2 The `build_port_context()` Function

```python
def build_port_context(base: Path | None = None) -> PortContext:
    root = base or Path(__file__).resolve().parent.parent
    source_root = root / 'src'
    tests_root = root / 'tests'
    assets_root = root / 'assets'
    archive_root = root / 'archive' / 'claude_code_ts_snapshot' / 'src'
```

The function accepts an optional base directory and derives the four sub-paths from it. The file counters are calculated via generator expressions with `rglob()`:

```python
python_file_count=sum(1 for path in source_root.rglob('*.py') if path.is_file()),
```

This pattern is memory-efficient: Instead of loading all paths into a list, each path is individually checked and counted. The `if path.is_file()` filter ensures that directories that happen to end in `.py` (theoretically possible) are not counted.

### 10.5.3 The `render_context()` Function

```python
def render_context(context: PortContext) -> str:
```

This helper function produces a simple line-based text representation of the context. It lists all eight fields one below the other and is intended for console output or log files. Unlike the `as_markdown()` method of the `SetupReport`, it does not use Markdown format but simple `key: value` lines.

---

## 10.6 The System Init Message (`system_init.py`)

The file `src/system_init.py` forms the topmost integration layer: It executes the setup, queries the registered commands and tools, and consolidates everything into a single init message.

### 10.6.1 The `build_system_init_message()` Function

```python
def build_system_init_message(trusted: bool = True) -> str:
    setup = run_setup(trusted=trusted)
    commands = get_commands()
    tools = get_tools()
    lines = [
        '# System Init',
        '',
        f'Trusted: {setup.trusted}',
        f'Built-in command names: {len(built_in_command_names())}',
        f'Loaded command entries: {len(commands)}',
        f'Loaded tool entries: {len(tools)}',
        '',
        'Startup steps:',
        *(f'- {step}' for step in setup.setup.startup_steps()),
    ]
    return '\n'.join(lines)
```

This function is the central entry point for the system message displayed at the beginning of a session. It:

1. Executes `run_setup()`, which starts all prefetches and performs the deferred init.
2. Calls `get_commands()` to obtain the list of all registered commands.
3. Calls `get_tools()` to obtain the list of all registered tools.
4. Calls `built_in_command_names()` to determine the number of built-in command names.

The generated message is a Markdown-formatted string containing the following information:

- The trust status of the session.
- The number of built-in command names (from `built_in_command_names()`).
- The number of loaded command entries (from `get_commands()`).
- The number of loaded tool entries (from `get_tools()`).
- The complete list of six startup steps.

This message serves as a startup report: It informs the user (or the calling system) about the state of the system after initialization. The numbers for commands and tools are particularly useful for recognizing at a glance whether all expected extensions were correctly loaded.

Notable is the separation between `built_in_command_names()` and `get_commands()`: The former delivers only the names of the built-in commands (as a flat list of strings), while the latter returns the complete command entries (as a list of objects with metadata). This distinction makes it possible to report both the total count and the built-in subset separately.

---

## 10.7 Interplay of the Components

The six files form a clear dependency hierarchy:

```
system_init.py
    |
    +-- setup.py
    |       |
    |       +-- prefetch.py       (PrefetchResult, 3 Startfunktionen)
    |       +-- deferred_init.py  (DeferredInitResult, run_deferred_init)
    |
    +-- commands.py               (get_commands, built_in_command_names)
    +-- tools.py                  (get_tools)

bootstrap_graph.py                (eigenständig, dokumentiert den Ablauf)
context.py                        (eigenständig, baut PortContext auf)
```

`system_init.py` sits at the top and orchestrates everything. `setup.py` is the middle layer that brings together `prefetch.py` and `deferred_init.py`. `bootstrap_graph.py` and `context.py` are standalone modules that have no dependencies on the other setup files and can be used independently.

This design follows the principle of minimal coupling: Each module has a clearly defined responsibility and only knows the modules it directly needs. The prefetch operations know nothing about the deferred init; the bootstrap graph knows no concrete implementation details; and the PortContext is entirely independent of the rest of the initialization logic.

---

## 10.8 Design Decisions and Architectural Principles

### Immutability Through `frozen=True`

All dataclasses in these six files use `frozen=True`. This means that their fields cannot be changed after creation. This decision has several advantages: It prevents accidental mutations, makes the objects hashable (and thus usable as dictionary keys or in sets), and clearly signals that these are value objects that freeze the state at a specific point in time.

### Simulation Instead of Real I/O

The prefetch functions and the deferred init are deliberately implemented as simulations. They do not perform actual network calls or file system operations (with the exception of the file counting in `build_port_context()`). This allows the entire initialization logic to be tested deterministically without requiring external dependencies or infrastructure.

### Trust Model as a Binary Switch

The trust model (`trusted=True/False`) is deliberately implemented as a simple boolean switch. This avoids the complexity of a multi-level permission system and makes the consequences immediately clear to the developer: Either everything is activated or nothing is. For a production system, one could extend this model to a fine-grained permission system, but for the current phase of the project, simplicity is an advantage.

### The Bootstrap Graph as a Declarative Model

The bootstrap graph describes the flow declaratively as a tuple of strings, rather than implementing it imperatively as a sequence of function calls. This has the advantage that the graph serves as documentation without having to be executable code at the same time. It can be used for visualization, validation, and diagnostics without affecting the actual execution logic.

---

## 10.9 Summary

The startup process of Claw Code is a carefully orchestrated process controlled by `system_init.py` and coordinated by `setup.py`. The three prefetch operations (MDM raw data, keychain, project scan) are started early to minimize latency. The deferred initialization ensures that security-relevant subsystems are only activated in trusted environments. The bootstrap graph formalizes this flow in seven clearly defined phases, from the first prefetch to the query engine submit loop. The PortContext quantitatively captures the project structure and enables the system to make informed decisions about available resources. Together, these components form a robust, testable, and clearly structured initialization system.


# Chapter 11: Execution Layer & Runtime Modes

## 11.1 Introduction

The preceding chapters have shown how Claw Code captures the entire command catalog and tool catalog of the original in the form of snapshot files, converts them into `PortingModule` instances, and makes them accessible through the modules `commands.py` and `tools.py`. But a catalog alone is not enough -- a CLI tool must be able to *execute* commands. In this chapter, we turn to the layer that handles exactly this task: the **execution layer**. It consists of three files, each covering an independent aspect of the runtime:

1. **`src/execution_registry.py`** -- The central registry that brings together commands and tools as executable wrapper objects.
2. **`src/remote_runtime.py`** -- Runtime modes for remote connections (Remote, SSH, Teleport).
3. **`src/direct_modes.py`** -- Direct modes for immediate connections (Direct-Connect, Deep-Link).

Together, these three modules form the backbone of what would function as a dispatch layer in a complete CLI -- with one crucial difference: Claw Code does not perform real operations. Instead, it consistently relies on **shim execution**, i.e., placeholder implementations that simulate the behavior of the original without actually intervening in the system. Why this decision was made and what architectural advantages it offers is the central topic of this chapter.

---

## 11.2 MirroredCommand and MirroredTool

### 11.2.1 Wrappers Around the Catalog

The classes `MirroredCommand` and `MirroredTool` in `execution_registry.py` are immutable data classes (`frozen=True`) that serve as a bridge between the static catalog and the execution logic. Each instance encapsulates exactly two pieces of information:

```python
@dataclass(frozen=True)
class MirroredCommand:
    name: str
    source_hint: str

    def execute(self, prompt: str) -> str:
        return execute_command(self.name, prompt).message
```

```python
@dataclass(frozen=True)
class MirroredTool:
    name: str
    source_hint: str

    def execute(self, payload: str) -> str:
        return execute_tool(self.name, payload).message
```

The `name` field uniquely identifies the command or tool -- it corresponds to the `name` field of the underlying `PortingModule`. The `source_hint` field indicates which area of the original the entry comes from (for example, `"commands/slash_commands.ts"` or `"tools/bash_tool.ts"`). These two fields are taken directly from the respective `PortingModule` when the registry is built.

### 11.2.2 The execute() Method

Both classes have an `execute()` method that "executes" the respective entry. For `MirroredCommand`, the method takes a `prompt: str` -- this corresponds to the text argument a user would pass to a slash command (e.g., `/review please check the test coverage`). For `MirroredTool`, the method takes a `payload: str` -- this corresponds to the input data a tool needs for processing (e.g., the file path for a file reading tool or a bash command for the bash tool).

Internally, both methods delegate to the identically named functions from the catalog modules:

- `MirroredCommand.execute(prompt)` calls `execute_command(self.name, prompt)` and returns the `.message` attribute of the resulting `CommandExecution` object.
- `MirroredTool.execute(payload)` calls `execute_tool(self.name, payload)` and returns the `.message` attribute of the resulting `ToolExecution` object.

### 11.2.3 What execute_command() and execute_tool() Actually Do

A look into `commands.py` and `tools.py` reveals the core of shim execution. The function `execute_command()` in `commands.py` (lines 75-80) first looks up the matching `PortingModule` via `get_command(name)`. If no entry is found, a `CommandExecution` object with `handled=False` and an error message is returned. If an entry is found, the function produces a **formatted status message** of the form:

```
Mirrored command 'review' from commands/slash_commands.ts would handle prompt 'bitte prüfe die Testabdeckung'.
```

`execute_tool()` in `tools.py` (lines 81-86) behaves analogously:

```
Mirrored tool 'BashTool' from tools/bash_tool.ts would handle payload 'ls -la'.
```

No actual execution takes place. No bash command is started, no file is read, no SSH tunnel is established. The method merely describes *what would* happen *if* the real implementation were present. This is the fundamental character of shim execution.

### 11.2.4 The Return Value: Only the Message

It is notable that `MirroredCommand.execute()` and `MirroredTool.execute()` do not return the full `CommandExecution` or `ToolExecution` object, but only its `message` field as a `str`. The wrappers thus provide a simplified interface: The caller receives a readable text describing the execution status without having to deal with the internal fields `handled`, `source_hint`, or `prompt`/`payload`. This decision follows the principle of information encapsulation -- the wrappers hide the complexity of the dispatch mechanism behind a single string return.

---

## 11.3 ExecutionRegistry

### 11.3.1 Structure and Layout

The `ExecutionRegistry` class is the central object of the execution layer. It bundles all executable commands and tools in two immutable tuples:

```python
@dataclass(frozen=True)
class ExecutionRegistry:
    commands: tuple[MirroredCommand, ...]
    tools: tuple[MirroredTool, ...]
```

The use of `tuple` instead of `list` is no accident. In combination with `frozen=True`, it is ensured that a registry, once created, can neither be changed nor extended. This follows the functional principle of *immutability*, which runs like a common thread through the entire Claw Code project. An immutable registry has several advantages:

- **Thread safety:** Multiple parts of the system can access the registry simultaneously without requiring synchronization mechanisms.
- **Predictability:** The state of the registry does not change after creation. Every call to `command()` or `tool()` is guaranteed to return the same result for the same input.
- **Testability:** Tests can create a registry with known content and rely on no side effect changing the state.

### 11.3.2 Case-insensitive Lookup: command() and tool()

The `command(name)` method linearly searches the `commands` tuple for an entry whose name -- regardless of upper and lower case -- matches the passed `name`:

```python
def command(self, name: str) -> MirroredCommand | None:
    lowered = name.lower()
    for command in self.commands:
        if command.name.lower() == lowered:
            return command
    return None
```

The `tool(name)` method works identically but searches the `tools` tuple:

```python
def tool(self, name: str) -> MirroredTool | None:
    lowered = name.lower()
    for tool in self.tools:
        if tool.name.lower() == lowered:
            return tool
    return None
```

Both methods return `None` if no matching entry is found. The return type `MirroredCommand | None` or `MirroredTool | None` makes this explicit at the type level and forces the caller to handle the error case.

The case insensitivity is a deliberate design decision that improves usability. A user who types `/Review` instead of `/review`, or a caller who requests `bashtool` instead of `BashTool`, will still find the correct entry. This mirrors the behavior of the original, which also exhibits a certain tolerance regarding the spelling of command names.

### 11.3.3 Linear Search Instead of Dictionary

It is notable that both `command()` and `tool()` perform a linear search over the tuple, instead of using a dictionary with precomputed keys. With a dictionary-based approach, the lookup would be O(1) instead of O(n). Why was the linear search chosen nonetheless?

The answer lies in the size of the catalogs and the project's prioritization. The command catalog and tool catalog together comprise a few dozen entries -- a magnitude at which linear search has practically no measurable speed disadvantage compared to a dictionary lookup. At the same time, the code remains maximally simple and readable through linear iteration. There is no additional initialization step, no key normalization during construction, and no possibility for keys and entries to get out of sync. Code simplicity is thus prioritized over theoretical efficiency -- a pragmatic decision that is quite appropriate for a mirroring project.

### 11.3.4 build_execution_registry()

The factory function `build_execution_registry()` is the only intended way to create an `ExecutionRegistry` instance:

```python
def build_execution_registry() -> ExecutionRegistry:
    return ExecutionRegistry(
        commands=tuple(MirroredCommand(module.name, module.source_hint) for module in PORTED_COMMANDS),
        tools=tuple(MirroredTool(module.name, module.source_hint) for module in PORTED_TOOLS),
    )
```

The function iterates over the global tuples `PORTED_COMMANDS` and `PORTED_TOOLS` -- i.e., over the `PortingModule` instances loaded from the snapshot files -- and creates a corresponding `MirroredCommand` or `MirroredTool` object for each module. The `name` and `source_hint` fields are transferred one-to-one.

This factory pattern has the advantage that the coupling between catalog and registry occurs at exactly one place. If the structure of the snapshot data changes or new fields are added, only this one function needs to be modified. At the same time, the `ExecutionRegistry` class itself remains free of any loading logic and knows neither file paths nor JSON formats.

---

## 11.4 Runtime Modes: RuntimeModeReport

### 11.4.1 The Data Class

The module `remote_runtime.py` defines the data class `RuntimeModeReport`, which describes the result of a runtime mode startup:

```python
@dataclass(frozen=True)
class RuntimeModeReport:
    mode: str
    connected: bool
    detail: str

    def as_text(self) -> str:
        return f'mode={self.mode}\nconnected={self.connected}\ndetail={self.detail}'
```

The three fields have the following meaning:

- **`mode`**: Identifies the runtime mode as a string (e.g., `'remote'`, `'ssh'`, `'teleport'`).
- **`connected`**: Indicates whether the connection is considered established. In the current shim implementation, this field is always set to `True`, since the connection is not actually built -- the placeholder optimistically assumes that everything would work.
- **`detail`**: A human-readable description of the current state.

The `as_text()` method produces a simple key-value representation suitable for logging, debugging, and status displays. The format is deliberately kept simple -- no JSON, no YAML, just simple `key=value` pairs separated by line breaks.

### 11.4.2 The Three Runtime Mode Functions

The module provides three functions, each representing a specific runtime mode:

**`run_remote_mode(target: str) -> RuntimeModeReport`**

```python
def run_remote_mode(target: str) -> RuntimeModeReport:
    return RuntimeModeReport('remote', True, f'Remote control placeholder prepared for {target}')
```

This function maps the remote mode, in which the original establishes a connection to a remote instance and delegates commands there. In Claw Code, only a report with mode `'remote'` and a placeholder description is created.

**`run_ssh_mode(target: str) -> RuntimeModeReport`**

```python
def run_ssh_mode(target: str) -> RuntimeModeReport:
    return RuntimeModeReport('ssh', True, f'SSH proxy placeholder prepared for {target}')
```

The SSH mode maps the case where an SSH connection is established to a remote host. In the original, an SSH session would be opened here, keys exchanged, and a channel built. In Claw Code, a report is created that describes this process without performing it.

**`run_teleport_mode(target: str) -> RuntimeModeReport`**

```python
def run_teleport_mode(target: str) -> RuntimeModeReport:
    return RuntimeModeReport('teleport', True, f'Teleport resume/create placeholder prepared for {target}')
```

The teleport mode is an abstraction for resuming or creating a remote session -- a concept that exists in the original as a way to resume running sessions on another host or start new ones. The report signals that such a process would be prepared.

All three functions follow the same pattern: They take a `target` (typically a hostname or URL), create a `RuntimeModeReport` object with `connected=True` and a descriptive `detail` message, and return it. There are no side effects, no network accesses, no state changes. The functions are pure functions in the mathematical sense.

---

## 11.5 Direct Modes: DirectModeReport

### 11.5.1 The Data Class

The module `direct_modes.py` defines `DirectModeReport`, a data class analogous to `RuntimeModeReport`:

```python
@dataclass(frozen=True)
class DirectModeReport:
    mode: str
    target: str
    active: bool

    def as_text(self) -> str:
        return f'mode={self.mode}\ntarget={self.target}\nactive={self.active}'
```

The difference from `RuntimeModeReport` lies in the fields:

- **`mode`**: The mode identifier (e.g., `'direct-connect'` or `'deep-link'`).
- **`target`**: The target of the connection, stored directly as a field (in `RuntimeModeReport`, the target is only contained in the `detail` message).
- **`active`**: Indicates whether the mode is considered active -- analogous to `connected` in `RuntimeModeReport`, but with a semantically more fitting name, since direct modes do not establish a "connection" in the classical sense.

The `as_text()` method follows the same `key=value` format as `RuntimeModeReport`. Both report classes thus share the same output pattern, but are deliberately modeled as separate classes since they represent different domain concepts.

### 11.5.2 The Two Direct Mode Functions

**`run_direct_connect(target: str) -> DirectModeReport`**

```python
def run_direct_connect(target: str) -> DirectModeReport:
    return DirectModeReport(mode='direct-connect', target=target, active=True)
```

The direct-connect mode maps the case where the CLI establishes a direct connection to an API endpoint or a local service, without the detour through SSH or remote proxies. In the original, an HTTP client would be configured here, a WebSocket connection opened, or a similar direct communication established.

**`run_deep_link(target: str) -> DirectModeReport`**

```python
def run_deep_link(target: str) -> DirectModeReport:
    return DirectModeReport(mode='deep-link', target=target, active=True)
```

The deep-link mode serves the integration with external applications via deep links -- URLs that trigger a specific action in a target application. In the original, this could be used to open an IDE, direct a browser to a specific location, or launch an external application with predefined parameters.

Here too: Both functions are pure functions without side effects. They exclusively produce report objects that describe the *intended* operation.

---

## 11.6 The Interplay of the Execution Layer

The three modules together form a coherent execution layer with a clear division of labor:

| Module | Responsibility | Output |
|---|---|---|
| `execution_registry.py` | Execute commands and tools | `str` (status message) |
| `remote_runtime.py` | Start remote runtime modes | `RuntimeModeReport` |
| `direct_modes.py` | Start direct connection modes | `DirectModeReport` |

The information flow is strictly unidirectional: The snapshot data flows from the JSON files through `PORTED_COMMANDS`/`PORTED_TOOLS` into the `ExecutionRegistry`, which in turn returns to the caller via `MirroredCommand`/`MirroredTool`. The runtime modes are orthogonal to this -- they are not concerned with the execution of individual commands, but with the question of *how* and *where* execution should take place.

In a fully implemented system, the runtime mode selection would occur *before* command execution: First it is decided whether to work locally, remotely, via SSH, or by teleport, and then commands are dispatched in the chosen context. Claw Code maps both aspects -- mode selection and command execution -- but each as a shim.

---

## 11.7 Why Shim Execution?

### 11.7.1 The Fundamental Architectural Decision

The decision to implement shim execution instead of real execution is not a cost-saving measure and not a sign of incompleteness. It is a **deliberate architectural decision** that follows from the nature of the Claw Code project.

Claw Code is a **mirroring project**. Its purpose is to reproduce the architecture, the surface, and the structures of the original in a different language (Python instead of TypeScript), in order to make them studiable, testable, and comparable. The goal is not to build a functionally equivalent CLI -- the goal is to **make the architecture of the original visible**.

Real execution would not only miss this goal but actively hinder it:

1. **Security risks:** The original executes bash commands, reads and writes files, opens network connections. A real reimplementation of these functions carries significant risks, especially when the implementation is not fully tested.

2. **Functional divergence:** Every real implementation of a tool would inevitably diverge from the original implementation -- whether in edge cases, error handling, or timing. These divergences would make the comparison between original and mirror more difficult.

3. **Maintenance effort:** Real implementations must keep pace with the original. With every change to the original, the Claw Code implementation would also need to be updated. Shim execution makes this trivial: Only the snapshot data needs to be updated.

4. **Focus on structure:** Claw Code focuses on the *structure* of the system -- what commands exist, what tools, how they are organized, how they are dispatched. Shim execution preserves exactly this structural information without obscuring the view with implementation details.

### 11.7.2 How Shim Execution Mirrors the Original

The shim execution is not arbitrarily chosen. It exactly replicates the **dispatch interfaces** of the original:

- In the original, there is a registry that manages commands and tools. In Claw Code, there is the `ExecutionRegistry`.
- In the original, commands are looked up by name and called with a prompt. In Claw Code, the same happens via `MirroredCommand.execute(prompt)`.
- In the original, tools are looked up by name and called with a payload. In Claw Code, the same happens via `MirroredTool.execute(payload)`.
- In the original, there are different runtime modes (Remote, SSH, Teleport). In Claw Code, there are the corresponding `run_*` functions.
- In the original, there are direct connection modes. In Claw Code, there are `run_direct_connect()` and `run_deep_link()`.

The crucial point is that the **interfaces are identical**. A caller who writes `registry.command('review').execute('check the code')` interacts with the same API that would exist in a real system. The only difference lies in the return value: Instead of a real execution result, the caller receives a descriptive message.

This is the principle of **architectural isomorphism**: The structure of the mirror implementation is isomorphic to the structure of the original, even if the semantics of the operations are simplified. One can think of Claw Code as an architectural model -- like a scale model of a building that shows all rooms, doors, and corridors, but in which no water flows through the pipes.

### 11.7.3 The Value of Shim Messages

The messages produced by the shim functions are not mere placeholders -- they are **machine-readable documentation**. The message `"Mirrored command 'review' from commands/slash_commands.ts would handle prompt 'check the code'."` contains three essential pieces of information:

1. **The name of the command** (`review`), enabling mapping to the catalog.
2. **The origin in the original** (`commands/slash_commands.ts`), enabling tracing back to the original's source code.
3. **The passed prompt**, ensuring traceability of the intended action.

In tests, these messages can be parsed to ensure that the dispatch works correctly -- that the right command was found, the right source file was referenced, and the right prompt was forwarded. Shim execution is thus not silent but explicit and transparent.

---

## 11.8 Design Patterns and Principles

### 11.8.1 Frozen Dataclasses as a Fundamental Building Block

All six data classes in the three modules (`MirroredCommand`, `MirroredTool`, `ExecutionRegistry`, `CommandExecution`, `ToolExecution`, `RuntimeModeReport`, `DirectModeReport`) use `frozen=True`. This is no coincidence but a consistent design principle: The execution layer exclusively produces immutable values. Once created, no report and no wrapper can be modified after the fact. This eliminates an entire class of bugs (unintended mutation) and makes the code easier to test and debug.

### 11.8.2 Factory Functions Instead of Constructors

Both `build_execution_registry()` and the `run_*` functions follow the factory pattern: They create configured objects and return them, instead of burdening the caller with the details of configuration. This decouples creation logic from usage and allows creation to be changed centrally without modifying callers.

### 11.8.3 Pure Functions

All `run_*` functions in `remote_runtime.py` and `direct_modes.py` are pure functions: They have no side effects, do not access global state, and always deliver the same output for the same input. This makes them trivially testable -- a test only needs to check whether the fields of the returned report contain the expected values.

### 11.8.4 Deliberate Separation of Report Types

Although `RuntimeModeReport` and `DirectModeReport` are structurally similar, they are modeled as separate classes. This follows the principle of semantic typing: Two concepts that happen to have similar fields are not the same concept. A remote mode and a direct-connect mode have different semantics, different failure cases, and different future extension possibilities. The separation into separate classes makes this distinction visible at the type level and prevents a `RuntimeModeReport` from being accidentally used where a `DirectModeReport` is expected.

---

## 11.9 Integration into the Overall System

The execution layer is not isolated but fits into the overall architecture of Claw Code:

- The `ExecutionRegistry` is created via `build_execution_registry()` and can be passed to higher-level layers (e.g., a dispatcher or a CLI main loop).
- The runtime mode reports can be evaluated by a configuration layer to decide which mode is active.
- The `as_text()` methods of the reports provide a uniform text representation that can be used for logging, debugging, and user output.

The execution layer thus forms the lowest layer of the dispatch stack: It knows *what* can be executed and *how* execution is configured, but it does not decide *when* or *whether* something is executed. That decision lies with the layers above -- the command parser, the permission system, and the session management.

---

## 11.10 Summary

The execution layer of Claw Code consists of three modules that together comprise 100 lines of Python and yet structurally map the entire dispatch and runtime logic of the original:

- **`execution_registry.py`** provides with `MirroredCommand`, `MirroredTool`, and `ExecutionRegistry` a complete, immutable registry that makes commands and tools accessible via case-insensitive lookups and serves them through shim execution.
- **`remote_runtime.py`** maps with `RuntimeModeReport` and the three `run_*` functions the remote runtime modes (Remote, SSH, Teleport) as placeholders.
- **`direct_modes.py`** maps with `DirectModeReport` and the two `run_*` functions the direct connection modes (Direct-Connect, Deep-Link) as placeholders.

The consistent use of shim execution is the central design decision of this layer. It makes it possible to fully replicate the architecture of the original -- with all interfaces, data flows, and dispatch paths -- without incurring the risks and effort of a real implementation. The shim messages serve as machine-readable documentation that describes the intended execution path and can be verified in tests.

This chapter has shown that the execution layer contributes significantly to the architectural mirroring not despite, but *because of* its simplicity. The deliberate restriction to shim execution is not a compromise but a strength: It keeps the focus on structure and prevents implementation details from obscuring the view of what is essential -- the architecture of the original.

CHAPTERS_12_14_PLACEHOLDER


# Chapter 12: The Subsystem Architecture

## 12.1 Einführung: Das Problem der strukturellen Abbildung

Wer ein komplexes Softwaresystem in eine andere Sprache portiert -- oder auch nur eine Referenzimplementierung davon erstellt --, steht vor einem fundamentalen Dilemma. Einerseits möchte man die Struktur des Originals möglichst getreu abbilden, damit Entwickler, die das Original kennen, sich sofort zurechtfinden. Andererseits wäre es unsinnig, tausende Dateien eins zu eins zu kopieren, wenn der Zweck des neuen Projekts nicht die vollständige Reimplementierung ist, sondern die Schaffung eines Python-Geruests, das die Architektur dokumentiert, Metadaten bereitstellt und als Ausgangspunkt für zukünftige Portierungen dient.

Das Claw-Code-Projekt löst dieses Dilemma durch ein elegantes Architekturmuster, das wir in diesem Kapitel im Detail untersuchen werden: die **Subsystem-Platzhalter-Architektur**. Jedes der 29 Subsysteme des originalen TypeScript-Projekts wird durch genau zwei Artefakte repräsentiert -- ein Python-Paket mit einer minimalen `__init__.py`-Datei und eine JSON-Metadatendatei, die den Umfang und die Struktur des Originals beschreibt. Gemeinsam bilden diese 58 Dateien (29 Python-Pakete plus 29 JSON-Dateien) das Rückgrat der gesamten Claw-Code-Architektur.

## 12.2 Das einheitliche Muster: Anatomie einer `__init__.py`-Datei

Die bemerkenswerteste Eigenschaft der Subsystem-Architektur ist ihre vollständige Uniformitaet. Jede einzelne der 29 `__init__.py`-Dateien folgt exakt demselben Muster. Es gibt keine Abweichungen, keine Sonderfaelle, keine subsystemspezifischen Erweiterungen. Betrachten wir das Muster am Beispiel des `bridge`-Subsystems:

```python
"""Python package placeholder for the archived `bridge` subsystem."""

from __future__ import annotations

import json
from pathlib import Path

SNAPSHOT_PATH = Path(__file__).resolve().parent.parent / 'reference_data' / 'subsystems' / 'bridge.json'
_SNAPSHOT = json.loads(SNAPSHOT_PATH.read_text())

ARCHIVE_NAME = _SNAPSHOT['archive_name']
MODULE_COUNT = _SNAPSHOT['module_count']
SAMPLE_FILES = tuple(_SNAPSHOT['sample_files'])
PORTING_NOTE = f"Python placeholder package for '{ARCHIVE_NAME}' with {MODULE_COUNT} archived module references."

__all__ = ['ARCHIVE_NAME', 'MODULE_COUNT', 'PORTING_NOTE', 'SAMPLE_FILES']
```

Dieses Muster lässt sich in fünf klar abgegrenzte Abschnitte gliedern, die wir nun einzeln untersuchen.

### 12.2.1 Der Docstring

Jede Datei beginnt mit einem einzeiligen Docstring der Form:

```python
"""Python package placeholder for the archived `<name>` subsystem."""
```

Der Begriff "placeholder" ist hier bewusst gewählt. Er signalisiert unmissverstaendlich, dass dieses Paket keine funktionale Implementierung enthält, sondern als Stellvertreter für das urspruengliche TypeScript-Subsystem dient. Das Wort "archived" verstärkt diese Botschaft: Die Module des Originals sind nicht verloren, sondern archiviert -- ihre Existenz ist dokumentiert, auch wenn ihr Code hier nicht vorliegt.

### 12.2.2 Die Importe

```python
from __future__ import annotations

import json
from pathlib import Path
```

Die Importliste ist minimalistisch. `from __future__ import annotations` aktiviert die verzoegerte Auswertung von Typ-Annotationen (PEP 563), was in diesem konkreten Fall zwar nicht strikt notwendig ist, aber eine Best Practice darstellt, die das Projekt durchgehend befolgt. Die einzigen genutzten Standardbibliotheksmodule sind `json` für das Parsen der Metadaten und `pathlib.Path` für die plattformübergreifende Pfadkonstruktion.

Das Fehlen externer Abhängigkeiten ist ein wichtiger Designaspekt: Jedes Subsystem-Paket kann importiert werden, ohne dass irgendwelche Pakete installiert sein müssen, die über die Python-Standardbibliothek hinausgehen.

### 12.2.3 Die Pfadkonstruktion und das Laden der Metadaten

```python
SNAPSHOT_PATH = Path(__file__).resolve().parent.parent / 'reference_data' / 'subsystems' / 'bridge.json'
_SNAPSHOT = json.loads(SNAPSHOT_PATH.read_text())
```

Diese beiden Zeilen bilden das Herzschlagwerk des Musters. Die Pfadkonstruktion verdient besondere Aufmerksamkeit:

1. `Path(__file__)` liefert den Pfad der aktuellen `__init__.py`-Datei, beispielsweise `/home/user/claw-code_claude/src/bridge/__init__.py`.
2. `.resolve()` wandelt diesen in einen absoluten, kanonischen Pfad um und löst dabei symbolische Links auf.
3. `.parent` navigiert zum Verzeichnis des Pakets: `.../src/bridge/`.
4. `.parent` navigiert eine weitere Ebene nach oben: `.../src/`.
5. `/ 'reference_data' / 'subsystems' / 'bridge.json'` konstruiert den vollständigen Pfad zur JSON-Metadatendatei.

Das Ergebnis ist ein Pfad wie `/home/user/claw-code_claude/src/reference_data/subsystems/bridge.json`. Bemerkenswert ist, dass die Pfadkonstruktion relativ zum Standort der `__init__.py`-Datei erfolgt, nicht relativ zum Arbeitsverzeichnis. Dadurch funktioniert der Import zuverlässig, unabhängig davon, von welchem Verzeichnis aus das Programm gestartet wird.

Die zweite Zeile liest den gesamten Inhalt der JSON-Datei als Text ein (`SNAPSHOT_PATH.read_text()`) und parst ihn mit `json.loads()` in ein Python-Dictionary. Das führende Unterstrich-Präfix von `_SNAPSHOT` signalisiert, dass diese Variable als modulintern betrachtet werden soll -- sie erscheint bewusst nicht in der `__all__`-Liste.

Ein wichtiger Nebeneffekt: Das Laden und Parsen der JSON-Datei geschieht zum Importzeitpunkt. Sobald ein anderes Modul `import bridge` oder `from bridge import MODULE_COUNT` ausführt, wird die JSON-Datei gelesen. Dies ist eine bewusste Designentscheidung: Die Metadaten stehen sofort nach dem Import zur Verfügung, ohne dass ein expliziter Initialisierungsschritt erforderlich wäre.

### 12.2.4 Die exportierten Konstanten

```python
ARCHIVE_NAME = _SNAPSHOT['archive_name']
MODULE_COUNT = _SNAPSHOT['module_count']
SAMPLE_FILES = tuple(_SNAPSHOT['sample_files'])
PORTING_NOTE = f"Python placeholder package for '{ARCHIVE_NAME}' with {MODULE_COUNT} archived module references."
```

Aus dem geparsten Dictionary werden vier benannte Konstanten extrahiert:

- **`ARCHIVE_NAME`** (str): Der kanonische Name des Subsystems, wie er im Original verwendet wird. In den meisten Faellen stimmt er mit dem Paketnamen überein (z. B. `"bridge"`, `"utils"`, `"components"`). Eine bemerkenswerte Ausnahme ist das Subsystem `native_ts`, dessen `archive_name` den Wert `"native-ts"` trägt -- der Bindestrich im Originalnamen ist in Python als Paketname nicht zulässig, weshalb der `package_name` zu `"native_ts"` wird, während der `archive_name` die originale Schreibweise bewahrt.

- **`MODULE_COUNT`** (int): Die Anzahl der Module (TypeScript-Dateien) im originalen Subsystem. Dieser Wert reicht von 1 (bei `coordinator`, `moreright`, `schemas`, `outputStyles`, `voice`, `assistant` und `bootstrap`) bis zu 564 (bei `utils`). Wie wir in Abschnitt 12.4 sehen werden, variiert die Größe der Subsysteme enorm.

- **`SAMPLE_FILES`** (tuple): Ein Tupel mit den Dateinamen der originalen Module. Die Konvertierung von der JSON-Liste zum Python-Tupel mit `tuple()` ist eine bewusste Entscheidung: Tupel sind unveränderlich und signalisieren, dass diese Sammlung nicht modifiziert werden soll. Bei kleinen Subsystemen enthält dieses Tupel saemtliche Dateien; bei großen Subsystemen wie `utils` (564 Module) oder `components` (389 Module) enthält es eine repräsentative Auswahl von bis zu 25 Eintraegen.

- **`PORTING_NOTE`** (str): Ein menschenlesbarer Hinweistext, der dynamisch aus `ARCHIVE_NAME` und `MODULE_COUNT` zusammengesetzt wird. Für das `bridge`-Subsystem lautet er beispielsweise: `"Python placeholder package for 'bridge' with 31 archived module references."`. Dieser String dient als schnelle Orientierung und kann von Werkzeugen, Dokumentationsgeneratoren oder interaktiven Shells ausgegeben werden.

### 12.2.5 Die `__all__`-Liste

```python
__all__ = ['ARCHIVE_NAME', 'MODULE_COUNT', 'PORTING_NOTE', 'SAMPLE_FILES']
```

Die explizite `__all__`-Definition kontrolliert, was bei einem `from bridge import *`-Statement exportiert wird. Bemerkenswert ist, dass `SNAPSHOT_PATH` hier zwar nicht aufgeführt ist, aber dennoch als regulaeres Modulattribut zugänglich bleibt -- es wird lediglich nicht bei Wildcard-Importen eingeschlossen. Die private Variable `_SNAPSHOT` wird durch ihren Unterstrich-Präfix ohnehin von Wildcard-Importen ausgeschlossen.

## 12.3 Das JSON-Metadaten-Format

Jede der 29 JSON-Dateien im Verzeichnis `src/reference_data/subsystems/` folgt einem einheitlichen Schema mit exakt vier Feldern:

```json
{
  "archive_name": "bridge",
  "package_name": "bridge",
  "module_count": 31,
  "sample_files": [
    "bridge/bridgeApi.ts",
    "bridge/bridgeConfig.ts",
    "bridge/bridgeDebug.ts",
    ...
  ]
}
```

### 12.3.1 `archive_name` (string)

Der kanonische Name des Subsystems in seiner urspruenglichen Schreibweise. Dieser Wert entspricht dem Verzeichnisnamen im originalen TypeScript-Projekt. Wie bereits erwähnt, weicht er bei `native-ts` vom Python-Paketnamen `native_ts` ab, da Python-Paketnamen keine Bindestriche enthalten duerfen.

### 12.3.2 `package_name` (string)

Der Python-konforme Paketname. In 28 von 29 Faellen ist er identisch mit dem `archive_name`. Nur bei `native_ts`/`native-ts` unterscheiden sich die beiden Werte. Dieses Feld ermöglicht es Werkzeugen, die korrekte Zuordnung zwischen dem originalen TypeScript-Verzeichnis und dem Python-Paket herzustellen.

### 12.3.3 `module_count` (integer)

Die Gesamtzahl der TypeScript-Module im originalen Subsystem. Dieser Wert ist eine exakte Zaehlung, nicht eine Schätzung. Er dient als Masseinheit für die Komplexitaet und den Umfang des jeweiligen Subsystems und ermöglicht Paritaetsprüfungen -- etwa um festzustellen, welcher Prozentsatz des Originals bereits portiert würde.

### 12.3.4 `sample_files` (array of strings)

Ein Array mit den relativen Dateipfaden der originalen TypeScript-Module. Die Pfade verwenden die Konventionen des Originals, einschließlich der TypeScript-Endungen `.ts` und `.tsx`. Bei Subsystemen mit wenigen Modulen (wie `coordinator` mit einem einzigen Modul `coordinatorMode.ts`) enthält dieses Array saemtliche Dateien. Bei großen Subsystemen wird eine repräsentative Stichprobe aufgeführt.

Die Dateipfade enthalten dabei stets den Subsystem-Ordner als Präfix, zum Beispiel `"bridge/bridgeApi.ts"` statt nur `"bridgeApi.ts"`. Diese Konvention sorgt dafür, dass die Pfade auch außerhalb ihres JSON-Kontextes eindeutig zuzuordnen sind.

## 12.4 Die 29 Subsysteme im Überblick

Die folgende Aufstellung listet alle 29 Subsysteme in absteigender Reihenfolge nach Modulzahl. Sie verdeutlicht die enorme Bandbreite: Das größte Subsystem (`utils`) umfasst 564 Module, während sieben Subsysteme aus nur einem einzigen Modul bestehen.

### 12.4.1 Die großen Subsysteme (100+ Module)

**utils (564 Module)** -- Das mit Abstand größte Subsystem ist die Werkzeugbibliothek. Sie enthält eine schier endlose Sammlung von Hilfsfunktionen und -klassen: vom `CircularBuffer` über `Shell`-Abstraktion, `QueryGuard`, `agentContext` bis hin zu spezialisierten Modulen wie `ansiToPng`, `apiPreconnect` oder `authFileDescriptor`. Die schiere Größe von 564 Modulen zeigt, dass die urspruengliche Anwendung eine umfangreiche interne Infrastruktur aufgebaut hat. Nahezu jede andere Komponente im System duerfte direkte oder indirekte Abhängigkeiten zu `utils` haben.

**components (389 Module)** -- Das zweitgrößte Subsystem umfasst die UI-Komponenten. Dateien wie `App.tsx`, `AgentProgressLine.tsx`, `BridgeDialog.tsx` oder `ContextVisualization.tsx` verraten, dass es sich um React-Komponenten handelt (die `.tsx`-Endung deutet auf JSX-Syntax hin). Bemerkenswert ist die Vielfalt: Von Dialogen (`AutoModeOptInDialog`, `BypassPermissionsModeDialog`, `CostThresholdDialog`) über Statusanzeigen (`CoordinatorAgentStatus`, `CompactSummary`) bis zu spezialisierten Eingabe-Widgets (`BaseTextInput`, `ConfigurableShortcutHint`). Dieses Subsystem bildet die gesamte Benutzeroberflaeche der Anwendung ab.

**services (130 Module)** -- Die Service-Schicht kapselt die Geschäftslogik. Hier finden sich klar strukturierte Subdomaenen: `AgentSummary` für Zusammenfassungen, `MagicDocs` für intelligente Dokumentation, `PromptSuggestion` für kontextabhängige Vorschlaege, `SessionMemory` für sitzungsübergreifende Erinnerungen. Der `analytics`-Bereich mit Modulen wie `datadog.ts`, `growthbook.ts` und `firstPartyEventLogger.ts` zeigt eine ausgefeilte Telemetrie-Infrastruktur. Die `api`-Untergruppe mit `claude.ts`, `client.ts` und `errorUtils.ts` bildet die Schnittstelle zum Backend.

**hooks (104 Module)** -- Dieses Subsystem enthält React-Hooks, ein Entwurfsmuster für zustandsbehaftete Logik in funktionalen Komponenten. Besonders auffaellig ist das `notifs`-Unterverzeichnis mit 17 spezialisierten Benachrichtigungs-Hooks: `useAutoModeUnavailableNotification`, `useDeprecationWarningNotification`, `useRateLimitWarningNotification` und viele mehr. Das `toolPermission`-Unterverzeichnis mit `PermissionContext.ts` und spezialisierten Handlern (`coordinatorHandler`, `interactiveHandler`, `swarmWorkerHandler`) zeigt ein differenziertes Berechtigungssystem.

### 12.4.2 Die mittleren Subsysteme (10-99 Module)

**bridge (31 Module)** -- Das Bridge-Subsystem implementiert die Kommunikationsbrücke zwischen verschiedenen Laufzeitumgebungen. Module wie `bridgeApi.ts`, `bridgeMessaging.ts`, `bridgePermissionCallbacks.ts` und `remoteBridgeCore.ts` deuten auf ein ausgefeiltes Nachrichtenprotokoll hin. `jwtUtils.ts` und `flushGate.ts` weisen auf Authentifizierung und Flusskontrolle hin. Dieses Subsystem ist offensichtlich geschaeftskritisch für die Anbindung an externe Systeme.

**constants (21 Module)** -- Eine Sammlung von Konstantendefinitionen, die das gesamte System durchziehen. Die Dateinamen sind selbstdokumentierend: `apiLimits.ts` definiert API-Grenzen, `betas.ts` steuert Feature-Flags für Betafunktionen, `cyberRiskInstruction.ts` enthält Sicherheitsrichtlinien, `prompts.ts` und `systemPromptSections.ts` definieren die Grundstruktur der KI-Prompts, und `spinnerVerbs.ts` sowie `turnCompletionVerbs.ts` steuern die Benutzeroberflaeche während Wartezeiten.

**skills (20 Module)** -- Das Skill-System repräsentiert erweiterbare Fähigkeiten der Anwendung. Im `bundled`-Unterverzeichnis finden sich fest eingebaute Skills wie `claudeApi.ts`, `loop.ts`, `remember.ts`, `simplify.ts` und `verify.ts`. `loadSkillsDir.ts` deutet darauf hin, dass neben den fest eingebauten Skills auch externe, verzeichnisbasierte Skills geladen werden koennen -- ein klassisches Plugin-Muster.

**cli (19 Module)** -- Das Kommandozeilen-Interface mit Handlern für verschiedene Befehle (`auth.ts`, `autoMode.ts`, `mcp.tsx`, `plugins.ts`), IO-Modulen (`remoteIO.ts`, `structuredIO.ts`) und einem bemerkenswerten `transports`-Unterverzeichnis mit `HybridTransport.ts`, `SSETransport.ts`, `WebSocketTransport.ts` und `WorkerStateUploader.ts` -- was auf multiple Kommunikationsstrategien hindeutet.

**keybindings (14 Module)** -- Ein vollständiges Tastenkürzel-System mit `defaultBindings.ts`, `loadUserBindings.ts`, `parser.ts`, `resolver.ts`, `validate.ts` und React-Integration (`KeybindingContext.tsx`, `useKeybinding.ts`). Die Existenz von `reservedShortcuts.ts` und `template.ts` deutet auf ein ausgereiftes, konfigurierbares System hin.

**migrations (11 Module)** -- Datenmigrationsskripte, die den Übergang zwischen verschiedenen Versionen der Anwendung ermöglichen. Die Dateinamen erzaehlen die Versionsgeschichte: `migrateFennecToOpus.ts`, `migrateLegacyOpusToCurrent.ts`, `migrateOpusToOpus1m.ts`, `migrateSonnet1mToSonnet45.ts`, `migrateSonnet45ToSonnet46.ts`. Man erkennt die Abfolge der Modellgenerationen und die Notwendigkeit, Benutzerkonfigurationen bei jedem Modellwechsel zu aktualisieren.

**types (11 Module)** -- TypeScript-Typdefinitionen, darunter `command.ts`, `hooks.ts`, `permissions.ts` und `plugin.ts`. Bemerkenswert sind die generierten Typen unter `generated/events_mono/`, die auf ein Schema-basiertes Codegenerierungssystem hindeuten -- vermutlich für Event-Tracking und Protokollpuffer.

### 12.4.3 Die kleinen Subsysteme (2-9 Module)

**memdir (8 Module)** -- Das Memory-Directory-System verwaltet persistente Erinnerungen. `findRelevantMemories.ts` sucht kontextabhängig nach relevanten Eintraegen, `memoryScan.ts` durchforstet den Speicher, `memoryAge.ts` verwaltet die Alterung von Eintraegen, und `teamMemPaths.ts` sowie `teamMemPrompts.ts` zeigen eine Team-Dimension des Erinnerungssystems.

**entrypoints (8 Module)** -- Die Einstiegspunkte der Anwendung: `cli.tsx` für die Kommandozeile, `mcp.ts` für das Model Context Protocol, `init.ts` für die Initialisierung. Das `sdk`-Unterverzeichnis mit `controlSchemas.ts`, `coreSchemas.ts` und `coreTypes.ts` definiert die SDK-Schnittstelle.

**buddy (6 Module)** -- Ein verspieltes Feature: `CompanionSprite.tsx` und `sprites.ts` deuten auf ein animiertes Begleit-Maskottchen hin. `companion.ts`, `prompt.ts` und `useBuddyNotification.tsx` integrieren dieses Feature in die Anwendung. Ein charmantes Detail in einer sonst streng technischen Architektur.

**state (6 Module)** -- Das zentrale Zustandsverwaltungssystem mit `AppState.tsx`, `AppStateStore.ts`, `store.ts` und `selectors.ts` -- ein klassisches State-Management-Muster, wie es aus Redux oder ähnlichen Bibliotheken bekannt ist. `teammateViewHelpers.ts` zeigt, dass der Zustand auch Multi-User-Szenarien unterstützt.

**vim (5 Module)** -- Eine Vim-Emulation mit `motions.ts`, `operators.ts`, `textObjects.ts`, `transitions.ts` und `types.ts`. Diese fünf Module bilden die grundlegenden Bausteine eines Vim-kompatiblen Editors: Bewegungen (wie `w`, `b`, `e`), Operatoren (wie `d`, `c`, `y`), Textobjekte (wie `iw`, `ap`) und Zustandsübergaenge zwischen den Modi.

**native_ts (4 Module)** -- TypeScript-Wrapper für native Bibliotheken: `color-diff` für Farbvergleiche, `file-index` für Dateiindizierung und `yoga-layout` für das Yoga-Layoutsystem (eine Cross-Platform-Layout-Engine von Meta). Dieses Subsystem ist das einzige, bei dem `archive_name` (`"native-ts"`) und `package_name` (`"native_ts"`) voneinander abweichen.

**remote (4 Module)** -- Fernsteuerungsfunktionalitaet mit `RemoteSessionManager.ts`, `SessionsWebSocket.ts`, `remotePermissionBridge.ts` und `sdkMessageAdapter.ts`. Dieses Subsystem ermöglicht die Steuerung der Anwendung aus der Ferne, beispielsweise über eine Web-Oberflaeche.

**screens (3 Module)** -- Die Hauptbildschirme der Anwendung: `Doctor.tsx` für die Systemdiagnose, `REPL.tsx` für die interaktive Sitzung und `ResumeConversation.tsx` für die Wiederaufnahme frueherer Gespraeche.

**server (3 Module)** -- Serverseitige Funktionalitaet für Direktverbindungen: `createDirectConnectSession.ts`, `directConnectManager.ts` und `types.ts`. Ein kompaktes, fokussiertes Subsystem.

**plugins (2 Module)** -- Das Plugin-System mit `builtinPlugins.ts` und `bundled/index.ts`. Die geringe Modulzahl täuscht: Dieses Subsystem dient als Registrierung und Lademechanismus für Plugins, die selbst in anderen Subsystemen definiert sein koennen.

**upstreamproxy (2 Module)** -- Ein Proxy-Subsystem mit `relay.ts` und `upstreamproxy.ts`, das vermutlich die Weiterleitung von Anfragen an vorgelagerte Server ermöglicht.

### 12.4.4 Die minimalen Subsysteme (1 Modul)

Sieben Subsysteme bestehen aus nur einem einzigen Modul:

**coordinator (1 Modul: `coordinatorMode.ts`)** -- Steuert den Koordinatormodus, in dem die Anwendung als Orchestrator für mehrere Agenten fungiert.

**moreright (1 Modul: `useMoreRight.tsx`)** -- Ein React-Hook, der vermutlich die "Mehr anzeigen"-Funktionalitaet in der rechten Seitenleiste steuert.

**schemas (1 Modul: `hooks.ts`)** -- Validierungsschemata für das Hook-System.

**outputStyles (1 Modul: `loadOutputStylesDir.ts`)** -- Laedt konfigurierbare Ausgabestile aus einem Verzeichnis.

**voice (1 Modul: `voiceModeEnabled.ts`)** -- Feature-Flag für die Sprachsteuerung.

**assistant (1 Modul)** -- Das zentrale Assistenten-Paket, das trotz seiner Modulzahl von 1 eine fundamentale Rolle in der Architektur spielt, da es den Kernbegriff "Assistent" im Namensraum verankert.

**bootstrap (1 Modul: `state.ts`)** -- Der Initialisierungszustand für den Anwendungsstart.

## 12.5 Statistische Analyse: Die Verteilung der Komplexitaet

Die Gesamtzahl aller Module über alle 29 Subsysteme beträgt circa 1.372. Die Verteilung ist extrem ungleich:

| Größenklasse | Subsysteme | Module gesamt | Anteil |
|---|---|---|---|
| Groß (100+) | 4 | 1.187 | ~86,5 % |
| Mittel (10-99) | 7 | 127 | ~9,3 % |
| Klein (2-9) | 11 | 51 | ~3,7 % |
| Minimal (1) | 7 | 7 | ~0,5 % |

Diese Verteilung folgt einem typischen Potenzgesetz: Eine kleine Anzahl von Subsystemen konzentriert einen überproportional großen Anteil der Komplexitaet. Allein `utils` und `components` umfassen zusammen 953 Module -- nahezu 70 Prozent des Gesamtsystems. Dies spiegelt ein gängiges Muster in gewachsenen Softwaresystemen wider, bei dem Werkzeug- und UI-Bibliotheken dazu neigen, über die Zeit erheblich anzuwachsen.

Für die Portierungsplanung ergibt sich daraus eine klare Priorisierung: Wer die vier großen Subsysteme (`utils`, `components`, `services`, `hooks`) portiert, hat bereits 86,5 Prozent des Modulumfangs abgedeckt. Gleichzeitig sind diese vier Subsysteme natürlich die komplexesten und erfordern den größten Aufwand.

## 12.6 Der Datenfluss: Vom JSON zum Python-Namensraum

Um das Zusammenspiel zwischen JSON-Metadaten und Python-Paketen vollständig zu verstehen, lohnt es sich, den Datenfluss Schritt für Schritt nachzuvollziehen. Betrachten wir, was geschieht, wenn ein Entwickler in einer Python-Shell folgenden Befehl eingibt:

```python
from bridge import MODULE_COUNT, SAMPLE_FILES
print(f"Das Bridge-Subsystem umfasst {MODULE_COUNT} Module.")
print(f"Beispieldateien: {SAMPLE_FILES[:3]}")
```

1. Python sucht das Paket `bridge` im Suchpfad und findet `src/bridge/__init__.py`.
2. Der Interpreter führt den Code in `__init__.py` aus.
3. `Path(__file__).resolve().parent.parent` ergibt `.../src/`.
4. Der Pfad `.../src/reference_data/subsystems/bridge.json` wird konstruiert.
5. `SNAPSHOT_PATH.read_text()` liest die JSON-Datei als String.
6. `json.loads()` parst den String in ein Dictionary:
   ```python
   {'archive_name': 'bridge', 'package_name': 'bridge', 'module_count': 31, 'sample_files': [...]}
   ```
7. Die Werte werden in die Modulkonstanten `ARCHIVE_NAME`, `MODULE_COUNT`, `SAMPLE_FILES` und `PORTING_NOTE` übertragen.
8. Die angeforderten Namen `MODULE_COUNT` und `SAMPLE_FILES` werden in den importierenden Namensraum gebunden.
9. Die Ausgabe erscheint:
   ```
   Das Bridge-Subsystem umfasst 31 Module.
   Beispieldateien: ('bridge/bridgeApi.ts', 'bridge/bridgeConfig.ts', 'bridge/bridgeDebug.ts')
   ```

Dieser Fluss zeigt, wie die Trennung zwischen statischen Daten (JSON) und dynamischer Logik (Python) saüber eingehalten wird. Die JSON-Dateien sind reine Datencontainer; die `__init__.py`-Dateien sind reine Lademechanismen. Keine der beiden Schichten enthält Geschäftslogik.

## 12.7 Architekturentscheidungen und ihre Begründung

### 12.7.1 Warum Platzhalter statt echter Implementierung?

Die Entscheidung, 29 Subsysteme als Platzhalter statt als vollständige Portierungen zu implementieren, gründet auf drei wesentlichen Überlegungen:

**Erstens: Metadaten-Abfrage zur Laufzeit.** Die Platzhalter-Architektur ermöglicht es, zur Laufzeit Informationen über die Struktur des Originalsystems abzufragen, ohne dass eine vollständige Portierung vorliegen muss. Ein Werkzeug zur Portierungsplanung kann beispielsweise alle 29 Subsysteme importieren, ihre `MODULE_COUNT`-Werte summieren und so den Gesamtumfang der ausstehenden Arbeit bestimmen. Ein Paritaetsprüfungsskript kann die `SAMPLE_FILES` mit tatsaechlich vorhandenen Python-Modulen vergleichen und den Portierungsfortschritt messen.

**Zweitens: Unterstützung der Paritaetsprüfung.** Im Claw-Code-Projekt existieren bereits Module wie `parity_audit.py` und `port_manifest.py`, die die strukturelle Übereinstimmung zwischen Original und Portierung prüfen. Die JSON-Metadaten liefern die Referenzdaten für diese Prüfungen. Ohne die Platzhalter-Architektur müssten diese Werkzeuge die Metadaten aus einer separaten Quelle beziehen -- beispielsweise aus einer monolithischen Konfigurationsdatei oder aus dem Dateisystem des Originalprojekts. Die dezentrale Speicherung in 29 JSON-Dateien, die jeweils direkt neben ihrem zugehörigen Python-Paket liegen, ist sowohl wartungsfreundlicher als auch robuster.

**Drittens: Vermeidung proprietaeren Codes.** Das Originalprojekt ist proprietaere Software. Eine vollständige Portierung würde bedeuten, den gesamten Quellcode zu kopieren und in Python zu übersetzen -- ein Vorgang, der sowohl urheberrechtlich problematisch als auch praktisch überfluessig wäre, solange das Ziel nicht die Ersetzung des Originals ist. Die Platzhalter-Architektur dokumentiert die Existenz und Struktur des Originals, ohne dessen Implementierungsdetails preiszugeben. Die `sample_files`-Listen zeigen lediglich Dateinamen, nicht Dateiinhalte.

### 12.7.2 Warum JSON statt Python-Literale?

Eine naheliegende Alternative wäre gewesen, die Metadaten direkt als Python-Literale in den `__init__.py`-Dateien zu speichern:

```python
# Hypothetische Alternative (NICHT so implementiert)
ARCHIVE_NAME = "bridge"
MODULE_COUNT = 31
SAMPLE_FILES = ("bridge/bridgeApi.ts", "bridge/bridgeConfig.ts", ...)
```

Die Entscheidung für JSON bietet jedoch mehrere Vorteile:

- **Sprachunabhängigkeit:** Die JSON-Dateien koennen von jedem Werkzeug gelesen werden, nicht nur von Python. Ein Shell-Skript, ein JavaScript-Tool oder ein CI/CD-Pipeline-Schritt kann die Metadaten direkt parsen.
- **Generierbarkeit:** Die JSON-Dateien würden offensichtlich automatisiert aus dem Originalprojekt generiert. Die Generierung eines JSON-Objekts ist einfacher und weniger fehleranfaellig als die Generierung von syntaktisch korrektem Python-Code.
- **Trennung von Daten und Code:** Änderungen an den Metadaten (etwa wenn im Original ein neues Modul hinzukommt) erfordern nur eine Änderung in der JSON-Datei. Der Python-Code in `__init__.py` bleibt unverändert. Diese Trennung vereinfacht automatisierte Updates erheblich.

### 12.7.3 Warum 29 separate Dateien statt einer einzigen?

Eine weitere Alternative wäre eine einzige, monolithische JSON-Datei gewesen, die alle 29 Subsysteme beschreibt. Die Entscheidung für separate Dateien folgt dem Prinzip der Lokalitaet: Jedes Subsystem verwaltet seine eigenen Metadaten. Dies erleichtert partielle Updates, vereinfacht das Debugging (bei einem Fehler weiß man sofort, welche JSON-Datei betroffen ist) und unterstützt parallele Entwicklung (zwei Entwickler koennen gleichzeitig an verschiedenen Subsystemen arbeiten, ohne Merge-Konflikte zu riskieren).

## 12.8 Praktische Nutzung: Beispiele und Anwendungsfaelle

### 12.8.1 Portierungsfortschritt ermitteln

```python
import importlib

subsystems = ['components', 'utils', 'services', 'hooks', 'bridge',
              'constants', 'skills', 'cli', 'keybindings', 'migrations',
              'types', 'memdir', 'entrypoints', 'buddy', 'state',
              'vim', 'native_ts', 'remote', 'screens', 'server',
              'plugins', 'upstreamproxy', 'coordinator', 'moreright',
              'schemas', 'outputStyles', 'voice', 'assistant', 'bootstrap']

total = 0
for name in subsystems:
    mod = importlib.import_module(name)
    total += mod.MODULE_COUNT
    print(f"{name:20s} {mod.MODULE_COUNT:4d} Module")

print(f"\nGesamt: {total} Module im Original")
```

### 12.8.2 Subsystem-Informationen abfragen

```python
from bridge import ARCHIVE_NAME, MODULE_COUNT, SAMPLE_FILES, PORTING_NOTE

print(PORTING_NOTE)
# Ausgabe: Python placeholder package for 'bridge' with 31 archived module references.

for f in SAMPLE_FILES[:5]:
    print(f"  - {f}")
```

### 12.8.3 Maschinenlesbare Bestandsaufnahme

```python
import json
from pathlib import Path

subsystem_dir = Path('src/reference_data/subsystems')
report = {}
for json_file in sorted(subsystem_dir.glob('*.json')):
    data = json.loads(json_file.read_text())
    report[data['archive_name']] = data['module_count']

print(json.dumps(report, indent=2, sort_keys=True))
```

## 12.9 Die Verzeichnisstruktur im Überblick

Die Subsystem-Architektur manifestiert sich in einer klaren Verzeichnisstruktur innerhalb von `src/`:

```
src/
  reference_data/
    subsystems/
      assistant.json
      bootstrap.json
      bridge.json
      buddy.json
      ... (29 JSON-Dateien insgesamt)
  assistant/
    __init__.py
  bootstrap/
    __init__.py
  bridge/
    __init__.py
  buddy/
    __init__.py
  ... (29 Paketverzeichnisse insgesamt)
```

Jedes der 29 Paketverzeichnisse enthält mindestens eine `__init__.py`-Datei. Diese Datei macht das Verzeichnis zu einem importierbaren Python-Paket und stellt gleichzeitig die Verbindung zur zugehörigen JSON-Metadatendatei her. Die `reference_data/subsystems/`-Verzeichnisstruktur ist bewusst von den Paketverzeichnissen getrennt -- sie gehört nicht zu einem bestimmten Subsystem, sondern dient als zentrale Datenablage für alle 29 Subsysteme.

## 12.10 Zusammenfassung

Die Subsystem-Architektur von Claw Code ist ein Paradebeispiel für durchdachtes Software-Design unter ungewoehnlichen Randbedingungen. Anstatt 1.372 TypeScript-Module blind in Python zu übersetzen oder die Strukturinformationen des Originals zu verwerfen, wählt das Projekt einen dritten Weg: Jedes der 29 Subsysteme wird durch ein minimales, aber informationsreiches Platzhalter-Paket repräsentiert.

Das einheitliche Muster -- identische `__init__.py`-Dateien, die ihre Metadaten aus standardisierten JSON-Dateien laden -- bietet mehrere entscheidende Vorteile:

- **Konsistenz:** Wer ein Subsystem kennt, kennt alle. Es gibt keine Sonderfaelle oder Überraschungen.
- **Wartbarkeit:** Änderungen am Muster koennen mechanisch auf alle 29 Pakete angewandt werden.
- **Abfragbarkeit:** Jedes Subsystem gibt programmatisch Auskunft über seinen Umfang und seine Struktur.
- **Erweiterbarkeit:** Neue Subsysteme koennen durch simples Kopieren des Musters und Erstellen einer JSON-Datei hinzugefuegt werden.
- **Integritaet:** Die Metadaten ermöglichen automatisierte Paritaetsprüfungen zwischen Original und Portierung.

Die 29 Subsysteme reichen von winzigen Einzelmodul-Paketen wie `voice` (1 Modul: `voiceModeEnabled.ts`) bis hin zu massiven Bibliotheken wie `utils` (564 Module). Zusammen dokumentieren sie die vollständige Oberflaeche eines komplexen TypeScript-Systems in einer Form, die sowohl für Menschen lesbar als auch für Maschinen auswertbar ist -- und die dabei keinen einzigen proprietaeren Codebaustein preisgibt.




# Chapter 13: Parity Checking & Quality Assurance

## 13.1 Einführung

In jedem größeren Software-Portierungsprojekt stellt sich frueher oder später eine zentrale Frage: Wie nahe ist der aktuelle Stand der Portierung am Original? Wenn ein umfangreiches TypeScript-Projekt nach Python übertragen wird, genuegt es nicht, einzelne Dateien zu übersetzen und auf das Beste zu hoffen. Es braucht systematische Werkzeuge, die den Fortschritt messen, Luecken aufdecken und den Gesamtzustand des Projekts quantifizieren koennen.

Das Claw-Code-Projekt löst dieses Problem mit drei eng verzahnten Bausteinen: dem **Parity Audit** (`src/parity_audit.py`), der die strukturelle Abdeckung zwischen dem archivierten TypeScript-Original und dem Python-Port misst; dem **Port Manifest** (`src/port_manifest.py`), das eine aktuelle Bestandsaufnahme des Python-Quellbaums liefert; und einer umfassenden **Testsuite** (`tests/test_porting_workspace.py`), die mit 24 Testmethoden das gesamte System end-to-end validiert, ohne auf Mocking zurückzugreifen.

Dieses Kapitel analysiert alle drei Komponenten im Detail. Wir beginnen mit dem Parity Audit, gehen dann zum Port Manifest über und schließen mit einer eingehenden Betrachtung der Testsuite ab.

---

## 13.2 Der Parity Audit (`src/parity_audit.py`)

### 13.2.1 Architektonischer Überblick

Die Datei `src/parity_audit.py` umfasst 139 Zeilen und bildet das Herzstück der Paritaetsmessung. Ihre Aufgabe ist es, den aktuellen Zustand des `src/`-Verzeichnisses mit den bekannten Strukturen des archivierten TypeScript-Originals zu vergleichen. Dabei werden mehrere Dimensionen der Abdeckung erfasst: Root-Dateien, Verzeichnisse, Gesamtdateizahl, Befehlsabdeckung und Werkzeugabdeckung.

Die Datei beginnt mit der Definition von vier Pfadkonstanten, die den gesamten Audit verankern:

```python
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent / 'archive' / 'claude_code_ts_snapshot' / 'src'
CURRENT_ROOT = Path(__file__).resolve().parent
REFERENCE_SURFACE_PATH = CURRENT_ROOT / 'reference_data' / 'archive_surface_snapshot.json'
COMMAND_SNAPSHOT_PATH = CURRENT_ROOT / 'reference_data' / 'commands_snapshot.json'
TOOL_SNAPSHOT_PATH = CURRENT_ROOT / 'reference_data' / 'tools_snapshot.json'
```

`ARCHIVE_ROOT` zeigt auf das archivierte TypeScript-Original unter `archive/claude_code_ts_snapshot/src`. `CURRENT_ROOT` ist das aktuelle `src/`-Verzeichnis des Python-Ports. Die drei JSON-Pfade verweisen auf Referenzdaten, die beim Erstellen des Archivs generiert würden und als Sollwerte für den Vergleich dienen.

### 13.2.2 ARCHIVE_ROOT_FILES: Die 18 Root-Datei-Mappings

Das Dictionary `ARCHIVE_ROOT_FILES` definiert eine explizite Zuordnung von 18 TypeScript-Quelldateien zu ihren erwarteten Python-Äquivalenten:

```python
ARCHIVE_ROOT_FILES = {
    'QueryEngine.ts': 'QueryEngine.py',
    'Task.ts': 'task.py',
    'Tool.ts': 'Tool.py',
    'commands.ts': 'commands.py',
    'context.ts': 'context.py',
    'cost-tracker.ts': 'cost_tracker.py',
    'costHook.ts': 'costHook.py',
    'dialogLaunchers.tsx': 'dialogLaunchers.py',
    'history.ts': 'history.py',
    'ink.ts': 'ink.py',
    'interactiveHelpers.tsx': 'interactiveHelpers.py',
    'main.tsx': 'main.py',
    'projectOnboardingState.ts': 'projectOnboardingState.py',
    'query.ts': 'query.py',
    'replLauncher.tsx': 'replLauncher.py',
    'setup.ts': 'setup.py',
    'tasks.ts': 'tasks.py',
    'tools.ts': 'tools.py',
}
```

Diese Zuordnungen spiegeln die zentralen Einstiegspunkte des Originals wider. Jede Zeile repräsentiert eine Kerndatei des TypeScript-Projekts und ihr Python-Gegenstück. Bemerkenswert ist, dass die Benennung nicht immer eins-zu-eins übernommen wird: `Task.ts` wird zu `task.py` (Kleinschreibung gemäß Python-Konvention), `cost-tracker.ts` wird zu `cost_tracker.py` (Bindestrich durch Unterstrich ersetzt), während `QueryEngine.ts` seinen CamelCase-Namen als `QueryEngine.py` behält. Die `.tsx`-Dateien (React-Komponenten wie `dialogLaunchers.tsx`, `interactiveHelpers.tsx`, `main.tsx`, `replLauncher.tsx`) werden ebenfalls auf reine `.py`-Dateien abgebildet, da die React-spezifische Rendering-Schicht in Python durch andere Mechanismen ersetzt wird.

Diese 18 Mappings bilden die "Root-Schicht" des Audits. Sie repräsentieren die oberste Ebene der Architektur: Einstiegspunkte, zentrale Engines, Hookpoints und Hilfsmodule, die direkt im Wurzelverzeichnis des Quellbaums liegen.

### 13.2.3 ARCHIVE_DIR_MAPPINGS: Die 35 Verzeichnis-Mappings

Das zweite Dictionary erfasst die Verzeichnisstruktur des Originals mit 35 Eintraegen:

```python
ARCHIVE_DIR_MAPPINGS = {
    'assistant': 'assistant',
    'bootstrap': 'bootstrap',
    'bridge': 'bridge',
    'buddy': 'buddy',
    'cli': 'cli',
    'commands': 'commands.py',
    'components': 'components',
    'constants': 'constants',
    'context': 'context.py',
    'coordinator': 'coordinator',
    'entrypoints': 'entrypoints',
    'hooks': 'hooks',
    ...
}
```

Hier zeigt sich ein wichtiges Architekturmuster des Portierungsprojekts: Nicht jedes TypeScript-Verzeichnis wird als eigenes Python-Package portiert. Manche Verzeichnisse werden zu einzelnen Dateien konsolidiert. So wird das gesamte `commands/`-Verzeichnis des Originals (das möglicherweise dutzende `.ts`-Dateien enthielt) im Python-Port durch eine einzige Datei `commands.py` abgebildet. Dasselbe gilt für `context/` (wird zu `context.py`), `ink/` (zu `ink.py`), `query/` (zu `query.py`), `tasks/` (zu `tasks.py`) und `tools/` (zu `tools.py`).

Die übrigen 29 Verzeichnisse behalten ihre Struktur als eigene Verzeichnisse bzw. Packages bei: `assistant`, `bootstrap`, `bridge`, `buddy`, `cli`, `components`, `constants`, `coordinator`, `entrypoints`, `hooks`, `keybindings`, `memdir`, `migrations`, `moreright`, `native_ts` (umbenannt von `native-ts`), `outputStyles`, `plugins`, `remote`, `schemas`, `screens`, `server`, `services`, `skills`, `state`, `types`, `upstreamproxy`, `utils`, `vim` und `voice`. Diese Vielfalt an Subsystemen zeigt den Umfang des Originalprojekts und die Breite der Portierungsarbeit.

### 13.2.4 ParityAuditResult: Die Ergebnis-Datenklasse

Das Ergebnis eines Audits wird in einer unveränderlichen Datenklasse (`frozen=True`) gekapselt:

```python
@dataclass(frozen=True)
class ParityAuditResult:
    archive_present: bool
    root_file_coverage: tuple[int, int]
    directory_coverage: tuple[int, int]
    total_file_ratio: tuple[int, int]
    command_entry_ratio: tuple[int, int]
    tool_entry_ratio: tuple[int, int]
    missing_root_targets: tuple[str, ...]
    missing_directory_targets: tuple[str, ...]
```

Jedes Feld erfuellt eine spezifische Rolle:

- **`archive_present`** (`bool`): Gibt an, ob das lokale Archiv des TypeScript-Originals vorhanden ist. Wenn der Archivordner fehlt (etwa in einer CI-Umgebung ohne das vollständige Repository), kann der Audit zwar laufen, liefert aber nur eingeschraenkte Ergebnisse.

- **`root_file_coverage`** (`tuple[int, int]`): Ein Paar aus (gefundene Dateien, erwartete Dateien). Bei vollständiger Abdeckung wäre dies `(18, 18)`. Der erste Wert zählt, wie viele der 18 erwarteten Python-Dateien im aktuellen `src/`-Verzeichnis tatsaechlich existieren.

- **`directory_coverage`** (`tuple[int, int]`): Analog für Verzeichnisse. Bei 35 erwarteten Zielen und 28 gefundenen wäre der Wert `(28, 35)`.

- **`total_file_ratio`** (`tuple[int, int]`): Verhältnis der aktuellen Python-Dateien zur Gesamtzahl der TypeScript-ähnlichen Dateien im Archiv. Dies wird aus der Referenzdatei `archive_surface_snapshot.json` geladen und gibt einen übergreifenden Indikator für den Portierungsfortschritt.

- **`command_entry_ratio`** (`tuple[int, int]`): Verhältnis der portierten Befehle zur Gesamtzahl im Original. Der erste Wert kommt aus `commands_snapshot.json`, der zweite aus der Referenzdatei.

- **`tool_entry_ratio`** (`tuple[int, int]`): Dasselbe für Werkzeuge (Tools). Quelle ist `tools_snapshot.json` gegenüber der Referenz.

- **`missing_root_targets`** (`tuple[str, ...]`): Eine Liste der Python-Dateinamen aus `ARCHIVE_ROOT_FILES`, die im aktuellen `src/`-Verzeichnis nicht gefunden würden. Diese Liste benennt konkret, welche Root-Dateien noch fehlen.

- **`missing_directory_targets`** (`tuple[str, ...]`): Analog die fehlenden Verzeichnis- oder Dateiziele aus `ARCHIVE_DIR_MAPPINGS`.

Die Verwendung von `frozen=True` und ausschließlich unver aenderlichen Typen (`bool`, `tuple`) macht `ParityAuditResult` zu einem wertbasierten, thread-sicheren Objekt. Es kann bedenkenlos zwischengespeichert, serialisiert oder in Tests verglichen werden, ohne dass Seiteneffekte befürchtet werden müssen.

### 13.2.5 `run_parity_audit()`: Die Kernlogik

Die Funktion `run_parity_audit()` führt den eigentlichen Vergleich durch:

```python
def run_parity_audit() -> ParityAuditResult:
    current_entries = {path.name for path in CURRENT_ROOT.iterdir()}
    root_hits = [target for target in ARCHIVE_ROOT_FILES.values() if target in current_entries]
    dir_hits = [target for target in ARCHIVE_DIR_MAPPINGS.values() if target in current_entries]
    missing_roots = tuple(target for target in ARCHIVE_ROOT_FILES.values() if target not in current_entries)
    missing_dirs = tuple(target for target in ARCHIVE_DIR_MAPPINGS.values() if target not in current_entries)
    current_python_files = sum(1 for path in CURRENT_ROOT.rglob('*.py') if path.is_file())
    reference = _reference_surface()
    ...
```

Der Algorithmus folgt einem klaren Schema:

1. **Bestandsaufnahme**: Alle Eintraege (Dateien und Verzeichnisse) im aktuellen `src/`-Verzeichnis werden als Menge von Namen erfasst (`current_entries`).

2. **Root-Abgleich**: Für jedes Ziel in `ARCHIVE_ROOT_FILES.values()` wird geprüft, ob es in `current_entries` existiert. Treffer werden in `root_hits` gesammelt, Fehlstellen in `missing_roots`.

3. **Verzeichnis-Abgleich**: Dasselbe geschieht für `ARCHIVE_DIR_MAPPINGS.values()` mit `dir_hits` und `missing_dirs`.

4. **Python-Dateizaehlung**: Ein rekursiver Scan (`rglob('*.py')`) zählt alle Python-Dateien im gesamten Quellbaum.

5. **Referenzdaten laden**: Die Funktion `_reference_surface()` liest `archive_surface_snapshot.json` ein, das Sollwerte wie `total_ts_like_files`, `command_entry_count` und `tool_entry_count` enthält.

6. **Snapshot-Zaehlung**: Die Hilfsfunktion `_snapshot_count()` liest die JSON-Arrays in `commands_snapshot.json` und `tools_snapshot.json` und gibt deren Laenge zurück.

7. **Ergebnis-Assembly**: Alle gesammelten Werte werden zu einem `ParityAuditResult` zusammengefuegt.

Bemerkenswert ist, dass die Funktion keine Ausnahmen wirft, wenn das Archiv fehlt. Stattdessen wird `archive_present=ARCHIVE_ROOT.exists()` gesetzt und der Aufrufer kann das Ergebnis entsprechend interpretieren.

### 13.2.6 `to_markdown()`: Berichtsformatierung

Die Methode `to_markdown()` auf `ParityAuditResult` erzeugt einen menschenlesbaren Markdown-Bericht:

```python
def to_markdown(self) -> str:
    lines = ['# Parity Audit']
    if not self.archive_present:
        lines.append('Local archive unavailable; parity audit cannot compare against the original snapshot.')
        return '\n'.join(lines)
    lines.extend([
        '',
        f'Root file coverage: **{self.root_file_coverage[0]}/{self.root_file_coverage[1]}**',
        f'Directory coverage: **{self.directory_coverage[0]}/{self.directory_coverage[1]}**',
        ...
    ])
```

Wenn das Archiv nicht vorhanden ist, wird sofort ein Kurztext zurückgegeben. Andernfalls werden alle fünf Metriken in fettgedruckten Bruchzahlen dargestellt, gefolgt von Listen der fehlenden Root-Dateien und Verzeichnisse. Falls nichts fehlt, erscheint `- none`. Diese Formatierung eignet sich sowohl für die Terminalausgabe (via `src.main parity-audit`) als auch für die Integration in automatisierte Berichte.

---

## 13.3 Das Port Manifest (`src/port_manifest.py`)

### 13.3.1 Zweck und Aufbau

Während der Parity Audit den Python-Port gegen das TypeScript-Original misst, liefert das Port Manifest eine eigenständige Bestandsaufnahme des Python-Quellbaums. Die Datei `src/port_manifest.py` umfasst 53 Zeilen und besteht aus einer Datenklasse und einer Erzeuger-Funktion.

### 13.3.2 Die Datenklasse `PortManifest`

```python
@dataclass(frozen=True)
class PortManifest:
    src_root: Path
    total_python_files: int
    top_level_modules: tuple[Subsystem, ...]
```

Die drei Felder erfassen:

- **`src_root`** (`Path`): Der Wurzelpfad des gescannten Quellbaums. Standardmäßig ist dies `src/`, kann aber über den Parameter von `build_port_manifest()` überschrieben werden.

- **`total_python_files`** (`int`): Die Gesamtzahl aller `.py`-Dateien im Quellbaum.

- **`top_level_modules`** (`tuple[Subsystem, ...]`): Eine nach Dateizahl absteigend sortierte Liste der Top-Level-Module. Jedes Modul wird durch die Datenklasse `Subsystem` repräsentiert, die in `src/models.py` definiert ist:

```python
@dataclass(frozen=True)
class Subsystem:
    name: str
    path: str
    file_count: int
    notes: str
```

`Subsystem` erfasst also den Namen, den Pfad relativ zum Projektverzeichnis, die Anzahl der enthaltenen Python-Dateien und einen beschreibenden Text.

### 13.3.3 `build_port_manifest()`: Filesystem-Scan und Modulzaehlung

Die Erzeuger-Funktion führt den eigentlichen Scan durch:

```python
def build_port_manifest(src_root: Path | None = None) -> PortManifest:
    root = src_root or DEFAULT_SRC_ROOT
    files = [path for path in root.rglob('*.py') if path.is_file()]
    counter = Counter(
        path.relative_to(root).parts[0] if len(path.relative_to(root).parts) > 1 else path.name
        for path in files
        if path.name != '__pycache__'
    )
```

Der Algorithmus ist elegant in seiner Einfachheit:

1. **Dateien sammeln**: Alle `.py`-Dateien werden rekursiv aufgelistet.

2. **Top-Level-Zuordnung**: Für jede Datei wird der erste Pfadteil relativ zum Root bestimmt. Dateien in Unterverzeichnissen werden ihrem übergeordneten Verzeichnis zugeordnet (z.B. `utils/formatting.py` wird dem Modul `utils` zugeordnet). Dateien direkt im Root-Verzeichnis behalten ihren eigenen Dateinamen als Schlüssel (z.B. `main.py`).

3. **Cache-Ausschluss**: `__pycache__`-Eintraege werden herausgefiltert, um kompilierte Bytecode-Dateien nicht mitzuzaehlen.

4. **Zaehlung**: `collections.Counter` zählt die Dateien pro Top-Level-Modul und ermöglicht über `most_common()` eine absteigende Sortierung.

Anschließend werden die Zaehlungen in `Subsystem`-Objekte umgewandelt:

```python
notes = {
    '__init__.py': 'package export surface',
    'main.py': 'CLI entrypoint',
    'port_manifest.py': 'workspace manifest generation',
    'query_engine.py': 'port orchestration summary layer',
    'commands.py': 'command backlog metadata',
    'tools.py': 'tool backlog metadata',
    'models.py': 'shared dataclasses',
    'task.py': 'task-level planning structures',
}
modules = tuple(
    Subsystem(name=name, path=f'src/{name}', file_count=count,
              notes=notes.get(name, 'Python port support module'))
    for name, count in counter.most_common()
)
```

Das `notes`-Dictionary ordnet bekannten Dateinamen beschreibende Texte zu. Alle unbekannten Module erhalten den Standardtext `'Python port support module'`. Die Methode `to_markdown()` auf `PortManifest` formatiert diese Informationen als Aufzaehlungsliste mit Dateianzahlen und Beschreibungen.

### 13.3.4 Zusammenspiel mit dem Parity Audit

Port Manifest und Parity Audit ergaenzen sich komplementaer: Das Manifest beantwortet die Frage "Was haben wir?", der Audit beantwortet "Was fehlt noch?". Beide werden über die CLI (`src.main summary` bzw. `src.main parity-audit`) zugänglich gemacht und durch die Query Engine (`QueryEnginePort.from_workspace()`) in einem übergreifenden Bericht zusammengeführt.

---

## 13.4 Die Testsuite (`tests/test_porting_workspace.py`)

### 13.4.1 Philosophie und Testarchitektur

Die Testdatei `tests/test_porting_workspace.py` enthält 24 Testmethoden in einer einzigen Testklasse `PortingWorkspaceTests`, die von `unittest.TestCase` erbt. Das herausragende Merkmal dieser Suite ist ihr konsequenter Verzicht auf Mocking. Statt einzelne Funktionen zu isolieren und ihre Abhängigkeiten zu simulieren, führen die Tests echte Operationen gegen den realen Quellbaum durch. CLI-Tests starten tatsaechliche Subprozesse mit `subprocess.run()`, Manifest-Tests scannen das echte Dateisystem, und Parity-Tests laden die realen Referenzdaten.

Dieser Ansatz hat tiefgreifende Konsequenzen: Die Tests sind **empfindlich gegenüber echten DatenÄnderungen**. Wenn eine Datei umbenannt wird, ein Verzeichnis hinzukommt oder eine Referenzdatei aktualisiert wird, koennen Tests fehlschlagen. Das ist beabsichtigt -- die Suite dient als Fruehwarnsystem für unbeabsichtigte StrukturÄnderungen.

Die Importe am Dateianfang zeigen die Abhängigkeiten:

```python
from src.commands import PORTED_COMMANDS
from src.parity_audit import run_parity_audit
from src.port_manifest import build_port_manifest
from src.query_engine import QueryEnginePort
from src.tools import PORTED_TOOLS
```

### 13.4.2 Manifest-Tests

**`test_manifest_counts_python_files`**: Der grundlegendste Test der Suite. Er ruft `build_port_manifest()` auf und prüft zwei Bedingungen: Die Gesamtzahl der Python-Dateien muss mindestens 20 betragen, und die Liste der Top-Level-Module darf nicht leer sein.

```python
def test_manifest_counts_python_files(self) -> None:
    manifest = build_port_manifest()
    self.assertGreaterEqual(manifest.total_python_files, 20)
    self.assertTrue(manifest.top_level_modules)
```

Dieser Test würde fehlschlagen, wenn ein katastrophaler Refactoring-Fehler die meisten Python-Dateien loeschen würde. Die Schwelle von 20 ist bewusst niedrig gewählt -- sie soll nicht den exakten Bestand prüfen, sondern nur sicherstellen, dass der Quellbaum überhaupt substantiell vorhanden ist.

### 13.4.3 Query-Engine-Tests

**`test_query_engine_summary_mentions_workspace`**: Dieser Test erzeugt eine `QueryEnginePort`-Instanz über die Fabrikmethode `from_workspace()` und prüft, ob die gerenderte Zusammenfassung die erwarteten Überschriften enthält:

```python
def test_query_engine_summary_mentions_workspace(self) -> None:
    summary = QueryEnginePort.from_workspace().render_summary()
    self.assertIn('Python Porting Workspace Summary', summary)
    self.assertIn('Command surface:', summary)
    self.assertIn('Tool surface:', summary)
```

Dieser Test validiert die Integration zwischen Query Engine, Port Manifest, Kommando-Inventar und Tool-Inventar. Wenn eine dieser Komponenten ausfaellt oder ihr Format ändert, schlaegt der Test fehl.

### 13.4.4 CLI-Integrationstests

Die größte Kategorie der Suite sind die CLI-Integrationstests. Sie starten den Python-Interpreter als Subprozess und führen verschiedene CLI-Befehle aus. Das Muster ist immer dasselbe:

```python
result = subprocess.run(
    [sys.executable, '-m', 'src.main', '<befehl>', ...],
    check=True,
    capture_output=True,
    text=True,
)
self.assertIn('<erwarteter_text>', result.stdout)
```

`check=True` sorgt dafür, dass jeder Nicht-Null-Exit-Code eine `CalledProcessError`-Ausnahme auslöst, die den Test sofort scheitern lässt. `capture_output=True` und `text=True` erfassen stdout und stderr als Strings zur Überprüfung.

Die einzelnen CLI-Tests decken das gesamte Befehlsspektrum ab:

**`test_cli_summary_runs`**: Testet den `summary`-Befehl und prüft, ob die Ausgabe die Workspace-Zusammenfassung enthält.

**`test_parity_audit_runs`**: Testet den `parity-audit`-Befehl und prüft auf die Überschrift "Parity Audit".

**`test_commands_and_tools_cli_run`**: Testet die Befehle `commands` und `tools` mit Filtern (`--limit 5`, `--query review` bzw. `--query MCP`). Prüft, ob die Ausgabe `Command entries:` bzw. `Tool entries:` enthält.

**`test_route_and_show_entry_cli_run`**: Testet drei Befehle in Folge: `route` (Routing einer Anfrage zu passenden Eintraegen), `show-command` (Detailansicht eines Befehls) und `show-tool` (Detailansicht eines Tools). Dieser Test validiert die Such- und Anzeigefunktionalitaet des Systems.

```python
def test_route_and_show_entry_cli_run(self) -> None:
    route_result = subprocess.run(
        [sys.executable, '-m', 'src.main', 'route', 'review MCP tool', '--limit', '5'],
        check=True, capture_output=True, text=True,
    )
    show_command = subprocess.run(
        [sys.executable, '-m', 'src.main', 'show-command', 'review'],
        check=True, capture_output=True, text=True,
    )
    show_tool = subprocess.run(
        [sys.executable, '-m', 'src.main', 'show-tool', 'MCPTool'],
        check=True, capture_output=True, text=True,
    )
    self.assertIn('review', route_result.stdout.lower())
    self.assertIn('review', show_command.stdout.lower())
    self.assertIn('mcptool', show_tool.stdout.lower())
```

**`test_bootstrap_cli_runs`**: Testet den `bootstrap`-Befehl, der eine vollständige Laufzeitsitzung startet. Die Ausgabe muss `Runtime Session`, `Startup Steps` und `Routed Matches` enthalten.

**`test_exec_command_and_tool_cli_run`**: Testet die `exec-command`- und `exec-tool`-Befehle, die einzelne Befehle bzw. Tools ausführen. Die erwarteten Ausgaben sind `"Mirrored command 'review'"` und `"Mirrored tool 'MCPTool'"`.

**`test_setup_report_and_registry_filters_run`**: Testet den `setup-report`-Befehl sowie gefilterte Auflistungen (`--no-plugin-commands`, `--simple-mode`, `--no-mcp`). Dieser Test validiert, dass die verschiedenen Filteroptionen die CLI nicht zum Absturz bringen und die erwarteten Überschriften weiterhin erscheinen.

**`test_load_session_cli_runs`**: Einer der komplexeren Tests. Er erzeugt zunächst eine Bootstrap-Session über die Python-API, extrahiert deren Session-ID aus dem persistierten Pfad und laedt sie dann über den `load-session`-CLI-Befehl erneut:

```python
def test_load_session_cli_runs(self) -> None:
    from src.runtime import PortRuntime
    session = PortRuntime().bootstrap_session('review MCP tool', limit=5)
    session_id = Path(session.persisted_session_path).stem
    result = subprocess.run(
        [sys.executable, '-m', 'src.main', 'load-session', session_id],
        check=True, capture_output=True, text=True,
    )
    self.assertIn(session_id, result.stdout)
    self.assertIn('messages', result.stdout)
```

Dieser Test validiert den gesamten Session-Lebenszyklus: Erzeugung, Persistierung und Wiederherstellung.

**`test_tool_permission_filtering_cli_runs`**: Testet das Tool-Berechtigungssystem über den `--deny-prefix`-Filter. Wenn `mcp` als abgelehntes Präfix angegeben wird, darf `MCPTool` nicht in der Ausgabe erscheinen:

```python
def test_tool_permission_filtering_cli_runs(self) -> None:
    result = subprocess.run(
        [sys.executable, '-m', 'src.main', 'tools', '--limit', '10', '--deny-prefix', 'mcp'],
        check=True, capture_output=True, text=True,
    )
    self.assertIn('Tool entries:', result.stdout)
    self.assertNotIn('MCPTool', result.stdout)
```

Dies ist einer der wenigen Tests, der eine Negativbedingung (`assertNotIn`) prüft. Er stellt sicher, dass das Berechtigungssystem tatsaechlich Eintraege herausfiltert.

**`test_turn_loop_cli_runs`**: Testet den `turn-loop`-Befehl, der eine mehrstufige Ausführungsschleife simuliert. Mit `--max-turns 2` und `--structured-output` wird geprüft, ob die Ausgabe Turnnummern und Abbruchgründe enthält.

**`test_remote_mode_clis_run`**: Testet drei Fernzugriffsmodi: `remote-mode`, `ssh-mode` und `teleport-mode`. Jeder muss seinen jeweiligen Modusnamen in der Ausgabe enthalten.

**`test_flush_transcript_cli_runs`**: Testet den `flush-transcript`-Befehl und prüft auf `flushed=True` in der Ausgabe.

**`test_command_graph_and_tool_pool_cli_run`**: Testet die strukturellen Übersichtsbefehle `command-graph` und `tool-pool`.

**`test_setup_report_mentions_deferred_init`**: Ein spezifischerer Test für den Setup-Bericht, der prüft, ob die verzoegte Initialisierung korrekt dokumentiert wird (`Deferred init:` und `plugin_init=True`).

**`test_bootstrap_graph_and_direct_modes_run`**: Testet `bootstrap-graph`, `direct-connect-mode` und `deep-link-mode`.

### 13.4.5 Inventory-Tests

**`test_command_and_tool_snapshots_are_nontrivial`**: Prüft direkt die importierten Daten `PORTED_COMMANDS` und `PORTED_TOOLS` auf Mindestgrößen:

```python
def test_command_and_tool_snapshots_are_nontrivial(self) -> None:
    self.assertGreaterEqual(len(PORTED_COMMANDS), 150)
    self.assertGreaterEqual(len(PORTED_TOOLS), 100)
```

Diese Schwellenwerte (150 Befehle, 100 Tools) dienen als Regressionsschutz: Wenn ein fehlerhafter Import oder eine Änderung an den Snapshot-Dateien die Listen drastisch verkürzt, schlaegt dieser Test an.

**`test_subsystem_packages_expose_archive_metadata`**: Prüft, ob die Subsystem-Packages (`assistant`, `bridge`, `utils`) ihre Metadaten korrekt exponieren:

```python
def test_subsystem_packages_expose_archive_metadata(self) -> None:
    from src import assistant, bridge, utils
    self.assertGreater(assistant.MODULE_COUNT, 0)
    self.assertGreater(bridge.MODULE_COUNT, 0)
    self.assertGreater(utils.MODULE_COUNT, 100)
    self.assertTrue(utils.SAMPLE_FILES)
```

Besonders bemerkenswert ist die Prüfung `utils.MODULE_COUNT > 100`, die zeigt, dass das `utils`-Subsystem im Original über 100 Module umfasste -- ein Hinweis auf die Größe des TypeScript-Originals.

### 13.4.6 Session- und Runtime-Tests

**`test_bootstrap_session_tracks_turn_state`**: Dieser Test verwendet die Python-API direkt (ohne CLI-Subprozess) und prüft den internen Zustand einer Bootstrap-Session:

```python
def test_bootstrap_session_tracks_turn_state(self) -> None:
    from src.runtime import PortRuntime
    session = PortRuntime().bootstrap_session('review MCP tool', limit=5)
    self.assertGreaterEqual(len(session.turn_result.matched_tools), 1)
    self.assertIn('Prompt:', session.turn_result.output)
    self.assertGreaterEqual(session.turn_result.usage.input_tokens, 1)
```

Hier wird geprüft, ob die Session mindestens ein gematchtes Tool enthält, ob die Ausgabe einen Prompt-Abschnitt hat und ob die Usage-Informationen (Eingabe-Token) plausible Werte enthalten.

### 13.4.7 Parity-Tests

**`test_root_file_coverage_is_complete_when_local_archive_exists`**: Der zentrale Paritaetstest, der die Ergebnisse von `run_parity_audit()` validiert:

```python
def test_root_file_coverage_is_complete_when_local_archive_exists(self) -> None:
    audit = run_parity_audit()
    if audit.archive_present:
        self.assertEqual(audit.root_file_coverage[0], audit.root_file_coverage[1])
        self.assertGreaterEqual(audit.directory_coverage[0], 28)
        self.assertGreaterEqual(audit.command_entry_ratio[0], 150)
        self.assertGreaterEqual(audit.tool_entry_ratio[0], 100)
```

Dieser Test ist bedingt: Er prüft nur bei vorhandenem Archiv. Dann verlangt er aber volle Root-File-Abdeckung (alle 18 von 18), mindestens 28 von 35 Verzeichnissen, mindestens 150 Befehle und mindestens 100 Tools. Die bedingte Ausführung ist ein pragmatischer Kompromiss: In Umgebungen ohne Archiv-Zugang würde ein strikter Test ständig fehlschlagen.

### 13.4.8 Registry-Tests

**`test_execution_registry_runs`**: Testet die Execution Registry, die Befehle und Tools als ausführbare Objekte bereitstellt:

```python
def test_execution_registry_runs(self) -> None:
    from src.execution_registry import build_execution_registry
    registry = build_execution_registry()
    self.assertGreaterEqual(len(registry.commands), 150)
    self.assertGreaterEqual(len(registry.tools), 100)
    self.assertIn('Mirrored command', registry.command('review').execute('review security'))
    self.assertIn('Mirrored tool', registry.tool('MCPTool').execute('fetch mcp resources'))
```

Dieser Test geht über bloße Zaehlung hinaus: Er führt tatsaechlich einen Befehl und ein Tool aus und prüft die Rückgabewerte. Das Wort "Mirrored" in der Ausgabe deutet darauf hin, dass die aktuelle Implementierung die Befehle noch nicht vollständig portiert hat, sondern sie als "gespiegelte" Platzhalter ausführt.

### 13.4.9 Permission-Tests

Der Test `test_tool_permission_filtering_cli_runs` (bereits in Abschnitt 13.4.4 beschrieben) ist der zentrale Berechtigungstest. Er stellt sicher, dass das `--deny-prefix`-System tatsaechlich Tools aus der Ausgabe entfernt, wenn deren Name mit dem angegebenen Präfix beginnt. Dies ist kritisch für Sicherheitsszenarien, in denen bestimmte Tools (etwa MCP-basierte externe Werkzeuge) gezielt blockiert werden sollen.

---

## 13.5 Zusammenspiel der drei Komponenten

Die drei in diesem Kapitel behandelten Dateien bilden ein geschlossenes Qualitaetssicherungssystem:

1. **Port Manifest** scannt den Quellbaum und liefert aktuelle Kennzahlen (Gesamtdateien, Module, Dateiverteilung).

2. **Parity Audit** vergleicht diese Kennzahlen mit den Referenzdaten des TypeScript-Originals und identifiziert Luecken.

3. **Testsuite** validiert beides -- sowohl die korrekte Funktion der Audit-Werkzeuge als auch die Integritaet der gesamten CLI und Runtime.

Dieses Dreigespann erzeugt einen Feedbackkreislauf: Wenn ein Entwickler eine neue Datei portiert, aktualisiert sich das Manifest automatisch beim nächsten Scan. Der Parity Audit reflektiert die verbesserte Abdeckung. Und die Tests stellen sicher, dass dabei nichts anderes kaputtgegangen ist.

Die Entscheidung gegen Mocking in der Testsuite ist dabei von besonderer Bedeutung. In einem Portierungsprojekt, bei dem sich die interne Struktur ständig weiterentwickelt, würden umfangreiche Mocks ständig hinterherhinken und falsche Sicherheit vermitteln. Die End-to-End-Tests dagegen fangen tatsaechliche Brueche auf -- allerdings zum Preis längerer Ausführungszeiten und der Abhängigkeit von einem korrekt eingerichteten Arbeitsverzeichnis.

---

## 13.6 Quantitative Schwellenwerte und ihre Bedeutung

Über die gesamte Testsuite hinweg finden sich wiederkehrende Schwellenwerte:

| Metrik | Schwellenwert | Bedeutung |
|--------|---------------|-----------|
| `total_python_files` | >= 20 | Minimalbestand des Quellbaums |
| `PORTED_COMMANDS` | >= 150 | Mindestanzahl portierter Befehle |
| `PORTED_TOOLS` | >= 100 | Mindestanzahl portierter Werkzeuge |
| `directory_coverage` | >= 28 | Mindestens 28 von 35 Verzeichnissen abgebildet |
| `root_file_coverage` | 18/18 | Vollständige Abdeckung aller Root-Dateien |
| `utils.MODULE_COUNT` | > 100 | Archiv-Metadaten für das utils-Subsystem |

Diese Schwellenwerte sind bewusst als Untergrenzen formuliert. Sie steigen nicht automatisch mit dem Projektfortschritt, sondern dienen als Sicherheitsnetz gegen Regressionen. Wenn das Projekt wächst, koennen und sollten diese Werte nach oben angepasst werden.

---

## 13.7 Zusammenfassung

Das Paritaetsprüfungs- und Qualitaetssicherungssystem von Claw Code verfolgt einen pragmatischen, datengetriebenen Ansatz. Der Parity Audit misst die strukturelle Nähe zum Original über fünf klar definierte Metriken. Das Port Manifest liefert die Grundlage dafür durch einen automatisierten Filesystem-Scan. Und die Testsuite bindet alles zusammen, indem sie sowohl die Werkzeuge selbst als auch das gesamte CLI end-to-end validiert.

Die Architektur zeigt, wie Qualitaetssicherung in einem Portierungsprojekt aussehen kann: nicht als nachtraegliche Pflicht, sondern als integraler Bestandteil des Entwicklungsworkflows. Jeder CLI-Befehl wird getestet, jede Metrik wird validiert, und fehlende Portierungsziele werden namentlich aufgelistet. So wird der Fortschritt messbar und die nächsten Schritte offensichtlich.




# Chapter 14: Summary and Outlook

## 14.1 Einleitung: Was wir gebaut haben -- und warum es wichtig ist

Dieses Buch hat sich in dreizehn Kapiteln mit einem Projekt beschaeftigt, das in einer einzigen Nacht entstand und seither nicht aufgehört hat, Fragen aufzuwerfen -- technische, architektonische und ethische. Claw Code begann als Reaktion auf die Offenlegung des Claude-Code-Quellcodes am 31. Maerz 2026 und würde innerhalb weniger Stunden zu einem der am schnellsten wachsenden Open-Source-Projekte auf GitHub. Doch hinter den 30.000 Stars und den Schlagzeilen steckt eine tiefere Geschichte: die Geschichte eines systematischen Versuchs, eine komplexe Agent-Harness-Architektur zu verstehen, zu dokumentieren und in einer anderen Programmiersprache von Grund auf nachzubauen.

In diesem abschließenden Kapitel ziehen wir Bilanz. Wir schauen zurück auf den aktuellen Stand des Projekts, fassen die architektonischen Errungenschaften zusammen, würdigen die eingesetzten Design Patterns und blicken nach vorn -- auf die Rust-Portierung, auf offene Fragen und auf das, was andere Entwicklerinnen und Entwickler aus diesem Projekt lernen koennen.

---

## 14.2 Der aktuelle Stand des Projekts

### 14.2.1 Zahlen und Fakten

Zum Zeitpunkt der Drucklegung umfasst der Python-Quellbaum unter `src/` rund 66 Python-Dateien, verteilt auf 32 Verzeichnisse beziehungsweise Subsystem-Pakete. Die Gesamtstruktur des Repositories ist bewusst schlank gehalten:

- **66 Python-Dateien** im `src/`-Baum, von Root-Level-Modulen wie `models.py`, `commands.py`, `tools.py` und `query_engine.py` bis hin zu Subsystem-Platzhalter-Paketen wie `cli/`, `hooks/`, `skills/`, `voice/` und vielen weiteren.
- **207 gespiegelte Befehle** und **184 gespiegelte Tools**, erfasst als JSON-Referenzdaten unter `src/reference_data/` und über `lru_cache`-gestützte Ladefunktionen in `commands.py` und `tools.py` zugänglich gemacht.
- **24 CLI-Befehle** über `main.py` erreichbar, darunter `summary`, `manifest`, `subsystems`, `commands`, `tools` und `parity-audit`.
- **49 Testfaelle** in der `tests/`-Verzeichnisstruktur, die den aktuellen Python-Arbeitsbereich verifizieren.
- **Keine externen Abhängigkeiten**: Das gesamte Projekt laeuft mit der Python-Standardbibliothek. Keine `requirements.txt`, kein `pip install`, keine Third-Party-Pakete. Dies ist eine bewusste Designentscheidung, die wir in den frueheren Kapiteln ausführlich begründet haben.

### 14.2.2 Was abgedeckt ist

Die Root-Datei-Abdeckung -- also die Frage, ob für jede wesentliche Datei im urspruenglichen TypeScript-Quellbaum ein Python-Äquivalent existiert -- ist weitgehend vollständig. Jedes der über 30 Subsystem-Verzeichnisse des Originals hat ein entsprechendes Python-Paket erhalten, und zwar nicht als leere Huelsen, sondern als strukturierte Platzhalter, die über JSON-Snapshots die Metadaten des Originals referenzieren. Ein typisches Subsystem-Paket wie `src/cli/__init__.py` laedt beim Import seinen JSON-Snapshot aus `src/reference_data/subsystems/cli.json` und stellt Informationen wie den Archivnamen, die Modulanzahl und Beispieldateien als Python-Konstanten bereit.

Die Verzeichnis-Abdeckung ist ebenfalls weitgehend komplett. Die 32 Unterverzeichnisse unter `src/` spiegeln die Subsystemstruktur des Originals wider: `assistant/`, `bootstrap/`, `bridge/`, `buddy/`, `cli/`, `components/`, `constants/`, `coordinator/`, `entrypoints/`, `hooks/`, `keybindings/`, `memdir/`, `migrations/`, `moreright/`, `native_ts/`, `outputStyles/`, `plugins/`, `reference_data/`, `remote/`, `schemas/`, `screens/`, `server/`, `services/`, `skills/`, `state/`, `types/`, `upstreamproxy/`, `utils/`, `vim/` und `voice/`. Jedes dieser Verzeichnisse repräsentiert ein eigenständiges Subsystem der urspruenglichen Agent-Harness-Architektur.

### 14.2.3 Was noch fehlt

Trotz dieser beeindruckenden Abdeckung muss klar gesagt werden: Der Python-Baum ist noch kein vollständiges Laufzeitäquivalent. Er hat weniger ausführbare Schichten als das Original. Die meisten Subsystem-Pakete sind strukturelle Platzhalter, die Metadaten bereitstellen, aber keine vollständige Laufzeitlogik implementieren. Die README des Projekts formuliert es unmissverstaendlich:

> Der aktuelle Python-Arbeitsbereich ist noch kein vollständiger 1:1-Ersatz für das Originalsystem, aber die primaere Implementierungsoberflaeche ist jetzt Python.

Das bedeutet: Die Befehls- und Tool-Inventare sind vollständig gespiegelt. Die Architektur ist klar nachgezeichnet. Aber die tiefen Ausführungspfade -- das tatsaechliche Routing von Prompts durch die Tool-Kette, die Echtzeit-Interaktion mit einem Sprachmodell, die komplexen Seiteneffekte der Agentenschleife -- sind in Python noch nicht in der gleichen Tiefe implementiert wie im TypeScript-Original.

---

## 14.3 Architektonische Errungenschaften

### 14.3.1 Saubere Drei-Schichten-Trennung

Die vielleicht wichtigste architektonische Errungenschaft von Claw Code ist die konsequente Trennung in drei Schichten, die sich durch den gesamten Python-Baum zieht:

1. **Datenmodellschicht** (`models.py`, `permissions.py`, `context.py`): Frozen Dataclasses definieren die unveränderlichen Strukturen des Systems. `Subsystem`, `PortingModule`, `PermissionDenial`, `UsageSummary`, `PortContext`, `ToolPermissionContext` -- all diese Typen sind als `@dataclass(frozen=True)` deklariert und damit nach ihrer Erzeugung unveränderlich. Dies eliminiert eine ganze Klasse von Fehlern, die in veraenderbaren Datenstrukturen auftreten koennen.

2. **Orchestrierungsschicht** (`query_engine.py`, `runtime.py`, `execution_registry.py`, `system_init.py`): Diese Schicht verbindet Datenmodelle mit Ausführungslogik. Die `QueryEnginePort`-Klasse ist das Herzstaeck: Sie verwaltet Sessions, verarbeitet Nachrichten, trackt Token-Budgets, kompaktiert Transkripte und persistiert den Zustand. Die `RuntimeSession` in `runtime.py` buendelt alle Aspekte einer Laufzeitsitzung in einem einzigen, zusammenhaengenden Objekt. Die `ExecutionRegistry` stellt eine einheitliche Schnittstelle für das Auffinden und Ausführen von gespiegelten Befehlen und Tools bereit.

3. **Präsentationsschicht** (`main.py`, `port_manifest.py`): Der CLI-Einstiegspunkt und die Manifest-Generierung bilden die äußerste Schicht. Sie transformieren die internen Datenstrukturen in menschenlesbare Ausgaben -- Markdown-Zusammenfassungen, tabellarische Auflistungen, Paritaetsprüfberichte.

Diese Trennung ist nicht nur ästhetisch befriedigend, sondern hat handfeste Vorteile: Jede Schicht kann unabhängig getestet, erweitert und -- im Fall der Rust-Portierung -- einzeln neu implementiert werden.

### 14.3.2 JSON-getriebene Referenzdaten

Ein zentrales Designprinzip von Claw Code ist die Auslagerung von Referenzdaten in JSON-Dateien. Die 207 Befehle und 184 Tools sind nicht als Python-Code hartcodiert, sondern in `commands_snapshot.json` und `tools_snapshot.json` unter `src/reference_data/` abgelegt. Ebenso haben alle Subsystem-Pakete ihre Metadaten in separaten JSON-Dateien unter `src/reference_data/subsystems/`.

Dieses Prinzip hat mehrere Vorteile:

- **Trennung von Daten und Logik**: Die JSON-Dateien koennen unabhängig vom Python-Code aktualisiert werden, etwa wenn sich das Original ändert.
- **Maschinenlesbarkeit**: Andere Werkzeuge -- einschließlich der Paritaetsprüfung -- koennen die JSON-Daten direkt konsumieren, ohne Python importieren zu müssen.
- **Nachvollziehbarkeit**: Die JSON-Snapshots bilden eine Art Vertrag zwischen dem Original und der Portierung. Jeder Eintrag dokumentiert Name, Verantwortlichkeit und Herkunftshinweis.

Die Ladefunktionen `load_command_snapshot()` und `load_tool_snapshot()` nutzen `@lru_cache(maxsize=1)`, um die JSON-Daten nur einmal zu lesen und dann im Speicher vorzuhalten. Dies ist ein sauberer Kompromiss zwischen Leistung und Einfachheit.

### 14.3.3 Trust-Gating für sichere Ausführung

Das Trust-Gating-System, implementiert in `permissions.py`, `system_init.py` und `setup.py`, stellt sicher, dass bestimmte Operationen nur in vertrauenswürdigen Kontexten ausgeführt werden. Die `ToolPermissionContext`-Klasse arbeitet mit einem Deny-List-Ansatz: Sie prüft, ob ein Tool-Name in der `deny_names`-Menge enthalten ist oder mit einem der `deny_prefixes` beginnt.

Die `run_setup()`-Funktion in `setup.py` akzeptiert einen `trusted`-Parameter, der den gesamten Initialisierungsfluss beeinflusst. Im nicht vertrauenswürdigen Modus werden bestimmte Deferred-Init-Schritte übersprungen und Prefetch-Operationen eingeschraenkt. Dies spiegelt ein fundamentales Designprinzip des Original-Claude-Code wider: Ein Agent-Harness muss in der Lage sein, zwischen vertrauenswürdigen und nicht vertrauenswürdigen Umgebungen zu unterscheiden, weil die Tools, die er bereitstellt -- Dateisystemzugriff, Codeausführung, Netzwerkkommunikation -- reale Seiteneffekte haben koennen.

### 14.3.4 Token-basiertes Prompt-Routing

Die `QueryEnginePort`-Klasse implementiert ein Token-basiertes Budget-System, das die Lebensdauer einer Session steuert. Jeder `submit_message()`-Aufruf berechnet die projizierte Token-Nutzung und kann die Session mit dem Stop-Reason `max_budget_reached` beenden, wenn das konfigurierte Maximum überschritten wird. Parallel dazu gibt es ein Turn-basiertes Limit (`max_turns`), das unabhängig vom Token-Verbrauch greift.

Dieses duale Begrenzungssystem -- Turns und Tokens -- ist typisch für Agent-Harness-Architekturen: Man möchte sowohl die Laenge einer Konversation als auch die Kosten kontrollieren koennen, und beide Dimensionen sind nicht immer korreliert.

### 14.3.5 Session-Lifecycle mit Persistenz

Der Session-Lifecycle in Claw Code umfasst mehrere Stufen: Erzeugung (mit `uuid4()`-basierter Session-ID), Nachrichtenverarbeitung, Transkript-Kompaktierung, Flush und Persistenz. Die `StoredSession`-Dataclass in `session_store.py` serialisiert den Zustand als JSON in das `.port_sessions/`-Verzeichnis. Sessions koennen später über `load_session()` wiederhergestellt werden, und die `QueryEnginePort.from_saved_session()`-Factory-Methode rekonstruiert den vollständigen Engine-Zustand aus einer gespeicherten Session.

Die `TranscriptStore`-Klasse implementiert ein Sliding-Window-Kompaktierungsverfahren: Wenn die Anzahl der Eintraege `compact_after_turns` übersteigt, werden nur die letzten Eintraege behalten. Dies verhindert unbegrenztes Wachstum des Arbeitsspeichers, ohne den Kontext der juengsten Interaktion zu verlieren -- ein Muster, das auch im Original-Claude-Code zu finden ist.

---

## 14.4 Die Rust-Portierung

### 14.4.1 Motivation

Während der Python-Baum als Verstaendnis- und Dokumentationswerkzeug hervorragend funktioniert, hat er inhaerent Grenzen als Laufzeitumgebung. Pythons Global Interpreter Lock, die dynamische Typisierung und die vergleichsweise langsame Ausführungsgeschwindigkeit machen es für eine produktive Agent-Harness-Laufzeit weniger geeignet.

Die Rust-Portierung, die auf dem `dev/rust`-Branch begonnen würde und auch bereits im Hauptzweig unter `rust/` sichtbar ist, verfolgt ein ambitionierteres Ziel: eine speichersichere, performante Harness-Laufzeitumgebung, die potenziell als echte Alternative zum TypeScript-Original dienen könnte.

### 14.4.2 Aktuelle Struktur

Das `rust/`-Verzeichnis enthält bereits eine organisierte Crate-Struktur:

- `crates/api/` -- API-Schnittstellen
- `crates/commands/` -- Befehlsverarbeitung
- `crates/compat-harness/` -- Kompatibilitaetsschicht
- `crates/runtime/` -- Laufzeitumgebung
- `crates/rusty-claude-cli/` -- CLI-Frontend
- `crates/tools/` -- Tool-Ausführung

Diese Struktur spiegelt die Drei-Schichten-Architektur des Python-Baums wider, nutzt aber Rusts Crate-System für eine noch strengere Modultrennung. Jede Crate hat ihren eigenen Namensraum, ihre eigenen Abhängigkeiten und ihre eigene Kompilierungseinheit.

### 14.4.3 Was die Rust-Portierung verspricht

Das Rust-Äquivalent bringt mehrere Vorteile:

- **Speichersicherheit ohne Garbage Collection**: Rusts Ownership-System garantiert Speichersicherheit zur Kompilierzeit. Für ein System, das langlebige Sessions verwaltet und parallel Tool-Ausführungen koordiniert, ist dies ein wesentlicher Vorteil.
- **Hohe Performanz**: Kompilierter Rust-Code erreicht C/C++-ähnliche Geschwindigkeit, was für das Parsen großer JSON-Snapshots, das Routing von Befehlen und die Verwaltung von Token-Budgets relevant ist.
- **Typsicherheit**: Rusts statisches Typsystem faengt Fehler ab, die in Python erst zur Laufzeit auftreten würden. Die Frozen-Dataclass-Garantien, die wir in Python explizit einfordern müssten, sind in Rust der Normalzustand.
- **Einbettbarkeit**: Ein Rust-Binary kann als eigenständiges Kommandozeilenwerkzeug ausgeliefert werden, ohne Python-Interpreter oder virtuelle Umgebung.

---

## 14.5 Offene Fragen

### 14.5.1 Ethische Implikationen der Reimplementierung

Wie bereits in Kapitel 2 dieses Buches ausführlich diskutiert, wirft die Clean-Room-Reimplementierung eines proprietaeren Systems fundamentale ethische Fragen auf. Das Projekt existiert in einer Grauzone: Der offengelegte Quellcode würde studiert, um die Architektur zu verstehen, aber die Python-Portierung würde von Grund auf geschrieben, ohne Code zu kopieren.

Doch reicht das? Die Frage, ob ein architekturelles Verstaendnis, das aus der Lektuere proprietaeren Codes gewonnen würde, in einer Neuimplementierung verwendet werden darf, ist nicht nur juristisch, sondern auch moralisch komplex. Das Projekt selbst reflektiert diese Spannung: Die README verweist auf einen Essay mit dem Titel "Is Legal the Same as Legitimate? AI Reimplementation and the Erosion of Copyleft", der die Erosion von Copyleft-Prinzipien im Zeitalter der KI-Reimplementierung thematisiert.

Diese Debatte ist nicht akademisch. Sie betrifft die gesamte Open-Source-Community und die Frage, wie geistiges Eigentum in einer Welt geschuetzt werden kann, in der KI-Systeme Code lesen, verstehen und funktional äquivalente Implementierungen in anderen Sprachen erzeugen koennen.

### 14.5.2 Wie weit kann und soll die Paritaet getrieben werden?

Die aktuelle Paritaet -- vollständige Befehls- und Tool-Inventare, vollständige Verzeichnisstruktur, aber unvollständige Laufzeittiefe -- wirft die Frage auf: Wie weit soll man gehen? Es gibt hier ein Kontinuum:

- **Strukturelle Paritaet**: Jedes Verzeichnis, jede Datei hat ein Äquivalent. Dies ist weitgehend erreicht.
- **API-Paritaet**: Jede öffentliche Funktion und Klasse hat ein Äquivalent mit kompatibler Signatur. Dies ist teilweise erreicht.
- **Verhaltensparitaet**: Für jeden Input erzeugt das System denselben Output. Dies ist noch weit entfernt.
- **Laufzeitparitaet**: Das System kann das Original in der Praxis ersetzen. Dies ist das erklaerte Ziel der Rust-Portierung.

Jede Paritaetsstufe erfordert exponentiell mehr Aufwand als die vorherige. Und jede Stufe wirft die ethische Frage von Kapitel 2 mit erneuter Schärfe auf: Ab welchem Punkt wird eine "inspirierte" Reimplementierung zur funktionalen Kopie?

### 14.5.3 Die Zukunft von Copyleft im Zeitalter von KI-Reimplementierung

Claw Code ist ein Fallbeispiel für eine Entwicklung, die weit über dieses einzelne Projekt hinausreicht. Wenn KI-Systeme in der Lage sind, eine Codebasis in Sprache A zu lesen und eine funktional äquivalente Codebasis in Sprache B zu erzeugen, was bedeutet das für:

- **GPL und LGPL**: Koennen Copyleft-Lizenzen eine Reimplementierung in einer anderen Sprache erfassen, wenn kein einziges Byte kopiert würde?
- **Clean-Room-Verfahren**: Genuegt es, dass der reimplementierende Entwickler den Originalcode nicht selbst gelesen hat, wenn die KI, die er verwendet, es getan hat?
- **Trade Secrets**: Kann eine architektonische Entscheidung -- etwa die Drei-Schichten-Trennung oder das Token-basierte Routing -- als Geschaeftsgeheimnis geschuetzt werden, wenn sie aus der Analyse eines geleakten Quellcodes rekonstruiert würde?

Diese Fragen haben keine einfachen Antworten. Aber Claw Code zwingt uns, sie zu stellen. Und allein darin liegt ein Wert, der über den technischen Beitrag des Projekts hinausgeht.

---

## 14.6 Design Patterns: Eine Zusammenfassung

Über die gesamte Codebasis hinweg setzt Claw Code eine konsistente Menge von Design Patterns ein, die hier noch einmal zusammengefasst werden sollen:

### 14.6.1 Frozen Dataclasses

Das am häufigsten verwendete Pattern im Projekt. Nahezu jede Datenstruktur -- `Subsystem`, `PortingModule`, `PermissionDenial`, `UsageSummary`, `PortContext`, `ToolPermissionContext`, `CommandExecution`, `ToolExecution`, `WorkspaceSetup`, `SetupReport`, `PortManifest`, `StoredSession`, `QueryEngineConfig`, `TurnResult`, `RoutedMatch`, `MirroredCommand`, `MirroredTool`, `ExecutionRegistry` -- ist als `@dataclass(frozen=True)` deklariert. Dies erzwingt Unveränderlichkeit nach der Erzeugung und macht die Objekte automatisch hashbar. In einem System, das Sessions verwaltet und Zustandsübergaenge trackt, ist diese Unveränderlichkeit ein mächtiges Werkzeug gegen eine ganze Klasse von Bugs.

### 14.6.2 LRU-Caching

Die Funktionen `load_command_snapshot()` und `load_tool_snapshot()` verwenden `@lru_cache(maxsize=1)`, um die JSON-Referenzdaten nur einmal von der Festplatte zu lesen. Da sich diese Daten während der Laufzeit nicht ändern, ist dies ein sauberer und effizienter Ansatz. Das Pattern wird konsequent nur dort eingesetzt, wo es sinnvoll ist -- bei idempotenten, reinen Funktionen ohne Seiteneffekte.

### 14.6.3 Factory Methods

Mehrere Klassen bieten klassenmethodenbasierte Factory-Methoden an: `QueryEnginePort.from_workspace()` erzeugt eine Engine aus dem aktuellen Arbeitsbereich, `QueryEnginePort.from_saved_session()` rekonstruiert eine Engine aus einer gespeicherten Session, und `ToolPermissionContext.from_iterables()` erzeugt einen Berechtigungskontext aus Listen statt aus Frozensets. Diese Factories kapseln die Konstruktionslogik und bieten eine klare, benannte Schnittstelle für unterschiedliche Erzeugungsszenarien.

### 14.6.4 Builder Pattern

Die Funktionen `build_port_context()`, `build_port_manifest()`, `build_command_backlog()`, `build_tool_backlog()`, `build_workspace_setup()`, `build_system_init_message()` und `build_execution_registry()` folgen einem einheitlichen Builder-Namensschema. Jede dieser Funktionen sammelt Informationen aus verschiedenen Quellen, konstruiert ein komplexes Objekt und gibt es zurück. Die Konsistenz dieses Namensschemas -- immer `build_*` -- macht den Code selbstdokumentierend.

### 14.6.5 Strategy Pattern

Das Permission-System implementiert ein Strategy Pattern: Die `ToolPermissionContext`-Klasse kapselt eine Filterungsstrategie (Deny-Liste plus Präfix-Matching), die von außen injiziert werden kann. Die Funktion `filter_tools_by_permission_context()` in `tools.py` wendet diese Strategie auf eine Menge von Tools an, ohne die Filtermechanik selbst zu kennen. Dies erlaubt es, verschiedene Berechtigungsstrategien auszutauschen, ohne die Tool-Lade- und Ausführungslogik zu ändern.

---

## 14.7 Was man aus diesem Projekt lernen kann

### 14.7.1 Agent-Harness-Architektur verstehen

Claw Code ist, soweit öffentlich bekannt, die detaillierteste Dokumentation einer Agent-Harness-Architektur in der Open-Source-Welt. Wer verstehen möchte, wie ein System wie Claude Code intern funktioniert -- wie Prompts geroutet werden, wie Tools ausgewählt und ausgeführt werden, wie Sessions verwaltet und persistiert werden, wie Berechtigungen durchgesetzt werden --, findet in diesem Projekt eine reichhaltige Quelle.

Die Architektur zeigt, dass ein modernes Agent-Harness weit mehr ist als eine Schleife, die Prompts an ein Sprachmodell sendet und Antworten zurückgibt. Es ist ein komplexes System mit eigenem Zustandsmanagement, eigener Berechtigungslogik, eigenem Token-Budgeting, eigener Session-Persistenz und eigener Tool-Registry. Diese Komplexitaet zu verstehen, ist für jeden Entwickler wertvoll, der an der nächsten Generation von KI-gestützten Werkzeugen arbeitet.

### 14.7.2 Clean-Room-Reimplementierung als Methode

Das Projekt demonstriert, wie eine Clean-Room-Reimplementierung als Methode des technischen Verstaendnisses eingesetzt werden kann. Indem man ein System in einer anderen Sprache nachbaut, ist man gezwungen, jede Designentscheidung bewusst nachzuvollziehen. Man kann nicht einfach Code kopieren; man muss ihn verstehen. Dieser Prozess des erzwungenen Verstaendnisses führt oft zu tieferen Einsichten als das bloße Lesen des Originalcodes.

Gleichzeitig zeigt das Projekt die Grenzen dieses Ansatzes: Die strukturelle Paritaet ist relativ schnell erreichbar, aber die Verhaltensparitaet erfordert ein Vielfaches an Aufwand. Die Reimplementierung deckt Designentscheidungen auf, aber sie kann die impliziten Annahmen und die gelebte Erfahrung der Originalentwickler nicht vollständig erfassen.

### 14.7.3 Modulare Python-Architektur ohne Abhängigkeiten

Für Python-Entwickler bietet Claw Code ein lehrreiches Beispiel dafür, wie eine nicht-triviale Anwendung vollständig ohne externe Abhängigkeiten strukturiert werden kann. Die Kombination aus `dataclasses`, `json`, `pathlib`, `functools.lru_cache`, `uuid`, `platform` und `unittest` -- alles Module der Standardbibliothek -- reicht aus, um ein System mit Dutzenden von Modulen, einer CLI-Schnittstelle, Session-Persistenz und einem Testsuite zu bauen.

Diese Abhängigkeitsfreiheit ist nicht nur eine technische Kuriosiaet. Sie hat praktische Vorteile: Das Projekt lässt sich auf jedem System mit einer Python-3-Installation ausführen, ohne dass Pakete installiert, virtuelle Umgebungen konfiguriert oder Versionskonflikte gelöst werden müssen. In einer Welt, in der selbst einfache Python-Projekte oft Dutzende transitiver Abhängigkeiten mit sich bringen, ist diese Schlankheit bemerkenswert -- und nachahmungswürdig.

---

## 14.8 Ein Blick nach vorn

### 14.8.1 Die nächsten Schritte

Die Zukunft von Claw Code liegt auf mehreren Achsen:

1. **Rust-Portierung abschließen**: Die sechs Crates unter `rust/crates/` müssen mit Laufzeitlogik gefuellt werden. Das Ziel ist ein eigenständiges Binary, das als Agent-Harness funktioniert.

2. **Laufzeittiefe in Python erhöhen**: Auch der Python-Baum kann und soll weiter vertieft werden. Die Subsystem-Platzhalter koennen schrittweise durch ausführbare Module ersetzt werden.

3. **Paritaetsprüfung automatisieren**: Der `parity-audit`-Befehl kann zum kontinuierlichen Regressionstest ausgebaut werden, der bei jedem Commit prüft, ob die Portierung mit dem Original synchron bleibt.

4. **Community-Beitraege ermöglichen**: Die modulare Struktur und die klare Trennung der Subsysteme laden zu Beitraegen ein. Jedes Subsystem kann unabhängig bearbeitet werden.

### 14.8.2 Die größere Bedeutung

Claw Code ist mehr als ein technisches Projekt. Es ist ein Experiment an der Schnittstelle von Reverse Engineering, KI-Ethik und Open-Source-Kultur. Es zeigt, dass die Offenlegung von Quellcode -- ob beabsichtigt oder nicht -- eine Kaskade von Reaktionen auslösen kann, die weit über das urspruengliche Ereignis hinausgeht. Es zeigt, dass die Grenzen zwischen "verstehen", "dokumentieren" und "reimplementieren" fliessend sind. Und es zeigt, dass die Open-Source-Community in der Lage ist, innerhalb von Stunden auf ein Ereignis zu reagieren und etwas Eigenes daraus zu schaffen.

Die 30.000 GitHub-Stars sind ein Indikator für das Interesse, aber nicht für den Wert des Projekts. Der wirkliche Wert liegt in dem, was wir über Agent-Harness-Architekturen gelernt haben, in den Fragen, die wir aufgeworfen haben, und in der Methodik, die wir demonstriert haben.

---

## 14.9 Schlusswort

Als Sigrid Jin sich an jenem fruehen Morgen des 31. Maerz 2026 hinsetzte und begann, die Kernfunktionen des Claude-Code-Harness nach Python zu portieren, könnte sie nicht wissen, dass daraus das am schnellsten wachsende GitHub-Repository der Geschichte werden würde. Aber vielleicht war das auch nicht der Punkt. Der Punkt war: verstehen, wie es funktioniert. Und dann: es besser machen.

Dieses Buch hat versucht, diesen Verstehensprozess nachzuzeichnen -- von der Architekturanalyse über die Designentscheidungen bis hin zu den ethischen Implikationen. Wenn Sie, liebe Leserin, lieber Leser, aus dieser Lektuere mitnehmen, dass Agent-Harness-Systeme keine Black Boxes sein müssen, dass modulare Architektur ohne Abhängigkeiten möglich ist und dass technische Neugier manchmal die staerkste Triebfeder für Innovation ist, dann hat dieses Buch seinen Zweck erfuellt.

Die Zukunft von Claw Code ist offen. Die Rust-Portierung wird die Laufzeitluecke schließen. Die Community wird die Subsysteme vertiefen. Und die ethische Debatte über KI-Reimplementierung wird weitergehen -- hoffentlich mit der Nuanciertheit und Ernsthaftigkeit, die sie verdient.

In diesem Sinne: Das Projekt ist nicht abgeschlossen. Es hat gerade erst begonnen.
