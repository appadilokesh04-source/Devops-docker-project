**DevOps CI/CD Pipeline with Kubernetes Deployment**

**Project Overview**
This project demonstrates a complete DevOps workflow by containerizing a Flask application with MySQL, deploying it on Kubernetes, and automating the CI/CD pipeline using GitHub Actions.

**Architecture**
User → Ingress → Flask Service → Flask Pod → MySQL Service → MySQL Pod

**Tech Stack**
 Docker 
 Kubernetes (Minikube) 
 GitHub Actions 
 Flask (Python) 
 MySQL 

**Features**
 Containerized Flask + MySQL application
 Kubernetes Deployments and Services
 Ingress configuration for external access
 CI/CD pipeline for automated build and push
 Secure handling of environment variables and secrets

**CI/CD Pipeline**
* Code pushed to GitHub
* GitHub Actions workflow triggers
* Docker image is built automatically
* Image is pushed to Docker Hub


**Project Structure**
flask-deployment.yaml
flask-service.yaml
mysql-deployment.yaml
mysql-service.yaml
ingress.yaml
Dockerfile
docker-compose.yml
.github/workflows/ci.yml

**How to Run Locally**
**1.Start Minikube**
minikube start --driver=docker

**2. Enable Ingress**
minikube addons enable ingress

**3. Apply Kubernetes Config**
kubectl apply -f .

**4. Run Tunne**l
minikube tunnel

**5. Update Hosts File**
Add this line:
192.168.49.2 myapp.local

**6. Access Application**
http://myapp.local

**Screenshots**
<img width="1920" height="1020" alt="Screenshot 2026-03-26 184407" src="https://github.com/user-attachments/assets/d36ff561-2833-467f-83fa-5d9bd78959df" />
<img width="1920" height="1020" alt="Screenshot 2026-03-22 082258" src="https://github.com/user-attachments/assets/e6f9de39-7d72-45cb-bcbc-cdefd11203c7" />
<img width="1920" height="1020" alt="Screenshot 2026-03-22 082239" src="https://github.com/user-attachments/assets/da90c987-ddbb-49a9-8378-5d6683eb2557" />
<img width="1920" height="1020" alt="Screenshot 2026-03-22 082218" src="https://github.com/user-attachments/assets/83857a5c-48f9-409c-9c67-11ba3eab8b10" />

 GitHub Actions successful run
 Kubernetes pods running
 Application UI in browser

**Key Learnings**
 End-to-end CI/CD pipeline implementation
 Kubernetes deployment and networking
 Ingress configuration for routing
 Docker containerization best practices

**Author**
Lokesh Appadi
