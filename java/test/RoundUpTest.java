import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RoundUpTest {

    Rounding rounding = new RoundUp();
    @Test
    void round() {
        assertEquals(4,rounding.round(15.0,4));
    }
}