import java.util.*;

public class ReverseHalf {
    public static void main(String args[]) {
        Stack<Integer> stack = new Stack<>();
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int nc = n;
        while (n-- > 0)
            stack.push(s.nextInt());
        reverseSecondHalf(stack, nc/2);
        System.out.println(stack);
    }

    // Method to reverse the last half of the elements from the bottom of the stack
    static void reverseSecondHalf(Stack<Integer> stack, int n) {
        // Write your code here
        if(n == 0){
            return;
        }
        int x = stack.pop();
        reverseSecondHalf(stack, n-1);
        insert(stack, x, n);
    }
    static void insert(Stack<Integer> stack, int ele, int n){
        if(n==0){
            stack.push(ele);
            return;
        }
        int x = stack.pop();
        insert(stack, ele, n-1);
        stack.push(x);
    }
}