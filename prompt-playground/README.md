# 🧪 Prompt Playground UI

> A visual web app for A/B testing AI prompts side by side — compare outputs, tune parameters, and save your best prompts to a local library. Built as part of my Generative AI learning journey.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36+-red?style=flat-square&logo=streamlit)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude%20API-orange?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 📌 What It Does

Most people interact with AI models through a single prompt box. This app exposes what's actually happening under the hood — and lets you experiment with it visually.

The Prompt Playground lets you:

- **A/B test prompts side by side** — write two different system prompts and send the same user message to both simultaneously
- **Compare outputs visually** — see how wording, tone, and structure in the prompt changes the response
- **Tune model parameters** — adjust temperature and max tokens with live sliders and see exactly how they affect output
- **Switch models** — run the same prompts on GPT-4o, GPT-4o-mini, Claude Sonnet, or Claude Opus
- **Save your best prompts** — store prompts to a local JSON library, reload or delete them any time
- **Track token usage and cost** — every output shows input tokens, output tokens, and estimated cost per run
- **Export results** — download your A/B comparison as a JSON or markdown file

---

## 🖥️ What It Looks Like

### Full app layout

```
┌─────────────────────────────────────────────────────────────────────┐
│  🧪 Prompt playground              Export results    Save session    │
├─────────────────────────────────────────────────────────────────────┤
│                    │                                                 │
│  MODEL             │  SYSTEM PROMPTS                                │
│  [ gpt-4o      ▼] │  ┌──────────────────┐  ┌──────────────────┐   │
│                    │  │ Prompt A  active  │  │ Prompt B  active  │  │
│  PARAMETERS        │  │                  │  │                  │   │
│  Temperature  0.7  │  │ You are a helpful│  │ You are an expert│   │
│  [────────●──────] │  │ assistant...     │  │ educator...      │   │
│  Max tokens  1024  │  └──────────────────┘  └──────────────────┘   │
│  [──●────────────] │                                                 │
│                    │  ▶ Run A  ▶ Run B  ▶ Run both  Clear  Save A  │
│  USER MESSAGE      │                                                 │
│  ┌──────────────┐  │  OUTPUTS                                       │
│  │ Explain how  │  │  ┌──────────────────┐  ┌──────────────────┐   │
│  │ neural nets  │  │  │ Output A 143 tok  │  │ Output B 198 tok │   │
│  │ learn...     │  │  │                  │  │                  │   │
│  └──────────────┘  │  │ A neural network │  │ Think of it like │   │
│                    │  │ learns by...     │  │ riding a bike... │   │
│  SAVED PROMPTS     │  │                  │  │                  │   │
│  ● ELI5 explainer  │  │ In: 312  Out:143 │  │ In:338  Out:198  │   │
│  ● Bullet summary  │  │ Est: $0.0004     │  │ Est: $0.0006     │   │
│  ● Code reviewer   │  └──────────────────┘  └──────────────────┘   │
│  [ Load ] [Delete] │                                                 │
└─────────────────────────────────────────────────────────────────────┘
```

> Replace this with a real screenshot once the app is running

---

## 🧠 What This Demonstrates

| Concept | What You'll See |
|---|---|
| **Temperature & sampling** | Drag the slider and watch outputs shift from focused to creative |
| **Few-shot prompting** | Add examples inside Prompt A and compare against zero-shot Prompt B |
| **Zero-shot vs Chain-of-Thought** | System prompt B uses step-by-step structure — CoT made visible |
| **Prompt engineering depth** | Same user message, two prompts, completely different outputs |
| **Multi-model comparison** | Switch between GPT-4o and Claude mid-session |
| **Token economics** | See exactly how prompt length drives cost |
| **Streamlit UI patterns** | Columns, containers, session state, sliders, radio, toast |

> **Key insight:** The same user question produces completely different answers based purely on the system prompt. This app makes that visible and measurable.

---

## 🗂️ Project Structure

```
prompt-playground/
│
├── app.py                  # Main Streamlit application
├── api/
│   ├── __init__.py
│   ├── anthropic_client.py # Anthropic API wrapper
│   └── openai_client.py    # OpenAI API wrapper
├── utils/
│   ├── __init__.py
│   ├── prompt_store.py     # Save/load prompts to JSON
│   └── exporter.py         # Export results to markdown/JSON
├── prompts/
│   └── saved_prompts.json  # Local prompt library (auto-created)
├── .env                    # API keys (never commit)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| **Streamlit** | Web UI — layout, widgets, session state |
| **Anthropic SDK** | Claude Sonnet & Opus API calls |
| **OpenAI SDK** | GPT-4o & GPT-4o-mini API calls |
| **python-dotenv** | API key management |
| **JSON** | Local prompt library storage |

---

## 🚀 Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/prompt-playground.git
cd prompt-playground
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
streamlit>=1.36.0
anthropic>=0.25.0
openai>=1.30.0
python-dotenv>=1.0.0
```

### 4. Get your API keys

**Anthropic:**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Navigate to API Keys → Create Key

**OpenAI:**
1. Go to [platform.openai.com](https://platform.openai.com)
2. Navigate to API Keys → Create new secret key

### 5. Create your `.env` file

```bash
touch .env
```

Add both keys:
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-openai-key-here
```

> ⚠️ **Never commit your `.env` file.** It is already in `.gitignore`.

### 6. Run the app

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`

---

## 🎮 How to Use

### Running an A/B test

1. Choose your model from the sidebar dropdown
2. Set temperature and max tokens using the sliders
3. Type your user message in the USER MESSAGE box
4. Write two different system prompts in Prompt A and Prompt B
5. Click **▶ Run both** — both outputs appear side by side instantly
6. Compare the responses, token counts, and estimated costs

### Understanding temperature

| Temperature | Effect | Best for |
|---|---|---|
| `0.0 – 0.3` | Focused, deterministic | Factual Q&A, code, classification |
| `0.4 – 0.7` | Balanced | General chat, summaries, explanation |
| `0.8 – 1.0` | Creative, varied | Brainstorming, storytelling, ideas |

Run the same prompt at `0.1` and `0.9` and compare — the difference is immediate.

### Saving prompts

1. Write a prompt in Prompt A that works well
2. Click **Save prompt A** — you'll be asked to name it
3. It appears instantly in the SAVED PROMPTS list in the sidebar
4. Click **Load** to restore it in any future session
5. Click **Delete** to remove it from the library

### Exporting results

Click **Export results** in the top bar to download a markdown file containing both prompts, both outputs, all parameters, and token stats — useful for documenting what works.

---

## 🔧 Configuration & Customisation

### Add a new model

Open `app.py` and add to the selectbox options:

```python
model = st.selectbox(
    label="model",
    options=["gpt-4o", "gpt-4o-mini", "claude-sonnet-4", "claude-opus-4", "your-new-model"],
    label_visibility="collapsed"
)
```

Then handle it in the API router:

```python
if model.startswith("gpt"):
    response = openai_client.generate_response(...)
elif model.startswith("claude"):
    response = anthropic_client.generate_response(...)
```

### Add a new parameter (e.g. Top P)

```python
top_p = st.slider(
    "Top P", min_value=0.0, max_value=1.0,
    value=1.0, step=0.05,
    key="top_p"
)
```

Pass it to the API call alongside temperature.

### Change the default prompts

Edit the `value` fields in the text areas:

```python
prompt_a = st.text_area(
    label="Prompt A",
    value="Your new default prompt here...",
    key="prompt_a"
)
```

---

## 💡 Key Concepts Explained

### What is temperature?

Temperature controls how random the model's output is. At `0`, the model always picks the most likely next word — predictable and focused. At `1`, it samples more freely — creative but sometimes off-topic. There is no universally correct value; the right temperature depends on your task.

### What is few-shot prompting?

Few-shot prompting means giving the model examples inside the prompt before asking your actual question. Instead of just saying "Summarise this text", you show it one or two examples of what a good summary looks like first. The model picks up the pattern and matches it. This app makes it easy to A/B test few-shot vs zero-shot side by side.

### What is Chain-of-Thought (CoT)?

Chain-of-Thought prompting instructs the model to reason step by step before giving a final answer. Adding "Think through this step by step" to your system prompt dramatically improves accuracy on reasoning tasks. Prompt B in the default setup uses this pattern — compare it against Prompt A to see the difference.

### Why do tokens matter?

Every word roughly equals one token. You pay for input tokens (your prompt + history) and output tokens (the model's response). The longer your system prompt, the more every single API call costs. This app shows you exactly what you're spending per run — critical for understanding real-world AI costs.

---

## 📈 Possible Extensions

- [ ] Add streaming output so responses appear word by word
- [ ] Add a history tab to review past A/B sessions
- [ ] Add a winner picker — thumbs up on the better output
- [ ] Support image inputs for multimodal A/B testing
- [ ] Add a cost tracker that accumulates across the whole session
- [ ] Deploy to Streamlit Cloud and share as a live link

---

## 🧑‍💻 About This Project

This is **Project 02** of my Generative AI learning series — a structured curriculum from API basics to multi-agent systems.

**What I learned building this:**
- How Streamlit's session state works and why it matters for interactive apps
- Why the same model gives completely different answers based on system prompt wording
- How temperature sampling actually affects output quality vs creativity
- The real cost difference between short and long system prompts
- How to build a clean, usable data app without writing any HTML or CSS from scratch

---

## 📄 License

MIT — free to use, fork, and build on.

---

*Part of my [Zero-to-AI-engineer](https://github.com/OlawoyeTaofeek/Zero-to-AI-engineer/tree/main) — documenting the journey from zero to AI engineer.*
