🏃‍♂️ Running Plan App

A Python application with Dockerized deployment and Jenkins CI/CD

📌 Overview

The Running Plan App is a Python-based application designed to generate and manage running plans.
This project demonstrates a complete CI/CD pipeline using GitHub, Docker, and Jenkins, where every code change is automatically built and deployed.

🧰 Tech Stack

Python (Application)

Docker (Containerization)

Jenkins (CI/CD automation)

GitHub (Source control)

Linux-based containers

🏗️ Architecture
Developer → GitHub → Jenkins (CI/CD) → Docker Image → Docker Container

⚙️ Application Setup (Local Development)
1️⃣ Clone the repository
git clone https://github.com/BALASUBRAMANI619/RUNNING-PLAN-APP.git
cd RUNNING-PLAN-APP

2️⃣ Create virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

3️⃣ Install dependencies
python -m pip install -r requirements.txt

4️⃣ Run the application
python app.py


App will be available at:

http://localhost:5000

🐳 Docker Setup
Build Docker image
docker build -t running-app-new .

Run Docker container
docker run -d -p 5000:5000 --name running-app running-app-new

Verify container
docker ps

🔁 CI/CD with Jenkins
✔ Jenkins Integration

Jenkins is configured to automatically:

Pull latest code from GitHub

Build Docker image

Stop old container

Deploy new container

⏰ Build Trigger

Jenkins uses Poll SCM with:

H/2 * * * *


Every GitHub push triggers Jenkins within 2 minutes

📄 Jenkinsfile (Pipeline Stages)

Checkout source code

Build Docker image

Stop existing container

Run updated container

Verify running containers

📂 Project Structure
<img width="146" height="123" alt="image" src="https://github.com/user-attachments/assets/cdf600de-db7e-48af-910e-956910181c87" />


✅ Deployment Verification

After a successful Jenkins build:

Application runs in Docker

Accessible at:

http://localhost:5000


Jenkins console shows:

Started by an SCM change

🧪 Future Enhancements

Add automated unit tests

Integrate GitHub Webhooks for instant builds

Push Docker image to Docker Hub

Add environment-based configuration

Add monitoring & logging

👨‍💻 Author

Balasubramani Vembu
GitHub: BALASUBRAMANI619

⭐ Acknowledgements

This project was built to demonstrate real-world CI/CD automation using Jenkins and Docker.

<img width="595" height="416" alt="image" src="https://github.com/user-attachments/assets/9b84d79e-b225-48d7-ad19-b89c22dae210" />
<img width="815" height="536" alt="image" src="https://github.com/user-attachments/assets/d489b11d-2d00-47e0-b1ee-fa6c93c93b09" />
