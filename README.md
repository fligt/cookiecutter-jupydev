# Welcome to the uv-project-a2z cookiecutter template 

Fasten your seatbelts. After a decade of learning to code with Python and Jupyter notebooks that 'work on my computer' it is now time to take the development of Python packages to a next level and join forces with colleagues. In order to do so we need an efficient workflow to to turn early experimental code in Jupyter notebooks into shared, solid, clean and well documented python packages. This can now be done by combining a handfull of modern powerfull systems: 

**uv + codium + jupyter + jupytext + quarto + git** 

Here are the steps that you need to take in order to get started with your first uv A to Z project. 

### STEP 1. Install the `uv` Python package and project manager 

Go to the [docs.astral.sh/uv/](https://docs.astral.sh/uv/) website and follow the download and installation instructions for your operating system. 

### STEP 2. Install VSCodium

Download and install VSCodium from their website [vscodium.com](https://vscodium.com/). 

### STEP 3. Install a bunch of extensions within VSCodium 

Open the Extensions pane from the VSCodium side menu and install the following extensions: Python, Python Debugger, Python Environments, Python Snippets 3, Jupyter, Jupyter Notebook Renderers, Jupyter Keymap, Jupytext Sync, Live Server, Material Icon Theme 

After installing the extensions restart VSCodium. 

### STEP 4. Install Quarto 

Go the [quarto.org](https://quarto.org/docs/get-started/) website and follow the download and installation instructions for your operating system. On a Debian based OS installing a .deb file can be done with the terminal command: *sudo dpkg -i <a-debian-package.deb*.    

### STEP 5. Configure `git` and create a Github account 

(Still need to find good instructions to set this up)  

### STEP 6. Clone existing or create a new local project folder   

If you step into an existing project you can start working by simply cloning onto your computer. 

    $ git clone git@github.com:fligt/your-repo.git

Otherwise if you need to start from scratch you can use the python `cookiecutter` package to build your fresh folder structure using the `uv-project-a2z` template with the following terminal command: 

     $  uvx cookiecutter https://github.com/fligt/cookiecutter-uv-project-a2z 
     
Answering all the cookiecutter questions in the terminal to generate the project folder structure. 




