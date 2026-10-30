import subprocess


def main() -> None:

    # create uv project environment  
    subprocess.run(
        ["uv", "add", "--dev", "pip", "ipykernel", "nbclient", "jupytext", "jupyter", "jupyterlab-quarto"],
        check=True,
    )
    
    # also initialize git  
    subprocess.run(
        ["git", "init", "-b", "master"], 
        check=True,
    )
    
    # and add github remote 
    subprocess.run(
        ["git", "remote", "add", "origin", "git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}.git"], 
        check=True, 
    )

if __name__ == "__main__":
    main()
