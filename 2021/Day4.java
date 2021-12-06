import java.util.*;
import java.io.File;
import java.io.IOException;

class Score {
    int age;
    int score;
    int board;

    Score(int age, int score, int board) {
        this.age = age;
        this.score = score;
        this.board = board;
    }
}

public class Day4 {

    static HashMap<Integer, Integer> nums = new HashMap<>();
    static ArrayList<int[]> boards = new ArrayList<>();

    public static void main(String[] args) {
        try {
            File fin = new File("Day4.in");
            Scanner in = new Scanner(fin);

            // scan first line
            String firstLine = in.nextLine();
            Scanner firstLineScanner = new Scanner(firstLine).useDelimiter(",");
            int i = 0;
            while (firstLineScanner.hasNextInt()) {
                nums.put(firstLineScanner.nextInt(), i++);
            }
            firstLineScanner.close();

            // scan bingo boards
            while (in.hasNextInt()) {
                int[] board = new int[25];
                for (int j = 0; j < 25; j++) {
                    board[j] = in.nextInt();
                }
                boards.add(board);
            }
            in.close();

            solB();
        } catch (IOException e) {
            System.out.println("Could not open input file");
        }
    }

    public static ArrayList<Score> getAllScores() {
        ArrayList<Score> scores = new ArrayList<>();
        for (int i = 0; i < boards.size(); i++) {
            int[] board = boards.get(i);

            // check rows
            for (int j = 0; j < 5; j++) {
                int[] row = new int[5];
                for (int k = 0; k < 5; k++) {
                    row[k] = board[j * 5 + k];
                }
                scores.add(calcScore(i, row));
            }

            // check columns
            for (int j = 0; j < 5; j++) {
                int[] col = new int[5];
                for (int k = 0; k < 5; k++) {
                    col[k] = board[j + k * 5];
                }
                scores.add(calcScore(i, col));
            }
        }
        return scores;
    }

    public static void solA() {
        // for each row, check when it would have been completed
        // keep running min of max num in 5-in-a-row + its score
        Score first = new Score(99999999, 0, 0);
        for (Score score : getAllScores()) {
            if (score.age < first.age) {
                first = score;
            }
        }
        System.out.println(first.score);
    }

    public static void solB() {
        // for each row, check when it would have been completed
        // keep running min of max num in 5-in-a-row + its score
        Score last = new Score(0, 0, 0);
        HashMap<Integer, Score> boardScore = new HashMap<>();
        for (Score score : getAllScores()) {
            if (!boardScore.containsKey(score.board)) {
                boardScore.put(score.board, score);
            } else if (score.age < boardScore.get(score.board).age) {
                boardScore.put(score.board, score);
            }
        }
        for (int i = 0; i < boards.size(); i++) {
            Score s = boardScore.get(i);
            if (s.age > last.age) {
                last = s;
            }
        }
        System.out.println(last.score);
    }

    public static Score calcScore(int boardIdx, int[] winners) {
        int[] board = boards.get(boardIdx);
        int maxIdx = 0, val = 0;
        // identifies oldest number in the 5-in-a-row winnesr
        for (int j = 0; j < 5; j++) {
            int num = winners[j];
            int idx = nums.get(num);
            if (idx > maxIdx) {
                maxIdx = idx;
                val = num;
            }
        }
        int score = val * sumUnmarked(board, maxIdx);
        return new Score(maxIdx, score, boardIdx);
    }

    public static int sumUnmarked(int[] board, int before) {
        int total = 0;
        for (int x : board) {
            if (nums.get(x) > before)
                total += x;
        }
        return total;
    }
}
