import java.util.LinkedList;
import java.util.Queue;
public class SUsingTQ {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    void push(int ele){
        q1.add(ele);
        return;
    }
    int pop(){
        if(q1.isEmpty()){
            System.out.println("Stack is empty");
            return -1;
        }
        int x;
        while(true){
            x = q1.remove();
            if(q1.isEmpty()){
                break;
            }
            q2.add(x);
            Queue<Integer> q = q1; 
            q1 = q2;
            q2 = q;
        }
        return x;
    }

    public static void main(String[] args){
        SUsingTQ stack = new SUsingTQ();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }
}
