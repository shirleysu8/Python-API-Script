# import model dictionaries
from dict.models import modelDict
from dict.model_versions import versionDict

# download model through url
import urllib.request
from onnxruntime import InferenceSession

# regular expression
import re

def get_model_versions(model):
    
        if versionDict.get(model) != None:
             print(versionDict.get(model))
        else:
            print("model name does not exist")

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
        pattern = re.compile(".*/([^/]+\\.onnx).*");
        m = pattern.match(self.path);
        self.file_name = m.group(1)
        
    def get_pretrained(self):
        model_url = self.path 
        model_directory = self.saved_path + self.file_name
        urllib.request.urlretrieve(model_url, model_directory)
        
    def get_metadata(self):
        sess = InferenceSession(self.saved_path + self.file_name)
        meta = sess.get_modelmeta()
        
        if meta.custom_metadata_map != "":
            print("custom_metadata_map={}".format(meta.custom_metadata_map))
        if meta.description != "":
            print("description={}".format(meta.description))
        if meta.domain != "":
            print("domain={}".format(meta.domain, meta.domain))
        if meta.graph_name != "":
            print("graph_name={}".format(meta.graph_name))
        if meta.producer_name != "":
            print("producer_name={}".format(meta.producer_name))
        if meta.version != "":
            print("version={}".format(meta.version))
        
        
#mobilenet = onnx_zoo("mobilenetv2-7", "/Users/shirleysu/Downloads/")
#mobilenet.get_pretrained()
#get_model_versions("efficientnet-lite4")