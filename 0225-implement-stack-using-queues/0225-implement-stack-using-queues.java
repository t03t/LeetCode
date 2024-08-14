import java.util.LinkedList;
import java.util.Queue;

class MyStack {
    private Queue<Integer> queue;

    public MyStack() {
        queue = new LinkedList<>();
    }

    public void push(int x) {
        queue.add(x);
        int size = queue.size();
        // Rotate the queue to simulate stack behavior
        while (size > 1) {
            queue.add(queue.remove());
            size--;
        }
    }

    public int pop() {
        if (!queue.isEmpty()) {
            return queue.remove();
        }
        return -1; // Or throw an exception for an empty stack
    }

    public int top() {
        if (!queue.isEmpty()) {
            return queue.peek();
        }
        return -1; // Or throw an exception for an empty stack
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */