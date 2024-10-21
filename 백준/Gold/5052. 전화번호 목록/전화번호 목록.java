import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {

    public static boolean flag = true;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {

            int n = Integer.parseInt(br.readLine());

            ArrayList<Tree> root = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                String word = br.readLine();
                ArrayList<Tree> before = root;

                for (int j = 0; j < word.length(); j++) {
                    char c = word.charAt(j);

                    Tree nodeWithCurChar = find(before, c);
                    if (nodeWithCurChar != null) {
                        before = nodeWithCurChar.after;

                        if (j == word.length() - 1) {
                            nodeWithCurChar.isEnd();
                        }
                    } else {
                        Tree nodeNew = new Tree(c);
                        before.add(nodeNew);
                        before = nodeNew.after;

                        if (j == word.length() - 1) {
                            nodeNew.isEnd();
                        }
                    }

                }
            }

            for (Tree node : root) {
                dfs(node);
            }

            if (flag) {
                bw.write("YES\n");
            } else {
                bw.write("NO\n");
            }
            flag = true;
        }
        bw.flush();
    }

    public static void dfs(Tree node) {
        // 다음 노드가 없으면 리턴
        if (node.after.isEmpty()) {
            return;
        } else {
            // 다음 노드가 있는데 맨 끝이라고 하면 false
            if (node.isEnd) {
                flag = false;
            }
        }
        for (Tree nextNode : node.after) {
            dfs(nextNode);
        }
    }

    private static Tree find(ArrayList<Tree> list, char c) {
        for (Tree t : list) {
            if (t.cur == c) {
                return t;
            }
        }
        return null;
    }

    public static class Tree {
        char cur;
        ArrayList<Tree> after;
        Boolean isEnd;

        public Tree(char cur) {
            this.cur = cur;
            this.after = new ArrayList<>();
            this.isEnd = false;
        }

        public void isEnd() {
            this.isEnd = true;
        }
    }

}