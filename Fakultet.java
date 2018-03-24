public class Fakultet {

    public static int fakultet(int a){
        //Calculates the faculty of the number a
        if (a>0){

            a = fakultet(a-1)*a;

            return a;
        }
        else{
            return 1;
        }
    }

    public static void main(String[] args){

        int a = fakultet(3);
        System.out.println(a);

    }
}


