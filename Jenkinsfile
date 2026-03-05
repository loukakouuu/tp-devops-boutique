pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                // Récupération du code source depuis Git
                checkout scm
            }
        }
        
        stage('Installation Dépendances') {
            steps {
                // Création d'un environnement virtuel et installation des paquets
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Analyse de Complexité (Radon)') {
            steps {
                sh '''
                . venv/bin/activate
                echo "Complexité Cyclomatique :"
                radon cc main.py -a
                echo "Indice de Maintenabilité :"
                radon mi main.py -s
                '''
            }
        }
        
        stage('Tests Unitaires & Couverture') {
            steps {
                sh '''
                . venv/bin/activate
                # Génère le rapport de couverture au format XML pour SonarQube
                pytest --cov=. --cov-report=xml --cov-report=term
                '''
            }
        }
        
        stage('Analyse SonarQube') {
            steps {
                // Attention: 'sonar-scanner' doit être configuré dans Jenkins
                // et l'instance SonarQube doit être liée avec le nom 'SonarQube'
                withSonarQubeEnv('SonarQube') {
                    sh '/opt/sonar-scanner-cli/bin/sonar-scanner' // Adapter le chemin selon ton installation si besoin
                }
            }
        }
    }
}