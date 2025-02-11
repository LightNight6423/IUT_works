public class Rover {
    private Position position;
    private Direction direction;
    private final String name;

    public Rover() {
        this(new Position(0,0), Direction.NORTH, "viper");
    }

    public Rover(Position position, Direction direction, String name) {
        this.position = position;
        this.direction = direction;
        this.name = name;
    }

    public Rover(Integer x, Integer y, Direction direction, String name) {
        this(new Position(x, y), direction, name);
    }

    public Position getPosition() {
        return position;
    }

    public Direction getDirection() {
        return direction;
    }

    public String getLocation() {
        return "at position " + position.toString() + " towards the " + direction.toString();
    }

    @Override
    public String toString() {
        return "Rover[" +
                "position=" + position +
                ", direction=" + direction +
                ", name='" + name + '\'' +
                ']';
    }

    public void move() {
        System.out.println(this.name + " is moving ");
        switch(direction) {
            case NORTH:
                this.position.setY(position.y() + 1);
                break;
            case EAST:
                this.position.setX(position.x() + 1);
                break;
            case SOUTH:
                this.position.setY(position.y() - 1);
                break;
            case WEST:
                this.position.setX(position.x() - 1);
                break;
        }
    }

    public void turnLeft(){
        System.out.println(this.name + " is turning left");
        switch(direction){
            case NORTH:
                this.direction = Direction.WEST;
                break;
            case EAST:
                this.direction = Direction.NORTH;
                break;
            case SOUTH:
                this.direction = Direction.EAST;
                break;
            case WEST:
                this.direction = Direction.SOUTH;
                break;
        }
        System.out.println("now " + getLocation());
    }

    public void turnRight(){
        System.out.println(this.name + " is turning right");
        switch(direction){
            case NORTH:
                this.direction = Direction.EAST;
                break;
            case EAST:
                this.direction = Direction.SOUTH;
                break;
            case SOUTH:
                this.direction = Direction.WEST;
                break;
            case WEST:
                this.direction = Direction.NORTH;
                break;
        }
        System.out.println("now " + getLocation());
    }
}
