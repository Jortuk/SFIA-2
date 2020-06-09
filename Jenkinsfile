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
        stage("Install Ansible and Run Playbook"){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage("Deploy Stack"){
            steps{
                sh './scripts/docker.sh'
            }
        }
    }
}