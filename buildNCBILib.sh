#!/bin/bash
set -eux

rm -fr NCBITextLib
git clone https://github.com/ncbi-nlp/NCBITextLib
cd NCBITextLib/lib
make

