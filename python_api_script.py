# import model dictionaries
from dict.models import modelDict

# download model through url
import urllib.request
import onnx
from onnxruntime import InferenceSession
import sys
import os

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
        try:
            onnx.checker.check_model(self.saved_path + self.file_name)
            print("Successfully downloaded the model!")
        except Exception:
            print("Error: " + Exception)
            sys.exit()
        
    def get_metadata(self):
        try:
            sess = InferenceSession(self.saved_path + self.file_name)
        except OSError as err:
            print("OS error: {0}".format(err))
            sys.exit()
        except:
            print("Error: Load " + self.file_name + " model first.")
            sys.exit()
        
        try:
            meta = sess.get_modelmeta()
        except OSError as err:
            print("OS error: {0}".format(err))
            sys.exit()
        except:
           print("Error: " + self.file_name + " model metadata is too big.")
           sys.exit()

        if meta is not None:
            print("custom_metadata_map={}".format(meta.custom_metadata_map))
            print("description={}".format(meta.description))
            print("domain={}".format(meta.domain, meta.domain))
            print("graph_name={}".format(meta.graph_name))
            print("producer_name={}".format(meta.producer_name))
            print("version={}".format(meta.version))
        else:
            print("Meta does not exist")
        

mobile = onnx_zoo("roberta", "/users/kundanapillari/Desktop/")
mobile.get_pretrained()

#mobilenet = onnx_zoo("mobilenetv2-7", "/Users/shirleysu/Downloads/")
#mobilenet.get_pretrained()
