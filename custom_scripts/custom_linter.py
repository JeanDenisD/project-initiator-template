import subprocess
import glob

def run_lint_on_notebooks():
    tools = ["black", "pylint", "flake8"]
    notebooks = glob.glob("**/*.ipynb", recursive=True)

    if not notebooks:
        print("❌ No notebooks found.")
        return

    for nb in notebooks:
        print(f"\n📘 Processing: {nb}")
        for tool in tools:
            print(f"🔧 Running {tool}...")
            result = subprocess.run(["nbqa", tool, nb])
            if result.returncode == 0:
                print(f"✅ {tool} completed.")
            else:
                print(f"⚠️ {tool} had issues.")

if __name__ == "__main__":
    run_lint_on_notebooks()
