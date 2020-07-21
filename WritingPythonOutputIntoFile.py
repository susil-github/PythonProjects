import subprocess;

with open("D://outputResult.txt","wb") as f:
    subprocess.check_call(["python","CentigradeToFarhenhite.py"],stdout=f);
