# Freud-Tool

Client-Specific Equivalence Checking with PyExSMT

## Installing

```bash
# Install this fork of PySMT >= 0.7.1dev
git clone https://github.com/FedericoAureliano/pysmt.git
cd pysmt
sudo python3 setup.py install
cd ..

# Install PyExSMT
git clone https://github.com/FedericoAureliano/PyExSMT.git
git checkout baseline_shadow
cd PyExSMT
sudo python3 setup.py install
cd ..

# Install Freud
git clone https://github.com/Client-Specific-Equivalence-Checker/freud-tool.git
cd freud-tool
sudo python3 setup.py install
```

## Usage

```bash
freud <V1_FILE> <V2_FILE> --client <NAME_OF_CLIENT> --library <NAME_OF_LIBRARY> <RETURN_TYPE> <ARG_TYPES>
```

## Example

```bash
freud loopmult20.py loopmult20_1.py --client loopmult20 --library lib int [int,int]

Attempting to Prove:
(((18 <= x) ? ((x < 22) ? ((... + ...) + x) : 0) : 0) = ((18 <= x) ? ((x < 22) ? ((... < ...) ? (... ? ... : ...) : Unknown) : 0) : 0))

CSE Proven by Assertion!
Execution time: 0.130 seconds
```
