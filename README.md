# Kidney-Disease-Classification with MLflow and DVC pipeline


## Creating files

1. config.yaml
2. params.yaml
3. common.py in utils folder

## Tasks
3. Update the config_entity.py in entity
4. Update the configuration.py in config
5. Update files of each stage in components folder 
6. Update files of each stage in pipeline folder 
7. Update the main.py
8. Update the dvc.yaml
9. Create index.html for UI 
10. app.py




# Steps for running


### Step 1. Clone the repository

Command : git clone https://github.com/yash631/Kidney_Disease_Classification.git


### STEP 2. Create a conda virtual environment 

Command : conda create -n kidney python=3.8 -y


### STEP 3. Activate the environment

Command : conda activate kidney


### STEP 4. Install the requirements

Command : pip install -r requirements.txt


### STEP 5. Run template.py to create files and folders 

Command : python template.py


### STEP 6. Execute program after creating the model

 -->  For running main file 
 Command : python main.py

 -->  For running dvc.yaml file
 Command : dvc repro

 -->  For running the app
 Command : python app.py




## MLflow

### STEP 1. Connect the github repository with dagshub
Repository Link => https://dagshub.com/yash631/Kidney_Disease_Classification/src/main 


### STEP 2. Open MLFlow UI

MLFLOW_TRACKING_URI=https://dagshub.com/yash631/Kidney_Disease_Classification.mlflow
MLFLOW_TRACKING_USERNAME=yash631
MLFLOW_TRACKING_PASSWORD=bacbf998668fae5fb780cd896be3ace34d52b928 


### STEP 3. Set MLFLOW variables as Environment variables

a) Git or bash commands

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0
```

b) Powershell commands

```Powershell
$env:MLFLOW_TRACKING_URI="https://dagshub.com/yash631/Kidney_Disease_Classification.mlflow"

$env:MLFLOW_TRACKING_USERNAME="yash631"

$env:MLFLOW_TRACKING_PASSWORD="bacbf998668fae5fb780cd896be3ace34d52b928"
```


### STEP 4. Execute the Program and use MLFLOW to visualize the models



### DVC commands

1. dvc init
2. dvc repro
3. dvc dag