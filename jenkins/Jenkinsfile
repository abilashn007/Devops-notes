pipeline {
    agent { label 'slave2' }
    stages {
        stage('Build') {
            steps {
                    git branch: 'master', url: 'https://github.com/jenkins-docs/simple-java-maven-app.git'
                    sh '''
                        #!/bin/bash 
                        pwd 
                        ls
                        echo "This is a BUILD stage"
                        mvn clean package
                    ''' 
            }
        }
    }
}