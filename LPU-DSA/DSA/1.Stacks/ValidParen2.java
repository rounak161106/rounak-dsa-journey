import java.util.Stack;

public class ValidParen2{
    public static void main(String[] args){
        try{
            System.out.println(match("{(){}{}[](())}"));
        }catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
    public static boolean match(String parens) throws Exception{
        Stack<Character> stack = new Stack<>();
        for(char ch : parens.toCharArray()){
            if(ch == '(' || ch == '{' || ch == '['){
                stack.push(ch);
            }
            else if(ch == ')'){
                try{
                    char x = stack.pop();
                    if(x != '('){
                        return false;
                    }
                }catch(Exception e){
                    return false;
                }
            }
            else if(ch == '}'){
                try{
                    char x = stack.pop();
                    if(x != '{'){
                        return false;
                    }
                }catch(Exception e){
                    return false;
                }
            }
            else if(ch == ']'){
                try{
                    char x = stack.pop();
                    if(x != '['){
                        return false;
                    }
                }catch(Exception e){
                    return false;
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