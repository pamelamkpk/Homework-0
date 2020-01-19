import subprocess

def main():
	upstream_repo = "https://github.com/fri-robotlearning/Homework-0"

	subprocess.Popen(["git", "remote", "add", "upstream", upstream_repo], stdout=subprocess.PIPE)
	subprocess.Popen(["git", "fetch", "upstream"], stdout=subprocess.PIPE)
	subprocess.Popen(["git", "pull", "upstream", "master"], stdout=subprocess.PIPE)
	
if __name__ == "__main__":
    main()