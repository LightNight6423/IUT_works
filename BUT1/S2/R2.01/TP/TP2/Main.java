public class Main {
    public static void main(String[] args) {

        Rover viper = new Rover();
        System.out.println("viper is actually " + viper.getLocation());
        viper.turnRight();
        viper.turnLeft();
        viper.turnLeft();
        viper.turnLeft();
        viper.move();
        System.out.println(viper.getLocation());
        viper.move();
        System.out.println(viper.getLocation());
        viper.move();
        System.out.println(viper.getLocation());
        viper.turnLeft();
        viper.turnLeft();
        viper.move();
        System.out.println(viper.getLocation());
        viper.turnLeft();
        viper.move();
        System.out.println(viper.getLocation());
        System.out.println("viper is actually : ");
        System.out.println(viper.getPosition());
        System.out.println(viper.getDirection());
        System.out.println(viper.toString());
        System.out.println("------------------------------------------");

        Rover python = new Rover(new Position(5, 10), Direction.EAST, "python");
        System.out.println("python is actually " + viper.getLocation());
        System.out.println("python is actually : ");
        System.out.println(python.getPosition());
        System.out.println(python.getDirection());
        System.out.println(python.toString());
        System.out.println("------------------------------------------");

        Rover anaconda = new Rover(20, 30, Direction.SOUTH, "anaconda");
        System.out.println("anaconda is actually " + viper.getLocation());
        System.out.println("anaconda is actually : ");
        System.out.println(anaconda.getPosition());
        System.out.println(anaconda.getDirection());
        System.out.println(anaconda.toString());
        System.out.println("------------------------------------------");
    }
}
