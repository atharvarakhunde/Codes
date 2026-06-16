import java.util.*;

public class NidhiConstruction {

    static class Coords {
        public int x;
        public int y;

        public Coords(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Coords that = (Coords) o;
            return x == that.x && y == that.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    static class Cmd implements Comparable<Cmd> {
        public int existing;
        public int newCube;
        public String dir;

        public Cmd(int existing, int newCube, String dir) {
            this.existing = existing;
            this.newCube = newCube;
            this.dir = dir;
        }

        @Override
        public int compareTo(Cmd other) {
            if (this.existing != other.existing) {
                return Integer.compare(this.existing, other.existing);
            }
            return Integer.compare(this.newCube, other.newCube);
        }
    }

    private static Map<Integer, Coords> cubeToPos = new HashMap<>();
    private static Map<Coords, Integer> posToCube = new HashMap<>();


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        scanner.nextLine();

        List<Cmd> commandList = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            int existing = scanner.nextInt();
            int newCube = scanner.nextInt();
            String dir = scanner.next();
            commandList.add(new Cmd(existing, newCube, dir));
        }
        
        int queryCube = scanner.nextInt();
        scanner.close();

        Collections.sort(commandList);

        if (!commandList.isEmpty()) {
             int firstExisting = commandList.get(0).existing;
             if (!cubeToPos.containsKey(firstExisting)) {
                Coords origin = new Coords(0, 0);
                cubeToPos.put(firstExisting, origin);
                posToCube.put(origin, firstExisting);
             }
        }
        
        for (Cmd command : commandList) {
            int E = command.existing;
            int N_cube = command.newCube;
            String D = command.dir;

            Coords ePos = cubeToPos.get(E);
            if (ePos == null) {
                continue; 
            }

            int x_e = ePos.x;
            int y_e = ePos.y;

            int x_n = x_e;
            int y_n = y_e;

            if (D.equals("top")) {
                y_n += 1;
            } else if (D.equals("down")) {
                y_n -= 1;
            } else if (D.equals("left")) {
                x_n -= 1;
            } else if (D.equals("right")) {
                x_n += 1;
            }
            
            Coords nPos = new Coords(x_n, y_n);

            if (posToCube.containsKey(nPos)) {
                int replacedCube = posToCube.get(nPos);
                cubeToPos.remove(replacedCube);
            }

            posToCube.put(nPos, N_cube);
            cubeToPos.put(N_cube, nPos);
        }
        
        if (!cubeToPos.containsKey(queryCube)) {
            System.out.println("-1 -1 -1 -1");
            return;
        }

        Coords qPos = cubeToPos.get(queryCube);
        int x_q = qPos.x;
        int y_q = qPos.y;

        int upVal = getNeighborValue(x_q, y_q + 1);
        int downVal = getNeighborValue(x_q, y_q - 1);
        int leftVal = getNeighborValue(x_q - 1, y_q);
        int rightVal = getNeighborValue(x_q + 1, y_q);

        System.out.println(upVal + " " + downVal + " " + leftVal + " " + rightVal);
    }

    private static int getNeighborValue(int x, int y) {
        Coords neighborPos = new Coords(x, y);
        Integer cubeNum = posToCube.get(neighborPos);
        
        if (cubeNum != null) {
            return cubeNum;
        } else {
            return -1;
        }
    }
}