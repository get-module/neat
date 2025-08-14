import subprocess
from pathlib import Path

class Format:
    def __init__(self, cwd=None):
        self.cwd = cwd

    def run_command(self, cmd):
        # Run a terminal cmd and print output to console
        try:
            subprocess.run(cmd, cwd=self.cwd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Command failed with exit code {e.returncode}")

    def go_fmt(self):
        self.run_command(["go", "fmt", "./..."])

    def go_imports(self):
        self.run_command(["goimports", "-w", "."])

    def golangci_lint(self):
        self.run_command(["golangci-lint", "run"])

    def go_deadcode(self):
        self.run_command(["deadcode", "./..."])

    # python
    def py_black(self):
        self.run_command(["black", "."])

    def py_isort(self):  # ordering of imports
        self.run_command(["isort", "."])

    def py_flake8(self):
        self.run_command(["flake8", "."])

    def py_vulture(self):
        self.run_command(["vulture", ".", "--min-confidence", "70"])

    # ts/js

    def ts_eslint(self):
        self.run_command(["eslint", "--fix", "."])

    def ts_prettier(self):
        self.run_command(["prettier", "--write", "."])

    # json/yaml
    def json_prettier(self):
        self.run_command(["prettier", "--write", "."])

    def json_sort_keys(self):
        self.run_command(["prettier", "--write", "--plugin=prettier-plugin-sort-json", "."])

    # shell
    # yeah fuck that
