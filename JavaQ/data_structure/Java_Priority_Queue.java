//https://www.hackerrank.com/challenges/java-priority-queue/problem

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Comparator; 
import java.util.PriorityQueue;

class Student {
    private final int id;
    private final String name;
    private final double cgpa;

    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    public int getID() { return this.id; }
    public String getName() { return this.name; }
    public double getCGPA() { return this.cgpa; }
}

class StudentComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        if (s1.getCGPA() == s2.getCGPA())
            return s1.getName().compareTo(s2.getName());
        else
            return s1.getCGPA() > s2.getCGPA() ? -1 : 1;
    }
}

class Priorities {

    public List<Student> getStudents(List<String> events) {
        PriorityQueue<Student> q = new PriorityQueue<Student>(events.size(), new StudentComparator());
        for (String str: events) {
            String[] s = str.split(" ");
            if (s[0].equals("ENTER")) {
                String name = s[1];
                double cgpa = Double.parseDouble(s[2]);
                int id = Integer.parseInt(s[3]);
                Student su = new Student(id, name, cgpa);
                q.offer(su);
            }
            if (s[0].equals("SERVED"))
                q.poll();
        }

        List<Student> list = new ArrayList<Student>();
        /* below is not correct way
        for (Student su : q) {
            // System.out.println(su.getName() + ": " + su.getCGPA());
            list.add(su);
        }
        */
        while (!q.isEmpty()) {
            list.add((Student) q.poll());
        }

        return list;

    }

}


public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();
    
    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());    
        List<String> events = new ArrayList<>();
        
        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }
        
        List<Student> students = priorities.getStudents(events);
        
        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}