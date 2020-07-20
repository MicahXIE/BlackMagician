import java.util.*;
class Solution{
    
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);
        Stack<Character> st = new Stack<Character>();
        int length = 0;
        boolean flag = true;

        while (sc.hasNext()) {
            String input=sc.next();
            length = input.length();
            st.clear();
            flag = true;
            for (int i=0; i<length; i++) {
                if (input.charAt(i) == '(' || input.charAt(i) == '[' ||
                    input.charAt(i) == '{')
                    st.push(input.charAt(i));
                if (input.charAt(i) == ')') {
                    if (!st.isEmpty() && st.peek() == '(')
                        st.pop();
                    else {
                        flag = false;
                        break;
                    }
                }
                if (input.charAt(i) == ']') {
                    if (!st.isEmpty() && st.peek() == '[')
                        st.pop();
                    else {
                        flag = false;
                        break;
                    }
                }
                if (input.charAt(i) == '}') {
                    if (!st.isEmpty() && st.peek() == '{')
                        st.pop();
                    else {
                        flag = false;
                        break;
                    }
                }
            }
            if (st.isEmpty() && flag)
                System.out.println("true");
            else
                System.out.println("false");
        }
        
    }
}

