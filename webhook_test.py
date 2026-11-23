import subprocess


def webhook_test(command):
    print("EvoAgent webhook test")
    subprocess.run(command, shell=True)
