#Java Stdin and Stdout II


Task
****
On the first line, print String: followed by the unaltered String read from stdin.
On the second line, print Double: followed by the unaltered double read from stdin.
On the third line, print Int: followed by the unaltered integer read from stdin.
If you use the nextLine() method immediately following the nextInt() method, recall that nextInt() reads integer tokens; because of this, 
the last newline character for that line of integer input is still queued in the input buffer
and the next nextLine() will be reading the remainder of the integer line (which is empty).


Program
*******
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();
        String s = scan.nextLine();

        

        System.out.println("String: " +s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}

Input
*****
42
3.1415
Welcome to HackerRank's Java tutorials!

Output
******
String: Welcome to HackerRank's Java tutorials!
Double: 3.1415
Int: 42
