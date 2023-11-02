package org.example

class Sandbox {
    String logHead = "[Sandbox]"

    Sandbox(){}

    void sampleOne() {
        println "${this.logHead} sampleOne"
        // def data = ["search":["hits":[]]]
        def data = ["search":["hits":[["object":["name":"test", "score":123]]]]]
        def object = data.search.hits[0]?.object
        println "${this.logHead} ${object}"
        def name = object.name
        println "${this.logHead} ${name}"
    }
    def checkType(value) {
        println "${this.logHead} checkType: ${value.getClass().getSimpleName()}"
        if (value instanceof String) {
            return "str"
        }
        if (value instanceof Integer) {
            return "int"
        }
        if (value instanceof Boolean) {
            return "bool"
        }
        if (value instanceof List) {
            return "list"
        }
        if (value instanceof HashMap) {
            return "hashMap"
        }
        return "none"
    }
}
