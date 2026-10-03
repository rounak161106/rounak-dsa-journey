import java.util.*;
class DuplicateParenthesis {
    public static String findDuplicateParenthesis(String inputString) {
        //write your code here
        Stack<Character> stack = new Stack<>();
        for(char ch : inputString.toCharArray()){
            if(ch != ')'){
                stack.push(ch);
            }
            else{
                boolean flag = false;
                while(stack.peek() != '('){
                    stack.pop();
                    flag = true;
                }
                stack.pop();
                if(!flag){
                    return "Input string contains duplicate parenthesis";
                }
            }
        }
        return "Input string does not contain duplicate parenthesis";
    }


        public static void main(String[] args){
            String inputString = new String();
            Scanner in = new Scanner(System.in);
            inputString = in.nextLine();
            System.out.println(findDuplicateParenthesis(inputString));

        }

    }

