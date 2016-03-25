#!/bin/sh

#make poretools dependencies locally
cd argparse-1.3.0
python setup.py install --user
cd ..

#make poretools and dependencies locally
cd poretools
pip install --user -r requirements.txt
python setup.py install --user
cd ..

#make marginAlign
cd marginAlign
pip install --user -r requirements.txt
make
#make test
cd ..

#make samtools, if applicable
:' if [[ ! -x $(which samtools) ]]; then 
    curl https://github.com/samtools/samtools/releases/download/1.3/samtools-1.3.tar.bz2
    cd samtools*
    make 
    make install 
fi'


#add local dir to PATH, if not there
if [[ $PATH == *"$HOME/.local/bin"* ]] ; then
    echo "echo $PATH"
else
    export PATH=$PATH:$HOME/.local/bin
fi

#add marginAlign bin to PATH
if [[ $PATH == *"$PWD/marginAlign"* ]] ; then
    echo "echo $PATH"
else
    export PATH=$PATH:$PWD/marginAlign
fi