package com.anthony.javaalgorithms.leetcodeProblems;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Hashtable;

public class RelativeRanks {
    public static String[] findRelativeRanks(int[] score) {
        Integer[] score1 = new Integer[score.length];
        for (int i = 0; i < score.length; i ++){
            score1[i] = score[i];
        }

        Arrays.sort(score1, Collections.reverseOrder());
        HashMap<Integer, Integer> ranking = new HashMap<Integer, Integer>();
        for (int i = 0; i < score1.length; i++) {
            ranking.put(score1[i], i + 1);
        }
        String[] answer = new String[score.length];
        for (int i = 0; i < score.length; i ++) {
            String curRanking = ranking.get(score[i]).toString();
            if (curRanking.equals("1")){
                curRanking = "Gold Medal";
            } else if (curRanking.equals("2")){
                curRanking = "Silver Medal";
            } else if (curRanking.equals("3")){
                curRanking = "Bronze Medal";
            }
            answer[i] = curRanking;
        }

        return answer;
    }


    public static void performCalc(){
        int[] arr = {1,4,5,2,3,9,8};
        System.out.println(Arrays.toString(findRelativeRanks(arr)));
    }
}
