package com.anthony.javaalgorithms;

import com.anthony.javaalgorithms.leetcodeProblems.RelativeRanks;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;



@SpringBootApplication
public class JavaAlgorithmsApplication {

	public static void main(String[] args) {
		SpringApplication.run(JavaAlgorithmsApplication.class, args);
		System.out.println("hello world.");
		RelativeRanks.performCalc();
	}

}
