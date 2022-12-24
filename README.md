# python-package-sphinx-template


# Step 1
First install the required pakages, where I am using conda

```
conda install sphinx
conda install -c conda-forge sphinx_rtd_theme
```


# Step 2
Go to the docs directory and add this command.
```
sphinx-quickstart
```
After that it will ask you 4 questions:
- Separate source and build directories (y/n) [n]: (default)
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
  |-- main
   |   |-- java
   |   |   |-- com
   |   |   |   |-- foxguardsolutions
   |   |   |   |   |-- jonavon
   |   |   |   |   |   |-- AbstractFile.java
   |   |   |   |   |   |-- roman
   |   |   |   |   |   |   |-- Main.java
   |   |   |   |   |   |   |-- Numeral.java
   |   |   |   |   |   |   |-- RomanNumberInputFile.java
   |   |   |   |   |   |   |-- RomanNumeralToDecimalEvaluator.java
   |-- test
   |   |-- java
   |   |   |-- com
   |   |   |   |-- foxguardsolutions
   |   |   |   |   |-- jonavon
   |   |   |   |   |   |-- roman
   |   |   |   |   |   |   |-- InterpretSteps.java
   |   |   |   |   |   |   |-- RunCukesTest.java
   |   |-- resources
   |   |   |-- com
   |   |   |   |-- foxguardsolutions
   |   |   |   |   |-- jonavon
   |   |   |   |   |   |-- roman
   |   |   |   |   |   |   |-- Interpret.feature
   |   |   |-- sample-input.txt

```
