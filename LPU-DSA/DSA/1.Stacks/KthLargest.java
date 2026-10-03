import java.util.*;

public class KthLargest {
  // This function returns the sorted stack
   public static Stack < Integer > sortStack(Stack < Integer > input) {
       //write your code here
       Stack<Integer> output = new Stack<>();
       while(!input.isEmpty()){
           int x = input.pop();
           if(output.isEmpty()){
               output.push(x);
           }
           else{
               while(!output.isEmpty() && output.peek() > x){
                   input.push(output.pop());
               }
               output.push(x);
           }
       }
       return output;
   }

  public static void findKthLargestNum(Stack <Integer> sortedStack, int k) {
      //write your code here
      while(--k > 0){
          sortedStack.pop();
      }
      System.out.println(sortedStack.peek());
  }


  public static void main(String args[]) {
        Stack < Integer > inputStack = new Stack < Integer > ();
        Scanner in = new Scanner(System.in);
        int n = in .nextInt();
        for (int i = 0; i < n; i++) {
            inputStack.add( in .nextInt());
        }

        if (inputStack.isEmpty()) {
            System.out.println("stack is empty");
            System.exit(0);
        }

        int k = in .nextInt();
        if (k > inputStack.size()) {
            System.out.println("invalid input");
            System.exit(0);
        }

        // This is the temporary stack

        Stack < Integer > temp = sortStack(inputStack);
        findKthLargestNum(temp, k);

    }
}
