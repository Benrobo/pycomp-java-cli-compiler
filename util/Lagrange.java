package main;

import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Nonny
 */
public class Lagrange {
    public static void main(String[] args) {
        // Declaration of the scanner variable
        Scanner myScanner = new Scanner(System.in);

        // Declaration of variables
        int n; // Number of terms
        int counta, countb; // Loop variables, for counting loops

        float[] arrayx = new float[200]; // Array limit 199
        float[] arrayy = new float[200]; // Array limit 199
        // The arbitrary value, x to be entered for
        // which the value of y can be known
        float x = 0;
        float y = 0; // The corresponding value, f(x)=y
        float numerator; // The numerator
        float denominator; // The denominator

        // Prompts a user to enter a value
        System.out.print("Enter the number of terms n: ");
        n = myScanner.nextInt(); // Store the value in n

        // Prompts user to enter the array for X
        System.out.println("Enter the values that are in xi.");

        for (counta = 0; counta < n; counta++) // Start the loop for X
        {
            // Prompts the user to enter the sequel for xi
            System.out.print("Enter the value for x" + counta + ": ");
            // Store the sequel in the Array, arrayx
            arrayx[counta] = myScanner.nextFloat();
        }
        // Promt user to enter the array for Y
        System.out.println("Enter the values that are in yi.");
        for (counta = 0; counta < n; counta++) // loop for Y
        {
            // Promp the user to enter the sequel for yi
            System.out.print("Enter the value for y" + counta + ": ");
            // Store the sequel in the Array, arrayy
            arrayy[counta] = myScanner.nextFloat();
        }
        // Prompts the user to enter any (the arbitray)
        // value x to get the corresponding value of y
        System.out.println("Enter the arbitrary value x for which you want the value y: ");
        x = myScanner.nextFloat(); // Store the value in x
        System.out.println("The point of interpolation. ");
        // first Loop for the polynomial calculation
        for (counta = 0; counta < n; counta++) {
            // Initialisation of variable
            numerator = 1;
            denominator = 1;

            // second Loop for the polynomial calculation
            for (countb = 0; countb < n; countb++) {
                if (countb != counta) {
                    numerator = numerator * (x - arrayx[countb]);
                    denominator = denominator * (arrayx[counta] - arrayx[countb]);
                }
            }
            y = y + (numerator / denominator) * arrayy[counta];
        }
        System.out.println("When x = " + x + "," + " y = " + y);
    }
}
