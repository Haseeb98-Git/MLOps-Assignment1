pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your_dockerhub_username/iris-predictor"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            mail to: 'admin@example.com',
                 subject: 'Deployment Successful',
                 body: 'The Flask app has been successfully deployed.'
        }
        failure {
            mail to: 'admin@example.com',
                 subject: 'Deployment Failed',
                 body: 'Something went wrong during deployment.'
        }
    }
}
