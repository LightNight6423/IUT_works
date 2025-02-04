import java.util.Objects;

public class ComputerPioneer {
    private final String lastName;
    private final String firstName;
    private final Device device;

    public ComputerPioneer(String lastName, String firstName, Device device) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.device = device;
    }

    public String toString() {
        return this.lastName + this.firstName + " is a computer pioneer";
    }

    public Device machine() {
        return device;
    }

    public Boolean worksOn(Device device) {
        if (this.device.equals(device))
            return true;
        else{
            return false;
        }
    }
}