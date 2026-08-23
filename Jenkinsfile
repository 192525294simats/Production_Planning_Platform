pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'feature/devsecops-final',
                    url: 'https://github.com/192525294simats/Production_Planning_Platform.git'
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker build -t production-planning-backend ./backend'
            }
        }

        stage('Build Frontend') {
            steps {
                sh 'docker build -t production-planning-frontend ./frontend'
            }
        }

        stage('Run Backend') {
            steps {
                sh 'docker rm -f production-planning-backend-ci 2>/dev/null || true'
                sh 'docker run -d --name production-planning-backend-ci -p 5001:5000 production-planning-backend'
            }
        }

        stage('Run Frontend') {
            steps {
                sh 'docker rm -f production-planning-frontend-ci 2>/dev/null || true'
                sh 'docker run -d --name production-planning-frontend-ci -p 8082:80 production-planning-frontend'
            }
        }
    }
}