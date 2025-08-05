# 📦 Neat – The Developer Hygiene CLI
Keep your codebase fast, clean, and consistent.
One command. One standard. Multi-language support.

## 🚀 What is Neat?
Neat is a powerful, no-BS CLI for tidying and maintaining modern codebases. It provides unified commands for:

* 🧹 Linting, formatting, and code cleanup

* 🧱 Scaffolding projects and templates

* 🧪 Running tests

* ⚙️ Managing configurations and developer tools

* 🧰 Utility scripts to make dev work faster and safer


## ⚡ ️ Installation
```bash
# Coming soon:
npm install -g neat-cli
# OR
curl -sSL https://neat.sh/install | bash
#Manual installation and binary builds for Go, Python, and Node available soon.
```

## 🛠 Commands
### 🔧 neat tidy – Lint, Format, Clean
Run all language-appropriate formatters, linters, and dead code scanners.

```bash
neat tidy [scope] [--fix] [--verbose]
```
| Scope     | 	Tools Used                                         |
|-----------|-----------------------------------------------------|
| go	       | gofmt, goimports, golangci-lint, deadcode           |
| py	       | black, flake8, vulture, isort                       |
| ts, js	   | eslint, prettier                                    |
| shell	    | shfmt, shellcheck                                   |
| json/yaml | 	prettier, optional key sorting                     |
| all       | 	Run everything intelligently across detected files |

### 🧱 neat gen – Generate Code or Templates
```bash
neat gen <type> <name> [options]
```
| Type     | 	Description                             |
|----------|------------------------------------------|
| sensor	  | Scaffold a new hardware ingestion module |
| service	 | Create a boilerplate service (Go/Py)     |
| cli      | 	Generate a CLI subcommand               |
| project  | 	Create a full project layout            |
| api	     | REST or gRPC scaffold                    |
| lib	     | Utility or shared library                |

### 🧪 neat test – Run Tests
```bash
neat test [target] [--watch] [--coverage]
```
>Auto-detects language & framework.
>Can be scoped to project, file, or dir

### 🧰 neat tools – Utilities
```bash
neat tools [subcommand]
```
| Subcommand      | Feature                                             |
|-----------------|-----------------------------------------------------|
| uuid            | Generate a UUID                                     | 
| env-check       | Check .env vs .env.example                          | 
| jsonfmt         | Prettify a JSON file                                | 
| loc             | Count lines of code per language                    | 
| memcheck        | Launch memory profiler if supported                 | 
| generatelicense | Generate open source licenses from the command line |

### ⚙️ neat config
```bash
neat config set <key> <value>
neat config get <key>
```
>Manage CLI preferences, global configs, or aliases.

## 💥 Example Workflows
```bash
neat tidy all --fix          # Fix all formatting issues
neat gen sensor AirQuality   # Create new sensor module
neat test terra-core         # Run tests for one module
neat tools loc               # Show code stats
neat config set default_scope go
```

## 🌐 Language Support (Current & Planned)
| Language   | 	Lint/Format | 	Generate	 | Test       |
|------------|--------------|------------|------------|
| Go	        | ✅ Yes        | 	✅ Yes     | 	✅ Yes     |
| Python     | 	✅ Yes	      | ✅ Yes	     | ✅ Yes      |
| TypeScript | 	✅ Yes       | 	✅ Yes     | 	✅ Yes     |
| Shell	     | ✅ Yes        | 	🚫 No	    | 🚫 No      |
| Rust	      | 🔜 Planned	  | 🔜	Planned | 🔜 Planned |
| Lua	       | 🔜 Planned	  | 🔜	Planned | 🔜 Planned |


>**Upcoming:**
>* File watching + auto-tidy on save
>
>* PR diff-only tidying
>
>* neat audit for hygiene scores
>
>* VSCode integration
>
>* Plugin system for custom commands


🙌 Contributing
PRs welcome. Bug reports too. Built with ❤️ by the Module team.