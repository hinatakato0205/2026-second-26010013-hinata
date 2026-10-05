import subprocess
result = subprocess.run(
    ["who"],
    capture_output=True,
    text=True
)

print(result.stdout)
