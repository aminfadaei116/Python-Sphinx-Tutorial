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


# Step 0

Our directory tree looks as the following
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
- Project name:
- Author names(s):
- Project release []: 
- Project language [en]: (default)

It is important to have the first question as default, different answers will cause error.

# Step 3
Go out of the doc folder any use this command.
```
sphinx-apidoc -o output_dir source_dir
```
e.g
```
sphinx-apidoc -o docs src/
```
This command will process all the files in `source_dir` and export them into `output_dir` 

# Step 4
Now go to the docs directory and open the project name directory (in our case it is called `Documents.rst`)

Add `src.` to the begining of the `.. automodule::` variable.

```
.. automodule:: src.Documents
.. automodule:: src.Documents.function1

```




# Step 5

```
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

```
