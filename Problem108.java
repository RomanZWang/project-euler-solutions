/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Roman Wang
 */

/*
The answers all contain pattern of fibonacci numbers
use fibonacci formula?
DP?

*/
public class Problem108 {
    public static double gnugget(double a){
        return (-(a+1)+Math.sqrt(Math.pow((a+1),2)+4*Math.pow(a,2)))/(2*a);
    }

    public static void main(String args[]){
        for(int i = 1; i<16; i++)
            System.out.println(gnugget(i));
    
    }

}
