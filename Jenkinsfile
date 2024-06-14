pipeline {
    # Ejecutamos en cualquier nodo de jenkins
	agent any
	
	# Declaramos las credenciales de Docker
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }
	
	# Eliminamos los datos del workspace
	# 1.	Limpieza del workspace.
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
		
		# Hacemos un checkout del repo de origen
		# 2.	Checkout del código de nuestro repositorio.
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/diegosanfuen/Actividad01_EOI_devops.git'
            }
        }
		
		# Construimos la imagen de Docker
		# 3.	Contruimos la imagen del contenedor.
        stage('Construimos la imagen de Docker') {
            steps {
                script {
                    dockerImage = docker.build("diegosanchezfuente/actividad2_devops:${env.BUILD_ID}")
                }
            }
        }
		
		# Testeamos la Docker Imagen
		# 4.	Probamos que se ejecuta correctamente. Posteriormente borramos el con-tenedor creado.
        stage('Probamos la imagen') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python lanzamiento_dados.py 10 6
                    }
                }
            }
        }
		
		# Subimos al repo de  Docker la imageb
		# 5.	Subimos la imagen a Docker Hub.
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        dockerImage.push("${env.BUILD_ID}")
                        dockerImage.push("latest")
                    }
                }
            }
        }
		
		# Revisamos el codigo con SonarQube
		# (Opcional) Análisis estático
        stage('Static Code Analysis') {
            when {
                expression {
                    return fileExists('sonar-project.properties')
                }
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }
    }

    post {
        failure {
            echo "El pipeline ha fallado."
        }
    }
}

