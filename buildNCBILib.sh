#!/bin/bash
set -eux

if [ ! -d NCBITextLib ]; then
	git clone https://github.com/ncbi-nlp/NCBITextLib
	cd NCBITextLib/lib
	make
fi

