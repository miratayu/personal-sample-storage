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
}
