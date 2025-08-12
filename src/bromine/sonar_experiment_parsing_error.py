"""
This file simulates a Ms Fabric Notebook, stored as a .py file, instead of as a .ipynb one.
When using the '%run' statement, which is valid for a Jupyter Notebook, but is invalid for a .py file, SonarQube logs a parsing ereror.
Here we experiment with using NOSONAR to try and suppress the parsing error
"""

print("Hello")

%run FooBar # NOSONAR

print("World")
