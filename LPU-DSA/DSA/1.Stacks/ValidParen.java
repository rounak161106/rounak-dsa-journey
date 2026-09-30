import java.util.Stack;

public class ValidParen{
    public static void main(String[] args){
        try{
            System.out.println(match("sga"));
        }catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
    public static boolean match(String parens) throws Exception{
        Stack<Character> stack = new Stack<>();
        for(char ch : parens.toCharArray()){
            if(ch == '('){
                stack.push('(');
            }
            else if(ch == ')'){
                if(stack.isEmpty()){
                    return false;
                }else{
                    stack.pop();
                }
            }
            else{
                throw new Exception("Invalid Character "+ch);
            }
        }
        if(stack.isEmpty()){
            return true;
        }else{
            return false;
        }
    }
}