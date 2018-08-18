import java.util.ArrayList;
import java.util.Arrays;

public class QuickSort{
    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<>(Arrays.asList(21, -4, -1, -1, 0, 900, 25, 6, 21, 14));

        ArrayList<Integer> quickSorted = quickSortUpdate(test);
        for (int i=0;i<quickSorted.size();i++){
            System.out.println(quickSorted.get(i)+", ");
        }
    }

    public static ArrayList<Integer> quickSort(ArrayList<Integer> aList){
        if (aList.size()<2){
            return aList;
        }

        ArrayList<Integer> less = new ArrayList<Integer>();
        ArrayList<Integer> equal = new ArrayList<Integer>();
        ArrayList<Integer> greater = new ArrayList<Integer>();

        //int pivot = aList[aList.length-1];
        int pivot = aList.get(aList.size() - 1);
        //add element in java list 
        //use list instead of array, cuz array is fixed-sized
        //https://stackoverflow.com/questions/28549489/how-to-add-an-element-at-the-end-of-an-array
        for (int i=0; i<aList.size();i++){
            if (aList.get(i) < pivot){
                less.add(aList.get(i));
            }else if (aList.get(i) == pivot){
                equal.add(aList.get(i));
            }else{
                greater.add(aList.get(i));
            }
        }
        quickSort(less).addAll(equal);
        less.addAll(quickSort(greater));
        return less; 
    }
    public static ArrayList<Integer> quickSortUpdate(ArrayList<Integer> aList){
        if(aList.size()<2){
            return aList;
        }
        ArrayList<Integer> less = new ArrayList<Integer>();
        ArrayList<Integer> equal = new ArrayList<Integer>();
        ArrayList<Integer> greater = new ArrayList<Integer>();

        int pivot = aList.get(aList.size()-1);

        for (int i=0;i<aList.size();i++){
            if (aList.get(i)<pivot){
                less.add(aList.get(i));
            }else if(aList.get(i)==pivot){
                equal.add(aList.get(i));
            }else{
                greater.add(aList.get(i));
            }
        }
        quickSortUpdate(less).addAll(equal);
        less.addAll(quickSortUpdate(greater));
        return less;
    }
}