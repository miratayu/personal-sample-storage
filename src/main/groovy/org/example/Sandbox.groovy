package org.example

import org.apache.commons.collections4.MapUtils;

class Sandbox {
    String logHead = "[Sandbox]"
    ArrayList dataList = []

    Sandbox(){}

    Boolean checkDataList() {
        println "${this.logHead} checkDataList"
        println "${this.logHead} this.class.name: ${this.class.name}"
        println "${this.logHead} this.class.methods: ${this.class.methods}"
        Boolean result = true
        if(!this.dataList) {
            result = false
        }
        println "${this.logHead} result: ${result}"
        return result
    }

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

    def splitText(
        String text = "sandbox",  // "test/sample/template/sandbox"
        String delimiter = "/",
        Integer limit = 2
    ) {
        println "${this.logHead} splitText"
        println "${this.logHead} text: ${text}"
        println "${this.logHead} delimiter: ${delimiter}"
        println "${this.logHead} text.contains(delimiter): ${text.contains(delimiter)}"

        String[] splitText = text.split(delimiter, limit)
        println "${this.logHead} splitText: ${splitText}"
        println "${this.logHead} splitText.size(): ${splitText.size()}"
        return [
            "main": splitText[0],
            "sub": text.contains(delimiter) ? splitText[1] : ""
        ]
    }

    def extraction(list) {
        println "$logHead extraction"
        def nameMap = [
            T1: 'test',
            S1: 'send',
            P1: 'post'
        ]
        def invertNameMap = MapUtils.invertMap(nameMap)
        String result = ""
        list.each { current ->
            if (nameMap?."$current") {
                result = current
            }
            if (invertNameMap?."$current") {
                result = invertNameMap."$current"
            }
        }
        return result
    }
}
