import java.util.Scanner;
import java.util.Stack;
public class Sort {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String line1 = scanner.nextLine();

        Stack<Integer> stack = new Stack<>();

        for (String elem : line1.split(" ")) {
            stack.push(Integer.parseInt(elem));
        }

        System.out.println("Before sorting : " + stack);
        
        sort(stack);
        
        System.out.println("Before sorting : " + stack);
    }

    public static void sort(Stack<Integer> stack){
        if(stack.isEmpty()){
            return;
        }
        int x = stack.pop();
        sort(stack);
        insert(stack, x);
    }

    public static void insert(Stack<Integer> stack, int ele){
        if(stack.isEmpty()){
            stack.push(ele);
            return;
        }
        int x ;
        if(stack.peek() > ele){
            x = stack.pop();
            insert(stack, ele);
            stack.push(x);
        }
        else{
            stack.push(ele);
        }   
    }
}   
