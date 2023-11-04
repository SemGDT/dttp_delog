# dttp Tool to build a timeline summary of user-defined events from a big txt log
## Overview
It happens so often that SW developers are provided with a massive log, so big that the developers don't have a good view of the timeline of the events of their interest.
Fortunately, this free software tool is a game changer since it allows the developers to define their own key events that they want to look for from any text log type
to build a much smaller log file that only shows their key events chronologically.
## Usage instruction
### Pre-requisite
Python3 is installed in the system where dttp_delog.py resides
### Steps
#### Craft the dttp_delog_tp.json based on the need
Key events are to be defined/adjusted in the dttp_delog_tp.json according to the following example:
```
{
  "<descriptive key>" : ["<matching keywords in the log>", "<how many lines to be extracted before the matching line>", "<after line>"]  
  "sunrise" : ["The rooster wakes up", "0", "0"],
  "sunset" : ["The bridge is closed", "0", "0"],
  "atwork" : ["Turn on the screen", "0", "10"],
  "cooking" : ["Turn on the cooker", "20", "10"]
}

Place this file in the same folder where dttp_delog.py resides.
When the <before> and <after> numbers are 0, the timestamp will be automatically detected and extracted from 1 of the 3 lines above the matching line. If not found, then no timestamp will be prepended.
When the <before> or <after> number is not 0, then timestamp won't be determined as enough information are displayed around the matching line already.
#### Run the command
```
python3 dttp_delog.py <folder/file.txt>

#### Enjoy your new reading
