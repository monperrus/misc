#!/usr/bin/python3
# preprocess a latex file
# author: Martin Monperrus
# url: https://github.com/monperrus/crypto/blob/main/preprocess-latex.py

import os
import re
import sys

def nocomment(line):
  x = re.sub(r'(.*[^\\])%.*$', r'\1', line) 
  if x == line: return x
  else: return nocomment(x)

def preprocess_latex(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    print("% start preprocess")
    # remove comments (take care of the escaped percent)
    lines = [ nocomment(line) for line in lines if not line.lstrip().startswith('%')]
    #re.sub(r'([^\\]).*$', r'\1', line)

    # stop if \endinput or \end{document} is encountered
    for i, line in enumerate(lines):
        if '\\endinput' in line or '\\end{document}' in line:
            if i<len(lines)-1: 
              lines = lines[:i+1]
            break

    output = []
    for line in lines:
      match = re.search(r'(?:input|include|subfile)\{(.*?)\}', line)
      if match:
              file = match.group(1)
              
              if not os.path.isfile(file):
                  file = file + '.tex'
              if os.path.isfile(file):
                  output.append("% " + line.strip())
                  output.extend(preprocess_latex(file))
              else:
                  output.append(line.strip())

      else:
          output.append(line.strip())

    return output

if __name__ == "__main__":
    for line in preprocess_latex(sys.argv[1]):
        print(line)


