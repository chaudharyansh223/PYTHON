import subprocess

cmd_output = subprocess.run(["df", "-Th"], capture_output=True, text=True)
with open("output.txt", "w") as file:
    file.write(cmd_output.stdout)

