#!/bin/sh

git submodule foreach git pull
./r3/autogen.sh
./r3/configure && make
cd ./r3/ && make check # run tests
cd ./r3/ && sudo make install
