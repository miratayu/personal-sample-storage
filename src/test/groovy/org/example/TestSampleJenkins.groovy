package org.example

import resources.DummyPipeline
import spock.lang.Specification

class TestSampleJenkins extends Specification {
    String logHead = "[TestSampleJenkins]"
    Object script = null
    SampleJenkins sampleJenkins = null

    def setup() {
        script = new DummyPipeline()
        sampleJenkins = new SampleJenkins(script: script)
    }

    def "run"() {
        expect:
        println("$logHead run")
        1 == sampleJenkins.run()
    }

    def "readFile"() {
        expect:
        println("$logHead readFile")
        'sample text' == sampleJenkins.readFile('test.txt')
    }

    def "readJSON"() {
        expect:
        println("$logHead readJSON")
        [sample: 'text'] == sampleJenkins.readJSON('test.json')
    }
}
