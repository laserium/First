package com.say_hello;

public class Main {
    public static final String RESET = "\u001B[0m";
    public static final String RED = "\u001B[31m";
    public static final String GREEN = "\u001B[32m";
    public static final String YELLOW = "\u001B[33m";
    public static final String BLUE = "\u001B[34m";
    public static final String PURPLE = "\u001B[35m";
    public static final String CYAN = "\u001B[36m";
    
    public static void main(String[] args) {
        // System.out.println(RED + "빨간색" + RESET);
        // System.out.println(GREEN + "초록색" + RESET);
        // System.out.println(YELLOW + "노란색" + RESET);
        // System.out.println(BLUE + "파란색" + RESET);
        // System.out.println(PURPLE + "보라색" + RESET);
        // System.out.println(CYAN + "청록색" + RESET);

        System.out.println(RED + "안" + GREEN + "녕" + YELLOW + "하" + BLUE + "십" + PURPLE + "니" + CYAN + "까" + RESET);
    }
}