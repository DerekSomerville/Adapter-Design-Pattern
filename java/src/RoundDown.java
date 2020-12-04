import java.lang.Math;

public class RoundDown implements Rounding{
    public double round (double total, Integer count){
        return Math.floor(total/count);
    }
}