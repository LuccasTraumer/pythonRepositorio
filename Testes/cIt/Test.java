public class Test
{
	public static void main(String[] args)
	{
		int valor = 10;
		String valo = valor+"";

		for(int i=0; i < valo.length();i++)
		{
			//if(valo.charAt(i) == '1')
			System.out.println(i);
			valo = i+"";
			System.out.println(valo.length());
		}

	}
}