import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AverageTest {
    Average average = new Average();
    @Test
    void calculateAverageDown() {
        Rounding roundDown = new RoundDown();
        average.setRoundingMethod(roundDown);
        assertEquals(3.0,average.calculateAverage("3,4,3,5"));
    }

    @Test
    void calculateAverageUp() {
        Rounding roundUp = new RoundUp();
        average.setRoundingMethod(roundUp);
        assertEquals(4.0,average.calculateAverage("3,4,3,5"));
    }
}