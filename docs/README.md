git add .* ```config.yaml```: Paths to the Artifacts in each phase

* ```params.yaml```: Configuration of Hyperparamters for the Deep Learning Model (VGG-16)

* ```Entity Directory```: Datatypes and Schema for the Data used in the pipeline.

* ```Configuration.py```: Configuration of the pipeline

* ```requirements.txt```: Required Libraries for pipeline execution


## Workflows Order

1. Update ```config.yaml```
2. Update ```params.yaml```
3. Update the ```Entity Directory```
4. Update the ```Configuration manager``` in src config
5. Update the ```Components```
6. Update the ```Training anf Prediction Pipeline```
7. Update the ```main.py```
8. Update the ```dvc.yaml```