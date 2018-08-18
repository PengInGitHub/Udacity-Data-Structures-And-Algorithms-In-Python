import java.util.List;

import jdk.nashorn.internal.runtime.arrays.ArrayData;

import java.util.ArrayList;
import java.util.Arrays;
class MergeSort{

    public static void main(String[] args){
        int[] aList = {-54, 26, 93, 0, 77, 31, 44, 55, 1};
        int left = 0;
        int right = aList.length - 1;
        int mid = (left + right)/2;
        mergeSort(aList, left, mid);
        mergeSort(aList, mid, right);
        ArrayList<Integer> test = new ArrayList<>(Arrays.asList(21, -4, -1, -1, 0, 900, 25, 6, 21, 14));
        ArrayList<Integer> test2 = new ArrayList<>(Arrays.asList(21));
        ArrayList<Integer> merged = mergeSortUpdate(test);
        for (int i = 0; i<merged.size(); i++){
            System.out.print(merged.get(i)+ ", ");
        }
    }

    public static ArrayList<Integer> mergeSortUpdate(ArrayList<Integer> aList){
        if (aList.size()<2){
            return aList;
        }
        int mid = (int) aList.size()/2;
        ArrayList<Integer> left = new ArrayList<Integer>();
        ArrayList<Integer> right = new ArrayList<Integer>();
        for (int i=0;i<mid;i++){
            left.add(aList.get(i));
        }
        for (int i=mid;i<aList.size();i++){
            right.add(aList.get(i));
        }
        left = mergeSortUpdate(left);
        right = mergeSortUpdate(right);
        return mergeUpdate(left, right);
    }

    public static ArrayList<Integer> mergeUpdate(ArrayList<Integer> left, ArrayList<Integer> right){
        int i = 0;
        int j = 0;
        ArrayList<Integer> result = new ArrayList<Integer>();

        while (i<left.size() && j<right.size()){
            if(left.get(i)<=right.get(j)){
                result.add(left.get(i));
                i++;
            }else{
                result.add(right.get(j));
                j++;                
            }
        }
        while (i<left.size()){
            result.add(left.get(i));
            i++;
        }
        while (j<right.size()){
            result.add(right.get(j));
            j++;
        }
        return result;
    }

    public static void mergeSort(int[] array, int low, int high){
        if(low < high){
            int middle = (low + high) / 2;
            mergeSort(array, low, middle);
            mergeSort(array, middle+1, high);
            merge(array, low, middle, high);
        }	
    }

    private static int[] merge(int[] array, int low, int middle, int high){
        int[] helper = new int[array.length];
        for (int i = low; i <= high; i++) {
            helper[i] = array[i];
        }
        
        int helperLeft = low;
        int helperRight = middle+1;
        int current = low;
        
        while (helperLeft <= middle && helperRight <=high) {
            if(helper[helperLeft] <= helper[helperRight]){
                array[current] = helper[helperLeft];
                helperLeft++;
                
            }else{
                array[current] = helper[helperRight];
                helperRight++;
            }
            current ++;		
        }
        
        int remaining = middle - helperLeft;
        for (int i = 0; i <= remaining; i++) {
            array[current+i] = helper[helperLeft+ i];
        }
        return helper;
    }

    // private static int[] merge2(int[] aList, int[] left, int[] right){
    //     int i = 0;
    //     int j = 0;
    //     int[] result = new int[aList.length];
    //     while (i<left.length && j<right.length){
    //         if (left[i] <= right[j]){
    //             result.add(left[i]);
    //             i++;
    //         }else{
    //             result.add(right[j]);
    //             j++;
    //         }
    //     }
    //     result.addAll(Arrays.copyOfRange(left, i, left.length));
    //     result.addAll(Arrays.copyOfRange(right, j, right.length));
    //     int[] resultConvert = result.stream().mapToInt(k -> k).toArray();

    //     return result;
    // }
}

