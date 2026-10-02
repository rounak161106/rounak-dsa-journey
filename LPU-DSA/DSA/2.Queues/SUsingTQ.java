import java.util.LinkedList;
import java.util.Queue;
public class SUsingTQ {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    void push(int ele){
        q2.add(ele);
        while(!q1.isEmpty()){
            q2.add(q1.remove());
        }
        Queue<Integer> q = q1; 
        q1 = q2;
        q2 = q;
    }
    int pop(){
        if(q1.isEmpty()){
            System.out.println("Stack is empty");
            return -1;
        }
        return q1.remove();
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
