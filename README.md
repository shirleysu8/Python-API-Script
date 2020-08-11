# Python-API-Script
Onnx Python API Script used to download and save pretrained models from [onnx model zoo](https://github.com/onnx/models). Retrieves metadata after the model is successfully downloaded. 

## Features 


```get_model_versions(model name)``` - Retrieves an array of all the versions of the specificed model folder in the Onnx Model Zoo. 
    Example: 
        Input:
            ```
            # Initiate the onnx_zoo class object.
            resnet = onnx_zoo()
            # Input the model name, in all lowercase, into the method.
            get_model_versions(resnet)
            ```
        Ouput: 
            
            ```
            # Outputs all the model's versions into an array. These model file names can then be inputted into the onnx_zoo class to download and view its metadata.
            ['resnet101-v1-7', 'resnet101-v2-7', 'resnet152-v1-7', 'resnet152-v2-7', 'resnet18-v1-7', 'resnet18-v2-7', 'resnet34-v1-7', 'resnet34-v2-7', 'resnet50-caffe2-v1-3', 'resnet50-caffe2-v1-6', 'resnet50-caffe2-v1-7', 'resnet50-caffe2-v1-8', 'resnet50-caffe2-v1-9', 'resnet50-v1-7', 'resnet50-v2-7']```
    

```get_pretrained()``` - Downloads and saves specific onnx models to desired path.
            Example Inputs: 
               Model File Name : ``` resnet101-v1-7 ``` 
               Saved Directory Path : ``` /Users/name/Downloads ```
       

```get_metadata()``` - Retrieves metadata of the onnx model. 
        
## Intialization 
Initiate the object by calling onnx_zoo class name.
```
MODEL_NAME = onnx_zoo()
```
The Python scipt will then ask to input the model folder name. When inputting the name, it should be in all lowercase. 

```Enter Model Name: resnet```
                       
After model folder name is inputted, the script will output all the model versions that exist in the folder. 

```['resnet101-v1-7', 'resnet101-v2-7', 'resnet152-v1-7', 'resnet152-v2-7', 'resnet18-v1-7', 'resnet18-v2-7', 'resnet34-v1-7', 'resnet34-v2-7', 'resnet50-caffe2-v1-3', 'resnet50-caffe2-v1-6', 'resnet50-caffe2-v1-7', 'resnet50-caffe2-v1-8', 'resnet50-caffe2-v1-9', 'resnet50-v1-7', 'resnet50-v2-7'] ```

From the array of versions, input the version that will be downloaded and input the local directory that the model will be saved in.

``` Enter model name from options: resnet101-v1-7 
    Enter saved path: /Users/name/Downloads
```

To download the model and output its metadata, run the following functions:

``` 
    MODEL_NAME.get_pretrained()
    MODEL_NAME.get_metadata()
```



    

## Installation 
Install onnx to check models

```pip install onnx```

Install [onnxruntime](https://github.com/microsoft/onnxruntime) to run onnx models

```pip install onnxruntime```
