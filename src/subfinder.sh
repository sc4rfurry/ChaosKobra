#!/usr/bin/env bash

git clone https://github.com/projectdiscovery/subfinder.git src/subfinder > /dev/null 2>&1
cd src/subfinder/v2/cmd/subfinder
go build > /dev/null 2>&1
cd -
chmod +x src/subfinder/v2/cmd/subfinder/subfinder
sudo cp  src/subfinder/v2/cmd/subfinder/subfinder /usr/bin/subfinder