#!/usr/bin/env bash

git clone https://github.com/projectdiscovery/httpx.git src/httpx > /dev/null 2>&1
cd src/httpx/cmd/httpx
go get > /dev/null 2>&1
go build > /dev/null 2>&1
chmod +x httpx
sudo mv  httpx /usr/bin/httpxt