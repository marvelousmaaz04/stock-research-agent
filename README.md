## 📈 Stock Research Agent

An AI-powered **Stock Research Assistant** built with [Agno](https://docs.agno.com/), **Gemini 2.0 Flash**, and **Streamlit**.
It performs live financial analysis, sentiment scanning, and news summarization using multiple integrated data sources.

---

### 🚀 Features

* 💹 **Real-time Stock Analysis** using Yahoo Finance (`YFinanceTools`)
* 🔍 **Web & News Search** via Tavily + Google Search
* 🧠 **AI-Powered Reasoning** using Gemini 2.0 Flash
* 📰 **Webpage Summaries** through Firecrawl (auto summarization)
* 🗂️ **Persistent Memory** using SQLite (via Agno’s built-in DB)
* 🧾 **Plain URL Citations** for full transparency
* 💬 **Interactive Chat UI** built with Streamlit

---

### 🧰 Tech Stack

| Component                       | Description                        |
| ------------------------------- | ---------------------------------- |
| **Agno**                        | Orchestrates multi-tool LLM agents |
| **Gemini 2.0 Flash**            | Main reasoning model               |
| **Streamlit**                   | Chat UI interface                  |
| **SQLite**                      | Persistent memory backend          |
| **Tavily, YFinance, Firecrawl** | Data and scraping toolkits         |

---

### ⚙️ Project Setup

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/stock-research-agent.git
cd stock-research-agent
```

#### 2️⃣ Install Dependencies (using `uv`)

If you don’t have [uv](https://github.com/astral-sh/uv) installed, first install it:

```bash
pip install uv
```

Then install all dependencies directly from your `pyproject.toml`:

```bash
uv sync
```

*(This automatically creates and uses a virtual environment.)*

#### 3️⃣ Create a `.env` File

Create a `.env` file in the project root with your API keys:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```


#### 4️⃣ Run the Streamlit App

```bash
uv run streamlit run main.py
```

Then open the link displayed in your terminal (usually [http://localhost:8501](http://localhost:8501)).

---

### 💬 How to Use

1. Enter a query like:

   * `research aapl`
   * `msft`
   * `research jio`
2. The agent automatically:

   * Identifies the correct ticker
   * Fetches company data, analyst ratings, and financials
   * Runs web searches for price targets and sentiment
   * Generates a structured research summary with **plain URL sources**

Example Output:

```
🏢 Company Summary
Apple Inc. (AAPL) designs and manufactures smartphones, computers, and services [1].

Should you buy Apple?

Positive Factors: strong brand, cash flow, growth in services  
Risks: competition, regulatory challenges  

🔗 Sources
[1] https://finance.yahoo.com/quote/AAPL/
[2] https://stockanalysis.com/stocks/aapl/forecast/
[3] https://edition.cnn.com/markets/stocks/AAPL
```

---

### 🧩 Project Structure

```
.
├── agent.py                # Core Agno agent setup (Gemini + Tools)
├── main.py                 # Streamlit chat frontend
├── agent_memory.db         # SQLite memory database (auto-created)
├── pyproject.toml          # uv project configuration
├── .env                    # API keys
└── README.md               # You’re here!
```

---

### 🧠 Supported Tools

| Tool                  | Purpose                                 |
| --------------------- | --------------------------------------- |
| **YFinanceTools**     | Stock price, fundamentals, analyst data |
| **TavilyTools**       | Web search and price target discovery   |
| **GoogleSearchTools** | Fallback for Tavily                     |
| **FirecrawlTools**    | Webpage summarization                   |

---

### 🩵 Example Session

**User:**

> research nvidia

**Agent:**

> Analyzing NVIDIA Corporation (NVDA)...
>
> 🏢 Company Summary
> NVIDIA Corporation provides GPUs and AI infrastructure solutions [1].
>
> 🔗 Sources
> [1] [https://finance.yahoo.com/quote/NVDA](https://finance.yahoo.com/quote/NVDA)
> [2] [https://www.reuters.com/companies/NVDA.OQ](https://www.reuters.com/companies/NVDA.OQ)
> [3] [https://www.cnbc.com/nvidia-stock-price-target](https://www.cnbc.com/nvidia-stock-price-target)


---

### 🧾 License

This project is for educational and personal research purposes.
All financial data is sourced from public APIs and news sources.

---