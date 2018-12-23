/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Roman Wang
 */
public class Problem20 {
    
    public static int factorialRecur(int i){
        return factorialRecurHelp(i, i);
    }
    
    public static int factorialRecurHelp(int i, int j){
        if(j==1){
            return i;
        }
        return factorialRecurHelp(i*(j-1), j-1);
    }
    public static void main(String args[]){
    System.out.println(factorialRecur(4));
    }
}
