#download model through url
import urllib.request

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
        
        
#mobilenet = onnx_zoo("mobilenetv2-7", "/Users/shirleysu/Downloads/")
#mobilenet.get_pretrained()