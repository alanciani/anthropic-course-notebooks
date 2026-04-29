# Anthropic Course Setup for NotebookLM + Claude Code

This repo helps you set up NotebookLM notebooks for Anthropic's courses so you can query them conversationally using Claude Code.

## What You Get

For each course, Claude Code will automatically create a NotebookLM notebook loaded with all the YouTube lesson videos. Once set up, you can ask questions like:

> *"Ask my Claude 101 notebook: what's the difference between a project and a conversation?"*

---

## The Courses

Full courses are available at [anthropic.skilljar.com](https://anthropic.skilljar.com). The links below are for lessons that include YouTube videos.

### Claude 101
*Learn how to use Claude for everyday work tasks, understand core features, and explore resources for more advanced learning.*

- [What is Claude?](https://www.youtube.com/watch?v=VHsp6Hp7Stw)
- [Your first conversation with Claude](https://www.youtube.com/watch?v=0vZ_UVLhSQQ)
- [Getting better results](https://www.youtube.com/watch?v=Zzn-g8lvLMA)
- [Introduction to projects](https://www.youtube.com/watch?v=GJ5jTgcbRHA)
- [Working with skills](https://www.youtube.com/watch?v=LpGpwhORWr0)
- [Connecting your tools](https://www.youtube.com/watch?v=_jjSS0qGFbI)
- [Research mode for deep dives](https://www.youtube.com/watch?v=R-KJgjIrh24)
- [Other ways to work with Claude](https://www.youtube.com/watch?v=s-avRazvmLg)

### Claude Code 101
*Learn how to use Claude Code effectively in your daily workflow.*

- [What is Claude Code?](https://www.youtube.com/watch?v=fl1DSmwQKKY)
- [How Claude Code works](https://www.youtube.com/watch?v=6bs5b4FltCU)
- [Installing Claude Code](https://www.youtube.com/watch?v=0kILa02vKuI)
- [Your first prompt](https://www.youtube.com/watch?v=gbetp6D7J_Q)
- [The explore → plan → code → commit workflow](https://www.youtube.com/watch?v=xJQuF02NAK8)
- [Context management](https://www.youtube.com/watch?v=eW3oTyfeWZ0)
- [Code review](https://www.youtube.com/watch?v=RKsADl0ZC3Y)
- [The CLAUDE.md file](https://www.youtube.com/watch?v=O0FGCxkHM-U)
- [Subagents](https://www.youtube.com/watch?v=jKErNxuxPXg)
- [Skills](https://www.youtube.com/watch?v=bjdBVZa66oU)
- [MCP](https://www.youtube.com/watch?v=kkBFmwkDzdo)
- [Hooks](https://www.youtube.com/watch?v=IkaPHiMDazM)

### Introduction to Claude Co-work
*Learn to work alongside Claude on your real files and projects.*

- [What is Cowork?](https://www.youtube.com/watch?v=UAmKyyZ-b9E)
- [Plugins: Cowork as a specialist](https://www.youtube.com/watch?v=bjdBVZa66oU)
- [File & document tasks](https://www.youtube.com/watch?v=LpGpwhORWr0)

### AIFluency: Framework & Foundations
*Learn to collaborate with AI systems effectively, efficiently, ethically, and safely.*

- [Introduction to AI Fluency](https://www.youtube.com/watch?v=JpGtOfSgR-c)
- [Why do we need AI Fluency?](https://www.youtube.com/watch?v=4szRHy_CT7s)
- [The 4D Framework](https://www.youtube.com/watch?v=W4Ua6XFfX9w)
- [Generative AI fundamentals](https://www.youtube.com/watch?v=RyvXxApfHkk)
- [Capabilities & limitations](https://www.youtube.com/watch?v=W5cga7xipRI)
- [A closer look at Delegation](https://www.youtube.com/watch?v=EljzyfdYkrc)
- [A closer look at Description](https://www.youtube.com/watch?v=DmgujoZ1mmk)
- [Effective prompting techniques](https://www.youtube.com/watch?v=2YCaBqP8muw)
- [A closer look at Discernment](https://www.youtube.com/watch?v=Y0KidGr9Z2Y)
- [A closer look at Diligence](https://www.youtube.com/watch?v=QbLf2zb3oPc)
- [Conclusion](https://www.youtube.com/watch?v=ytEN_iAk09c)

### Introduction to Agent Skills
*Learn how to build, configure, and share Skills in Claude Code.*

- [What are skills?](https://www.youtube.com/watch?v=bjdBVZa66oU)
- [Creating your first skill](https://www.youtube.com/watch?v=Wx6_vjFFyHM)
- [Configuration and multi-file skills](https://www.youtube.com/watch?v=98KaK_rn5rQ)
- [Skills vs. other Claude Code features](https://www.youtube.com/watch?v=IgNN4v0BJdU)
- [Sharing skills](https://www.youtube.com/watch?v=OCBi3eScNLk)
- [Troubleshooting skills](https://www.youtube.com/watch?v=YBa1cwaG7is)

### Introduction to Subagents
*Learn how to use and create subagents in Claude Code to manage context and delegate tasks.*

- [What are subagents?](https://www.youtube.com/watch?v=jKErNxuxPXg)
- [Creating a subagent](https://www.youtube.com/watch?v=arD6qEWa2Xc)
- [Designing effective subagents](https://www.youtube.com/watch?v=WPxWKT_OaU4)
- [Using subagents effectively](https://www.youtube.com/watch?v=n5LoKZ8Oa-A)

### AI Capabilities and Limitations
*An introductory course about how AI works.*

- [Intro to AI Capabilities and Limitations](https://www.youtube.com/watch?v=Sj1yynxA9hw)
- [What We Mean by AI](https://www.youtube.com/watch?v=AiiiyYiEJa4)
- [How AI Gets Its Character](https://www.youtube.com/watch?v=6jRk3nC4-xI)
- [Next Token Prediction](https://www.youtube.com/watch?v=kl0gunXTvyk)
- [Knowledge](https://www.youtube.com/watch?v=iSLdQXeKbHs)
- [Working Memory](https://www.youtube.com/watch?v=QJjt4wF4iHM)
- [Steerability](https://www.youtube.com/watch?v=M_RwSRmp220)
- [When Properties Collide](https://www.youtube.com/watch?v=SPkg5WRfnEE)
- [Next Steps](https://www.youtube.com/watch?v=F7ciHDKAlCA)

---

## Setup

### 1. Install Claude Code

Follow the instructions at [claude.ai/code](https://claude.ai/code).

### 2. Install the NotebookLM skill

```bash
mkdir -p ~/.claude/skills
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
```

### 3. Add the notebook creation script

```bash
curl -o ~/.claude/skills/notebooklm/scripts/create_notebooks.py \
  https://raw.githubusercontent.com/alanciani/anthropic-course-notebooks/main/create_notebooks.py
```

### 4. Authenticate with Google (one time)

Open Claude Code and say:

> *"Set up NotebookLM authentication"*

A browser window will open — log in with your Google account.

---

## Creating Your Notebooks

Open Claude Code, paste the course list from this README, and say:

> *"Create a NotebookLM notebook for each of these courses"*

Claude Code will:
1. Parse the course names and YouTube URLs
2. Open a browser and create each notebook automatically
3. Load all the video lessons as sources
4. Register each notebook so you can query it by name

This takes a few minutes per course. You'll see a browser window working through each one.

---

## Querying Your Notebooks

Once notebooks are created, ask Claude Code anything about the course content:

> *"Ask my Claude 101 notebook: when should I use a project vs a regular conversation?"*

> *"Ask my Claude Code 101 notebook: what does the CLAUDE.md file do?"*

> *"Ask my AI Fluency notebook: what is the 4D framework?"*

Answers come directly from the video transcripts — grounded in the source material, not guessed.
