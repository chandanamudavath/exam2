
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
                bat 'docker tag hi:latest mudavathchandana/kubernetes:latest'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push mudavathchandana/kubernetes:latest'
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
