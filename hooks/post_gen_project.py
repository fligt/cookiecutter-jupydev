import subprocess


def main() -> None:
    subprocess.run(
        ["uv", "add", "--dev", "pip", "ipykernel", "nbclient", "jupytext"],
        check=True,
    )

if __name__ == "__main__":
    main()
