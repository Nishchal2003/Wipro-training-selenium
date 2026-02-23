import subprocess

result = subprocess.run("dir", shell = True, capture_output = True, text=True)
#print(result)
print(result.stdout)

result = subprocess.run("python --version", shell = True, capture_output = True, text=True)
#print(result)
print(result.stdout)
print(result.stderr)