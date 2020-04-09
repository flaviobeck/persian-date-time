timestamps {

  node () {

  	stage ('pit-test1 - Checkout') {
   	 checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/flaviobeck/persian-date-time.git']]])
  	}
  	stage ('pit-test1 - Build') {
      // Maven build step
      withMaven(maven: 'Maven 3.6.1') {
        if(isUnix()) {
   				sh "mvn test -DoutputFormats=XML org.pitest:pitest-maven:mutationCoverage "
  			} else {
   				bat "mvn test -DoutputFormats=XML org.pitest:pitest-maven:mutationCoverage "
  			}
   		}
  	}
  }
}
