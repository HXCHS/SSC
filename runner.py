import subprocess

def git_pull():
    subprocess.run(['git', 'pull'])

if __name__ == "__main__":
    git_pull()
