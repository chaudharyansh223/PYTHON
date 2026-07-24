node {
    try {
        // 1. Pehle normal sequential stages
        stage("test") {
            sh 'echo "test"'
        }
        stage("build") {
            sh 'echo "build"'
        }

        // 2. Phir parallel execution stage
        stage("test on locally") {
            parallel(
                "Locally testing": {
                    sh 'echo "testing locally"'
                },
                "Parallel testing": {
                    stage("parallel") {
                        sh 'echo "running parallely"'
                    }
                }
            )
        }
    } catch (Exception e) {
        echo "Pipeline failed"
        throw e
    } finally {
        echo "Pipeline execution completed"
    }
}