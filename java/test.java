import java.io.File;

public class test {
	public static void main(String[] args) {
		// String path = "F:" + File.separator + "lan" + File.separator + "git" +
		// File.separator + "java" + File.separator
		// + "1_java_基础知识.md";
		File f = new File("F:" + File.separator + "lan" + File.separator + "git" + File.separator + "java"
				+ File.separator + "1_java_基础知识.md");
		try {
			System.out.println(f.getCanonicalPath());
			System.out.println(f.canWrite());
		} catch (Exception e ) {
			e.printStackTrace();
		}

	}

}
