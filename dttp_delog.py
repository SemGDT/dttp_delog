"""
Software to build a timeline of the events of interest
from a text log.

The events can be defined in the dttp_delog_tp.json

Author: dttp (aka phbtt) 11/2023

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute
this software, either in source code form or as a compiled binary, for any
purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the
public domain. We make this dedication for the benefit of the public at
large and to the detriment of our heirs and successors. We intend this
dedication to be an overt act of relinquishment in perpetuity of all present
and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
import json
import os
import re
import sys

def build_keyword(jsonfile):
    """
    Build search keyword from tp json file
    """
    with open(jsonfile) as keywords:
        json_data = json.loads(keywords.read())

    return json_data

def locate_timestamp(linesdict, currlineindex, reverse_dist):
    """
    Search backward, up to reverse_dist step. Return the first encountered timestamp
    """
    timestamp_fmt = "\d{2}:[0-5]\d:[0-5]\d"
    for i in range(currlineindex, currlineindex - reverse_dist, -1):
        match = re.search(timestamp_fmt, linesdict[i])
        if match:
            return linesdict[i][:match.end() + 4]

def build_buf(linesdict, currlineindex, back_dist, forward_dist):
    """
    Build the buf starting from back_dist to forward_dist
    """
    buf = ''

    for i in range(currlineindex - back_dist, currlineindex + forward_dist, 1):
        buf += linesdict[i]
    return  i, buf

#####################################################################
#
# Main program starts here
#
#####################################################################

if len(sys.argv) != 2:
    print(f"Usage: python dttp_delog.py <txt log to parse>")
else:
    keywordsfile = "dttp_delog_tp.json"
    txtfile = sys.argv[1]

with open(txtfile, 'r') as file:
    # Read the entire file content
    lines = file.readlines()

json_data = build_keyword(keywordsfile)
values = json_data.values()
for index, line in enumerate(lines):
    for index_tp, tp_item in enumerate(values):
        text = tp_item[0]
        if text in line:
             back_dist = int(tp_item[1])
             forward_dist = int(tp_item[2])
             if 0 == back_dist and 0 == forward_dist:
                 timestamp = locate_timestamp(lines, index, 3)
                 if timestamp:
                     print(f"{timestamp} {line}")
                 else:
                     print(line)
             else:
                 index, buf = build_buf(lines, index, back_dist, forward_dist)
                 line = lines[index]
                 print(buf)

             # Done with the current line, process next line
             break
