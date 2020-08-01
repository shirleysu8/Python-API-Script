import onnx
import numpy as np
from pathlib import Path
import re

# identify list of onnx models in model Zoo
model_list = []
dict = {}

# generate paths to onnx models in the text folder
for path in Path('text').rglob('*.onnx'):
    model_list.append(str(path))
    if path != None:
        # generate the url to download onnx models
        url_paths = 'https://github.com/onnx/models/blob/master/' + str(path)  + '?raw=true'
        # use regular expression to obtain model name
        pattern = re.compile(".*/([^/]+\\.*)/model")
        m = pattern.match(url_paths)
        if m != None:
            file_name = m.group(1)
            # if model name is already in dict, then generate its name based on the file name
            if file_name in dict:
                pattern = re.compile(".*/([^/]+\\.*).onnx")
                m = pattern.match(url_paths)
                file_name = m.group(1)
            # add model and url to dict
            dict[file_name] = url_paths
            
        
# generate paths to onnx models in the vision folder  
for path in Path('vision').rglob('*.onnx'):
    model_list.append(str(path))
    if path != None:
        # generate the url to download onnx models
        url_paths = 'https://github.com/onnx/models/blob/master/' + str(path)  + '?raw=true'
        # use regular expression to obtain model name
        pattern = re.compile(".*/([^/]+\\.*)/model")
        m = pattern.match(url_paths)
        if m != None:
            file_name = m.group(1)
            # if model name is already in dict, then generate its name based on the file name
            if file_name in dict:
                pattern = re.compile(".*/([^/]+\\.*).onnx")
                m = pattern.match(url_paths)
                file_name = m.group(1)
            # add model and url to dict
            dict[file_name] = url_paths
            
# print out the keys and values from dict 
for keys,values in dict.items():
    print (f'"{keys}"' + " : " + f'"{values}"' + " ,")