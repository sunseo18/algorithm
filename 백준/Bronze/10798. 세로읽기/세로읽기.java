
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class Main {


    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        final int height = 5;
        final int width = 15;
        char[][] chars = new char[height][width];

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                chars[i][j] = ' ';
            }
        }

        for (int i = 0; i < height; i++) {
            String line = br.readLine();

            for (int j = 0; j < line.length(); j++) {
                chars[i][j] = line.charAt(j);
            }
        }


        for (int j = 0; j < width; j++) {
            for (int i = 0; i < height; i++) {
                if (chars[i][j] != ' ') {
                    System.out.print(chars[i][j]);
                }
            }
        }

    }

    public static class Node {
        private int data;
        private List<Node> child;

        public Node(int data) {
            this.data = data;
            this.child = null;
        }

        public void addChild(Node child) {
            this.child.add(child);
        }

        public int getData() {
            return data;
        }

        public List<Node> getChild() {
            return child;
        }
    }
}