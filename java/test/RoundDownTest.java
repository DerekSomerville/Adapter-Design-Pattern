import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RoundDownTest {

    Rounding rounding = new RoundDown();
    @Test
    void round() {
        assertEquals(3,rounding.round(15,4));
    }
}