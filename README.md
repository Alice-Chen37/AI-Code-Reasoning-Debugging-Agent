# AI-Code-Reasoning-Debugging-Agent

 **AI-Powered Code Reasoning & Debugging**

A Python project that simulates AI-assisted code reasoning and debugging across multiple Python files. It can detect cross-file bugs, generate step-by-step reasoning, and visualize results in a simple dashboard.

---

## Features

- **Cross-file bug detection** – e.g., finds unexpected additions like `compute_total(nums) + 10`.
- **Multi-file reasoning** – generates human-readable steps and trajectories for debugging.
- **Single-file analysis** – detailed reasoning with memory tracking (`memory.json`).
- **Streamlit dashboard** – upload files, run batch analysis, and see AI suggestions live.
- **Lightweight and extensible** – works without heavy LLMs; ready for AI/ML model integration.

---

## Quick Start

### Run Multi-file Analysis
```bash
python mulmain.py

Run Single-file Analysis
python agent.py

Streamlit Dashboard
streamlit run dashboard.py

-----------------

Sample Output:
{
  "files": [
    "calc.py",
    "main.py",
    "utils.py"
  ],
  "debug": {
    "bug_file": "calc.py",
    "bug": "Unexpected addition of constant 10",
    "fix": "Remove '+ 10'"
  },
  "reasoning": "Step 1: Inspect all project files\nStep 2: Identify functions and dependencies\nStep 3: Detect compute_total bug in calc.py\nStep 4: Suggest fix by removing '+ 10'",
  "trajectory": [
    {
      "step": 1,
      "action": "Step 1: Inspect all project files",
      "type": "cross-file reasoning"
    },
    {
      "step": 2,
      "action": "Step 2: Identify functions and dependencies",
      "type": "cross-file reasoning"
    },
    {
      "step": 3,
      "action": "Step 3: Detect compute_total bug in calc.py",
      "type": "cross-file reasoning"
    },
    {
      "step": 4,
      "action": "Step 4: Suggest fix by removing '+ 10'",
      "type": "cross-file reasoning"
    }
  ]
}