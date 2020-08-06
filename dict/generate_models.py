import onnx
import numpy as np
from pathlib import Path
import re
import pdb

model_list = []
dict = {}   # ex: "vgg" : "https://github.com/onnx/models/blob/master/vision/classification/vgg/model/vgg16-7.onnx?raw=true"
folder_names = ["text", "vision"]

# generate paths to text or vision onnx models
for model_type in folder_names:
    generate_paths(model_type)
            
# print out the keys and values from dict 
for keys,values in dict.items():
    print (f'"{keys}"' + " : " + f'"{values}"' + " ,")

def generate_paths(folder_names):
    """
    Generates a list of onnx models and
    stores them in `dict` and `model_list`
    """
    for path in Path(folder_names).rglob('*.onnx'):
        model_list.append(str(path))
        if path != None:
            # Generate onnx model URL
            url_paths = 'https://github.com/onnx/models/blob/master/' + str(path)  + '?raw=true'
            # Obtain model name
            pattern = re.compile(".*/([^/]+\\.*)/model")
            m = pattern.match(url_paths)
            if m != None:
                file_name = m.group(1)
                # if model name is already in dict, then generate its name based on the file name
                if file_name in dict:
                    pattern = re.compile(".*/([^/]+\\.*).onnx")
                    m = pattern.match(url_paths)
                    file_name = m.group(1)
                dict[file_name] = url_paths