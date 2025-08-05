# Tidy

An all-in-one code hygiene utility built into the Module CLI.
It enforces formatting, linting, import sorting, and dead code detection across all major language stacks used in the Module ecosystem 

Use this tool to keep your codebase fast, readable, and clean.

---

## 🚀 Usage

```bash
module tidy [scope] [--fix] [--verbose]

# Examples
module tidy all             # Lint and format all languages
module tidy py              # Only tidy Python code
module tidy go --fix        # Auto-fix Go formatting issues
module tidy ts --verbose    # Show full output while linting TS
```

| lang           | actions performed                          |
|----------------|--------------------------------------------|
| Go	            | go fmt, goimports, golangci-lint, deadcode |
| Python         | 	black, isort, flake8, vulture             |
| TypeScript/JS	 | eslint --fix, prettier --write             |
| JSON/YAML	     | prettier, sort keys (optional)             |
| Shell          | 	shfmt, shellcheck                         |

## 📂 Directory Awareness
> ### module tidy will:
> * Auto-detect your repo root (via .git, go.mod, or pyproject.toml)
> * Respect language-specific ignore files like .eslintignore, .blackignore
> * Only operate on tracked files unless --all is passed

## ⚙️ Flags
| Flag	      | Description                           |
|------------|---------------------------------------|
| --fix	     | Auto-apply fixes                      |
| --verbose	 | Show all output from linters          |
| --all	     | Run tidy on untracked/uncommitted     |
| --dry	     | Show what would be changed (no write) |
| --diff	    | Show diff of changes applied          |

