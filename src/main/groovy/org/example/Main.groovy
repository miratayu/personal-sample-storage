package org.example

class Sample {
    static int add(int a, int b) {
        println "[Sample] add"
        return a + b
    }
}

static void main(String[] args) {
    String logHead = "[Main]"
    println "${logHead} Hello world!"
    println "${logHead} ${Sample.add(1, 2)}"
    Sandbox sandbox = new Sandbox()
    println "${logHead} ${sandbox.sampleOne()}"
    println "${logHead} ${sandbox.checkType("test")}"
    println "${logHead} ${sandbox.checkType(1)}"
    println "${logHead} ${sandbox.checkType(true)}"
    println "${logHead} ${sandbox.checkType([])}"
    println "${logHead} ${sandbox.checkType([:])}"
}
