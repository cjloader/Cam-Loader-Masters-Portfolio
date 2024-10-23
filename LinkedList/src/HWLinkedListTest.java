import java.util.Scanner;

public class HWLinkedListTest {
    public static void main(String[] args) {
        HWLinkedList studentList = new HWLinkedList();
        Scanner scanner = new Scanner(System.in);
        boolean menu = true;

        while (menu) {
            System.out.println("1. Add a new student to the end");
            System.out.println("2. Add a new student to the head");
            System.out.println("3. Remove a student");
            System.out.println("4. Search for a student");
            System.out.println("5. Print all students");
            System.out.println("6. QUIT");

            System.out.print("Please choose an option: ");
            String option = scanner.nextLine();

            if (option.equals("1")) {
                System.out.print("Please enter student's name: ");
                String name = scanner.nextLine();
                System.out.print("Please enter the house name: ");
                String house = scanner.nextLine();
                Student student = new Student(name, house);
                studentList.add(student);
                System.out.println("Student: " + student.name + " House: " + student.house + " was added.");
            }

            if (option.equals("2")) {
                System.out.print("Please enter student's name: ");
                String name = scanner.nextLine();
                System.out.print("Please enter the house name: ");
                String house = scanner.nextLine();
                Student student = new Student(name, house);
                studentList.addAtHead(student);
                System.out.println("Student: " + student.name + " House: " + student.house + " was added to the head.");
            }

            if (option.equals("3")) {
                System.out.print("Please enter student's name to remove: ");
                String name = scanner.nextLine();
                studentList.remove(name);
            }

            if (option.equals("4")) {
                System.out.print("Please enter student's name to search: ");
                String name = scanner.nextLine();
                Student student = new Student(name, null);
                if (studentList.searchList(student)) {
                    System.out.println("Found " + student.name);
                } else {
                    System.out.println("Not Found");
                }
            }

            if (option.equals("5")) {
                System.out.println(studentList.toString());
            }

            if (option.equals("6")) {
                menu = false;
            }
        }
        scanner.close();
    }
}