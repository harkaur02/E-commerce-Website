pipeline {
    agent any

    environment {
        // Set environment variables (if needed)
        DOCKER_IMAGE = "thethymca/e-commerce-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository
                git branch: 'main', url: 'https://github.com/harkaur02/E-commerce-Website.git'
                echo "cloned successfully!"
            }
        }


        /* stage('Build Docker Image') {
            steps {
                // Build the Docker image
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Push Docker Image') {
            steps {
                // Push Docker image to Docker Hub
                withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_TOKEN')]) {
                    sh '''
                    echo "$DOCKER_TOKEN" | docker login -u "your-dockerhub-username" --password-stdin
                    docker push ${DOCKER_IMAGE}
                    '''
                }
            }
        } */

      stage('Build and Push Docker Image') {
      environment {
        DOCKER_IMAGE = "thethymca/e-commerce-app:${BUILD_NUMBER}"
        // DOCKERFILE_LOCATION = "java-maven-sonar-argocd-helm-k8s/spring-boot-app/Dockerfile"
        REGISTRY_CREDENTIALS = credentials('docker-cred')
      }
      steps {
        script {
            sh 'docker build -t ${DOCKER_IMAGE} .'
            echo "image build done"
            def dockerImage = docker.image("${DOCKER_IMAGE}")
            docker.withRegistry('https://index.docker.io/v1/', "docker-cred") {
                dockerImage.push()
            }
        }
      }
    }

        /*stage('Deploy') {
            steps {
                // Deploy using docker-compose or another deployment method
                sh 'docker-compose up -d'
            }
        }*/
      stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images after build
            sh 'docker system prune -f'
        }
        success {
            echo 'Build and deployment successful!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
