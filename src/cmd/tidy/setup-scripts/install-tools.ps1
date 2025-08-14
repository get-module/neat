# Ensure script stops on error
$ErrorActionPreference = "Stop"

Write-Host "Installing dependencies for Go, Python, TypeScript/JavaScript, JSON/YAML, and Shell..." -ForegroundColor Green

# --- Check for Chocolatey ---
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Chocolatey not found. Installing Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# --- Go Tools ---
choco install -y golang
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/tsenart/deadcode@latest
choco install -y golangci-lint

# --- Python Tools ---
choco install -y python
pip install --upgrade pip
pip install black isort flake8 vulture

# --- Node Tools ---
choco install -y nodejs
npm install -g eslint prettier prettier-plugin-sort-json

# --- Shell Tools ---
choco install -y shfmt
choco install -y shellcheck

Write-Host "All dependencies installed successfully." -ForegroundColor Green
