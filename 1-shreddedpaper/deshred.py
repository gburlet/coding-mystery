import os

blanksheet_path = "blanksheet.txt"
shreddedsheet_path = "shreddedsheet.txt"

line_prefix_hash = {}
with open(blanksheet_path, 'r') as bsf:
    bslines = bsf.readlines()
    for i_line, line in enumerate(bslines):
        line_prefix_hash[line[:20]] = i_line

deshred_lines = ["" for i in range(len(bslines))]
with open(shreddedsheet_path, 'r') as ssf:
    sslines = ssf.readlines()
    for line in sslines:
        deshred_lines[line_prefix_hash[line[:20]]] = line

deshred_path = "deshreddedsheet.txt"
with open(deshred_path, 'w') as dsf:
    dsf.writelines(deshred_lines)
