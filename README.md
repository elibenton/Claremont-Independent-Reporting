## Understanding the Claremont Independent

* Read the article [here]().
* See the dataset of Collegiate Network publications [here]().
* Assess the methodolgy of linguistic and backlink visualizations [here]().

Continue reading this page to set up a coding environment where you can explore our data for yourself.

### Getting Started

##### Step 1: Download [Anaconda (MacOS)](https://www.anaconda.com/download/#macos)
```bash
# Ensure the path to the "conda" command is in your $PATH
cd
vi .bash_profile

# You should see the following somewhere in the file;
export PATH="/Users/{your-user-name}/anaconda3/bin:$PATH"

# To exit the file viewer, type:
:q
```

##### Step 2: Make Project Directory
```bash
# Create project folder on your desktop.
cd Dekstop
mkdir Claremont-Independent-Report
cd Claremont-Independent-Report
```

##### Step 3: Create Virtual Environment
```bash
# Create virtual environment in which to install packages.
conda create --name ci-report

# Install all packages needed for analysis:
# - Requests
# - Beautiful Soup
# - Jupyter Lab
conda install --name ci-report requests beautifulsoup4
conda install --name ci-report -c conda-forge jupyterlab

# Activate the environment. The comand line prompt should now start with (ci-report).
source activate ci-report
```
Referece: [Setting Up a Conda Environtment](https://conda.io/docs/user-guide/getting-started.html)

##### Step 4: Install Mozcape Package
```bash
# Clone mozscape package from github and install the contents.
git clone https://github.com/seomoz/SEOmozAPISamples.git
cd SEOmozAPISamples/python
pip install .
```
Reference: [Mozscape API - Python Code Examples](https://github.com/seomoz/SEOmozAPISamples/tree/master/python)


##### Step 5: Launch Jupyter Lab
```bash
# Go back to root of project folder and launch jupyter.
cd ../..
jupyter lab
```
Reference: [Jupyter Documenation](http://jupyterlab.readthedocs.io/en/latest/getting_started/installation.html) 

##### Step 6: Import Necessary Libaries
```python
# Imports for python code to function properly
import pprint, os, csv, json, pickle, requests, html5lib
from bs4 import BeautifulSoup

# Import mozscape and give API credentials
from mozscape import Mozscape
client = Mozscape('my_access_id', 'my_secret_key')

# Print in format easier to read
pp = pprint.PrettyPrinter(indent=4)
```
Reference: [Mozscape API - Python Code Examples](https://github.com/seomoz/SEOmozAPISamples/tree/master/python)