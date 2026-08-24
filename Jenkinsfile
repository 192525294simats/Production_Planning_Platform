pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Production Planning Platform'
                git branch: 'feature/devsecops-final',
                    url: 'https://github.com/192525294simats/Production_Planning_Platform.git'
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                echo 'Building Backend Docker Image'
                sh '''
                    docker build -t production-planning-backend ./backend
                '''
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                echo 'Building Frontend Docker Image'
                sh '''
                    docker build -t production-planning-frontend ./frontend
                '''
            }
        }

        stage('Run Backend Container') {
            steps {
                echo 'Starting Backend Container'
                sh '''
                    docker rm -f production-planning-backend-ci 2>/dev/null || true
                    docker run -d \
                        --name production-planning-backend-ci \
                        -p 5001:5000 \
                        production-planning-backend
                '''
            }
        }

        stage('Run Frontend Container') {
            steps {
                echo 'Starting Frontend Container'
                sh '''
                    docker rm -f production-planning-frontend-ci 2>/dev/null || true
                    docker run -d \
                        --name production-planning-frontend-ci \
                        -p 8082:80 \
                        production-planning-frontend
                '''
            }
        }

        stage('Deployment Check') {
            steps {
                echo 'Checking running containers'
                sh '''
                    docker ps
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check Console Output.'
        }
    }
}