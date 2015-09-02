#!/bin/bash

#make poretools dependencies locally
cd argparse-1.3.0
python setup.py install --user
cd ..

#make poretools and dependencies locally
cd poretools
python setup.py install --user
cd ..

#make marginAlign
cd marginAlign
pip install --user -r requirement.txt
make
#make test
cd ..

#add local dir to PATH, if not there
if [[ :$PATH: == *:"$HOME/.local/bin":* ]] ; then
    echo $PATH
else
    export PATH=$PATH:$HOME/.local/bin
fi

#add marginAlign bin to PATH
if [[ :$PATH: == *:"$PWD/marginAlign":* ]] ; then
    echo $PATH
else
    export PATH=$PATH:$PWD/marginAlign
fi
