package org.example

import resources.DummyPipeline
import spock.lang.Specification

class TestSampleJenkinsSpec extends Specification {
    Object script = null

    void setup() {
        script = new DummyPipeline()
    }

    void "testRun"() {
        setup:
        def sampleJenkins = new SampleJenkins(script: script, text: "abc")

        expect:
        assert sampleJenkins.run() == 1
    }

    void "testReadFile"() {
        setup:
        def sampleJenkins = new SampleJenkins(script: script)

        expect:
        assert sampleJenkins.readFile('src/test/resources/sample.txt') == 'sample text'
    }

    void "testReadJSON"() {
        setup:
        def sampleJenkins = new SampleJenkins(script: script)

        expect:
        assert sampleJenkins.readJSON('src/test/resources/sample.json') == [sample: 'text']
    }
}
