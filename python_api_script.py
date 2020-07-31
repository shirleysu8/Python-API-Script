# Import model dictionaries
from dict.text import text
from dict.vision import vision

#download model through url
import urllib.request
from onnxruntime import InferenceSession

#regular expression
import re

class onnx_zoo:
    
    def __init__(self, model_name, saved_path):
        
        #obtain model file name through regular expression
        pattern = re.compile(".*/([^/]+\\.onnx).*");
        m = pattern.match(self.path);
        self.file_name = m.group(1)
        
        #save the intended directory path
        self.saved_path = saved_path
        
        #obtain model url through dict
        if vision.get(model_name) != None:
            self.path = vision.get(model_name)
        elif text.get(model_name) != None:
            self.path = text.get(model_name)
        else:
            print("model name does not exist")
            
        
    def get_pretrained(self):
        model_url = self.path 
        model_directory = self.saved_path + self.file_name
        urllib.request.urlretrieve(model_url, model_directory)
        
    def get_metadata(self):
        sess = InferenceSession(self.name)
        meta = sess.get_modelmeta()
        
        print("custom_metadata_map={}".format(meta.custom_metadata_map))
        print("description={}".format(meta.description))
        print("domain={}".format(meta.domain, meta.domain))
        print("graph_name={}".format(meta.graph_name))
        print("producer_name={}".format(meta.producer_name))
        print("version={}".format(meta.version))
        
        
#mobilenet = onnx_zoo("mobilenetv2-7", "/Users/shirleysu/Downloads/")
#mobilenet.get_pretrained()
