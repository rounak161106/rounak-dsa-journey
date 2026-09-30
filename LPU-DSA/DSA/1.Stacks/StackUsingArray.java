import java.util.EmptyStackException;

public  class StackUsingArray{
    public static class MyStack<T>{
        int capacity;
        T[] arr;
        int top;
        @SuppressWarnings("unchecked")  
        MyStack(int capacity){
            this.capacity = capacity;
            this.top = -1;
            this.arr = (T[]) new Object[capacity];
        }

        public boolean isEmpty(){ return top == -1; }
        public boolean isFull(){ return top == capacity-1; }
        public void push(T element){
            if(isFull()){
                throw new StackOverflowError("Stack is already full");
            }
            arr[++top] = element;
        }
        public T pop(){
            if(isEmpty()){
                throw new EmptyStackException();
            }
            return arr[top--];
        }
    }
    public static void main(String[] args){
        MyStack<Integer> stack = new MyStack<>(5);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }
}