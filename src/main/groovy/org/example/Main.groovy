package org.example

class Sample {
    static int add(int a, int b) {
        println "add"
        return a + b
    }
}

static void main(String[] args) {
    println "Hello world!"
    println Sample.add(1, 2)
    println Sandbox.sampleOne()
    println Sandbox.checkType("test")
    println Sandbox.checkType(1)
    println Sandbox.checkType(true)
    println Sandbox.checkType([])
    println Sandbox.checkType([:])
}
