#!/bin/sh

git submodule foreach git pull
./autogen.sh
./configure && make
make check # run tests
sudo make install
