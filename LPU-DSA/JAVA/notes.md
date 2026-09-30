# Java Notes

## JDK

To run Java programs, we need to install the JDK.

The JDK contains:

- JRE (Java Runtime Environment): contains built-in classes and functions required to run Java programs. It also contains the JVM, which makes Java platform-independent and allows it to run on any machine.
- Java compiler (javac): translates high-level code into bytecode. This bytecode is not the final executable code; it is further converted to machine code by the JVM.

---

## Data Types in Java

Java has primitive data types such as:

- byte
- short
- int
- long
- float
- double
- boolean
- char

To declare a long number, write:

```java
long n = 123456789L;
```

For a float value:

```java
float num = 10.5f;
```

Boolean values are:

- true
- false

---

## Non-Primitive Types

### String

```java
String name1 = "Rounak";
String name2 = "Rounak";
System.out.println(name1.equals(name2));  
System.out.println(name1 == name2);   // In this case, both variables refer to the same string object in memory. A new object is not created again.

String name3 = new String("Prasad");
String name4 = new String("Prasad");
System.out.println(name3.equals(name4));
System.out.println(name3 == name4);  //Here, both are different objects in memory because `new` creates a separate copy.
System.out.println(name == name2); // true
System.out.println(name_new == name2_new); // false
```

### String Methods

```java
String name = "Rounak";
"Rounak" + " Prasad"   // "Rounak Prasad"
name.charAt(0);        // 'R'
name.replace("o", "a"); // "Raunak"  Note: Strings are immutable, so methods like `replace()` return a new string instead of modifying the original.
name.substring(0, 4);   // "Roun"
System.out.println(name.length()); // 6
```



---

## Arrays

```java
int[] marks = new int[3];
```

or

```java
int[] marks = {10, 30, 500};
```

For a 2D array:

```java
int[][] arr = {{98, 532, 63}, {63, 77, 55}};
```

```java
marks[0] = 90;
```

If we print the array reference directly, we get its memory location, not the actual values.

If an array is not initialized and we try to access an element, the default value is:

- 0 for int, false for boolean, null for strings, 0.0 for floats

To find length:

```java
arr.length
```

To sort an array:

```java
Arrays.sort(arr);
```

We need to import:

```java
import java.util.Arrays;
```

---

## Type Casting

Casting is allowed only when the target type can hold the value.

Example:

```java
int x = 10 + 20.53; // wrong
```

This is invalid because `double` cannot be stored in `int` without explicit conversion.

```java
double y = 10 + 20; // valid
```

To convert explicitly:

```java
(int) 20.53
```

---

## Constants

We declare constants using the `final` keyword:

```java
final int x = 10;
```

---

## Math Class

```java
Math.max(4, 5); // 5
Math.min(4, 5); // 4
Math.random();  // between 0 and 1
```

---

## Input in Java

To take input, create a `Scanner` object:

```java
Scanner sc = new Scanner(System.in);
```

- `sc.next()` reads a single word
- `sc.nextLine()` reads a full line

Example:

```java
int n = Integer.parseInt(scn.nextLine());
```

This converts a string to an integer.


Simpler usage of loops in collections.
eg. 1
String[] words = {"apple", "banana", "cherry"};
for (String word : words) {
    System.out.println(word);
}
eg.2 
int[] numbers = {10, 20, 30, 40};
for (int num : numbers) {
    System.out.println(num);
}
eg. 3(widely used)
String str = "Hello";
for (char ch : str.toCharArray()) {
    System.out.println(ch);
}