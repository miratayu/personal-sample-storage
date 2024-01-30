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
}
