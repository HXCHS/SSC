import subprocess

def git_pull():
    subprocess.run(['git', 'pull'])
    print(f"Hello, Again")

if __name__ == "__main__":
    git_pull()
