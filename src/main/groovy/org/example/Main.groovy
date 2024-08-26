package org.example

class Sample {
    static int add(int a, int b) {
        println "[Sample] add"
        return a + b
    }
}

static void main(String[] args) {
    String logHead = "[Main]"
    println "$logHead Hello world!"
    println "$logHead ${Sample.add(1, 2)}"
    Sandbox sandbox = new Sandbox()
    println "$logHead ${sandbox.sampleOne()}"
    println "$logHead ${sandbox.checkType("test")}"
    println "$logHead ${sandbox.checkType(1)}"
    println "$logHead ${sandbox.checkType(true)}"
    println "$logHead ${sandbox.checkType([])}"
    println "$logHead ${sandbox.checkType([:])}"
    def nameList = [
        ['test'],
        ['mail', 'send'],
        ['post'],
        ['S1']
    ]
    nameList.each {
        println "$logHead extraction_result: ${sandbox.extraction(it)}"
    }
    def queryBase = [
        select: "*",
        from: "test_measured",
        where: [
            ["ipAddress": "0.0.0.0"],
            ["version": "1.2.3"],
            ["os": "windows, linux, android, ios"]
        ]
    ]
    println "$logHead createdQuery: ${sandbox.createQuery(queryBase)}"
}
