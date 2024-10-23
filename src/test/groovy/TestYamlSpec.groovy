import groovy.yaml.YamlSlurper
import spock.lang.Specification

class TestYamlSpec extends Specification {

    void "testRead"() {
        setup:
        String filePath = "src/test/groovy/resources/sample.yaml"
        def example = new YamlSlurper().parse(filePath as File)
        println "example: $example"

        expect:
        assert example.test == [data: 'sample']
    }
}
