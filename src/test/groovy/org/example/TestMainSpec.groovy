package org.example

import spock.lang.Specification

class TestMainSpec extends Specification {

    void "testSampleAdd"() {
        setup:
        Sample sample = new Sample()

        expect:
        assert sample.add(1, 2) == 3
    }

    void "testMap"() {
        given:
        def testData = [:]
        println(testData)

        when:
        testData = baseData + addData

        then:
        assert testData == baseData + addData
        assert testData?.abc?.data == null

        where:
        expected | index  | baseData                 | addData
        true     | 'gold' | [test: 'a', sample: 'b'] | [gold: 'Au', silver: 'Ag', copper: 'Cu']

    }
}
