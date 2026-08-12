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
                echo 'Creating Python virtual environment...'
                sh 'python3 -m venv venv'

                echo 'Installing dependencies...'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'venv/bin/pytest'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application...'
                sh 'venv/bin/python app.py'
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
