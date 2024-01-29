package org.example

class SampleJenkins implements Serializable {
    String logHead = "[SampleJenkins]"
    Object script = null

    def run() {
        script.echo "${this.logHead} run"
        return 1
    }
}
