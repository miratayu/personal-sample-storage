package org.example

class Sandbox {
    static void sampleOne() {
        // def data = ["search":["hits":[]]]
        def data = ["search":["hits":[["object":["name":"test", "score":123]]]]]
        def object = data.search.hits[0]?.object
        println object
        def name = object.name
        println name
    }
    static def checkType(value) {
        println value.getClass().getSimpleName()
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
