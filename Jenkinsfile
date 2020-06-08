pipeline{
    agent any
    stages{
        stage("Make Scripts Executable"){
            steps{
                sh 'chmod +x ./scripts/*'
            }
        }
        stage("Export Variables"){
            steps{
                sh './scripts/vars.sh'
            }
        }
        stage("Deploy Stack"){
            steps{
                sh './scripts/docker.sh'
            }
        }
    }
}