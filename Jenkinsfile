pipeline {
    agent {
        label 'azure-agent'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out project...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m pytest'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application...'
                sh 'python3 app.py'
            }
        }
    }

    post {
        success {
            echo 'DevOps pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
