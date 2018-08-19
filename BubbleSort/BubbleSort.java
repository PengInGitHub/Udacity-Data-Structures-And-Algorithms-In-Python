public class BubbleSort{
    public static void main(String[] args){
        int[] aList = {103, -54, 26, 93, 0, -17, 77, 1, 17, 31, 44, 55, 20};
        int[] aList1 = {0};
        int[] aList2 = {1};
        int[] aList3 = {-11};

        int[] sorted = bubbleSortUpdate(aList);
        for (int ele = 0; ele<sorted.length; ele++){
            System.out.print(sorted[ele] + ",");
        }
    }

    public static void bubble_sort(int[] aList){
        int start = aList.length - 1;//in Java: aList.length, in Go and Py: len(aList)
        int stop = 0;
        //outer loop index i
        //Java loop: for (int i = 0; i < 10; i++){}
        //Go loop: for i:=0; i<10; i++{}
        //Py loop: for i in range(9, 0, -1):
        for (int i = start; i > stop; i--){
            for (int j = 0; j < i; j++){
                //swap 
                if (aList[j] > aList[j+1]){
                    int tmp = aList[j];
                    aList[j] = aList[j+1];
                    aList[j+1] = tmp;
                }
            }
        }

    }

    public static int[] bubbleSortUpdate(int[] aList){
        int length = aList.length;
        if (length<2){
            return aList;
        }
        //outter loop
        for(int i=length-1;i>0;i--){
            //inner loop
            for (int j=0;j<i;j++){
                if (aList[j]>aList[j+1]){
                    //swap
                    int tmp = aList[j];
                    aList[j] = aList[j+1];
                    aList[j+1] = aList[j];
                }
            }
        }
        return aList;
    }
}