import subprocess


def main() -> None:

    # create uv project environment  
    subprocess.run(
        ["uv", "add", "--dev", "pip", "ipykernel", "nbclient", "jupytext", "jupyter"],
        check=True,
    )
    
    # also initialize git  
    subprocess.run(
        ["git", "init", "-b", "master"], 
        check=True,
    )

if __name__ == "__main__":
    main()
