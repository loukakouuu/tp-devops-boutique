pipeline {
    agent any

    stages {
        stage('Installation') {
            steps {
                // Installation des outils nécessaires cités dans le TP [cite: 454, 455]
                sh 'pip install pytest pytest-cov radon pylint'
            }
        }

        stage('Linting & Analyse Statique') {
            steps {
                // Vérification de la qualité de forme du code [cite: 435, 291]
                sh 'pylint app.py'
            }
        }

        stage('Tests & Couverture') {
            steps {
                // Exécution automatisée des tests unitaires [cite: 436, 293]
                // Génération du rapport XML pour SonarQube [cite: 445]
                sh 'pytest --cov=app --cov-report=xml:coverage.xml'
            }
        }

        stage('Analyse de Complexité') {
            steps {
                // Évaluation de la maintenabilité avec Radon [cite: 437, 444]
                sh 'radon cc app.py -s'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // Envoi des métriques vers le serveur SonarQube [cite: 445, 453]
                // Note : Nécessite que le serveur SonarQube soit configuré dans Jenkins
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}