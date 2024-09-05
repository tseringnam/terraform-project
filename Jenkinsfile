pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials("aws_access_key_id")
        AWS_SECRET_ACCESS_KEY = credentials("aws_secret_access_key")
    }

    stages {
        stage('Checkout') {
            steps {
                git(branch: "main", credentialsId: "55d8f489-c67a-4275-a145-b10f4fa90ab6", url: "https://github.com/tseringnam/terraform-project.git")
            }
        }
        
        stage('Init') {
            steps {
                sh 'terraform init'
            }
        }
        
        stage('Plan') {
            steps {
                sh 'terraform plan -input=false -out=tfplan'
            }
        }
        
        stage('Apply') {
            steps {
                 echo "this is apply terraform"
                //sh 'terraform apply -input=false tfplan'
            }
        }

        stage('Wait Before Destroy') { 
            steps { 
                script {
                    input message: 'Do you want to proceed with applying the Terraform destroy?', ok: 'Apply'
                }
            } 
        }

        stage('Input Message') {
            steps {
                script {
                    // Prompt for user input in Jenkins
                    def userInput = input(
                        id: 'userInput', 
                        message: 'Enter the message for the Python script:', 
                        parameters: [
                            string(name: 'MESSAGE', defaultValue: 'Cyber Knights', description: 'Message to pass to the Python script')
                        ]
                    )

                    // Print the user input for debugging
                    echo "User input: ${userInput.MESSAGE}"

                    // Run Python script with the user input
                    sh "python3 my-script.py '${userInput.MESSAGE}'"
                }
            }
        }
        // stage('Debug Workspace') {
        //     steps {
        //         // Print environment variables and workspace content
        //         sh 'env'
        //         sh 'ls -l ${WORKSPACE}'
        //     }
        // }

        // stage('Run Python Script') {
        //     steps {
        //         // Run the Python script
        //         sh 'python3  ${WORKSPACE}/my-script.py' 
        //     }
        // }
    
        stage('Terraform Destroy') { 
            steps {
                 echo "this is destroy terraform"
                // sh 'terraform destroy -auto-approve -input=false'
            }  
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

