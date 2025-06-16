[![Use this template](https://img.shields.io/badge/-Use%20this%20template-brightgreen?style=for-the-badge)](https://github.com/JeanDenisD/project-initiator-template/generate)

# 🧪 Custom Notebook Linter Template

A reusable Python project template to apply linters and formatters (`pylint`, `black`, `flake8`) to Jupyter notebooks using `nbqa`.

## 📦 Features

- Applies quality checks to `.ipynb` files
- Works from CLI (`custom-linter`) or from notebooks
- Can be reused as a template across projects
- Built-in `.env` support with example file

## 🚀 How to Use

1. **Clone this repo**
2. (Optional) Click “Use this template” on GitHub
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install in dev mode to enable CLI:
   ```bash
   pip install -e .
   ```
5. Run the linter:
   ```bash
   custom-linter
   ```

## 🛠️ Project Structure

```
custom_scripts/
├── custom_linter.py       ← main script
.env.example                ← template for API keys (never commit .env)
.gitignore
setup.py
requirements.txt
```

## 🔐 .env Support

Copy `.env.example` to `.env` and fill in your variables:
```bash
cp .env.example .env
```

## ✨ Credit

Created by [Jean-Denis Drane](https://github.com/JeanDenisD)
