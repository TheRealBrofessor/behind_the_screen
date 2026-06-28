#!/usr/bin/env python3
"""Beginner-friendly local networking helper.

This script only reads basic network information from the local machine.
It does not scan other devices or attempt to connect to private systems.
"""

from __future__ import annotations

import platform
import shutil
import socket
import subprocess
from typing import Iterable


def run_command(command: Iterable[str]) -> str:
    """Run a local read-only command and return clean output."""
    command_list = list(command)
    if not command_list:
        return "No command provided."

    if not shutil.which(command_list[0]):
        return f"Command not found: {command_list[0]}"

    try:
        result = subprocess.run(
            command_list,
            check=False,
            capture_output=True,
            text=True,
            timeout=8,
        )
    except subprocess.TimeoutExpired:
        return "Command timed out."

    output = result.stdout.strip() or result.stderr.strip()
    return output or "No output returned."


def print_section(title: str, body: str) -> None:
    """Print a clean section for beginners reading terminal output."""
    print(f"\n=== {title} ===")
    print(body)


def main() -> None:
    hostname = socket.gethostname()

    print("Behind the Screen - Mini Network Lab")
    print("This only checks your own computer. No scanning. No attacking.\n")

    print_section("Computer Name", hostname)
    print_section("Operating System", platform.platform())
    print_section("Local IP Addresses", run_command(["hostname", "-I"]))
    print_section("Network Adapters", run_command(["ip", "-brief", "addr"]))
    print_section("Default Route", run_command(["ip", "route"]))
    print_section("DNS / Internet Check", run_command(["ping", "-c", "4", "example.com"]))

    print("\nWrite down what you saw:")
    print("- Local IP address:")
    print("- Router/default gateway:")
    print("- Wi-Fi or Ethernet adapter:")
    print("- Did ping work:")


if __name__ == "__main__":
    main()
