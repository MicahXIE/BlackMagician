import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ArrayList<Integer> list = new ArrayList<Integer>();
        int element;
        for (int i=0; i<n; i++) {
            element = in.nextInt();
            list.add(element);
        }
        int op = in.nextInt();
        for (int i=0; i<op; i++) {
            String s = in.next();
            if (s.equals("Insert")) {
                int index = in.nextInt();
                int value = in.nextInt();
                list.add(index, value);
            } else {
                int index = in.nextInt();
                list.remove(index);
            }
        }
        in.close(); 
        
        for (Integer item : list) {
            System.out.print(item + " ");
        }
    }
}
