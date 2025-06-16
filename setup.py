from setuptools import setup, find_packages

setup(
    name="custom_linter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "nbqa",
        "black",
        "flake8",
        "pylint",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "custom-linter=custom_scripts.custom_linter:run_lint_on_notebooks"
        ]
    },
    author="Jean-Denis Drane",
    description="A reusable linter for Jupyter notebooks using nbqa.",
    python_requires=">=3.7",
)
