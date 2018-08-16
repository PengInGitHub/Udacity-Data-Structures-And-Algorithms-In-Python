public class BubbleSort{
    public static void main(String[] args){
        int[] aList = {103, -54, 26, 93, 0, -17, 77, 1, 17, 31, 44, 55, 20};
        int[] aList1 = {0};
        int[] aList2 = {1};
        int[] aList3 = {-11};

        bubble_sort(aList);
        for (int ele = 0; ele<aList3.length; ele++){
            System.out.print(aList3[ele] + ",");
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
}