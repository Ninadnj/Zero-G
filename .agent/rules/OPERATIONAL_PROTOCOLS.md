# Operational Protocols (Zero-G)

## 1. Skill Selection Protocol

- **Rule**: Always prefer specialized Skills/Agents over general capabilities.
- **Procedure**:
    1. **Analyze** the user request.
    2. **Scan** the `.agent/agents/` and `.agent/skills/` directories.
    3. **Identify** if a specific Specialist exists (e.g., use `frontend-specialist` for UI, `security-auditor` for auth).
    4. **Execute**: If a matching Skill/Agent is found, **YOU MUST USE IT** and follow its defined workflow strictly. Do not hallucinate a generic solution if a specialized tool exists.

## 2. Context Isolation Protocol

- **Rule**: One Repository = One Context. Protect the user's active project identity.
- **Procedure**:
    1. **Identify** the current project's goal (read `README.md` or `package.json`).
    2. **Sanitize**: If the user provides a template or example from another project (e.g., a tutorial or a different client's code):
        - **Extraction**: Identify the *logic/structure* (e.g., "authentication flow" or "component layout").
        - **Discard**: Purge the *content/context* (previous brand names, specific colors, irrelevant jargon).
    3. **Remap**: Apply the extracted logic onto the **CURRENT** project's architecture and style.
    4. **Reject**: Do not introduce styles, names, or concepts from other projects. Maintain strict narrative consistency within this repository.

## 3. Skill Gap Protocol

- **Rule**: If you lack a tool/skill, admit it and propose a build.
- **Procedure**:
    1. **Evaluate**: If a user request requires specialized procedural knowledge that no current `skill` covers.
    2. **Report**: Explicitly state: "I do not currently have a specialized skill for [Task Name]."
    3. **Suggest**: Propose creating the new skill using the `mcp-builder` or manual creation.
    - **Example**: "Shall I design a `[new-skill-name]` skill to handle this consistently?"

## 4. Systems Thinking (Zero-G Philosophy)
- **Rule**: Prefer architecture over surface tasks.
- **Focus**: Capture error messages and analyze the underlying mechanism (Cause → Effect).
- **Trajectory**: "Build and upgrade." Don't just patch; improve the system for the future.
- **Architecture First**: Before coding, always check `ARCHITECTURE.md` to ensure alignment with the system design.
