#!/usr/bin/env bash
set -e

echo "Installing dependencies for Go, Python, TypeScript/JavaScript, JSON/YAML, and Shell..."

# --- Update system ---
sudo apt update && sudo apt upgrade -y

# --- Go Tools ---
sudo apt install -y golang-go
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/tsenart/deadcode@latest
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s latest

# --- Python Tools ---
sudo apt install -y python3 python3-pip
pip3 install --upgrade pip
pip3 install black isort flake8 vulture

# --- Node Tools ---
sudo apt install -y nodejs npm
sudo npm install -g eslint prettier prettier-plugin-sort-json

# --- Shell Tools ---
sudo apt install -y shfmt shellcheck

echo "All dependencies installed successfully."
