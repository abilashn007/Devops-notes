node {
   def mvnHome = tool 'M3'

   stage('Checkout Code') { 
      git 'https://github.com/maping/java-maven-calculator-web-app.git'
   }
   stage('Test Server') {
      sh '''
         docker run -it -d --rm -v maven_repo:/root/.m2 \
            -v "$(pwd)":/app -w /app \
            -p 9999:9999 \
            --network maven \
            --name jetty_container maven:3.8.6-openjdk-18-slim mvn jetty:run
      '''
   }
   stage('Junit Test') {
      sh '''
         docker run -it --rm -v maven_repo:/root/.m2 \
            -v "$(pwd)":/app -w /app \
            --network maven maven:3.8.6-openjdk-18-slim mvn clean test 
      '''
   }

   stage('Integration Test') {
      sh '''
         docker run -it --rm -v maven_repo:/root/.m2 \
            -v "$(pwd)":/app -w /app \
            --network maven maven:3.8.6-openjdk-18-slim mvn clean integration-test 
      '''
   }

   stage('Build and Deploy') {
      timeout(time: 10, unit: 'MINUTES') {
           input message: 'Deploy this web app to production ?'
      }
      echo 'Deploy...'
   }
}
   
