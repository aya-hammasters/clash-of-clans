# clash-of-clans
A collection of scripts to get data from Supercell's Clash of Clans' API server.

## Requirements

1. Need python 3 to run
1. To run any of the scripts, you have to obtain a Clash of Clans API token. See [Getting Started](https://developer.clashofclans.com/#/getting-started) on how to get it

## current-cwl
This script prints the enemy TH distribution during CWL for the specified clans.

### How to Run
1. Edit the script in `current-cwl/currentCwlInfo.py` and search for the string `INPUT`
1. Enter the API Token and clans to get CWL info for
1. Change directory to `current-cwl` and run:
```
python currentCwlInfo.py
```
