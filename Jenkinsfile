pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub-creds')
        DOCKER_IMAGE = "suzhi11/two-tier-app"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Code checked out ✅"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
                sh "docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest"
                echo "Docker image built ✅"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh "echo ${DOCKER_HUB_CREDENTIALS_PSW} | docker login -u ${DOCKER_HUB_CREDENTIALS_USR} --password-stdin"
                sh "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                sh "docker push ${DOCKER_IMAGE}:latest"
                echo "Image pushed ✅"
            }
        }

       
    stage('Deploy') {
    steps {
        sh '''
            cd /home/isha/myproject
            docker compose down || true
            docker compose up -d
        '''
        echo "App deployed ✅"
    }
}
    post {
        success {
            echo "✅ Build #${env.BUILD_NUMBER} successful!"
        }
        failure {
            echo "❌ Build #${env.BUILD_NUMBER} failed!"
        }
        always {
            sh "docker logout || true"
        }
    }
}
