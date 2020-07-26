import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        try {
            int divisor = in.nextInt();
            int dividend = in.nextInt();
            System.out.println(divisor/dividend);
        } catch (InputMismatchException e1) {
            System.out.println("java.util.InputMismatchException");
        } catch (ArithmeticException e2) {
            System.out.println(e2);
        } catch (Exception e3) {
            System.out.println(e3);
        }
    }
}
