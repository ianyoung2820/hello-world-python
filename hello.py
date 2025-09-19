#!/usr/bin/env python3
"""
hello.py — tiny starter app for portfolio modules.

Shows basic I/O, a function, and a main guard. 
"""

from datetime import datetime
import platform

def greet(name: str = "World") -> str:
    """Return a friendly greeting string."""
    return f"Hello {name}!"

def diagnostics() -> str:
    """Return a short runtime diagnostic string for fun/personality."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        "— Diagnostics —\n"
        f"Timestamp: {ts}\n"
        f"Python:    {platform.python_version()}\n"
        f"Platform:  {platform.system()} {platform.release()}\n"
    )

if __name__ == "__main__":
    print(greet("World"))
    print(diagnostics())
