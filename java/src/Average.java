import java.util.Arrays;
import java.util.List;

public class Average {
    Rounding roundingMethod = new RoundDown();

    public void setRoundingMethod(Rounding roundingMethod){
        this.roundingMethod = roundingMethod;
    }

    public double calculateAverage(String numberAsString){
        List<String> numbers = Arrays.asList(numberAsString.split(","));
        Integer count = numbers.size();
        double total = 0;
        for (String number : numbers){
            total += Double.parseDouble(number);
        }
        return roundingMethod.round(total,count);
    }
}
