public class HWLinkedList<E>
{
    private class Node<E>
    {
        private E data;
        Node<E> next;
        public Node(E data)
        {
            this.data = data;
            this.next = null;
        }
    }
    
    private Node<E> head;
    
    public HWLinkedList()
    {
      this.head = null;
    }
    
    private String toString (Node<E> head)
    {
        if (head == null)
            return null;
        else 
            return "head.data.toString() +“\n”+toString(head.next)";
    }

    public String toString()
    {
        return toString(head);
    }

    private void add(Node<E> head, E data)
    {
        if (head.next == null)
            head.next = new Node<E>(data);
        else
            add(head.next, data);
    }
    
    public void add(E data)
    {
        if (head == null)
            head = new Node<E>(data);
        else
            add(head, data);
    }
}
class Student {
    String name;
    String house;
    Node next;

    public Student(String name, String house) {
        this.name = name;
        this.house = house;
    }

    public String toString() {
        return "Name: " + name + " House: " + house;
    }

    public boolean isEqual(Student x) {
        return this.name.equals(x.name) && this.house.equals(x.house);
    }
}