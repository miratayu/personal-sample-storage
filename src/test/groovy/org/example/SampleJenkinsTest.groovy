package org.example

import com.lesfurets.jenkins.unit.BasePipelineTest
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

class SampleJenkinsTest extends BasePipelineTest {
    String logHead = "[SampleJenkinsTest]"
    Object script = null

    @Override
    @BeforeEach
    void setUp() {
        super.setUp()
        this.script = loadScript('src/test/resources/EmptyPipeline.groovy')
        helper.addReadFileMock('output', 'FAILED!!!')
    }

    @Test
    void testSampleJenkins() {
        System.out.printf("${this.logHead} test start\n");
        def sampleJenkins = new SampleJenkins(script: script, text: "abc")
        Assertions.assertEquals(1, sampleJenkins.run())
        System.out.printf("${this.logHead} test end\n");
    }

    @Test
    void testReadFile() {
        System.out.printf("${this.logHead} test start\n");
        def sampleJenkins = new SampleJenkins(script: script)
        Assertions.assertEquals('', sampleJenkins.readFile('src/test/resources/sample.txt'))
        System.out.printf("${this.logHead} test end\n");
    }

    @Test
    void testReadJSON() {
        System.out.printf("${this.logHead} test start\n");
        def sampleJenkins = new SampleJenkins(script: script)
        Assertions.assertEquals([sample: 'text'], sampleJenkins.readJSON('src/test/resources/sample.json'))
        System.out.printf("${this.logHead} test end\n");
    }
}
