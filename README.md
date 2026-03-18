#  AI-Powered Data Modelling Assistant  
### *An Agentic AI approach to simplifying data modelling*

---

## 🚀 Why I built this

In most data projects, a significant amount of time goes into:

- understanding raw datasets  
- figuring out relationships  
- designing data models  
- documenting everything  

These steps are often manual, repetitive, and dependent on experience.

I wanted to explore:

> Can we use AI not just to assist, but to actively participate in data modelling workflows?

This project is an attempt to answer that using an Agentic AI approach, where multiple specialised agents collaborate to solve the problem.

---

## 🧩 What this project does

This is a Proof of Concept (POC) that uses multiple AI agents to:

- understand dataset structure  
- analyse relationships between data  
- suggest data modelling approaches  
- generate basic documentation  

Instead of doing everything in one step, the system breaks the problem into smaller tasks handled by different agents.

---

## 🏗️ How it works (High Level)

The system follows a staged flow:

1. Understand the data  
2. Analyse relationships and patterns  
3. Generate modelling recommendations  

Each stage is handled by a dedicated AI agent.

---

## 🤖 Agents in the system

### 1. Data Profiling Agent  
This is the first layer of understanding.

It looks at the dataset and answers questions like:
- What are the data types?  
- Are there missing values?  
- What does the distribution look like?  
- Are there anomalies?  

Output: A structured summary of the dataset

---

### 2. Data Analysis Agent  
This agent tries to make sense of the data.

It identifies:
- possible relationships between tables  
- key columns and joins  
- patterns in how data is structured  

Output: Logical relationships and insights

---

### 3. Data Modelling Agent  
This is where things become actionable.

Based on the previous agents, it:
- suggests table structures  
- proposes relationships (like ER models)  
- recommends modelling approaches (e.g. dimensional modelling)  

Output: A proposed data model

---

## 🏁 Final Output

The system produces a combination of:

- Dataset documentation  
- Suggested schema / modelling approach  
- Data insights  
- Recommendations for improvement  

---

## 🧪 Current Status

This is an active POC, not a finished product.

- Multi-agent design is defined  
- Core logic is being implemented  
- Initial outputs are being tested  
- Improvements are ongoing  

---

## 🧠 What makes this interesting

Most AI solutions in data engineering focus on:

- query generation  
- summarisation  

This project explores something different:

> Using AI as a collaborative system of agents that can assist in design-level decisions, not just execution.

---

## 🔧 Tech Direction (Current / Planned)

- Python-based implementation  
- LLM integration (OpenAI / similar models)  
- Agent orchestration (planned via LangChain / CrewAI)  
- Extensible design to plug into data platforms  

---

## 🔮 Future Ideas

- Add a Data Quality Agent  
- Integrate with BigQuery / Snowflake  
- Generate visual ER diagrams automatically  
- Build a simple UI for interaction  
- Add feedback loop between agents  

---

## 💡 Example Use Case

Given a new dataset, instead of manually:

- reading schema  
- understanding relationships  
- designing models  

You can run this system to get:

- a first draft of the data model  
- documentation  
- insights  

---

## 📸 Sample Output

(Add 1–2 screenshots here)

---

## ✨ Closing Thought

This is a small step toward a bigger idea:

> Data engineering workflows can evolve from manual processes to AI-assisted systems.

---

## 🔗 Author

Built as part of exploration into Agentic AI for data engineering workflows.

---

## 🧾 One-liner

Built a multi-agent AI system to assist in data profiling, analysis, and modelling, demonstrating practical application of Agentic AI in data engineering.
