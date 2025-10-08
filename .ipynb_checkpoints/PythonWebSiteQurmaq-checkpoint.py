import subprocess

# Explorer restart
subprocess.run("taskkill /f /im explorer.exe", shell=True)
subprocess.run("start explorer.exe", shell=True)
