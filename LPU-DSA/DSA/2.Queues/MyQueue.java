public class MyQueue<T> {
    T[] arr;
    int capacity;
    int front;
    int rear;
    @SuppressWarnings("unchecked")
    MyQueue(int capacity){
        this.capacity = capacity;
        this.arr = (T[]) new Object[capacity];
        this.front = -1;
        this.rear = -1;
    }
    public boolean isEmpty(){
        return this.rear == -1;
    }
    public boolean isFull(){
        return (this.rear + 1)%this.capacity == this.front;
    }
    public void enqueue(T ele){
        if(this.isFull()){
            System.out.println("Queue is already full");
            return;
        }
        if(isEmpty()){
            front = front + 1;
        }
        rear = (rear + 1)%capacity;
        arr[rear] = ele;
    }
    public T dequeue() throws Exception{
        if(isEmpty()){
            throw new Exception("Queue is empty");
        }
        T x = arr[front];
        if (front == rear){
            front = -1;
            rear = -1;
        } 
        else{
            front = (front + 1) % capacity;
        }
        return x;
    }   
    public static void main(String[] args) throws Exception{
        MyQueue<Integer> queue = new MyQueue<>(5);
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.enqueue(50);
        queue.enqueue(40);
        System.out.println(queue.dequeue());
        System.out.println(queue.dequeue());
        System.out.println(queue.dequeue());
        System.out.println(queue.dequeue());
        System.out.println(queue.dequeue());
        queue.enqueue(60);
    }
}
