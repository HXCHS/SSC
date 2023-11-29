import subprocess

def git_pull():
    subprocess.run(['git', 'pull'])
    print(f"Hello")

if __name__ == "__main__":
    git_pull()
