# Client-Specific Equivalence Checking

## Installing

```bash
# 0. Prepare
pip3 install virtualenv
mkdir clever
virtualenv clever
cd clever
source bin/activate 

# 1. Clone repo
git clone https://github.com/Client-Specific-Equivalence-Checker/CLEVER.git
cd CLEVER

# 2. Install PySMT
cd deps/pysmt
# (may need) sudo apt-get install python3-setuptools
python3 setup.py install
cd ../..

# 3. Install Z3 with Python bindings
pysmt-install --z3
# 4. Obtain a string to update your PYTHONPATH and then update it 
# (you can just paste the string into your shell)
pysmt-install --env
# 5. Check that z3 was correctly installed
pysmt-install --check
# It should show
# z3        True (4.5.1)
# If you see
# "z3       False (None)"
# then step 3 failed. Follow the isntructions at https://github.com/Z3Prover/z3 to install z3 with python3 bindings
# If you see "Not in Python's path!" then step 4 was not completed correctly

# 6. Install PyExZ3
cd deps/PyExZ3
python3 setup.py install
cd ../..

# 7. Install CLEVER
cd src
python3 setup.py install
cd ..

# 8. Use. See below.

# 9. Deactiviate Virtualenv
deactivate
```

## Usage

```bash
CLEVER <V1_FILE> <V2_FILE> --client <NAME_OF_CLIENT> --library <NAME_OF_LIBRARY> <RETURN_TYPE> [<ARG_TYPES>]
```

## Example

```bash
CLEVER loopmult20.py loopmult20_1.py --client loopmult20 --library lib int [int,int]

Attempting to Prove:
(((18 <= x) ? ((x < 22) ? ((... + ...) + x) : 0) : 0) = ((18 <= x) ? ((x < 22) ? ((... < ...) ? (... ? ... : ...) : Unknown) : 0) : 0))

CSE Proven by Assertion!
Execution time: 0.130 seconds
```
