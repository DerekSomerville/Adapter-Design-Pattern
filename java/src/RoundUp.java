import java.lang.Math;

public class RoundUp implements Rounding{
    public double round (double total, Integer count){
        return Math.ceil(total/count);
    }
}