# Azure-Cloud-DevOps-Builing-CI-CD-Pipeline

### Introduction
The target of this project is to create a CI/CD integration between a Github code repository and an Azure App Service. The code contains two workflows (pipelines).
The first pipeline “pythonapp.yml” is used to build an artifact from the file “hello.py” of the repository. After making the build, the code is validated using the file “test_hello.py”.
The second pipeline “main_flaskalberto.yml” is used to build and deploy an artifact using the file “app.py”. Once the app is deployed and working in Azure, it can be tested using the file “locustfile.py”

### Getting Started
1. Clone this project to your own code repository.
2. Make sure that the code is available from Azure shell, like in this screenshot:
![2023-04-23 18_55_54-](https://user-images.githubusercontent.com/40852884/235792036-814a881c-6346-4252-8a22-fd7d23b3da68.png)
3. Create an Azure web application service from Azure portal (don’t forget to link your own Github repository while creating it).


### Instructions
1. Execute the “make all” command and check that the output is correct, and the hello.py application is validated:
![2023-04-23 19_33_23-Inicio - Microsoft Azure](https://user-images.githubusercontent.com/40852884/235792123-420879d3-02b2-4db6-9354-f199a50bdc34.png)
2. Push a commit to your code repository and check that both pipelines are triggered:
![Sin título](https://user-images.githubusercontent.com/40852884/235792341-9bea6961-a08b-4693-aa08-4f309521a5aa.png)
3. The pipeline “pythonapp.yml” should build the artifact correctly:
![image](https://user-images.githubusercontent.com/40852884/235792236-74074309-3c18-428e-947b-6965b0159bc8.png)
4. The pipeline “main_flaskalberto.yml” should build the artifact and deploy the application correctly to your Azure Cloud environment.
![image](https://user-images.githubusercontent.com/40852884/235792874-83bb6d25-f108-47d0-91f4-700f1db3e66a.png)
5. The deployed application can be tested the file “locustfile.py”
![image](https://user-images.githubusercontent.com/40852884/235793343-bfb1f2d4-e535-4ce0-96e2-8e352260129d.png)


### Demo on Youtube
The complete demonstration of the whole process can be watched in this Youtube video:
https://youtu.be/uiDfz1AEr1s

