package org.example

class SampleJenkins implements Serializable {
    String logHead = "[SampleJenkins]"
    Object script = null
    def text = "a"

    def run() {
        script.echo "${this.logHead} run"
        script.echo "${this.logHead} text: ${text}"
        return 1
    }

    def readFile(fileName) {
        script.echo "${this.logHead} readFile"
        def contents = script.readFile file: fileName
        script.echo "${this.logHead} contents: ${contents}"
        return contents
    }

    def readJSON(fileName) {
        script.echo "${this.logHead} readJSON"
        def contents = script.readJSON file: fileName
        script.echo "${this.logHead} contents: ${contents}"
        return contents
    }
}
