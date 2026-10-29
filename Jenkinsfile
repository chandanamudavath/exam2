
pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hi:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                bat 'docker login'
            }
        }

        stage('Tag Docker Image') {
            steps {
                bat 'docker tag hi:latest mudavathchandana/kubernetes8:latest'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push mudavathchandana/kubernetes8:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
    }

    post {
        success {
            echo 'Week 8 pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
