# 📋 Zero-G Master Flight Plan

> **Standard Operating Procedure for All Projects**

---

## phase-1: 🔭 Discovery & Architecture
- [ ] **Define Goal**: Write a clear one-sentence objective.
- [ ] **Select Agents**: Identify which Zero-G specialists are needed (e.g., `@frontend`, `@security`).
- [ ] **Brainstorm**: Run `/brainstorm` if the path isn't clear.
- [ ] **Technical Spec**: Create `implementation_plan.md` defining:
    - [ ] Tech Stack
    - [ ] Data Schema
    - [ ] API Endpoints
    - [ ] User Flows

## phase-2: 🏗️ Foundation
- [ ] **Scaffold**: Initialize project structure (e.g., `npx zero-g init`).
- [ ] **Git Setup**: `git init`, `.gitignore`, and initial commit.
- [ ] **Safety Checks**: Install `checklist.py` or verification scripts.
- [ ] **Environment**: Set up `.env` (and ensure it's ignored!).

## phase-3: ⚡ Execution (The Build)
- [ ] **Core Logic**: Implement backend/business logic first.
- [ ] **Unit Tests**: Add tests for critical logic immediately (`@test-engineer`).
- [ ] **UI Implementation**: Build components (`@frontend-specialist`).
- [ ] **Integration**: Connect UI to Backend.

## phase-4: 🔍 Verification
- [ ] **Automated Audit**: Run `python .agent/scripts/checklist.py`.
- [ ] **Security Scan**: Run `@security-auditor` check.
- [ ] **UX Polish**: Run `/ui-ux-pro-max` review.
- [ ] **Manual Test**: Verify the "Happy Path" works perfectly.

## phase-5: 🚀 Launch
- [ ] **Documentation**: Update `README.md` with install instructions.
- [ ] **Cleanup**: Remove debug logs and temporary files.
- [ ] **Final Commit**: "chore: ready for launch".
- [ ] **Deployment**: Run `/deploy`.
