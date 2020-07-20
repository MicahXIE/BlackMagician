import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<ArrayList<Integer>> inputArrayList = new ArrayList<ArrayList<Integer>>();
        int n = in.nextInt();
        int count = 0;
        int element = 0;
        for (int i=0; i<n; i++) {
            ArrayList<Integer> mArrayList = new ArrayList<Integer>();
            count = in.nextInt();
            for (int j=0; j<count; j++) {
                element = in.nextInt();
                mArrayList.add(element);
            }
            inputArrayList.add(mArrayList);
        }
        
        int query = in.nextInt();
        int row = 0;
        int col = 0;
        for (int i=0; i<query; i++) {
            row = in.nextInt();
            col = in.nextInt();
            if (row > inputArrayList.size() || col > inputArrayList.get(row-1).size())
                System.out.println("ERROR!");
            else 
                System.out.println(inputArrayList.get(row-1).get(col-1));
        }
    }
}