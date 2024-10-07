package org.example

class Sample {
    String logHead = "[Sample]"
    int add(int a, int b) {
        println "$logHead add"
        return a + b
    }
}

static void main(String[] args) {
    String logHead = "[Main]"
    println "$logHead Hello world!"
    Sample sample = new Sample()
    println "$logHead ${sample.add(1, 2)}"
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
            [ipAddress: "0.0.0.0"],
            [version: "1.2.3"],
            [os: "windows, linux, android, ios"],
            [timestamp: ""]
        ]
    ]
    println "$logHead createdQuery: ${sandbox.createQuery(queryBase)}"
    def sector = 'select'
    def sectorData = queryBase?."$sector"
    println "$logHead $sectorData"
    println "$logHead ${queryBase[sector]}"
    println "$logHead ${queryBase?[sector]}"
    def dummyBase = [:]
    println "$logHead ${dummyBase?[sector]}"
    println "$logHead ${dummyBase[sector]}"
}
