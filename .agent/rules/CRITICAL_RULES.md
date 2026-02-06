# ⛔ CRITICAL RULES (Zero-G Guardrails)

> **THESE RULES ARE INVIOLABLE. DO NOT BREAK THEM.**

---

## 🔒 Security
1.  **NO SECRETS IN CODE**: Never commit API keys, tokens, or passwords. Use `.env`.
2.  **VERIFY LIBRARIES**: Do not install npm/pip packages without checking they are standard/safe.
3.  **SANITIZE INPUTS**: Always validate user input. No raw SQL execution.

## 💾 Data Safety
4.  **DESTRUCTIVE ACTIONS**: Ask for permission before `rm -rf`, dropping tables, or overwriting non-empty files.
5.  **BACKUPS**: Before a major refactor, commit current state to Git.

## 💻 Code Quality
6.  **NO BROKEN BUILDS**: Do not leave the codebase in a broken state at the end of a turn.
7.  **TYPESCRIPT STRICT**: If using TS, no `any` unless absolutely necessary.
8.  **DRY PRINCIPLE**: Don't repeat code. Extract utilities.

## 🤖 Agent Behavior
9.  **ADMIT IGNORANCE**: If you don't know a library, read the documentation first.
10. **NO HALLUCINATIONS**: Do not import non-existent functions. Verify they exist.
