# Freud-Tool

Client-Specific Equivalence Checking with PyExSMT

## Installing

```bash
# Install PySMT >= 0.7.1dev
git clone https://github.com/pysmt/pysmt.git
cd pysmt
sudo python3 setup.py install
cd ..

# Install PyExSMT
git clone https://github.com/FedericoAureliano/PyExSMT.git
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