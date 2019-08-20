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
git checkout KLEE_CLEVER

# 2. Installing Klee
sudo apt-get install build-essential curl libcap-dev git cmake libncurses5-dev python-minimal python-pip unzip libtcmalloc-minimal4 libgoogle-perftools-dev libsqlite3-dev
sudo apt-get install clang-6.0 llvm-6.0 llvm-6.0-dev llvm-6.0-tools
sudo pip install lit
git clone https://github.com/FedericoAureliano/klee
cd klee
git checkout Nick
mkdir build
cd build
cmake -DLLVM_CONFIG_BINARY=/usr/bin/llvm-config-6.0 .. -DENABLE_SOLVER_Z3=ON ..
sudo make install

# 3. Install pycparser:
pip install pycparser

# 4. Install CLEVER
cd src
python3 setup.py install
cd ..

# 5. Use. See below.

# 6. Deactiviate Virtualenv
deactivate
```

## Usage

```bash
CLEVER --old=<V1_FILE> --new=<V2_FILE> --client <NAME_OF_CLIENT> --lib <NAME_OF_LIBRARY>
```

## Example

```bash
KLEE_CLEVER --old examples/neq/loopmult100/old.c --new examples/neq/loopmult100/new.c --client main --library foo

time : 0.690563

CEX x : 85
```
