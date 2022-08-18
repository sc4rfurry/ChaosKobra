#!/usr/bin/env bash

git clone https://github.com/tomnomnom/httprobe.git src/httprobe > /dev/null 2>&1
cd src/httprobe
go build > /dev/null 2>&1
cd ../
chmod +x httprobe/httprobe
sudo cp  httprobe/httprobe /usr/bin/httprobe