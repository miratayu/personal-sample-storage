package resources

class DummyPipeline implements Serializable {
    String logHead = "[DummyPipeline]"

    def echo(String text) {
        println("$logHead dummy echo")
        println("$text")
    }

    def readFile(args) {
        println("$logHead dummy readFile")
        println("args: $args")
        return "sample text"
    }

    def readJSON(args) {
        println("$logHead dummy readJSON")
        println("args: $args")
        return [sample: "text"]
    }
}
