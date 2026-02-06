import asyncio
import os
import subprocess
import glob
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("Zero-G")

# --- TOOLS ---

@mcp.tool()
async def audit_project(path: str = ".") -> str:
    """
    Run the standard Zero-G Checklist (Security, Lint, Schema, Tests).
    Use this to verify project health before major changes.
    """
    script_path = os.path.join(os.getcwd(), ".agent/scripts/checklist.py")
    if not os.path.exists(script_path):
        return "Error: checklist.py not found. Are you in a Zero-G project?"
    
    try:
        result = subprocess.run(
            ["python3", script_path, path],
            capture_output=True,
            text=True
        )
        return result.stdout + "\n" + result.stderr
    except Exception as e:
        return f"Error running audit: {str(e)}"

@mcp.tool()
async def read_skill(skill_name: str) -> str:
    """
    Read the instructions for a specific Zero-G skill.
    Example: read_skill("nextjs-react-expert")
    """
    base_path = os.path.join(os.getcwd(), ".agent/skills")
    skill_file = os.path.join(base_path, skill_name, "SKILL.md")
    
    if os.path.exists(skill_file):
        with open(skill_file, "r") as f:
            return f.read()
    else:
        # Fallback: List available skills if not found
        skills = [os.path.basename(d) for d in glob.glob(os.path.join(base_path, "*")) if os.path.isdir(d)]
        return f"Skill '{skill_name}' not found. Available skills:\n- " + "\n- ".join(sorted(skills))

# --- RESOURCES ---

@mcp.resource("zero-g://operational_protocols")
def get_protocols() -> str:
    """Return the global Operational Protocols for Agents."""
    path = os.path.join(os.getcwd(), ".agent/rules/OPERATIONAL_PROTOCOLS.md")
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return "Protocol file not found."

def main():
    mcp.run()

if __name__ == "__main__":
    main()
