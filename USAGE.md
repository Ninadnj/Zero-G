# 📘 Zero-G Kit: Usage Manual

> **Comprehensive Guide to Intelligent Engineering**

---

## 1. 🧠 Core Philosophy

Zero-G is not just a template; it's an **Operating System**. It works by dynamically assembling a team of AI experts based on your needs.

### How it Works
1.  **You Request**: "Build a React login page."
2.  **Orchestrator Analyzes**: Detects "Frontend" domain.
3.  **Team Assembles**: Activates `@frontend-specialist`, `@nextjs-expert`, `@security-auditor`.
4.  **Skills Load**: Pulls in `tailwind-patterns` and `auth-flows`.
5.  **Execution**: The agents write the code matching your specific standards.

---

## 2. ⚙️ Configuration (Adaptability)

Zero-G assumes "Nina Defaults" (Next.js/Tailwind) unless you tell it otherwise.

### Override per Project (The DNA Method)
To make Zero-G work for a specific client or legacy project:

1.  **Copy the Template**:
    ```bash
    cp .agent/templates/PROJECT_DNA.md .agent/rules/PROJECT_DNA.md
    ```
2.  **Edit the File**:
    Fill in the tech stack and brand rules.
    *   *Example*: Change "Tailwind" to "Bootstrap" or "Next.js" to "Vue".
3.  **That's it!**
    The AI automatically reads this file first and adapts its behavior.

---

## 3. 🚦 Common Workflows

### 🚀 Starting a New App
```bash
/create
# Follow the interactive prompts to build the skeleton.
```

### 🔭 Planning a Complex Feature
Don't just code. Plan first.
```bash
/brainstorm "I need a video processing pipeline"
# Discuss options
/plan
# Generate implementation_plan.md
```

### 🐛 Fixing a Hard Bug
Standard debugging often fails. Use the **Systematic Protocol**:
```bash
/debug "The payment API returns 400 randomly"
# The AI runs a 4-phase root cause analysis.
```

### 🚢 Deploying Safely
Never ship broken code.
```bash
/deploy
# Runs: Security Scan → Lint → Tests → Build → Deploy
```

---

## 4. 🧩 The Skill System

Tools are loaded automatically, but you can force common patterns:

- **`@security-auditor`**: "Audit this file."
- **`@frontend-specialist`**: "Polishing the UI."
- **`/ui-ux-pro-max`**: "Give me 50 premium UI styles."

---

## 5. 🛠️ Important Commands

| Script | Purpose |
| :--- | :--- |
| `python .agent/scripts/checklist.py` | **Quick Sanity Check** (Sec/Lint/Tests) |
| `python .agent/scripts/verify_all.py` | **Full Production Audit** (Lighthouse/E2E) |

---

> **Tip:** Detailed instructions for each specific skill are inside `.agent/skills/<skill-name>/SKILL.md`.
