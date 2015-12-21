import java.io.*;
import java.util.Arrays;

class MyIntArrayList {
    // Implement me!
    private int _capacity = 2;
    private int[] _array;
    private int _numItems = 0;
    
    // add an int
    public void add(int elementToAdd) {
        _numItems = _numItems + 1; 
        if (_capacity <= _numItems) {
            int[] holder = new int[_capacity*2];
            for (int index = 0; index < _capacity; index++) {
                holder[index] = _array[index];
            }
            _array = holder; 
            _capacity = _capacity * 2;
        }
        _array[_numItems-1] = elementToAdd; 
    }
    
    public void delete(int index) {
        if (index < 0 || index > _numItems) {
            throw new IndexOutOfBoundsException("Index " + index + " is out of bounds!");
        }
        int[] holder = _array;
        index = index + 1;
        for (int i = index; i < _numItems; i++) {
            _array[i - 1] = holder[i];
        }
        _numItems = _numItems - 1; 
    }
    
    public int at(int index){ 
        if (index < 0 || index > _numItems) {
            throw new IndexOutOfBoundsException("Index " + index + " is out of bounds!");
        }
        else { 
            return _array[index];
        }
    }
    
    public int size() {
        return _numItems;
    }
    
    public String toString() {
        int[] holder = new int[_numItems];
        for (int i = 0; i < _numItems; i++){
            holder[i] = _array[i];
        }
        return Arrays.toString(holder);
    }
    
    public MyIntArrayList() {
        _array = new int[_capacity];
    }
}    


class myCode
{

    
    public static void main (String[] args) throws java.lang.Exception
    {

        MyIntArrayList testArrayList = new MyIntArrayList();
        System.out.println("My ArrayList contains " + testArrayList.size() + " items");
        testArrayList.add(1);
        testArrayList.add(2); 
        testArrayList.add(3); 
        System.out.println("My ArrayList contains " + testArrayList.size() + " items");
        System.out.println("My arraylist should say that it has 1, 2, 3 and it has: " + testArrayList.toString());
        System.out.println("The element at index 0 should be 1, and it is: " + testArrayList.at(0));
        testArrayList.delete(1);
        System.out.println("I deleted the element at index 1 which is 2. My array should have 1, 3. It as: "+ testArrayList.toString());
    
        
        int size = testArrayList.size();

    }
}

