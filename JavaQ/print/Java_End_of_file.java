import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int ln = 0;
        while (in.hasNextLine()) {
            ln++;
            System.out.println(ln + " " + in.nextLine());
        }
    }
}
