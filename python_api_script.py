# Import model dictionaries
from dict.text import text
from dict.vision import vision

#download model through url
import urllib.request
from onnxruntime import InferenceSession

class onnx_zoo:
    
    def __init__(self, model_name, saved_path):
        PATH_MAP = {
        #Image Classification
        "mobilenetv2-7": "https://github.com/onnx/models/blob/master/vision/classification/mobilenet/model/mobilenetv2-7.onnx?raw=true"
        } 
        self.name = model_name + ".onnx"
        self.saved_path = saved_path
        self.path = PATH_MAP.get(model_name)
            
        
    def get_pretrained(self):
        #model_path = "https://github.com/onnx/models/blob/master/vision/classification/resnet/model/"
        #raw = "?raw=true"
        url = self.path 
        url_input = self.saved_path + self.name
        urllib.request.urlretrieve(url, url_input)
        
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
