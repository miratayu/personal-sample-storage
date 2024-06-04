package org.example

import org.apache.groovy.util.concurrent.concurrentlinkedhashmap.ConcurrentLinkedHashMap
import org.junit.jupiter.api.Test
import static org.junit.jupiter.api.Assertions.assertEquals

class MainTest {
    @Test
    void testMain() {
        System.out.printf("test start\n")
        assertEquals(3, Sample.add(1, 2))
        System.out.printf("test end\n")
    }

    @Test
    void testTest() {
        System.out.printf("test start\n")
        def addressMap = [test: "a"]
        System.out.printf("addressMap: ${addressMap}\n")
        def addMapData = [sample:"b", gold:"Au", silver:"Ag", copper:"Cu"]
        System.out.printf("addMapData: ${addMapData}\n")
        addressMap += addMapData
        System.out.printf("addressMap: ${addressMap}\n")
        def testData = [:]
        System.out.printf("test: ${testData?.abc?.data}\n")
        if (addressMap?.abc?.data) {
            System.out.printf("exist: true\n")
        } else {
            System.out.printf("exist: false\n")
        }
        System.out.printf("test end\n")
    }
}
