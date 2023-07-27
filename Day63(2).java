Task
****
Read 3 integers from stdin and then print them to stdout. Each integer must be printed on a new line.

Scanner class
************
  
Scanner scanner = new Scanner(System.in);
String myString = scanner.next();
int myInt = scanner.nextInt();
scanner.close();

System.out.println("myString is: " + myString);
System.out.println("myInt is: " + myInt);

Input
*****
Hi 5

Output
******
myString is: Hi
myInt is: 5
  
Program
*******

  public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i1= scan.nextInt();
        int i2= scan.nextInt();
        int i3= scan.nextInt();
        scan.close();

        System.out.println(i1);
        System.out.println(i2);
        System.out.println(i3);
        
    }
}
Input
*****
42
100
125

Output
******
42
100
125







