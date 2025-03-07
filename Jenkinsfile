pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "theusername/iris-predictor"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Haseeb98-Git/MLOps-Assignment1'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        bat "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }
}
