import java.util.*;
public class Practice {

  List<String> items = new ArrayList<String>();

  public int getClassiness(){ 
    int res = 0;
    if (items.size() > 0) {
      for (int i = 0; i < items.size(); i++){
        if (items.get(i) == "tophat"){
          res += 2;
        }
        if (items.get(i) == "bowtie"){
          res += 4;
        }
        if (items.get(i) == "monocle"){
          res += 5;
        }              
      }
    }
    return res;
  }

  private void addItem(String newItem){
    items.add(newItem);
  }  

  public static void main(String[] args){
    Practice practice = new Practice();
    practice.addItem("tophat");
    practice.addItem("bowtie");
    practice.addItem("jacket");
    practice.addItem("monocle");
    practice.addItem("bowtie");
    System.out.println(practice.items);
    System.out.println(practice.getClassiness());
  }
}
  