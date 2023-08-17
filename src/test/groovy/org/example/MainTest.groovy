package org.example

import org.junit.jupiter.api.Test
import static org.junit.jupiter.api.Assertions.assertEquals

class MainTest {
    @Test
    void testMain() {
        System.out.printf("test start\n")
        assertEquals(3, Sample.add(1, 2))
        System.out.printf("test end\n")
    }
}
