import java.util.LinkedList;
import java.util.Queue;
public class SUsing1Queue {
    Queue<Integer> queue = new LinkedList<>();
    void push(int ele){
        int size = queue.size();
        queue.add(ele);
        for(int i = 0;i<size;i++){
            queue.add(queue.remove());
        }
    }
    int pop(){
        if(queue.isEmpty()){
            System.out.println("Stack is empty");
            return -1;
        }
        return queue.remove();
    }

    public static void main(String[] args){
        SUsing1Queue stack = new SUsing1Queue();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }
}
