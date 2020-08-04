# import model dictionaries
from dict.models import modelDict

# download model through url
import urllib.request
from onnxruntime import InferenceSession

# regular expression
import re

class onnx_zoo:
    
    def __init__(self, model_name, saved_path):
        
        # save the intended directory path
        self.saved_path = saved_path
        
        # obtain model url through dict
        if modelDict.get(model_name) != None:
            self.path = modelDict.get(model_name)
        else:
            print("model name does not exist")
        
        # obtain model file name through regular expression
        pattern = re.compile(".*/([^/]+\\.onnx).*")
        m = pattern.match(self.path)
        self.file_name = m.group(1)
        
    def get_pretrained(self):
        model_url = self.path 
        model_directory = self.saved_path + self.file_name
        urllib.request.urlretrieve(model_url, model_directory)
        
    def get_metadata(self):
        sess = InferenceSession(self.saved_path + self.file_name)
        meta = sess.get_modelmeta()

        if meta is not None:
            print("custom_metadata_map={}".format(meta.custom_metadata_map))
            print("description={}".format(meta.description))
            print("domain={}".format(meta.domain, meta.domain))
            print("graph_name={}".format(meta.graph_name))
            print("producer_name={}".format(meta.producer_name))
            print("version={}".format(meta.version))
        else:
            print("Meta does not exist")
        
        
#mobilenet = onnx_zoo("mobilenetv2-7", "/Users/shirleysu/Downloads/")
#mobilenet.get_pretrained()
