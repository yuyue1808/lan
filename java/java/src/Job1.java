class MyArray{
	int[] array;
	
	public MyArray(int[] array){
		this.array = array;
	} 

    public void printArray(){
    	for(int i=0;i<array.length;i++)
    		System.out.print(array[i]+",");
    	System.out.println();
    }
/*采用冒泡排序法*/
	public void sortArray(){
		int temp;
		for(int i=0; i<(array.length-1); i++)
		{
			for(int j=0; j<(array.length-1-i);j++)
			{
				if(array[j]>array[j+1])
				{
					temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
				}
			}
		}
    }

}

public class Job1{
	public static void main(String[] args) {
		int[] array = {23,43,12,9,35};
		MyArray my = new MyArray(array);
		my.printArray();
		my.sortArray();
		my.printArray();
	}
}