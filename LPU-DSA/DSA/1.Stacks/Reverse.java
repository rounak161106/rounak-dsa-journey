import java.util.*;

public class Reverse {

    public static void reverse(Stack<Integer> stack) {
        if(stack.isEmpty()){
            return;
        }
        int x = stack.pop();
        reverse(stack);
        insert(stack, x);
    }
    public static void insert(Stack<Integer> stack, int x){
        if(stack.isEmpty()){
            stack.push(x);
            return ;
        }
        int y = stack.pop();
        insert(stack, x);
        stack.push(y);
    }
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String line1 = scanner.nextLine();

        Stack<Integer> stack = new Stack<>();

        for (String elem : line1.split(" ")) {
            stack.push(Integer.parseInt(elem));
        }

        System.out.println(stack);

        reverse(stack);

        System.out.println(stack);
    }
}