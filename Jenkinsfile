pipeline {
    agent any

    stages {
        stage ('#1 Git checkout') {
            steps {
                git branch: 'main',
                url: 'git@github.com:Amitk3293/WorldOfGames-Python-Project.git'
                }
        }
        stage ('#2 Build and run wog-app and wog-flask containers using docker-compose') {
            steps {
                sh 'docker-compose up -d'

                }
        }
        stage ('#3 run tests') {
            steps {
                sh 'docker exec -t -d wog-app python /tests/e2e.py'
               }
        }   
        stage ('#4 stop and delete containers') {
            steps {
                sh 'docker rm -f wog-app'
                sh 'docker rm -f wog-flask'
                sh 'docker push docker.io/amitk3293/wog:v2'
                }
        }        
    }
}