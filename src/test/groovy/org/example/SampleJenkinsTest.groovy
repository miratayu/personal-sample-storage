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
    }

    @Test
    void testSampleJenkins() {
        System.out.printf("${this.logHead} test start\n");
        def sampleJenkins = new SampleJenkins(script: script, text: "b")
        Assertions.assertEquals(1, sampleJenkins.run())
        System.out.printf("${this.logHead} test end\n");
    }
}
