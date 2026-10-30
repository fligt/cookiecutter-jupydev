# Welcome to the jupydev cookiecutter template 

Fasten your seatbelts. After a decade of learning to code with Python and Jupyter notebooks that 'work on my computer' it is now time to take the development of Python packages to a next level and join forces with colleagues. In order to do so we need an efficient workflow to turn early experimental code in Jupyter notebooks into shared, solid, clean, well documented and version controlled python packages. This can now be done by combining a handfull of modern powerfull systems: 

**uv + jupyter + jupytext + quarto + git** 

Here are the steps that you need to take in order to get started with your first jupydev project. 

### STEP 1. Install the Miniconda Python environment and a few Python packages 

Go to the Anaconda website and follow the [installation instructions](https://www.anaconda.com/docs/getting-started/installation) for your operating system. We advice to install Miniconda which provides a basic Python environment. 

After installing Miniconda, upgrade pip and install jupyter with the following commands: 

    $ pip install -U pip 
    $ pip install jupyter 
    $ pip install cookiecutter 
 
### STEP 2. Install the `uv` Python package and project manager 

Go to the [docs.astral.sh/uv/](https://docs.astral.sh/uv/) website and follow the download and installation instructions for your operating system. 

### STEP 3. Install Quarto 

Go the [quarto.org](https://quarto.org/docs/get-started/) website and follow the download and installation instructions for your operating system. On a Debian-linux based OS installing a `.deb` file can be done with the terminal command: 

    $ sudo dpkg -i some-package.deb     


### STEP 4. Configure `git` and create a Github account 

(Still need to find good instructions to set up git and a github account)  

### STEP 5. Create your new jupydev project with cookiecutter 

 Use the jupydev cookiecutter template to create your own local project folder with the following terminal command: 
 
      $ cookiecutter https://github.com/fligt/cookiecutter-jupydev 
      
Answer all questions to generate the complete project folder structure with example notebooks. 
 
### Start working on your project 

In order to get started open a terminal, cd into the project folder and start jupyter lab with the following command: 

    $ uv run jupyter lab . 
    
If you have used `jupyter lab .` before you might wonder why we have prepended `uv run` to the command. By prepending `uv run` the jupyterlab instance is aware of the python modules that are present in the `src/<your_package>` folder of the uv project. This means that they can be imported into your notebooks.   

(Need some further instructions here on how to do things.)


