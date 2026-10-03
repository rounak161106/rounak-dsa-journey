import java.util.Scanner;
import java.util.Stack;

public class BottomOfStack {

    public static void main(String args[]) {
        Stack<Integer> stack = new Stack<>();
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int nc = n;
        while (n-- > 0) {
            stack.push(s.nextInt());
        }
        deleteFirstHalf(stack, nc);
    }
    static void deleteFirstHalf(Stack<Integer> stack, int n) {
        Stack<Integer> temp = new Stack<>();
        // Move everything to temp
        while (!stack.isEmpty()) {
            temp.push(stack.pop());
        }
        // Remove floor(n/2) elements
        int half = n / 2;
        while (half-- > 0) {
            temp.pop();
        }
        // Put remaining elements back
        while (!temp.isEmpty()) {
            stack.push(temp.pop());
        }
        System.out.println(stack);
    }
}