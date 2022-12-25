# python-package-sphinx-template

<!-- For future purposes
.
├── dir1
│   ├── file11.ext
│   └── file12.ext
├── dir2
│   ├── file21.ext
│   ├── file22.ext
│   └── file23.ext
├── dir3
├── file_in_root.ext
└── README.md
-->



The directory distribution looks like this:
```
.
├── ProjectName
    ├── docs
    └── src
        ├── main
        │   ├── __init__.py
        │   └── function1.py
        └── test
```

In the `__init__.py` and `function1.py` there should be some code with proper comments.

# Step 1
First install the required pakages, where I am using conda

```
conda install sphinx
conda install -c conda-forge sphinx_rtd_theme
```


# Step 2
Go to the `docs` directory and add this command.
```
sphinx-quickstart
```
After that it will ask you 4 questions:
- `Separate source and build directories (y/n) [n]:` (default)
- `Project name:`
- `Author names(s):`
- `Project release []:` 
- `Project language [en]:` (default)

It is important to have the first question as default, different answers will cause error.

# Step 3
Go out of the `docs` folder (currently in `\ProjectName\` directory) and use this command.
```
sphinx-apidoc -o output_dir source_dir
```
This command will process all the files in `source_dir` and export them into `output_dir` 
which in our case we will use:
```
sphinx-apidoc -o docs src/
```


# Step 4
Now go to the docs directory and open the project name directory (in our case it is called `Documents.rst`)

Add `src.` to the begining of the `.. automodule::` variable.

```
.. automodule:: src.Documents
.. automodule:: src.Documents.function1

```

# Step 5
Go to the `conf.py` and uncomment the imports and add the following import
```
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import src.main
```
You also need to modify the `extensions` and `html_theme` as.
```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',

]
```
```
html_theme = 'sphinx_rtd_theme'
```

# Step 6

Now go to the `index.rst` and add `.. include:: Documents.rst`  below the `..toctree::`.

# Step 7

In the end go to `Project\docs\` and run `make html`.


