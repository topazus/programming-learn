import os
import shlex
import subprocess

# subprocess in Python is a task that Python scripts delegate to (operating system) OS
subprocess.run("ls")
subprocess.run("ls -la", shell=True)
subprocess.run(["ls", "-la"])

print(shlex.split("ls -la"))
print("ls -la".split())

# `capture_output=True` store output of subprocess in a variable
out = subprocess.run(["uname", "-m"], capture_output=True)
print(out.stdout)
# decode bytes to str
arch = out.stdout.decode().strip()
print(arch)
# `text=True` return in str
out = subprocess.run(["date"], capture_output=True, text=True)
print(out.stdout)

out = subprocess.run(["echo $SHELL"], shell=True, capture_output=True, text=True)
print(out.stdout)
