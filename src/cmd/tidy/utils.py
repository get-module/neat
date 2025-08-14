import subprocess
import sys

def is_windows() -> bool:
    # returns true if 'win32' else false
    return sys.platform == 'win32'

def install_tools():
    # TODO: check/rewrite install tools scripts
    # I had copilot write those for testing
    if is_windows():
        subprocess.run([
            "Set-ExecutionPolicy", "Bypass",
            "-Scope", "-Process", "-Force",
            ".\setup-scripts\install-tools.ps1"
        ])
    else:
        subprocess.run([
            "chmod +x ./setup-scripts/install-tools.sh",
            "./setup-scripts/install-tools.sh"
        ])