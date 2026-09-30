public class Demo{
    public static void main(String[] args){
        String name1 = "Rounak";
        String name2 = "Rounak";
        System.out.println(name1.equals(name2));
        System.out.println(name1 == name2);

        String name3 = new String("Prasad");
        String name4 = new String("Prasad");
        System.out.println(name3.equals(name4));
        System.out.println(name3 == name4);

    }
}