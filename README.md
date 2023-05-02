# Azure-Cloud-DevOps-Builing-CI-CD-Pipeline

### Introduction
The target of this project is to create a CI/CD integration between a Github code repository and an Azure App Service. The code contains two workflows (pipelines).
The first pipeline “pythonapp.yml” is used to build an artifact from the file “hello.py” of the repository. After making the build, the code is validated using the file “test_hello.py”.
The second pipeline “main_flaskalberto.yml” is used to build and deploy an artifact using the file “app.py”. Once the app is deployed and working in Azure, it can be tested using the file “locustfile.py”

### Getting Started
1. Clone this project to your own code repository.
2. Make sure that the code is available from Azure shell, like in this screenshot:

3. Create an Azure web application service from Azure portal (don’t forget to link your own Github repository while creating it).


### Instructions
1. Execute the “make all” command and check that the output is correct, and the hello.py application is validated:


2. Push a commit to your code repository and chech that both pipelines are triggered:


### Demo on Youtube
The complete demonstration of the whole process can be watched in this Youtube video:

