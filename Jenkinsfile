pipeline {
  agent any
  triggers { pollSCM('* * * * *') }
  environment {
    DB_HOST = 'localhost'
    DB_USER = 'catering'
    DB_PASS = 'ISI_PASSWORD_MYSQL_KAMU'
  }
  stages {
    stage('Install') {
      steps { sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt' }
    }
    stage('Test') {
      steps { sh '. venv/bin/activate && python -m pytest -q' }
    }
    stage('Deploy') {
      steps {
        sh '''
          pkill -f "python app.py" || true
          . venv/bin/activate
          JENKINS_NODE_COOKIE=dontKillMe nohup python app.py > app.log 2>&1 &
        '''
      }
    }
  }
  post {
    success { echo 'Build & deploy berhasil' }
    failure { echo 'Build gagal, cek Console Output' }
  }
}